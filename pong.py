'''
    Name: Pong (CST8279 Final Project)
    Description: Pong, but for Python
    Coder: Matt Beaudin
    Date: 2026-03-23

    Requirements:
    - This should be as close as we can get to the original 1972 version of Pong.
    - The keyboard should allow for two players. Player one uses the up/down directional keys, and Player 2 uses Q/A
    - There should be a simple way to exit the game and pause it.
    - There should be a scoreboard visible as well.

    As a nostalgic note, There use to be a game played in the browser in the early 2000s called
    slime volleyball, and it could be played with two players on one keyboard. I think the
    playability of that game influenced me here. We can forget the fact that it was over 20
    years ago and move on I suppose :)

    I also decided to not use turtle, and use a different library, pygame, in this case. Somewhat as an additional challenge,
    and I guess the other part as I wanted something a bit more aesthetically pleasing.

    This also targets Python 3.10, which is compatible with Pygame. 3.14 didn't really work for me.
'''

# import modules
import sys, pygame, random

# initialize pygame
pygame.init()

#initialize a font as well, since I want to display the score.
pygame.font.init()

# create the font object
font_path = "images/PlayerSansMono8x13-Classic.ttf"
font_size = 30
score_font = pygame.font.Font(font_path, font_size)

# define the size of the playable area window
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
# defines the background of the window
black = (0,0,0)

# define how fast we want the ball to move, and what image we want to use for it
speed =[2,2]
ball = pygame.image.load('images/ball_glowy.png')
ballrect = ball.get_rect()

#define the score
score = [0, 0]

# Define the images we're using for the paddles, and where they are
# displayed in their start position on the screen.

# load the images
paddle_player_1 = pygame.image.load('images/paddle_green.png')
paddle_player_2 = pygame.image.load('images/paddle_green.png')

# get the size, and plat the locations of the paddles on the screen.
paddlerect_player_1 = paddle_player_1.get_rect()
paddlerect_player_2 = paddle_player_2.get_rect()
paddlerect_player_1.x = 10
paddlerect_player_2.x = 775
paddlerect_player_1.y = 250
paddlerect_player_2.y = 250

# Game loop
while True  :

    # To make it fair, make the ball go in different directions when the game restarts.
    balldirection = [random.choice([2,-2]),random.choice([2,-2])]
    ballrect.x = random.randint(300,500)
    ballrect.y = random.randint(200,600)
    screen.fill(black)

    #reset the continue_game variable when the game restarts. This way after each point the game resets, but keeps the score.
    continue_game = True
    print("game restarted")

    # For the scoreboard, get the score from the int list, and store it as a string since we need to output it onto the streen with text.
    player_1_score = score[0]
    player_2_score = score[1]

    #convert the whole message into string and set it into the font.
    score_text = "      P1: " + str(player_1_score) + "       P2: " + str(player_2_score)
    score_text = score_font.render(str(score_text), True, (255, 255, 255))
    score_text_rect = score_text.get_rect()


    while continue_game:
        # First off, we need to control the speed of the game to make it interesting, otherwise it seems
        # that it defaults to the speed of the CPU, which makes it fun unless you're the squirrel from Over the Hedge
        clock = pygame.time.Clock()
        clock.tick(150)

        # Let's watch for an event to quit the game, and do so cleanly.
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # The paddles are controlled by the players, so we need to listen to
        # key events. We're only going to watch 2 for each player,
        # Player 1 is UP/DOWN
        # Player 2 is W/S
        keys = pygame.key.get_pressed()

        # paddle movement for player 1. We're watching W and S
        if keys[pygame.K_w]:
            # y limit check
            if paddlerect_player_1.y > 0:
                paddlerect_player_1.y = paddlerect_player_1.y - 3
        if keys[pygame.K_s]:
            # y limit check
            if paddlerect_player_1.y < 540:
                paddlerect_player_1.y = paddlerect_player_1.y + 3

        # paddle movement player 2: We're watching UP and DOWN
        # We're also adding some limits on how far the paddle can go so it stays on the screen.
        if keys[pygame.K_UP]:
            # y limit check
            if paddlerect_player_2.y > 0:
                paddlerect_player_2.y = paddlerect_player_2.y - 3
        if keys[pygame.K_DOWN]:
            # y limit check
            if paddlerect_player_2.y < 540:
                paddlerect_player_2.y = paddlerect_player_2.y + 3

        # Here is where we define how the ball moves and how it interacts with the paddles
        ballrect = ballrect.move(speed)

        # We want to make sure that the ball always bounces off of the top and bottom half of the court.
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        # But if a ball contacts the players paddle, it bounces back off of it.
        if ballrect.colliderect(paddlerect_player_1):
            speed[0] = -speed[0]
        if ballrect.colliderect(paddlerect_player_2):
            speed[0] = -speed[0]

        # if the player 1 misses the ball, then it's a point for player 2 and the game restarts.
        if ballrect.x <= 0:
            score[1] = score[1] + 1
            continue_game = False
            break
        if ballrect.x >= 800:
            score[0] = score[0] + 1

            continue_game = False
            break

        # display the changes on the screen.
        screen.fill(black)
        screen.blit(ball, ballrect)
        screen.blit(paddle_player_1, paddlerect_player_1)
        screen.blit(paddle_player_2, paddlerect_player_2)
        screen.blit(score_text, score_text_rect)
        pygame.display.flip()