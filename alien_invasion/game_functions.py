import sys
import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # 响应按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建子弹，并将其加入到编组bullets中
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    # 如果还没有达到限制，就发射一颗子弹
    # 创建子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    # 响应松开按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    # 响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    # 更新屏幕上的图像，切换到新屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面，重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # 显示最新的屏幕
    pygame.display.flip()

def update_bullets(aliens, bullets):
    # 更新子弹位置
    bullets.update()
    
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))

    # 检查子弹是否击中外星人，如果击中，删除外星人和子弹; P248
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True) 

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
#     # create aliens
#     # create one alien, and count the qty of alien in one lien
#     # the space between alien = alien.width
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

def update_aliens(ai_settings, aliens):
    # 更新外星人群的中的外星人位置
    # 检查是否有外星人位于屏幕边缘，并更新整群外星人的位置
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


    
