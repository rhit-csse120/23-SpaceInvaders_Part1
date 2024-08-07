# TODO: Put your names here (entire team)

import pygame
from Game import Game
from Controller import Controller
from View import View


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 650))  # TODO: Choose your own size
    pygame.display.set_caption("My Game Name")  # TODO: Choose your own title
    clock = pygame.time.Clock()
    frame_rate = 60  # TODO: Choose your own frame rate

    game = Game(screen)  # the Model
    viewer = View(screen, game)  # the View
    controller = Controller(game)  # the Controller

    while True:
        clock.tick(frame_rate)

        controller.get_and_handle_events()
        game.run_one_cycle()
        viewer.draw_everything()  # Includes the pygame.display.update()


main()
