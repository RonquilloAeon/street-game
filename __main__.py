"""
workon game

Resources:
https://opengameart.org/content/isometric-city
https://kenney.nl/assets/road-textures

Info:
https://stackoverflow.com/questions/40443430/displaying-an-image-using-a-class-on-pygame
"""
import pygame
from pygame.locals import *


class Road(pygame.sprite.Sprite):
    def __init__(self, fp, dx, dy, width=256, height=256) -> None:
        super().__init__()

        # To ensure transparency works, open image w/ Gimp to change mode:
        # Image -> Mode -> Indexed... and use the defaults
        self.image = pygame.transform.scale(pygame.image.load(fp).convert(), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rect)


class Car(pygame.sprite.Sprite):
    def __init__(self, fp, dx, dy, width=128, height=64) -> None:
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(fp).convert(), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy
        self.speed = 5

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rect)

    def move_up(self) -> None:
        self.rect.y -= self.speed

    def move_down(self) -> None:
        self.rect.y += self.speed


def main(surface: pygame.Surface) -> None:
    Road("assets/roads/PNG/Default/roadTexture_13.png", 0, 100).draw(surface)
    Road("assets/roads/PNG/Default/roadTexture_13.png", 256, 100).draw(surface)
    Road("assets/roads/PNG/Default/roadTexture_13.png", 512, 100).draw(surface)

def event_handler(surface: pygame.Surface, background: pygame.Surface, car: Car) -> None:
    for event in pygame.event.get():
        print(f"{event}: {pygame.event.event_name(event.type)}")
        if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q)):
            pygame.quit()
            quit()
        elif event.type == KEYDOWN and event.key == K_d:
            pygame.draw.rect(game_display, (200, 200, 200), pygame.Rect(10, 10, 100, 100))
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            print("mouse click!")
            pygame.draw.rect(game_display, (255, 50, 50), pygame.Rect(*event.pos, 20, 20))
        
        if event.type == KEYDOWN:
            surface.blit(background, car.rect, car.rect)

            if event.key == K_UP:
                car.move_up()
            elif event.key == K_DOWN:
                car.move_down()

            car.draw(surface)

if __name__ == "__main__":
    # Init pygame
    pygame.init()

    display_width = 800
    display_height = 600

    game_display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Street Game')

    clock = pygame.time.Clock() 

    # Dirt background
    background_image = pygame.image.load("assets/dirt_2.png").convert()
    game_display.blit(background_image, (0, 0))

    # Game init
    main(game_display)
    pygame.display.update()
    car = Car("assets/red_car.png", 248, 164)
    car.draw(game_display)

    while True:
        event_handler(game_display, background_image, car)

        pygame.display.update()
        clock.tick()
