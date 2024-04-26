import pygame
import random
import time
from pygame import mixer

a1_distance = (350,400,500,600)
a2_distance = (200,700,450,900)
pygame.init()

mixer.init()

sound1 = pygame.mixer.Sound("spacebg.mp3")
pygame.mixer.find_channel(True).play(sound1)

sound2 = pygame.mixer.Sound("shooting.mp3")

screen = pygame.display.set_mode((690,1380))

space = pygame.image.load("space.png")

space = pygame.transform.scale(space,(1090,2080))

#jetpack
jetpack = pygame.image.load("jetpack.png")
jetpack = pygame.transform.scale(jetpack,(170,170))
jetpack = pygame.transform.rotate(jetpack,(270))
jetpack_rect = jetpack.get_rect(topright=(200,690))

#rbutton
rbutton = pygame.image.load("sbutton.png")
rbutton = pygame.transform.scale(rbutton,(120,120))
rbutton = pygame.transform.rotate(rbutton,(270))
rbutton_rect = rbutton.get_rect(topright=(200,100))

#lbutton
lbutton = pygame.image.load("lbutton.png")
lbutton = pygame.transform.scale(lbutton,(120,120))
lbutton = pygame.transform.rotate(lbutton,(270))
lbutton_rect = lbutton.get_rect(topright=(200,1300))

#shootbutton
sbutton = pygame.image.load("shoot.png")
sbutton = pygame.transform.scale(sbutton,(120,120))
sbutton = pygame.transform.rotate(sbutton,(270))
sbutton_rect = sbutton.get_rect(topright=(200,1100))

#bbutton
bbutton = pygame.image.load("bullet.png")
bbutton = pygame.transform.scale(bbutton,(80,80))
bbutton = pygame.transform.rotate(bbutton,(180))
bbutton_rect = bbutton.get_rect(topright=(170,740))

#astroid1
astroid1 = pygame.image.load("astroid1.png")
astroid1= pygame.transform.scale(astroid1,(120,120))
astroid1_rect = astroid1.get_rect(topright=(700,540))

#astroid2
astroid2 = pygame.image.load("astroid2.png")
astroid2 = pygame.transform.scale(astroid2,(120,120))
astroid2_rect = astroid2.get_rect(topright=(1300,900))

#gameover
game_over = pygame.image.load("game_over.png")
game_over= pygame.transform.scale(game_over,(370,370))
game_over= pygame.transform.rotate(game_over,(270))
game_over_rect = game_over.get_rect(topright=(570,590))

score = 0

right_move = False

left_move = False

fire = False

launched = False

i = 10

destroy = 0

while True:
	
	distance = random.choice((a1_distance))
	distance2 = random.choice((a2_distance))
	screen.fill((0,0,0))
	screen.blit(space,(i,0))
	screen.blit(space,(690+i,0))
	if i == -690:
		screen.blit(space,(690+i,0))
		i = 10
		
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			
			pygame.quit()
			
		elif event.type == pygame.MOUSEBUTTONDOWN:
			
			if lbutton_rect.collidepoint(event.pos):
				right_move = True
				
			elif sbutton_rect.collidepoint(event.pos):
				fire = True
				
			elif rbutton_rect.collidepoint(event.pos):
				left_move = True
				
		elif event.type == pygame.MOUSEBUTTONUP:
				left_move = False
				right_move = False
			
	if left_move:
			
			rbutton_rect.clamp_ip(rbutton_rect)
			jetpack_rect.y -= 40
			if not launched:
				bbutton_rect.y -= 40
				
			
	if right_move:
			
			lbutton_rect.clamp_ip(lbutton_rect)
			jetpack_rect.y += 40

			
			if not launched:
				bbutton_rect.y += 40
			
	if fire:
			pygame.mixer.find_channel(True).play(sound2)
			
			launched = True
			sbutton_rect.clamp_ip(sbutton_rect)
			bbutton_rect.x += 100
			
			if bbutton_rect.x >= 690:
				bbutton_rect = bbutton.get_rect(topright=(170,jetpack_rect.y+50))
				fire = False
				launched = False
			
	i -= 10
	
	score += 1
	
	astroid1_rect.x -= 30
	astroid2_rect.x -= 20
	
	if astroid2_rect.colliderect(bbutton_rect) or astroid1_rect.colliderect(bbutton_rect):
		
		destroy += 1
	
	if astroid1_rect.right <= -100 or astroid1_rect.colliderect(bbutton_rect):
		astroid1_rect = astroid1.get_rect(topright = [900,distance])
		
	if astroid2_rect.right <= -100 or astroid2_rect.colliderect(bbutton_rect):
		astroid2_rect = astroid2.get_rect(topright = [900,distance2])
		
			
				
	score_board = pygame.font.Font(None,40)
	load = score_board.render(f"SCORE : {score}",True,"white")
	load = pygame.transform.rotate(load,(270))
	
	attack_board = pygame.font.Font(None,40)
	attack = attack_board.render(f"Destroys : {destroy}",True,"white")
	attack = pygame.transform.rotate(attack,(270))
	
	if jetpack_rect.colliderect(astroid1_rect) or jetpack_rect.colliderect(astroid2_rect):
		mixer.music.load("gameover.mp3")

		mixer.music.play()
		
		screen.blit(game_over,game_over_rect)
		game = pygame.font.Font(None,40)
		over = game.render(f"Score : {score}",True,"white")
		over = pygame.transform.rotate(over,(270))
		screen.blit(over,(200,600))
		
		game = pygame.font.Font(None,40)
		over = game.render(f"Destroys : {destroy}",True,"white")
		over = pygame.transform.rotate(over,(270))
		screen.blit(over,(200,800))
		pygame.display.update()
		time.sleep(3)
		pygame.quit()
		exit()
	screen.blit(load,(660,30))
	screen.blit(attack,(660,1250))
	screen.blit(bbutton,bbutton_rect)
	screen.blit(astroid1,astroid1_rect)
	screen.blit(astroid2,astroid2_rect)
	screen.blit(jetpack,jetpack_rect)
	screen.blit(rbutton,rbutton_rect)
	screen.blit(lbutton,lbutton_rect)
	screen.blit(sbutton,sbutton_rect)

	pygame.display.update()