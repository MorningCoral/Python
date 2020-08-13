import pygame
import random

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE

BOX_WIDTH = 100
BOX_HEIGHT = 50
LEFT_BOX_X = SCREEN_WIDTH * (1/4)
BOX_Y = SCREEN_HEIGHT * (2/3)
RIGHT_BOX_X = SCREEN_WIDTH * (3/4) - BOX_WIDTH

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

light_blue = (93,216,228)
dark_blue = (84,194,205)

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)

prevClick = ('#init', pygame.time.get_ticks()) # (id, time_of_click)


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + 50), 0, 32)
pygame.display.set_caption('Snake')

def text_object(text, fontSize, color=black):
    font = pygame.font.SysFont("monospace", fontSize)
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(id, x, y, width, height, btnColor, btnAction, textMsg, textSize, textColor=black):
    global prevClick
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    btn = pygame.Rect(x, y, width, height) 
    if (x < mouse[0] < x + width) and (y < mouse[1] < y + height):
        btn = btn.inflate(20, 20)
        textSize += int((height/width) * 20)
        # left click
        if click[0] == 1:
            print('click')
            if((prevClick[0] == id) or ((prevClick[0] != id) and (pygame.time.get_ticks() > prevClick[1] + 500))):
                print('action click', id, prevClick)
                prevClick = (id, pygame.time.get_ticks())

                # use recursion to allow multiple m
                if isinstance(btnAction, list):
                    for action, param in btnAction:
                        pass
                        if(param is not None):
                            action(param)
                        else:
                            action()
                else:
                    btnAction()
            else:
                print('click rejected', id, prevClick)
    pygame.draw.rect(screen, btnColor, btn)

    # button text
    textSurface, textRect = text_object(textMsg, textSize, textColor)
    textRect.center = ((x + width/2), (y + height/2))
    screen.blit(textSurface, textRect)

def checkBox():
    pass

def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if(x + y) % 2 == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE),(GRIDSIZE,GRIDSIZE))
                pygame.draw.rect(surface, light_blue, r)
            else:
                rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE),(GRIDSIZE,GRIDSIZE))
                pygame.draw.rect(surface, dark_blue, rr)



