import pygame
import time
import random


import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="dika",
    user="dika",
    password="dikamiko2006",
    host="localhost",
    port="3000"
)

# Create tables if they don't exist
with conn.cursor() as cursor:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "user" (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE,
            level INTEGER DEFAULT 1
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES "user"(id),
            score INTEGER
        )
    ''')
    conn.commit()

def check_user_exists(username):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM \"user\" WHERE username=%s", (username,))
        user = cursor.fetchone()
    return user

def create_user(username):
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO \"user\" (username) VALUES (%s) RETURNING id", (username,))
        user_id = cursor.fetchone()[0]
        conn.commit()
    return user_id

def get_user_level(user_id):
    with conn.cursor() as cursor:
        cursor.execute("SELECT level FROM \"user\" WHERE id=%s", (user_id,))
        level = cursor.fetchone()[0]
    return level

def update_user_level(user_id, level):
    with conn.cursor() as cursor:
        cursor.execute("UPDATE \"user\" SET level=%s WHERE id=%s", (level, user_id))
        conn.commit()

def save_score(user_id, score):
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO user_score (user_id, score) VALUES (%s, %s)", (user_id, score))
        conn.commit()

def pause_and_save_state(user_id, score, level):
    save_score(user_id, score)
    update_user_level(user_id, level)
    print("Game paused and current state saved.")

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display dimensions
dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')

clock = pygame.time.Clock()

# Define constants
snake_block = 10
snake_speed = 10

# Define fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display score
def Your_score(score):
    value = score_font.render("Your score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
# Function to display score
def Your_level(level):
    value = score_font.render("Your level: " + str(level), True, yellow)
    dis.blit(value, [0, dis_height-100])

# Function to draw snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Function to display message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Function to generate food with different weights
def generate_food():
    weights = [red] * 5 + [blue] * 3 + [yellow] * 2  # Assigning different weights to colors
    return random.choice(weights)  # Randomly select a color based on weights

# Function to run the game loop
def gameLoop(username):
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # Timer for disappearing food
    food_timer = time.time() + 5  # Set initial timer to 5 seconds
    food_color = generate_food()

    user = check_user_exists(username)

    if not user:
        user_id = create_user(username)
        print("New user created.")
        level = 1
    else:
        user_id = user[0]
        level = get_user_level(user_id)
        print("Welcome back, {}! Your current level is {}.".format(username, level))

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pause_and_save_state(user_id, Length_of_snake - 1, level)
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        pause_and_save_state(user_id, Length_of_snake - 1, level)
                        gameLoop(username)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != snake_block:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -snake_block:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != snake_block:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -snake_block:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            x1 %= dis_width
            y1 %= dis_height
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        # Draw food
        pygame.draw.rect(dis, food_color, [foodx, foody, snake_block, snake_block])

        # Check if food timer has expired
        if time.time() > food_timer:
            # Generate new food with different color and reset timer
            food_color = generate_food()
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            food_timer = time.time() + 5  # Reset timer to 5 seconds

        # Update snake list and check for collisions
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        Your_level(level)

        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            if food_color == blue:
                Length_of_snake += 2
            else:
                Length_of_snake += 1
            if Length_of_snake % 5 == 0:
                level += 1

        clock.tick(snake_speed + level)

    pygame.quit()
    quit()

# Run the game loop
username = input('Enter your username: ')
gameLoop(username)
