import pygame
import sys
import os

from utils.screen import *

pygame.init()


screen = get_screen(pygame)
clock =  pygame.time.Clock()
frame_rate = 30

stars_coord = generate_stars()
player_image = pygame.image.load("resources/player.png").convert()

player_span_coord = get_screen_size().copy()
player_span_coord[0] = player_span_coord[0]//2
player_span_coord[1] = player_span_coord[1]//2

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
        clock.tick(frame_rate)

    if show_setting:
        print("settings ",show_main_menu, show_setting, start_game)
        screen.fill([0,0,0])
        pygame.display.flip()
        clock.tick(frame_rate)

    if start_game:
        print("start game ",show_main_menu, show_setting, start_game)
        screen.fill([0,0,0])
        animate_starts(pygame, stars_coord, screen)
        player_span_coord = move_player(pygame, player_span_coord)
        spam_player(player_image, screen, player_span_coord)

        pygame.display.flip()
        clock.tick(frame_rate)

    if show_main_menu == False and show_setting == False and start_game == False:
        print("quit",show_main_menu, show_setting, start_game)
        pygame.quit()
        sys.exit()