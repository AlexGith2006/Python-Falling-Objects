import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Objects Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

basket_width, basket_height = 100, 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - basket_height - 10
basket_speed = 10

object_radius = 15
object_speed = 5
objects = []
score = 0

def draw_basket(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, basket_width, basket_height))

def draw_objects(objects):
    for obj in objects:
        pygame.draw.circle(screen, RED, (obj['x'], obj['y']), object_radius)

def move_objects(objects):
    for obj in objects:
        obj['y'] += object_speed
        
def check_collision(basket_x, basket_y, obj):
    if (basket_x < obj['x'] < basket_x + basket_width and
            basket_y < obj['y'] + object_radius < basket_y + basket_height):
        return True
    return False

def game_loop():
    global basket_x, basket_y, score
    running = True
    while running:
        screen.fill(WHITE) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
            basket_x += basket_speed
        if random.randint(1, 30) == 1:
            new_object = {'x': random.randint(0, WIDTH), 'y': 0}
            objects.append(new_object)
        move_objects(objects)
        for obj in objects[:]:
            if check_collision(basket_x, basket_y, obj):
                objects.remove(obj)
                score += 1
            elif obj['y'] > HEIGHT:
                objects.remove(obj)

        draw_basket(basket_x, basket_y)
        draw_objects(objects)

        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(text, (10, 10))

        pygame.display.update()

        clock.tick(60)
    
    
        
    pygame.quit()

if __name__ == "__main__":
    game_loop()

