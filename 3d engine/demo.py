import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click to Change Color")

# Object properties
rect_width, rect_height = 100, 50
rect_x, rect_y = (WIDTH - rect_width) // 2, (HEIGHT - rect_height) // 2
rect_color = RED

def draw():
    screen.fill(WHITE)
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Check if mouse click is inside the rectangle
            if rect_x < mouse_x < rect_x + rect_width and rect_y < mouse_y < rect_y + rect_height:
                # Change color when clicked
                if rect_color == RED:
                    rect_color = BLUE
                else:
                    rect_color = RED

    draw()

pygame.quit()
sys.exit()
