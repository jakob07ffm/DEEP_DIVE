import pygame
import random

pygame.mixer.init()
pygame.init()

back_sound = pygame.mixer.Sound("Sound/background_sound.mp3")
back_sound.set_volume(0.5)                                                                                                                                                                  
back_sound.play(-1)
wave_sound = pygame.mixer.Sound("Sound/wave.flac")
wave_sound_played = False
game_over_sound = pygame.mixer.Sound("Sound/game_over.mp3")
game_over_sound_played = False
diving_sound = pygame.mixer.Sound("Sound/diving.mp3")
diving_sound_played = False

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
r_red = (239, 98, 98)

player_x = 500
player_y = 580
player_width = 60
player_height = 60
player_speed = 10
player_left_image = pygame.image.load("Assets/diver_left.png")
player_right_image = pygame.image.load("Assets/diver_right.png")
player_still_image = pygame.image.load("Assets/diver_still.png")
player_image = player_still_image

win_x = 1000
win_y = 1000

camera_y = 0

clock = pygame.time.Clock() 

water_start = 590

tank_0_6 = pygame.image.load("Assets/tank_0_6.png")
tank_1_6 = pygame.image.load("Assets/tank_1_6.png")
tank_2_6 = pygame.image.load("Assets/tank_2_6.png")
tank_3_6 = pygame.image.load("Assets/tank_3_6.png")
tank_4_6 = pygame.image.load("Assets/tank_4_6.png")
tank_5_6 = pygame.image.load("Assets/tank_5_6.png")
tank_6_6 = pygame.image.load("Assets/tank_6_6.png")
 
font_size = 40
font = pygame.font.Font("font/upheavtt.ttf", font_size)

small_font_size = 20
small_font = pygame.font.Font('font/upheavtt.ttf', small_font_size)

text_bar = small_font.render("Air", True, (black)) 
text_bar_x = 495  
text_bar_y = 140 

timer = 0 

air_bar_width = 200
air_bar_height = 40
air_bar_x = 460
air_bar_y = player_y - 420
back_air_bar_x = 460
back_air_bar_y = player_y - 420
back_air_bar_width = 200
back_air_bar_height = 40
air_usage = 4

chest_image = pygame.image.load("Assets/chest.png")
resized_chest_image = pygame.transform.scale(chest_image, (200, 200))
chest_x = 400
chest_y = 2500

back_image_x = 0
back_image_y = 0
back_min_y = 500
back_max_y = 2500
back_image = pygame.image.load("Assets/ocean.png")

ship_x = 500 
ship_y = 435
ship_x = 0
ship_min_x = False
ship_image = pygame.image.load("Assets/ship.png")
resized_ship_image = pygame.transform.scale(ship_image, (300, 300))
flipped_ship_image = pygame.transform.flip(resized_ship_image, True, False)

tank_level = 1

coins = []
coin_image = pygame.image.load("Assets/coin.png")
coin_sound =  pygame.mixer.Sound("Sound/coin.mp3")
resized_coin_image = pygame.transform.scale(coin_image, (30, 30))
red_gem_image = pygame.image.load("Assets/red_gem.png")
green_gem_image = pygame.image.load("Assets/green_gem.png")
money = 0
for _ in range(50):
        coin_x = random.randint(0, 1000 - 20)  
        coin_y = random.randint(600, 2400 - 20)
        
        coins.append((coin_x, coin_y))

win = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption("Tauch_Spiel")

def player_movement():
    
    global player_x, player_y, back_image_y, ship_y, player_left_image, player_image, player_right_image, fish_y, fish_x #global wenn man üerall im code daraf zugreifen kann
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and player_x >= -10:
        player_x -= player_speed
        player_image = player_left_image
    if keys[pygame.K_d] and player_x <= 950:
        player_x += player_speed
        player_image = player_right_image
    if keys[pygame.K_w] and player_y > 580:
        player_y -= player_speed
        player_image = player_still_image
    if keys[pygame.K_s] and player_y < back_max_y:
        player_y += player_speed
        player_image = player_still_image

