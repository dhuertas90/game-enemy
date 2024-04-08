import pygame
import sys
from modules.player import Player
from modules.enemy import Enemy

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Función para mostrar el menú principal
def show_menu(screen):
    font = pygame.font.Font(None, 36)
    text1 = font.render("Presiona ESPACIO para jugar", True, WHITE)
    text1_rect = text1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
    screen.blit(text1, text1_rect)

    text2 = font.render("Presiona Q para salir", True, WHITE)
    text2_rect = text2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
    screen.blit(text2, text2_rect)

    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


# Función principal del juego
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simple Pygame Game")

    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    for _ in range(10):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    clock = pygame.time.Clock()
    running = True
    show_menu(screen)  # Mostrar el menú principal antes de comenzar el juego
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, enemies, False)
        if hits:
            running = False

        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()