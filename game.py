import pygame

pygame.init()
from generation_lab import Labyrinthe
from ligne import Ligne
from Resolution import Resolution


class Game:

    def __init__ (self):

        # creer la fenetre du jeu
        self.screen = pygame.display.set_mode((691, 691))
        pygame.display.set_caption("Labyrinthe")
        self.lab = Labyrinthe()
        self.groupe_mur = pygame.sprite.Group()
        self.surface = pygame.Surface((691, 691))

    def run (self):

        # boucle du jeu
        running = True
        game_interface = 'en_jeu'

        # Si Interface labyrinthe :
        if game_interface == 'en_jeu':

            grid = self.lab.create_lab()
            for elt in self.lab.Mur:
                self.groupe_mur.add(elt)

            res = Resolution(grid, self.lab.start, self.lab.end)

            res_path = res.res_dfs()
            print(res_path)


        while running:

            # Fermeture de l'application
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            count = 10

            # Interface d'accueil
            if game_interface == 'home':
                pass

            # Interface du labyrinthe
            if game_interface == 'en_jeu':

                self.screen.fill((255, 255, 255))
                self.groupe_mur.draw(self.surface)
                self.screen.blit(self.surface, (0, 0))

                for elt in res_path:

                    Ligne(elt[0], elt[1])
                    ligne = pygame.Surface((10, 10))
                    ligne.set_alpha(100)
                    rect = ligne.get_rect()
                    rect.x = elt[1]*10
                    rect.y = elt[0]*10
                    ligne.fill((255, 0, 0))
                    self.screen.blit(ligne, rect)

                pygame.display.update()

        pygame.quit()