def game_over():
    global player_x, player_y, game_over_sound_played, tank_level
    if game_over_sound_played == False:
        game_over_sound.play(0)
        game_over_sound_played == True
    if game_over_sound_played == True:
        game_over_sound.stop()
        game_over_sound_played = False
    player_y = 580 
    player_x = 500
    tank_level = 1
    
    

def sound_controll():
    global wave_sound_played, diving_sound_played
    if player_y >= 590:
        if wave_sound_played == True:
            wave_sound.fadeout(2000)
            wave_sound_played = False
        if diving_sound_played == False:
            diving_sound.play(-1)
            diving_sound_played = True
    if player_y <= 590:
        if wave_sound_played == False:
            wave_sound.play(-1)
            wave_sound_played = True
        if diving_sound_played == True:
            diving_sound.fadeout(2000)
            diving_sound_played = False
            

def ship_movement():
    global ship_x, ship_min_x
    ship_speed = 1

    if ship_x >= 0 and ship_min_x == False:
        ship_x -= ship_speed
        if ship_x <= 0:
            ship_min_x = True
    if ship_min_x == True and ship_x <= 700:
        ship_x += ship_speed
        if ship_x >= 700:
            ship_min_x = False


            
def spawn_coin():
    coin_x = random.randint(0, 1000 - 20)  
    coin_y = random.randint(600, 1000 - 20)  
    coins.append((coin_x, coin_y))

