import sys
# sleep 是用来干嘛的？
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

# 主框架中调用的函数
def check_events(ai_settings, screen, stats, play_button, sb, ship, aliens, bullets):
    # 响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 点击关闭
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # 按键按下
            check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            # 按键松开
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 检查用户是否点击PLAY按钮
            # 鼠标左击（单击）根据鼠标单击范围确定单击元素
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # 调用PLAY按钮
            check_play_button(ai_settings, screen, stats, play_button, sb, ship, aliens,
                bullets, mouse_x, mouse_y)

def check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets):
    # 响应按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        # 修改移动标志为True，运行到主框架中的ship.update() 时，会执行向右移动的代码；
        # 只要一直按着RIGHT，ship.moving_right 一直等于True，ship.update 也会一直运行右移代码
        # ship 也会一直向右移动
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建子弹，并将其加入到编组bullets中
        fire_bullet(ai_settings, screen, ship, bullets)
        # 封装的函数，在本文件中
        # fire_bullet() 为啥不放入bullet.py中的Bullet类中？

        # 按照SPACE子弹一直发射的实现方法：参考按住右箭头ship一直右移的方法
        # 设置射击标志，只要射击标志 =True,一直循环执行fire_bullet()代码块
    elif event.key == pygame.K_q:
        sys.exit()
        # 退出，不是在这里封装的
    elif event.key == pygame.K_p:
        # 按p，开始游戏
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建子弹，并将其加入到编组bullets中
    # 如果还没有达到限制，就发射一颗子弹
    if len(bullets) < ai_settings.bullets_allowed:
        # 创建bullet 实例
        new_bullet = Bullet(ai_settings, screen, ship)
        # 加入到bullets编组中
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    # 响应松开按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_play_button(ai_settings, screen, stats, play_button, sb, ship, aliens, 
        bullets, mouse_x, mouse_y):
    # 检查用户是否点击PLAY按钮；
    
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    # 返回值 True, False；参数是光标点击的位置
    # play_button 在主框架中定义的是，初始化程序时显示
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()
        # 开始新的游戏
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)

# 初始化系统设置
def start_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # 按P重新开始游戏
    # 隐藏光标
    pygame.mouse.set_visible(False)
    # 重置游戏统计信息：本质就是重新执行一遍对应的代码
    stats.reset_stats()
    # 启动游戏标志
    stats.game_active = True

    # 重记记分牌图像；飞船与外星人撞击时调用 sb
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()

    # 清空编组；aliens 是在主框架中创建的编组；
    aliens.empty()
    bullets.empty()

    # 重新绘制外星人、飞船
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
        
# 更新屏幕上的图像，切换到新屏幕
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):

    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面，重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # 显示得分
    sb.show_score()
    # 当游戏处于非活动状态，绘制Play 按钮
    if not stats.game_active:
        play_button.draw_button()

    # 显示最新的屏幕
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # 更新子弹位置
    bullets.update()
    
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
    """
    为啥遍历的是bullets.copy()? 删除的是bullets.remove()?
    好像有点感觉了，循环、删除时，是按照bullets中的元素位置执行的：1-5 逐个执行。
    先处理第一个
    位置，然后处理第二个位置，依次类推，不管是不是这个元素。如果循环bullets，
    删除1 后，2 补位到 1 的
    位置，那2 原来的位置是空，那就不会删除 2 了，最后只会删除1、3、5， 2、4 补
    位了，所以没删除。

    循环副本时，先删除 bullets 中 的 1 ，2 前移到 1 的位置；因为bullets.copy中 
    的 1 没有删除，2 不会前移，所以第二次循环 bullets.copy 中的第二个元素：2；
    之后是循环 第三个元素：3， 依次类推，这样就避免了上面的问题。虽然bullets中
    的元素被删除了，但是bullets.copy的元素并没有改动，所以会循环到bullets（=
    bullets.copy）的中的所有元素。

    """

    # 检查子弹是否击中外星人，如果击中，删除外星人和子弹; P248
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # 检查子弹是否击中外星人，如果击中，删除外星人和子弹; P248
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        # 统计分数；collisions 返回的是字典，collisions.values(), 返回的是键值中的值。
        # 检查每个子弹击中的外星人的数量，键值关系：一对多关系
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            # 为啥这里统计的是len(aliens)? 什么原理？aliens 是 collisions.values()中的aliens, 这样就说的通了。
            # groupcollide 返回的是字典，为啥不统计字典中元素的数量呢？
            sb.prep_score()
        # 查看是否生成新的最高分
        check_high_score(stats, sb)
        # 为啥在击中外星人后检查呢？

    if len(aliens) == 0:
        # 当外星人都被消灭之后，清空子弹，并创建新的外星人
        bullets.empty()
        # 每成功击落完后，提高游戏速度
        ai_settings.increase_speed()
        # 提高等级
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)



