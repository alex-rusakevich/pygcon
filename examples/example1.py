import pygame
import pygame.font


class Cell:
    text = ""
    surface = None

    bg_color = None
    fg_color = None

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


if __name__ == "__main__":
    pygame.init()

    font = pygame.font.SysFont("couriernew", 24)
    base_cell = Cell(font, "@", pygame.Color("#000000"), pygame.Color("#ffffff"))

    matrix_width = 80
    matrix_height = 20
    screen_width = matrix_width * base_cell.surface.get_width()
    screen_height = matrix_height * base_cell.surface.get_height()
    screen = pygame.display.set_mode((screen_width, screen_height))

    cell_matrix = [
        [
            Cell(font, "@", pygame.Color("#2A2B2C"), pygame.Color("#C7C6C5"))
            for x in range(80)
        ]
        for y in range(20)
    ]

    clock = pygame.time.Clock()
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit("QUIT")

        x_pos = 0
        y_pos = 0
        for y in cell_matrix:
            for x in y:
                screen.blit(
                    x.surface,
                    (
                        x_pos * base_cell.surface.get_width(),
                        y_pos * base_cell.surface.get_height(),
                    ),
                )
                x_pos += 1
            x_pos = 0
            y_pos += 1
        pygame.display.update()

        clock.tick(24)