start_game = False
tutorial = False
show_tutorial = False
running = False
while not start_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                start_game = True
                show_tutorial = True
            if event.key == pygame.K_p:
                start_game = True
                running = True
            

    start_text = font.render("Play = 'p'", True, white)
    start_text_rect = start_text.get_rect(center=(win_x // 2, win_y // 2))
    
    tutorial_start_text = font.render("Tutorial = 't'", True, white)
    tutorial_start_text_rect = tutorial_start_text.get_rect(center=(win_x // 2, 600))
    
    haed_text = font.render("DEEP_DIVER", True, white)
    haed_text_rect = haed_text.get_rect(center=(500, 40))  #center is the pos of the center of the pic
    
    win.blit(haed_text, haed_text_rect) 
    win.blit(tutorial_start_text, tutorial_start_text_rect) 
    win.blit(start_text, start_text_rect)
    pygame.display.update()
    

while show_tutorial:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                show_tutorial = False
                running = True 
    win.fill(black)
    head_tutorial_text = small_font.render("Tutorial:" , True, (white))
    head_tutorial_text_rect = head_tutorial_text.get_rect()
    head_tutorial_text_rect.topleft = (40, 40)
    
    tutorial_text = small_font.render("The money counter counts how much money you have collected." , True, (white))
    tutorial_text_rect = tutorial_text.get_rect()
    tutorial_text_rect.topleft = (40, 100)
    
    tow_tutorial_text = small_font.render("Coins = 1, Green Gems  = 2, Red Gems = 5" , True, (white))
    tow_tutorial_text_rect = tow_tutorial_text.get_rect()
    tow_tutorial_text_rect.topleft = (40, 120)
    
    tree_tutorial_text = small_font.render("The tank level counter shows what level your tank has. Higher = longer diving" , True, (white))
    tree_tutorial_text_rect = tree_tutorial_text.get_rect()
    tree_tutorial_text_rect.topleft = (40, 140)
    
    four_tutorial_text = small_font.render("If you have enough money for the next tank level, you will be upgraded automatically." , True, (white))
    four_tutorial_text_rect = four_tutorial_text.get_rect()
    four_tutorial_text_rect.topleft = (40, 160)
    
    five_tutorial_text = small_font.render("The level costs increase exponentially" , True, (white))
    five_tutorial_text_rect = five_tutorial_text.get_rect()
    five_tutorial_text_rect.topleft = (40, 180)
    
    six_tutorial_text = small_font.render("p = Play", True, (white))
    six_tutorial_text_rect = six_tutorial_text.get_rect()
    six_tutorial_text_rect.topleft = (40, 180)
    
    win.blit(head_tutorial_text, head_tutorial_text_rect)
    win.blit(tutorial_text, tutorial_text_rect)
    win.blit(tow_tutorial_text, tow_tutorial_text_rect)
    win.blit(tree_tutorial_text, tree_tutorial_text_rect)
    win.blit(four_tutorial_text, four_tutorial_text_rect)
    win.blit(five_tutorial_text, five_tutorial_text_rect)
    win.blit(six_tutorial_text, six_tutorial_text_rect)
    pygame.display.update()
    
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
           
    player_movement()
    sound_controll()
    ship_movement()
 
    if player_y >= water_start:
        air_bar_width -= air_usage
    if player_y <= water_start and air_bar_width <= back_air_bar_width:
        air_bar_width += air_usage      

    if air_bar_width < 0:
        game_over()
        money = 0        
        game_over_text = font.render("YOU Died!", True, (black))
        game_over_text_rect = game_over_text.get_rect(center=(win_x / 2, 500))
        win.blit(game_over_text, game_over_text_rect)
        pygame.display.update()
        
        
    camera_y = player_y - win_y // 2
    
    win.fill(black)
    win.blit(back_image, (back_image_x, back_image_y - camera_y)) 
    
    if ship_x >= 0 and ship_min_x == False:
        win.blit(resized_ship_image, (ship_x, ship_y - camera_y))
    if ship_min_x == True and ship_x <= 700:
        win.blit(flipped_ship_image, (ship_x, ship_y - camera_y))
        
    for coin in coins:
        coin_rect = pygame.Rect(coin[0], coin[1] - camera_y, 20, 20)
        if coin[1] <= 1000:
            win.blit(resized_coin_image, coin_rect)
        if coin[1] <= 1600 and coin[1] > 1000:
            win.blit(green_gem_image, coin_rect)
        if coin[1] <= 2300 and coin[1] > 1600:
            win.blit(red_gem_image, coin_rect)
        player_rect = pygame.Rect(player_x, player_y - camera_y, player_width, player_height)
        if player_rect.colliderect(coin_rect):
            coins.remove(coin)
            if coin[1] <= 1000: 
                money += 1
            if coin[1] <= 1600 and coin[1] > 1000:
                money += 2
            if coin[1] <= 2300 and coin[1] > 1600:
                money += 5
            coin_sound.play(0)
            spawn_coin()
           
    air_usage = 0.25       
    if money >= 10:
        air_usage = 3
        tank_level = 2
    if money >= 20:
        air_usage = 2
        tank_level = 3
    if money >= 40:
        air_usage = 1
        tank_level = 4
    if money >= 80:
        air_usage = 0.5
        tank_level = 5
    if money >= 160:
        air_usage = 0.25   # ist mehr als genug
        tank_level = 6
        
    if player_y >= 2400:
        win_text = font.render("YOU WON!", True, (black))
        win_text_rect = win_text.get_rect(center=(win_x / 2, 500))
        win.blit(win_text, win_text_rect)
    

    money_text = small_font.render("Money: " + str(money), True, (black))
    money_text_rect = money_text.get_rect()
    money_text_rect.x = 20
    money_text_rect.y = 40
    win.blit(money_text, money_text_rect)
    
    tank_level_text = small_font.render("Tank level: " + str(tank_level), True, (black))
    tank_level_text_rect = tank_level_text.get_rect()
    tank_level_text_rect.x = 20
    tank_level_text_rect.y = 80
    win.blit(tank_level_text, tank_level_text_rect)
    win.blit(resized_chest_image, (chest_x, chest_y - camera_y))
    win.blit(player_image, (player_x, player_y - camera_y))
    win.blit(text_bar, (text_bar_x, text_bar_y))
    back_air_bar = pygame.draw.rect(win, black, pygame.Rect(back_air_bar_x, back_air_bar_y, back_air_bar_width, back_air_bar_height), 2)
    usage_air_bar = pygame.draw.rect(win, (3, 36, 112), pygame.Rect(air_bar_x, air_bar_y, air_bar_width, air_bar_height))
  
    pygame.display.update()

pygame.quit()
