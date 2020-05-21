#!/usr/bin/env python

import pygame
import json
from uuid import *
from time import *
from os import path
from math import *

from version.assets import Assets
from version.credits import credit

pygame.init()

gamecompany = 'Totobird Creations'
gameversion = 'r00'

info = pygame.display.Info()
windowsize = (1280, 1000)
def loadoptions():
    options = {
        'maxfps': 60,
        'loadfps': 30,
        'assets': './tilesets/default'
    }
    try:
        j = json.load(open('./options.json', 'r'))
        for tag in j.keys():
            options[tag] = j[tag]
    except FileNotFoundError:
        pass
    except json.decoder.JSONDecodeError:
        pass
    with open('./options.json', 'w') as f:
        json.dump(options, f)

    lang = {
        "gametitle": "Dungeon Crawler",
        'campaign': "Campaign"
    }
    try:
        j = json.load(open(path.join(options['assets'], 'lang.json'), 'r'))
        for tag in j.keys():
            options[tag] = j[tag]
    except FileNotFoundError:
        pass
    except json.decoder.JSONDecodeError:
        pass
    with open(path.join(options['assets'], 'lang.json'), 'w') as f:
        json.dump(lang, f)

    return((options, lang))
options, lang = loadoptions()

assets = Assets(options)

pygame.display.set_caption(lang['gametitle'])
clock = pygame.time.Clock()
display = pygame.display.set_mode(windowsize)
#display = display.convert()

def illegiblescroll(display, windowsize):
    text = []
    for i in range(5):
        text.append(str(uuid4())[:-2])
    for c in range(len(text[0])):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        b = pygame.Surface(windowsize, pygame.SRCALPHA)
        b.fill((0, 0, 0, 64))
        display.blit(b, (0, 0))
        fontsize = round(windowsize[0] / 25)
        font = pygame.font.Font(path.join(options['assets'], 'illegible.ttf'), fontsize)
        offsety = -1 * font.render(text[0][:c:], True, (255, 255, 255)).get_rect().size[1] * 2.5
        lineheight = font.render(text[0][:c:], True, (255, 255, 255)).get_rect().size[1]
        for line in range(len(text)):
            rendered = font.render(text[line][:c:], True, (255, 255, 255))
            renderedsize = rendered.get_rect().size
            display.blit(rendered, (round(windowsize[0] / 2 - renderedsize[0] / 2), round(windowsize[1] / 2 - renderedsize[1] / 2 - offsety)))
            offsety += lineheight
        pygame.display.flip()
        clock.tick(options['loadfps'])
        text = []
        for i in range(5):
            text.append(str(uuid4())[:-2])

    for c in range(len(text[0])):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        b = pygame.Surface(windowsize, pygame.SRCALPHA)
        b.fill((0, 0, 0, 33))
        display.blit(b, (0, 0))
        fontsize = round(windowsize[0] / 25)
        font = pygame.font.Font(path.join(options['assets'], 'illegible.ttf'), fontsize)
        offsety = -1 * font.render(text[0][:c:], True, (255, 255, 255)).get_rect().size[1] * 2.5
        lineheight = font.render(text[0][:c:], True, (255, 255, 255)).get_rect().size[1]
        for line in range(len(text)):
            rendered = font.render(text[line], True, (255, 255, 255))
            renderedsize = rendered.get_rect().size
            display.blit(rendered, (round(windowsize[0] / 2 - renderedsize[0] / 2), round(windowsize[1] / 2 - renderedsize[1] / 2 - offsety)))
            offsety += lineheight
        pygame.display.flip()
        clock.tick(options['loadfps'])
        for i in range(len(text)):
            u = str(uuid4())
            text[i] = u[0] + text[i][1:-1] + u[-1]

    for c in range(len(text[0]) + 10):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        b = pygame.Surface(windowsize, pygame.SRCALPHA)
        b.fill((0, 0, 0, 64))
        display.blit(b, (0, 0))
        fontsize = round(windowsize[0] / 25)
        font = pygame.font.Font(path.join(options['assets'], 'illegible.ttf'), fontsize)
        offsety = -1 * font.render(text[0][c + 1:], True, (255, 255, 255)).get_rect().size[1] * 2.5
        lineheight = font.render(text[0][c + 1:], True, (255, 255, 255)).get_rect().size[1]
        for line in range(len(text)):
            rendered = font.render(text[line][c + 1:], True, (255, 255, 255))
            renderedsize = rendered.get_rect().size
            display.blit(rendered, (round(windowsize[0] / 2 - renderedsize[0] / 2), round(windowsize[1] / 2 - renderedsize[1] / 2 - offsety)))
            offsety += lineheight
        pygame.display.flip()
        clock.tick(options['loadfps'])
        text = []
        for i in range(5):
            text.append(str(uuid4())[:-2])

