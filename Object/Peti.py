import pygame

semua_peti = pygame.sprite.Group()

class Peti(pygame.sprite.Sprite):
    animasi_diam = pygame.image.load("./Assets/Img/Peti/diam.png")
    animasi_buka = [pygame.image.load("./Assets/Img/Peti/Peti1.png"), pygame.image.load("./Assets/Img/Peti/Peti2.png"), pygame.image.load("./Assets/Img/Peti/Peti3.png"), pygame.image.load("./Assets/Img/Peti/Peti4.png"), pygame.image.load("./Assets/Img/Peti/Peti5.png"), pygame.image.load("./Assets/Img/Peti/Peti6.png"), pygame.image.load("./Assets/Img/Peti/Peti7.png"), pygame.image.load("./Assets/Img/Peti/Peti8.png"), pygame.image.load("./Assets/Img/Peti/Peti9.png"), pygame.image.load("./Assets/Img/Peti/Peti10.png")]
    animasi_count = 0

    buka = False
    
    def __init__(self, x, y):
        super(Peti, self).__init__()
        self.peti_x = x 
        self.peti_y = y
        self.rect = self.animasi_diam.convert_alpha().get_rect()
        self.rect.center = (self.peti_x, self.peti_y)
        self.suara_buka = pygame.mixer.Sound("./Assets/Music/buka_peti.wav")
        self.boost = pygame.mixer.Sound("./Assets/Music/boost.mp3")
        self.debuff = pygame.mixer.Sound("./Assets/Music/debuff.mp3")
        self.suara_counter = 0
        self.timer = 15
        self.powup = False
        self.powdown = False
        semua_peti.add(self)
       


    def update(self, screen, offset=(0,0)):
            # pygame.draw.rect(screen, "Red", self.rect)

            if self.animasi_count == 27:
                self.buka = False
                self.animasi_diam = pygame.image.load("./Assets/Img/Peti/Peti10.png")
                
            if self.buka == True:
                if self.suara_counter == 0:
                    pygame.mixer.Sound.play(self.suara_buka)
                self.suara_counter += 1
                self.animasi_count += 1 
                screen.blit(self.animasi_buka[self.animasi_count // 3], (self.rect[0] - offset[0], self.rect[1] - offset[1]))
            else:  
                screen.blit(self.animasi_diam, (self.rect[0] - offset[0], self.rect[1] - offset[1]))

    def reset(self):
        self.suara_counter = 0
        self.animasi_count = 0
        self.animasi_diam = pygame.image.load("./Assets/Img/Peti/diam.png")
