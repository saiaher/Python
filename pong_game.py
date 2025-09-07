import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 700, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 6

# Ball settings
BALL_RADIUS = 8
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Fonts
score_font = pygame.font.SysFont("comicsans", 40)

# Define paddles and ball
left_paddle = pygame.Rect(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 20, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2 - BALL_RADIUS, HEIGHT//2 - BALL_RADIUS, BALL_RADIUS*2, BALL_RADIUS*2)

# Scores
left_score = 0
right_score = 0

clock = pygame.time.Clock()

def draw():
    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, left_paddle)
    pygame.draw.rect(win, WHITE, right_paddle)
    pygame.draw.ellipse(win, WHITE, ball)
    pygame.draw.aaline(win, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    left_score_text = score_font.render(str(left_score), True, WHITE)
    right_score_text = score_font.render(str(right_score), True, WHITE)
    win.blit(left_score_text, (WIDTH//4, 20))
    win.blit(right_score_text, (WIDTH*3//4, 20))

    pygame.display.update()

def main():
    global left_score, right_score, BALL_SPEED_X, BALL_SPEED_Y

    run = True

    ball_speed_x = BALL_SPEED_X
    ball_speed_y = BALL_SPEED_Y

    while run:
        clock.tick(60)  # 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        # Left paddle movement (W/S keys)
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
            left_paddle.y += PADDLE_SPEED
        # Right paddle movement (Up/Down arrow keys)
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += PADDLE_SPEED

        # Move ball
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Ball collision with top/bottom
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1

        # Ball collision with paddles
        if ball.colliderect(left_paddle) and ball_speed_x < 0:
            ball_speed_x *= -1
        if ball.colliderect(right_paddle) and ball_speed_x > 0:
            ball_speed_x *= -1

        # Ball goes past left side (right player scores)
        if ball.left <= 0:
            right_score += 1
            ball.center = (WIDTH//2, HEIGHT//2)
            ball_speed_x *= -1

        # Ball goes past right side (left player scores)
        if ball.right >= WIDTH:
            left_score += 1
            ball.center = (WIDTH//2, HEIGHT//2)
            ball_speed_x *= -1

        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
