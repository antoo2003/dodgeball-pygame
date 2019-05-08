#First PyGame
import pygame, sys
pygame.init()
import random
#variables
FPS = 30
WINDOW_SIZE = (1000,700)
fps_clock = pygame.time.Clock()
BLACK = (0,0,0)
AQUAMARINE = (41,84,116)
GREEN = (51,121,19)
BLUE = (24,37,232)
RED = (234,26,19)
YELLOW = (228,242,60)
SKIN_COLOR = (225,222,168)
WHITE = (225,225,225)
blue_score = 0
red_score = 0
character_1_x = 200
character_1_y = 400
character_2_x = 600
character_2_y = 350
dodgeball_x = 500
dodgeball_y = 350
dodgeball_2_x = 500
dodgeball_2_y = 500
dodgeball_3_x = 500
dodgeball_3_y = 200
half_line_x = 500
half_line_y = 0
dodgeball_color = YELLOW

ball_speed = 0
ball_speed_2 = 0
ball_speed_3 = 0
right_wall_x = 1000
right_wall_y = 0
left_wall_x = 0
left_wall_y = 0
ball_placement_count = 0
score_counter = 0



#functions
def character_1_shape(x,y):
	pygame.draw.rect(screen, BLACK, (x-14, y-10,26,65))
	pygame.draw.circle(screen, BLUE, (x+9,y-10),10) #(200,400)
	pygame.draw.rect(screen, BLUE,(x,y,16,30))
	pygame.draw.rect(screen, BLUE,(x+17,y,5,15))
	pygame.draw.rect(screen, BLUE,(x-6,y,5,15))
	pygame.draw.rect(screen, BLUE,(x+8,y+30,8,15))
	pygame.draw.rect(screen, BLUE,(x,y+30,8,15))
	pygame.draw.line(screen, BLACK,(x+7,y+30),(x+7,y+45),1)
def character_1_head(x,y):
	pygame.draw.circle(screen,BLUE,(x+9,y-10),10)
def character_2_head(x,y):
	pygame.draw.circle(screen,RED,(x+9,y-10),10)
def character_2_shape(x,y):
	#hitbox
	pygame.draw.rect(screen, BLACK, (x-14, y-10,26,65))
	pygame.draw.circle(screen, RED, (x+9,y-10),10) #(400,600)
	pygame.draw.rect(screen, RED,(x,y,16,30))
	pygame.draw.rect(screen, RED,(x-6,y,5,15))
	pygame.draw.rect(screen, RED,(x+17,y,5,15))
	pygame.draw.rect(screen, RED,(x,y+30,8,15))
	pygame.draw.rect(screen, RED,(x+8,y+30,8,15))
	pygame.draw.line(screen, BLACK,(x+7,y+30),(x+7,y+45),1)
def dodgeball(x,y,dodgeball_color):
	pygame.draw.rect(screen, BLACK, (x-20,y-20,40,40))
	pygame.draw.circle(screen, dodgeball_color, (x,y),20)
def dodgeball_2(x,y,dodgeball_color):
	pygame.draw.rect(screen, BLACK, (x-20,y-20,40,40))
	pygame.draw.circle(screen, dodgeball_color, (x,y),20)
def dodgeball_3(x,y,dodgeball_color):
	pygame.draw.rect(screen, BLACK, (x-20,y-20,40,40))
	pygame.draw.circle(screen, dodgeball_color, (x,y),20)
def half_line(x,y):
	pygame.draw.rect(screen,BLACK,(x,y,3,1000))
	pygame.draw.line(screen, WHITE,(x,y),(x,y+700),3)
def right_wall(x,y):
	pygame.draw.rect(screen, WHITE,(x,y,1,700))
def left_wall(x,y):
	pygame.draw.rect(screen, WHITE,(x,y,1,700))
	
#set up window
screen = pygame.display.set_mode(WINDOW_SIZE)