class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = black
        self.wall = False
        self.alive = True
        self.pause = False
    
    def get_head_postion(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]* -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point
    
    def move(self):
        cur = self.get_head_postion()
        x, y = self.direction
        # allow pass through walls
        new = ((cur[0] + (x*GRIDSIZE)) % SCREEN_WIDTH, (cur[1] + (y*GRIDSIZE)) % SCREEN_HEIGHT)
        
        # collide with wall
        if self.wall:
            new = ((cur[0] + (x*GRIDSIZE)), (cur[1] + (y*GRIDSIZE)))
            if((not (0 <= new[0] < SCREEN_WIDTH)) or (not (0 <= new[1] < SCREEN_HEIGHT))):
                self.alive = False
                print('collided with wall!')
                return
        # collide with body
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.alive = False
            print('collide with body!')

        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((int(p[0]), int(p[1])), (GRIDSIZE, GRIDSIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, light_blue, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    main_menu()
                if event.key == pygame.K_SPACE:
                   self.pause = not self.pause
                if(not self.pause):
                    if event.key == pygame.K_UP:
                        self.turn(UP)
                    elif event.key == pygame.K_DOWN:
                        self.turn(DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.turn(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.turn(RIGHT)

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = (223, 163, 49)
        self.randomize_position([])

    def randomize_position(self, snake_positions):
        place = False
        while(not place):
            self.position = (random.randint(0, GRID_WIDTH-1) * GRIDSIZE, random.randint(0, GRID_HEIGHT-1) * GRIDSIZE)
            if self.position not in snake_positions:
                place = True
            else:
                print('cannot place food here', self.position)
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, light_blue, r, 1)



class Game:
    def __init__(self):
        self.page = self.main_menu
        self.game_mode = ''
        self.score = 0
        self.new_highscore = False
        # self.pause = False
        self.mode = "easy"
        self.time_battle = False       # easy/hard
        self.time_limit = 5000
        self.highscores = []
        self.read_highscores()
    
    def load_page(self):
        return self.page()

    def set_page(self, page):
        self.page = page

    def reset_time(self):
        self.time = pygame.time.get_ticks()

    def set_mode(self, mode):
        self.mode = mode

    def read_highscores(self):
        score_file = open("snake-highscore.txt","r")
        data = score_file.readlines()
        for line in data:
            line = line.rstrip()
            key, value = line.split(',')
            self.highscores.append([key,int(value)])
        score_file.close()


    def handle_events(self):
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE and self.page == self.play_game:
            #         self.pause = not self.pause
            #         print('pause', self.pause)
              
    def main_menu(self):
        screen.fill(white)

        # title
        title, titleRect = text_object("SNAKE", 100)
        titleRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/4))
        screen.blit(title, titleRect)

        # buttons
        button('#play',SCREEN_WIDTH * (1/2) - 100/2, SCREEN_HEIGHT * (7/16), 100, 50, green, [(self.set_page, self.select_mode)], "PLAY", 30)
        button('#highscores',SCREEN_WIDTH * (1/2) - 210/2, SCREEN_HEIGHT * (10/16), 210, 50, light_blue, [(self.set_page, self.highscore_board)], "HIGHSCORES", 30)
        button('#quit',SCREEN_WIDTH * (1/2) - 100/2, SCREEN_HEIGHT * (13/16), 100, 50, red, self.quit_game, "QUIT", 30)
        
        pygame.display.update()

    def select_mode(self):
        # while True:
        screen.fill(white)

        # title
        title, titleRect = text_object("LEVEL", 60)
        titleRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT *(2/8))
        screen.blit(title, titleRect)
        
        # buttons
        button('#easy', SCREEN_WIDTH * (1/2) - 100/2, SCREEN_HEIGHT * (7/16), 100, 50, light_blue, [(self.set_mode, "easy"), (self.set_page, self.play_game)], "EASY", 30, black)
        button('#hard', SCREEN_WIDTH * (1/2) - 100/2, SCREEN_HEIGHT * (10/16), 100, 50, light_blue, [(self.set_mode, "hard"), (self.set_page, self.play_game)], "HARD", 30)
        
        # time mode
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # text
        timeModeText, timeModeRect = text_object("TIME BATTLE", 30)
        timeModeRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT *(7/8))
        screen.blit(timeModeText, timeModeRect)
        # checkbox
        checkbox = pygame.Rect(SCREEN_WIDTH/5, SCREEN_HEIGHT*(7/8)- 26/2, 26, 26) 
        pygame.draw.rect(screen, black, checkbox, 2)
        global prevClick
        if (SCREEN_WIDTH/5 < mouse[0] < SCREEN_WIDTH/5 + 26) and (SCREEN_HEIGHT*(7/8) - 26/2 < mouse[1] < SCREEN_HEIGHT*(7/8) + 26/2):
            if click[0] == 1:
                if(pygame.time.get_ticks() > prevClick[1] + 500):
                    prevClick = ("#checkbox", pygame.time.get_ticks())
                    self.time_battle = not self.time_battle
                    print('clicked checkbox: ', not self.time_battle)
                else:
                    print('rejected click checkbox')

        if(self.time_battle):
            # cross
            # \
            pygame.draw.line(screen, black, (SCREEN_WIDTH/5, SCREEN_HEIGHT*(7/8)- 26/2),  (SCREEN_WIDTH/5 + 26, SCREEN_HEIGHT*(7/8) + 26/2), 3)
            # /
            pygame.draw.line(screen, black, (SCREEN_WIDTH/5, SCREEN_HEIGHT*(7/8) + 26/2),  (SCREEN_WIDTH/5 + 26, SCREEN_HEIGHT*(7/8) - 26/2), 3)
        pygame.display.update()

    def count_down(self):
        start_time = pygame.time.get_ticks()
        text = '3'
        while True:
            self.handle_events()
        
            screen.fill(black)
            current_time = pygame.time.get_ticks()
            if 1000 < current_time - start_time < 2000:
                text = '2'
            
            if 2000 < current_time -start_time  < 3000:
                text = '1'

            if 3000 < current_time - start_time < 4000:
                text = 'GO!'
            
            if (current_time - start_time) > 4000:
                # play_game()
                break
            
            textSurf, textRect = text_object(text, 100, white)
            textRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
            screen.blit(textSurf, textRect)
            pygame.display.update()

            clock.tick(15)

    def play_game(self):
        self.count_down()
        print("start play_game")
        surface = pygame.Surface(screen.get_size())
        surface = surface.convert()
        drawGrid(surface)

        snake = Snake()
        food = Food()
        
        self.score = 0
        if self.mode == 'hard':
            snake.wall = True
        
        self.reset_time()
        
        while snake.alive and self.page == self.play_game:
            clock.tick(15)
            snake.handle_keys()
            # self.handle_events()

            if(snake.pause):
                # pause
                self.pause_screen()
                self.reset_time()
                continue
            
            drawGrid(surface)
            snake.move()
            
            # eat food
            if snake.get_head_postion() == food.position:
                self.reset_time()
                self.score += 1
                snake.length += 1
                if snake.length == (SCREEN_WIDTH/GRIDSIZE)*(SCREEN_HEIGHT/GRIDSIZE):
                    break
                food.randomize_position(snake.positions)

            snake.draw(surface)
            food.draw(surface)
            screen.blit(surface, (0, 0))
            
            # score display
            scoreText, scoreRect = text_object("Score: {0}".format(self.score), 25, white)
            scoreRect.center = (75, 505)
            screen.blit(scoreText, scoreRect)
            
             # time display
            current_time = pygame.time.get_ticks()
            time_left = round((self.time_limit - (current_time - self.time)) / 1000, 2)

            if(self.time_battle):
                scoreText, scoreRect = text_object("Time: {0}".format(time_left if time_left > 0 else 0 ), 25, white)
                scoreRect.center = (380, 505)
                screen.blit(scoreText, scoreRect)

            pygame.display.update()

            if self.time_battle and time_left < 0 :
                print('exceeded time')
                snake.alive = False
                break

        self.handle_score()

        # next page
        if(snake.alive and self.page == self.play_game):
            print('you win!')
            self.set_page(self.win)
        else:
            print('died')
            self.set_page(self.game_over)

    def handle_score(self):
        # handle highscore
        if(self.mode == "easy" and self.time_battle == False):
            if(self.score > self.highscores[0][1]):
                self.highscores[0][1] = self.score
                self.new_highscore = True
        elif(self.mode == "easy" and self.time_battle == True):
            if(self.score > self.highscores[1][1]):
                self.highscores[1][1] = self.score
                self.new_highscore = True
        elif(self.mode == "hard" and self.time_battle == False):
            if(self.score > self.highscores[2][1]):
                self.highscores[2][1] = self.score
                self.new_highscore = True
        elif(self.mode == "hard" and self.time_battle == True):
            if(self.score > self.highscores[3][1]):
                self.highscores[3][1] = self.score
                self.new_highscore = True

        # write out
        score_file = open("snake-highscore.txt","w")
        for x in self.highscores:
            score_file.write("{},{}\n".format(x[0],x[1]))
            
        score_file.close()
        
    def get_highscore(self):
        if(self.mode == "easy" and self.time_battle == False):
            return self.highscores[0][1]
        elif(self.mode == "easy" and self.time_battle == True):
            return self.highscores[1][1]
        elif(self.mode == "hard" and self.time_battle == False):
            return self.highscores[2][1]
        elif(self.mode == "hard" and self.time_battle == True):
            return self.highscores[3][1]


    def pause_screen(self):
        screen.fill(black)
        pauseText, pauseRect = text_object("PAUSE", 60, white)
        pauseRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT * (2/5))
        screen.blit(pauseText, pauseRect)

        button('#exit', SCREEN_WIDTH * (1/2) - 100/2, SCREEN_HEIGHT * (3/5), 100, 50, light_blue, [(self.set_page, self.game_over)], "EXIT", 30)

        pygame.display.update()

    def quit_game(self):
        pygame.quit()
        quit()


    def game_over(self):
        screen.fill(black)

        # title
        title, titleRect = text_object("GAME OVER", 60, white)
        titleRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT *(2/8))
        screen.blit(title, titleRect)

        # score display
        scoreText, scoreRect = text_object("Score: {0}".format(self.score), 35, white)
        scoreRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT * (3/8))
        screen.blit(scoreText, scoreRect)
        
        # highscore display
        highscoreText, highscoreRect = text_object("Highscore: {0}".format(self.get_highscore()), 35, white)
        highscoreRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT * (4/8))
        screen.blit(highscoreText, highscoreRect)

        # buttons
        button('#restart', SCREEN_WIDTH * (1/2) - 150/2, SCREEN_HEIGHT * (10/16), 150, 50, green, [(self.set_page, self.play_game)], "RESTART", 30)
        button('#menu', SCREEN_WIDTH * (1/2) - 100/2, SCREEN_HEIGHT * (13/16), 100, 50, light_blue, [(self.set_page, self.main_menu)], "MENU", 30)

        pygame.display.update()

    def win(self):
        screen.fill(white)

        # title
        title, titleRect = text_object("YOU WIN!", 60, black)
        titleRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT *(2/8))
        screen.blit(title, titleRect)

        # score display
        scoreText, scoreRect = text_object("Score: {0}".format(self.score), 35, black)
        scoreRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT * (3/8))
        screen.blit(scoreText, scoreRect)
        
        # buttons
        button('#restart', SCREEN_WIDTH * (1/2) - 150/2, SCREEN_HEIGHT * (9/16), 150, 50, green, [(self.set_page, self.play_game)], "RESTART", 30)
        button('#menu', SCREEN_WIDTH * (1/2) - 100/2, SCREEN_HEIGHT * (12/16), 100, 50, light_blue, [(self.set_page, self.main_menu)], "MENU", 30)

        pygame.display.update()


    def highscore_board(self):
        screen.fill(white)

        # title
        title, titleRect = text_object("HIGHSCORES", 40, black)
        titleRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT *(1/8))
        screen.blit(title, titleRect)

        # score display
        i = 2
        labels = {'easy-untimed': 'Easy (untimed)', 'easy-timed': 'Easy (timed)', 'hard-untimed': 'Hard (untimed)', 'hard-timed': 'Hard (timed)'}
        for key, value in self.highscores:
            textSurface, textRect = text_object("{:14} : {}".format(labels[key], value), 25, black)
            textRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT * (i/8))
            screen.blit(textSurface, textRect)
            i += 1

        # text1, textRect1 = text_object("{:20}{}".format("Easy (not timed):",self.score), 25, black)
        # textRect1.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT * (2/8))
        # screen.blit(text1, textRect1)

        # text2, textRect2 = text_object("{:20}{}".format("Easy (timed):",self.score), 25, black)
        # textRect2.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT * (3/8))
        # screen.blit(text2, textRect2)

        # text3, textRect3 = text_object("{:20}{}".format("Hard (not timed):",self.score), 25, black)
        # textRect3.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT * (4/8))
        # screen.blit(text3, textRect3)

        # text4, textRect4 = text_object("{:20}{}".format("Hard (timed):",self.score), 25, black)
        # textRect4.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT * (5/8))
        # screen.blit(text4, textRect4)

        
        # buttons
        button('#menu', SCREEN_WIDTH * (1/2) - 100/2, SCREEN_HEIGHT * (14/16), 100, 50, light_blue, [(self.set_page, self.main_menu)], "MENU", 30)

        pygame.display.update()

# game init

game = Game()
while True:
    game.handle_events()
    # game.main_menu()
    game.load_page()

# intro()
# game_over(12)
# count_down()
# play_game()
# choose_level()
