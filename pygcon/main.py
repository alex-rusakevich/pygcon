import pygcon
import pygame
import pygame.font


class Cell:
    text = ""
    surface = None

    bg_color = None
    fg_color = None

    screen_pos = None

    def set(self, font, text, bg_color, fg_color, antialias=True):
        self.font = font
        self.text = text
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.antialias = antialias

        pure_cell_text = font.render(self.text, self.antialias, self.fg_color)
        self.cell_size = (pure_cell_text.get_width(), pure_cell_text.get_height())
        self.fg_surface = pygame.Surface(self.cell_size, pygame.SRCALPHA)
        self.fg_surface.blit(pure_cell_text, (0, 0))

        self.bg_surface = pygame.Surface(self.cell_size)
        self.bg_surface.fill(self.bg_color)

        self.surface = self.bg_surface
        self.surface.blit(self.fg_surface, (0, 0))

    def __init__(self, font, text, bg_color, fg_color, antialias=True):
        self.set(font, text, bg_color, fg_color, antialias)


class Main_Application:
    FPS_Limit = 24

    def __init__(self, font, matrix_size):
        pygame.init()
        pygame.font.init()

        self.set_basement(font, matrix_size)

    def set_basement(self, font, matrix_size):
        self.font = font
        self.matrix_size = matrix_size

        self.base_cell = Cell(
            font, "@", pygame.Color("#000000"), pygame.Color("#ffffff")
        )

        matrix_width = matrix_size[0]
        matrix_height = matrix_size[1]
        screen_width = matrix_width * self.base_cell.surface.get_width()
        screen_height = matrix_height * self.base_cell.surface.get_height()
        self.screen = pygame.display.set_mode((screen_width, screen_height))

        self.cell_matrix = [
            [
                Cell(font, "@", pygame.Color("#2A2B2C"), pygame.Color("#C7C6C5"))
                for x in range(80)
            ]
            for y in range(20)
        ]

    def start(self):
        self.load()

        clock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    self.on_quit()
            self.update(events)

            self.draw()
            x_pos = 0
            y_pos = 0
            for y in self.cell_matrix:
                for x in y:
                    x.screen_pos = (
                        x_pos * self.base_cell.surface.get_width(),
                        y_pos * self.base_cell.surface.get_height(),
                    )

                    self.screen.blit(x.surface, x.screen_pos)
                    x_pos += 1
                x_pos = 0
                y_pos += 1

            self.custom_surface_draw()
            pygame.display.update()

            clock.tick(self.FPS_Limit)

    def load(self):
        pass

    def update(self, events):
        pass

    def draw(self):
        pass

    def custom_surface_draw(self):
        pass

    def on_quit(self):
        raise SystemExit("QUIT")
