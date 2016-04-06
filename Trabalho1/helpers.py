#! /usr/bin/env python

import os, sys
import pygame
from pygame.locals import *

def load_image(name, colorkey=None):
    
    fullname = os.path.join("images", name)
    try:
        image = pygame.image.load(name)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image#, image.get_rect()