mode = 'main'
singlehovered = False
singleclicked = False
end = False
darken = 0
while not end:
    # General Events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            end = True

    # Background
    display.fill((0, 0, 0))
    background = assets.background
    background = pygame.transform.scale(background, windowsize)
    display.blit(background, (0, 0))

    # Per-Mode Interfaces
    if mode == 'main':
        # Title
        fontsize = round(windowsize[0] / 10)
        font = pygame.font.Font(path.join(options['assets'], 'title.ttf'), fontsize)
        title = font.render(lang['gametitle'], True, (255, 123, 0))
        titlesize = title.get_rect().size
        if titlesize[1] >= floor(windowsize[1] / 8):
            title = pygame.transform.scale(title, (round(titlesize[0] / (titlesize[1] / floor(windowsize[1] * (1/8)))), floor(windowsize[1] / 8)))
            titlesize = title.get_rect().size
        display.blit(title, (round(windowsize[0] / 2 - titlesize[0] / 2), round(windowsize[1] / 2 - titlesize[1] / 2)))
        # Buttons
        if singleclicked:
            button = assets.buttons_click
        elif singlehovered:
            button = assets.buttons_hover
        else:
            button = assets.buttons
        buttonsize = button.get_rect().size
        s = pygame.Surface((buttonsize[0], buttonsize[1] / 4), pygame.SRCALPHA)
        s.blit(button, (0, 0), (0, round(buttonsize[1] * (3/4)), buttonsize[0], round(buttonsize[1] / 4)))
        button = s.copy()
        button = pygame.transform.scale(button, (round(windowsize[0] * (9 / 10)), round(windowsize[1] / 10)))
        buttonsize = button.get_rect().size
        fontsize = round(windowsize[0] / 25)
        font = pygame.font.Font(path.join(options['assets'], 'title.ttf'), fontsize)
        title = font.render(lang['campaign'], True, (0, 0, 0))
        titlesize = title.get_rect().size
        button.blit(title, (round(buttonsize[0] / 2 - titlesize[0] / 2), round(buttonsize[1] / 2 - titlesize[1] / 2)))
        buttonpos = (round(windowsize[0] / 2 - buttonsize[0] / 2), round(windowsize[1] - buttonsize[1]))
        display.blit(button, buttonpos)

        mousepos = pygame.mouse.get_pos()
        buttonsize = button.get_rect().size
        if mousepos[0] > buttonpos[0] and mousepos[0] < buttonpos[0] + buttonsize[0] and mousepos[1] > buttonpos[1] and mousepos[1] < buttonpos[1] + buttonsize[1]:
            singlehovered = True
        else:
            singlehovered = False

        # Info & Credits
        font = pygame.font.Font(path.join(options['assets'], 'debug.ttf'), 12)
        infocomp = font.render(gamecompany, True, (255, 255, 255))
        infocompsize = infocomp.get_rect().size
        display.blit(infocomp, (0, 0))
        infottvs = font.render(f'{lang["gametitle"]} {gameversion}', True, (255, 255, 255))
        infottvssize = infottvs.get_rect().size
        display.blit(infottvs, (windowsize[0] - infottvssize[0], 0))

        # Per-Mode Events
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if singlehovered:
                        singleclicked = True
                    elif mousepos[0] > 0 and mousepos[0] < infocompsize[0] and mousepos[1] > 0 and mousepos[1] < infocompsize[1]:
                        credit(display, windowsize, options, pygame)
                        darken = 1
            if event.type == pygame.MOUSEBUTTONUP:
                singleclicked = False
                if event.button == 1:
                    if singlehovered:
                        illegiblescroll(display, windowsize)
                        singlehovered = False
                        singleclicked = False
    b = pygame.Surface(windowsize, pygame.SRCALPHA)
    b.fill((0, 0, 0, round(darken * 255)))
    display.blit(b, (0, 0))
    if darken - 0.5 > 0:
        darken -= 0.5
    else:
        darken = 0
    pygame.display.flip()
    clock.tick(options['maxfps'])