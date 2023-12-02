from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

# (self, player_image, player_x, player_y, size_x, size_y, player_speed)
rocket_1 = Player("rocket_1.png", 25, 200, 25, 150, 5) 
rocket_2 = Player("rocket_1.png", 550, 200, 25, 150, 5) 
ball = GameSprite("ball.png",  200, 200, 50, 50, 5)

speed_x = 5
speed_y = 5

win_width = 600
win_height = 500
display.set_caption("П И Н Г - П О Н Г")
window = display.set_mode((win_width, win_height))
background = (55,155,55)
window.fill(background)
# background = transform.scale(image.load(img_back), (win_width, win_height))
font.init()
font = font.Font(None, 36)
lose_1 = font.render('ЛЕВЫЙ ПРОИГРАЛ', True, (255,255,0))
lose_2 = font.render('ПРАВЫЙ ПРОИГРАЛ', True, (255,255,0))

game = True
finish = False
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(background)
        rocket_1.update_l()
        rocket_2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(rocket_1, ball) or sprite.collide_rect(rocket_2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose_1, (200, 200))
            game_over = True
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose_2, (200, 200))
            game_over = True    
        rocket_1.reset()
        rocket_2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)




# gameIcon = image.load('rocket.png')
# display.set_icon(gameIcon)

# #фоновая музыка
# mixer.init()
# mixer.music.load('Kim and Buran - Mystery of the Third Planet.mp3')
# mixer.music.play()
# fire_sound = mixer.Sound('blaster.ogg')
# lose_sound = mixer.Sound('mario_lose.ogg')
# win_sound = mixer.Sound('mario_win.ogg')
# mixer.music.set_volume(0.5)

# #шрифты и надписи
# font.init()
# font2 = font.SysFont('Arial', 36)
# font1 = font.SysFont('Arial', 80)
# win = font1.render('ПОБЕДА', True, (255,255,0))
# lose = font1.render('ПРОИГРАЛ', True, (255,0,0))




# score = 0 #сбито кораблей
# lost = 0 #пропущено кораблей
# max_lost = 3
# goal = 10



#метод "выстрел" (используем место игрока, чтобы создать там пулю)
    # def fire(self):
    #     bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
    #     bullets.add(bullet)

# class Bullet(GameSprite):
#     #движение врага
#     def update(self):
#         self.rect.y += self.speed
#         #исчезает, если дойдет до края экрана
#         if self.rect.y < 0:
#             self.kill()

# #класс спрайта-врага  
# class Enemy(GameSprite):
#     #движение врага
#     def update(self):
#         self.rect.y += self.speed
#         global lost
#         #исчезает, если дойдет до края экрана
#         if self.rect.y > win_height:
#             self.rect.x = randint(80, win_width - 80)
#             self.rect.y = 0
#             lost += 1



# #создаём спрайты
# ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)

# monsters = sprite.Group()
# for i in range(1, 6):
#     monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
#     monsters.add(monster)

# bullets = sprite.Group()

# #переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
# finish = False
# #Основной цикл игры:
# run = True #флаг сбрасывается кнопкой закрытия окна
# while run:
#     #событие нажатия на кнопку “Закрыть”
#     for e in event.get():
#         if e.type == QUIT:
#             run = False
#         elif e.type == KEYDOWN:
#             if e.key == K_SPACE:
#                 fire_sound.play()
#                 ship.fire()

#     if not finish:
#         #обновляем фон
#         window.blit(background,(0,0))
#         #пишем текст на экране
#         text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
#         window.blit(text, (10, 20))
#         text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
#         window.blit(text_lose, (10, 50))
#         #производим движения спрайтов
#         ship.update()
#         monsters.update()
#         bullets.update()
#         #обновляем их в новом местоположении при каждой итерации цикла
#         ship.reset()
#         monsters.draw(window)
#         bullets.draw(window)
#         collides = sprite.groupcollide(monsters, bullets, True, True)
#         for c in collides:
#             score += 1
#             monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1,5))
#             monsters.add(monster)
#         if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
#             finish = True
#             window.blit(lose, (200,200))
#             lose_sound.play()
#         if score >= goal:
#             finish = True
#             window.blit(win, (200,200))
#             win_sound.play()
#         display.update()

#     else:
#         finish = False
#         score = 0
#         lost = 0
#         for b in bullets:
#             b.kill()
#         for m in monsters:
#             m.kill()
#         time.delay(5000)
#         for i in range(1, 6):
#             monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
#             monsters.add(monster)

#     #цикл срабатывает каждую 0.05 секунд
#     time.delay(50)