# 重构前：
# def create_fleet(ai_settings, screen, aliens):
#     # create aliens
#     # create one alien, and count the qty of alien in one lien
#     # the space between alien = alien.width
#     alien = Alien(ai_settings, screen)
#     alien_width = alien.rect.width
#     available_space_x = ai_settings.screen_width - 2 * alien_width
#     number_aliens_x = int(available_space_x/ (2 * alien_width))

#     # create the first aliens
#     for alien_number in range(number_aliens_x):
#         # create an alien and put itto current lien
#         alien = Alien(ai_settings, screen)
#         alien.x = alien_width + 2 * alien_width * alien_number
#         alien.rect.x = alien.x
#         aliens.add(alien)

# 对比：将一个大的封装，根据功能，分拆成3个封装；嵌套函数；
# 好处是方便拓展；容易理解，看着封装名称，基本明白代码的功能；总体来说，封装还是好的

# 重构后：
def get_number_aliens_x(ai_settings, alien_width):
    # count the number of aliens in one lien 
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x


def get_number_rows(ai_settings, alien_height, ship_height):
    # 计算屏幕可容纳的外星人行数
    # 计算可用空间：
    available_space_y = (ai_settings.screen_height - ship_height - 3 * alien_height)
    # 计算外星人行数
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # create an alien and put itto current lien
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    # create aliens
    # create one alien, and count the qty of alien in one lien
    # the space between alien = alien.width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # create the first aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # create an alien and put itto current lien
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

# 写了行数代码，但是没有实现
# alien.rect.y, 写错了，少写了 rect

# AttributeError: module 'game_functions' has no attribute 'update_screen'
# = 一定是哪里没有赋值，仔细查看
# 即使再仔细，也可能错漏的地方；而调试是解决错漏效率最高的方式。
# 当然在写代码的过程中，还是要尽量避免这种错漏
# 写完代码后，脑补一下代码是如何运行的，可以帮助理解，可以发现错误；



def check_fleet_edges(ai_settings, aliens):
    # 当外星人到达边缘时，采取措施
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    # 将整群外星人下移，并改变运动方向
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_factor
        # 是加号，不是减号
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
    # 更新外星人群的中的外星人位置
    # 检查是否有外星人位于屏幕边缘，并更新整群外星人的位置
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人是否和飞船碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        # print('Ship Hit!!!')
        # 打印在终端，不是screen
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)

    # 检查是否有外星人撞倒屏幕底部
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    # 当外星人和飞船相撞
    if stats.ships_left > 0:
        # 扣减剩余数量
        stats.ships_left -= 1

        # 更新得分牌
        sb.prep_ships()

        # 清空外星人和子弹
        aliens.empty()
        bullets.empty()

        # 创建新的外星人，并将飞船放到屏幕中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # sleep
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    # 检查外星人是否到了屏幕底部
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞倒一样处理
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    # 查看是否生成了新的最高分
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
