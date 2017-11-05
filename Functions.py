'''

file to make the world a whole lot easier
credits to: Pier from FX628 CS, thank you for helping me so much and let me use some of his code

'''
from pygame import *
from pygame.sprite import *

class imagesprite(Sprite):

    '''this clas s is used to create and display image unto the game screen'''

    def __init__(self, filename, xpos, ypos):  #fill in the parameters so that it is reusable
        Sprite.__init__(self)
        self.image = image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

class textsprite(Sprite):

    '''This class is used to create and display a text as a sprite onto the screen'''

    def __init__(self, fontstyle, text, fontsize, xpos, ypos, R, G, B):
        Sprite.__init__(self)
        self.font = pygame.font.SysFont(fontstyle, fontsize)
        self.image = self.font.render(text, False, (R, G, B))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos



def call_sprite(text, screen_type, mainscreen):

    '''This function displays the sprite into the screen'''

    text_group = Group(text)
    if screen_type == "Image":
        text_group.draw(mainscreen.display)
    if screen_type == "Fill":
        text_group.draw(mainscreen.screen)

class MainScreen():

    '''This class is used to set up the main screen and main menu background'''

    def __init__(self, imagefile):
        clock=pygame.time.Clock()
        displayw=800
        displayh=600
        self.display = pygame.display.set_mode((displayw, displayh))
        pygame.display.set_caption("Sora - a short VN")
        self.image = image.load(imagefile)
        self.display.blit(self.image, (0,0))
        clock.tick(120)

class sound():

    '''This class is used to play the music continously without interrruptions'''

    def __init__(self, musicfile):
        pygame.mixer.Sound(musicfile).play() #Use Sound instead of music as it won't be interrupted

class bgm():

    '''This class is used to play the bgm'''

    def __init__(self, music):
        pygame.mixer.music.load(music) #Use mixer.music so that it won't interrupt the background music
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1) #plays the sound file
