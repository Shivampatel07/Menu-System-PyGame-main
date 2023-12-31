import pygame, sys
from button import Button
from Galaxiyan.code.main import main
from Tetris_main.main import main2
from A_day_in_Hell.main import main3

# from DOOM_style_Game_main import main1,map,npc,obect_handler,object_renderer,pathfinding,player,raycasting,settings,sound,sprite_object,weapon,resources
# from DOOM_style_Game_main import settings
# from DOOM_style_Game_main import main1 as dm1
# import DOOM_style_Game_main as dm

pygame.init()

# SCREEN = pygame.display.set_mode((1920, 1080))
# pygame.display.set_caption("Menu")

BG = pygame.image.load("assets\\Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets\\font.ttf", size)


# def play():
#     while True:
#         PLAY_MOUSE_POS = pygame.mouse.get_pos()

#         SCREEN.fill("black")

#         PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
#         PLAY_RECT = PLAY_TEXT.get_rect(center=(960,540 ))
#         SCREEN.blit(PLAY_TEXT, PLAY_RECT)

#         PLAY_BACK = Button(image=None, pos=(960, 640),
#                             text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

#         PLAY_BACK.changeColor(PLAY_MOUSE_POS)
#         PLAY_BACK.update(SCREEN)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
#                     main_menu()

#         pygame.display.update()

# def options():
#     while True:
#         OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

#         SCREEN.fill("white")

#         OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
#         OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(960, 540))
#         SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

#         OPTIONS_BACK = Button(image=None, pos=(960, 540),
#                             text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

#         OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
#         OPTIONS_BACK.update(SCREEN)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
#                     main_menu()

#         pygame.display.update()
SCREEN = pygame.display.set_mode((1920, 1080))


def main_menu(screen, screen_width, screen_height):
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("RETRO ARCADE", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(960, 200))

        BUTTON_1 = Button(
            image=pygame.image.load("assets\\Play Rect.png"),
            pos=(960, 450),
            text_input="A Day In Hell",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        BUTTON_2 = Button(
            image=pygame.image.load("assets\\Options Rect.png"),
            pos=(960, 600),
            text_input="GALAXIYAN",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        BUTTON_3 = Button(
            image=pygame.image.load("assets\\Tetris Rect.png"),
            pos=(960, 750),
            text_input="TETRIS",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        BUTTON_4 = Button(
            image=pygame.image.load("assets\\Quit Rect.png"),
            pos=(960, 900),
            text_input="QUIT",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [BUTTON_1, BUTTON_2, BUTTON_3, BUTTON_4]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BUTTON_1.checkForInput(MENU_MOUSE_POS):
                    main3()
                if BUTTON_2.checkForInput(MENU_MOUSE_POS):
                    pygame.display.flip()
                    main(screen, screen_width, screen_height)
                if BUTTON_3.checkForInput(MENU_MOUSE_POS):
                    main2()
                if BUTTON_4.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("RETRO ARCADE")
main_menu(screen, screen_width, screen_height)
