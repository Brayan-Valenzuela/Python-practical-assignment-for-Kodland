available_screen_sizes = [(400, 600),(200, 300),(100, 150)]
available_font_title_sizes = [80, 40, 20]
available_font_options_sizes = [40, 20, 10]
available_options_space = [60, 30, 15]

select_conf = 0
selected_option = 0
print(selected_option)
options = ["Start", "Settings", "Exit"]

def init_conf(os_instance):
    os_instance.environ['select_conf'] = 0
    os_instance.environ['selected_option'] = 0

def get_screen(pygame_instance):
    screen = pygame_instance.display.set_mode(get_screen_size())
    pygame_instance.display.set_caption("Main menu")

    return screen

def get_screen_size():
    return available_screen_sizes[select_conf]

def get_font_title_size():
    return available_font_title_sizes[select_conf]

def get_font_options_size():
    return available_font_options_sizes[select_conf]

def get_options_space():
    return available_options_space[select_conf]

def get_fonts(pygame_instance):
    font_title = pygame_instance.font.Font(None, get_font_title_size())
    font_options = pygame_instance.font.Font(None, get_font_options_size())

    return font_title, font_options

def show_text(text, font, color, screen, x, y):
    text_objet = font.render(text, True, color)
    rect_text = text_objet.get_rect()
    rect_text.center = (x, y)
    screen.blit(text_objet, rect_text)

def prepare_title(pygame_instance, screen):
    font_title, _ = get_fonts(pygame_instance)
    screen_size = get_screen_size()
    x = screen_size[0]/2
    y= screen_size[1]/4
    show_text("Crash Cars!", font_title,[255,255,255], screen, x, y)

def prepare_options(pygame_instance, screen):
    _, font_options = get_fonts(pygame_instance)
    screen_size = get_screen_size()
    x = screen_size[0]/2
    y = screen_size[1]/2

    for idx, item in enumerate(options):
        if idx == selected_option:
            show_text("---> " + item, font_options, [255,255,255], screen, x, y)
        
        else:
            show_text(item, font_options, [255,255,255], screen, x, y)

        y += get_options_space()

def control_selection(pygame_instance):
    global selected_option
    keys = pygame_instance.key.get_pressed()

    if keys[pygame_instance.K_UP]:
        if selected_option == 0:
            selected_option = 2

        else:
            selected_option -= 1

    if keys[pygame_instance.K_DOWN]:
        if selected_option == 2:
            selected_option = 0

        else:
            selected_option += 1

def evaluate_selection(pygame_instance, show_main_menu, show_setting, start_game):
    global selected_option
    keys = pygame_instance.key.get_pressed()

    if keys[pygame_instance.K_RETURN]:

        if selected_option == 0:
            show_main_menu = False
            show_setting = False
            start_game = True

        if selected_option == 1:
            show_main_menu = False
            show_setting = True
            start_game = False

        if selected_option == 2:
            show_main_menu = False
            show_setting = False
            start_game = False

    return show_main_menu, show_setting, start_game