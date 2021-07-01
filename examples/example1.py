import pygame
import pygame.font


class Cell:
    text = ""
    surface = None

    bg_color = None
    fg_color = None

    def set(self, font, text, bg_color, fg_color, antialias=False):
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

    def __init__(self, font, text, bg_color, fg_color, antialias=False):
        self.set(font, text, bg_color, fg_color, antialias)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    font = pygame.font.SysFont("couriernew", 14)
    cell1 = Cell(font, "@", pygame.Color("#aaaaaa"), pygame.Color("#ffffff"))

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit("QUIT")
        screen.blit(cell1.surface, (0, 0))
        pygame.display.update()
