import pygame

pygame.init()

fps = 60
clock = pygame.time.Clock()

#screen settings

background_image = pygame.image.load("images/mass_effect_andromeda_planet__7_4k_wallpaper_by_allanzax_dbr9sti-fullview.jpg")
hight = 900
width = 1500
screen = pygame.display.set_mode((width, hight))
pygame.display.set_caption('space invaders')

#lives_bar
ship_bmp_lives = pygame.transform.scale(pygame.image.load("images/starship.png"), (40, 40))

#ship settings

lives = 3
ship_bmp = pygame.transform.scale(pygame.image.load("images/starship.png"), (65, 65))
ship_gs = pygame.sprite.GroupSingle()

#aliens settings

aliens_pngs = ["images/ufodark.png", "images/ufo.png"]
aliens_images = [pygame.transform.scale(pygame.image.load(alien_png), (80, 80)) for alien_png in aliens_pngs]
speed = 1

#alien group size
rows = 1
columns = 7

#collision sounds

memes_wav = ["sounds/bruh.wav", "sounds/emotional_damage.wav"]
memes = [pygame.mixer.Sound(meme_wav) for meme_wav in memes_wav]

kills_wav = ["sounds/yeet.wav", "sounds/hehe_boi.wav", "sounds/nice.wav"]
kills = [pygame.mixer.Sound(kill_wav) for kill_wav in kills_wav]

#projectile

projectile_image1 = pygame.transform.scale(pygame.image.load("images/torpedo.png"), (30, 30))
projectile_image2 = pygame.transform.scale(pygame.image.load("images/torpedodark.png"), (30, 30))
#shot_sound = pygame.mixer.Sound("sounds/yeet.wav")
 #timing alien fire
time = pygame.time.get_ticks()

#ending screen
game_over = pygame.transform.scale(pygame.image.load("images/rip.jpg"), (width, hight))
sad = pygame.mixer.Sound("sounds/sad.wav")

level = 1

#score
font = pygame.font.Font("fonts/Royalacid.ttf", 32)
