import pygame
import sys
import os

from utils.screen import get_screen, prepare_title, prepare_options, control_selection, evaluate_selection

pygame.init()


screen = get_screen(pygame)
clock =  pygame.time.Clock()

show_main_menu = True
show_setting = False
start_game = False

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    if show_main_menu:
        control_selection(pygame)
        show_main_menu, show_setting, start_game = evaluate_selection(pygame, show_main_menu, show_setting, start_game)
        print("main menu ",show_main_menu, show_setting, start_game)
        screen.fill([0,0,0])

        prepare_title(pygame, screen)
        prepare_options(pygame, screen)

        pygame.display.flip()
        clock.tick(15)

    if show_setting:
        print("settings ",show_main_menu, show_setting, start_game)
        screen.fill([0,0,0])
        pygame.display.flip()
        clock.tick(15)

    if start_game:
        print("start game ",show_main_menu, show_setting, start_game)
        screen.fill([0,0,0])
        pygame.display.flip()
        clock.tick(15)

    if show_main_menu == False and show_setting == False and start_game == False:
        print("quit",show_main_menu, show_setting, start_game)
        pygame.quit()
        sys.exit()