my_font_1 = pygame.font.Font('FjallaOne-Regular.ttf',48)
text_1 = my_font_1.render('Blue Score: ' + str(blue_score), True, BLUE)
textRect_1 = text_1.get_rect()
textRect_1.center = (150, 100)
my_font_2 = pygame.font.Font('FjallaOne-Regular.ttf',48)
text_2 = my_font_2.render('Red Score: ' + str(red_score), True, RED)
textRect_2 = text_2.get_rect()
textRect_2.center = (850, 100)

#game loop
while True:
	#draw stuff here
	screen.fill(BLACK)
	ball_placement_list = [50,80,110,140,170,200,230,260,290,320,350,380,410,440,470,500,530,560,590,620,650,680]
	random_number = random.choice(ball_placement_list)
	ball_placement = random_number
	my_font_1 = pygame.font.Font('FjallaOne-Regular.ttf',48)
	text_1 = my_font_1.render('Blue Score: ' + str(blue_score), True, BLUE)
	textRect_1 = text_1.get_rect()
	textRect_1.center = (150, 100)
	my_font_2 = pygame.font.Font('FjallaOne-Regular.ttf',48)
	text_2 = my_font_2.render('Red Score: ' + str(red_score), True, RED)
	textRect_2 = text_2.get_rect()
	textRect_2.center = (850, 100)
	screen.blit(text_1, textRect_1)
	screen.blit(text_2, textRect_2)
	
	#Drawing characters and hitboxes
	character_2_shape(character_2_x, character_2_y)
	character_1_shape(character_1_x,character_1_y)
	character_1_head(character_1_x,character_1_y)
	character_2_head(character_2_x,character_2_y)
	dodgeball(dodgeball_x,dodgeball_y,dodgeball_color)
	dodgeball_2(dodgeball_2_x,dodgeball_2_y,dodgeball_color)
	dodgeball_3(dodgeball_3_x,dodgeball_3_y,dodgeball_color)
	
	#Setting rects
	half_line(half_line_x, half_line_y)
	keystate = pygame.key.get_pressed()
	dodgeball_x += ball_speed
	dodgeball_2_x += ball_speed_2
	dodgeball_3_x += ball_speed_3
	dodgeball.Rect = pygame.Rect(dodgeball_x,dodgeball_y,40,40)
	dodgeball_2.Rect = pygame.Rect(dodgeball_2_x,dodgeball_2_y,40,40)
	dodgeball_3.Rect = pygame.Rect(dodgeball_3_x,dodgeball_3_y,40,40)
	character_1_shape.Rect = pygame.Rect(character_1_x, character_1_y,26,25)
	character_1_head.Rect = pygame.Rect(character_1_x, character_1_y,26,25)
	character_2_shape.Rect = pygame.Rect(character_2_x, character_2_y, 26,25)
	character_2_head.Rect = pygame.Rect(character_1_x, character_1_y,26,25)
	right_wall.Rect = pygame.Rect(right_wall_x,right_wall_y,1,700)
	left_wall.Rect = pygame.Rect(left_wall_x,left_wall_y,1,700)
	
	#character movement
	if keystate[pygame.K_a]:
		a = True
		if a:
			character_1_x -= 10
	if keystate[pygame.K_d]:
		d = True
		if d:
			character_1_x += 10
	if keystate[pygame.K_w]:
		w = True
		if w:
			character_1_y -= 10
	if keystate[pygame.K_s]:
		s = True
		if s:
			character_1_y += 10
	if keystate[pygame.K_LEFT]:
		LEFT = True
		if LEFT:
			character_2_x -= 10
	if keystate[pygame.K_RIGHT]:
		RIGHT = True
		if RIGHT:
			character_2_x += 10
	if keystate[pygame.K_UP]:
		UP = True
		if UP:
			character_2_y -= 10
	if keystate[pygame.K_DOWN]:
		DOWN = True
		if DOWN:
			character_2_y += 10
	
	#maintaining speeds
	if character_1_y <= 0:
		character_1_y +=10
	if character_1_y >= 660:
		character_1_y -=10
	if character_2_y <= 0:
		character_2_y +=10
	if character_2_y >= 660:
		character_2_y -=10
	if character_1_x <= 0:
		character_1_x += 10
	if character_2_x >= 1000:
		character_2_x -= 10
	if character_1_x == 500:
		character_1_x -= 10
	if character_2_x == 500:
		character_2_x += 10
	
	#collisions
	#dodgeball 1
	if character_1_shape.Rect.colliderect(dodgeball.Rect):
		ball_speed = ball_speed + 20
	if character_1_head.Rect.colliderect(dodgeball.Rect):
		ball_speed = ball_speed + 10
	if character_2_shape.Rect.colliderect(dodgeball.Rect):
		ball_speed = ball_speed - 10
	if character_2_head.Rect.colliderect(dodgeball.Rect):
		ball_speed = ball_speed - 10
	if right_wall.Rect.colliderect(dodgeball.Rect):
		ball_speed -= 10
		blue_score += 1     
	if left_wall.Rect.colliderect(dodgeball.Rect):
		ball_speed += 10
		red_score += 1
	if ball_speed > 10:
		ball_speed = 10
	if ball_speed < -10:
		ball_speed = -10
	if ball_speed == 0:
		if dodgeball_color == BLUE:
			ball_speed += 10
	if ball_speed == 0:
		if dodgeball_color == RED:
			ball_speed -= 10
	if ball_speed == 0:
		ball_speed += 5
	
	#dodgeball 2
	if character_1_shape.Rect.colliderect(dodgeball_2.Rect):
		ball_speed_2 = ball_speed_2 + 20
	if character_1_head.Rect.colliderect(dodgeball_2.Rect):
		ball_speed_2 = ball_speed_2 + 10
	if character_2_shape.Rect.colliderect(dodgeball_2.Rect):
		ball_speed_2 = ball_speed_2 - 10
	if character_2_head.Rect.colliderect(dodgeball_2.Rect):
		ball_speed_2 = ball_speed_2 - 10
	if right_wall.Rect.colliderect(dodgeball_2.Rect):
		ball_speed_2 -= 10
		blue_score += 1     
	if left_wall.Rect.colliderect(dodgeball_2.Rect):
		ball_speed_2 += 10
		red_score += 1
	if ball_speed_2 > 10:
		ball_speed_2 = 10
	if ball_speed_2 < -10:
		ball_speed_2 = -10
	if ball_speed_2 == 0:
		if dodgeball_color == BLUE:
			ball_speed_2 += 10
	if ball_speed_2 == 0:
		if dodgeball_color == RED:
			ball_speed_2 -= 10
	if ball_speed_2 == 0:
		ball_speed_2 += 5
	
	#dodgeball 3
	if character_1_shape.Rect.colliderect(dodgeball_3.Rect):
		ball_speed_3 = ball_speed_3 + 20
	if character_1_head.Rect.colliderect(dodgeball_3.Rect):
		ball_speed_3 = ball_speed_3 + 10
	if character_2_shape.Rect.colliderect(dodgeball_3.Rect):
		ball_speed_3 = ball_speed_3 - 10
	if character_2_head.Rect.colliderect(dodgeball_3.Rect):
		ball_speed_3 = ball_speed_3 - 10
	if right_wall.Rect.colliderect(dodgeball_3.Rect):
		ball_speed_3 -= 10
		blue_score += 1
	if left_wall.Rect.colliderect(dodgeball_3.Rect):
		ball_speed_3 += 10
		red_score += 1
	if ball_speed_3 > 10:
		ball_speed_3 = 10
	if ball_speed_3 < -10:
		ball_speed_3 = -10
	if ball_speed_3 == 0:
		if dodgeball_color == BLUE:
			ball_speed_3 += 10
	if ball_speed_3 == 0:
		if dodgeball_color == RED:
			ball_speed_3 -= 10
	if ball_speed_3 == 0:
		ball_speed_3 += 5
	if score_counter == 10:
		blue_score = 0
		red_score = 0
	score_counter += 1
	
	#event handlers
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	if blue_score >= 50.0:
		sys.exit()
		
	if red_score >= 50.0:
		sys.exit()
		
	#refresh the screen
	pygame.display.update()
	fps_clock.tick(FPS)


