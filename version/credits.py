#!/usr/bin/env python

from os import path
from math import *

def credit(display, windowsize, options, pygame):
    dtext = open(path.join(options['assets'], 'credits.txt'), 'r').read().split('\n')
    maxlength = 0
    for i in dtext:
        if len(i) >= maxlength:
            maxlength = len(i)
    end = False
    count = 0.0
    mode = True
    darken = 1
    while not end:
        text = dtext.copy()
        for i in range(len(text)):
            text[i] = text[i][:floor(count):]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            elif event.type == pygame.VIDEORESIZE:
                windowsize = (event.w, event.h)
                display = pygame.display.set_mode(windowsize, pygame.RESIZABLE)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    mode = False
        b = pygame.Surface(windowsize, pygame.SRCALPHA)
        b.fill((0, 0, 0, 64))
        display.blit(b, (0, 0))
        fontsize = round(windowsize[0] / 35)
        font = pygame.font.Font(path.join(options['assets'], 'credits.ttf'), fontsize)
        surfaces = []
        totalheight = 0
        totalwidth = 0
        for i in range(len(text)):
            s = font.render(text[i], True, (255, 255, 255))
            ssize = s.get_rect().size
            totalheight += ssize[1]
            if ssize[0] >= totalwidth:
                totalwidth = ssize[0]
            surfaces.append(s)

        s = pygame.Surface((totalwidth, totalheight), pygame.SRCALPHA)
        for i in range(len(surfaces)):
            size = surfaces[i].get_rect().size
            s.blit(surfaces[i], (totalwidth / 2 - size[0] / 2, totalheight / len(surfaces) * i))
        size = s.get_rect().size
        display.blit(s, (windowsize[0] / 2 - size[0] / 2, windowsize[1] / 2 - size[1] / 2))
        if mode:
            if count < maxlength:
                count += 0.5
        else:
            count -= 0.5
        if count == 0.0:
            end = True

        pygame.display.flip()

    return(windowsize)