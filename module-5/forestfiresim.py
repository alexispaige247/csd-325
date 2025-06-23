"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = 'W'

INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:
        displayForest(forest)

        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest or forest.get((x, y)) == WATER:
                    continue  # Skip if water or already processed

                if forest[(x, y)] == EMPTY and random.random() <= GROW_CHANCE:
                    nextForest[(x, y)] = TREE
                elif forest[(x, y)] == TREE and random.random() <= FIRE_CHANCE:
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            neighbor = (x + ix, y + iy)
                            if forest.get(neighbor) == TREE:
                                nextForest[neighbor] = FIRE
                    nextForest[(x, y)] = EMPTY
                else:
                    nextForest[(x, y)] = forest[(x, y)]

        # Keep water in place
        for x in range(forest['width']):
            for y in range(forest['height']):
                if forest.get((x, y)) == WATER:
                    nextForest[(x, y)] = WATER

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure with lake."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    lakeWidth = 15
    lakeHeight = 5
    lakeStartX = (WIDTH // 2) - (lakeWidth // 2)
    lakeStartY = (HEIGHT // 2) - (lakeHeight // 2)

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if lakeStartX <= x < lakeStartX + lakeWidth and lakeStartY <= y < lakeStartY + lakeHeight:
                forest[(x, y)] = WATER
            elif (random.random() <= INITIAL_TREE_DENSITY):
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY
    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            cell = forest[(x, y)]
            if cell == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif cell == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif cell == WATER:
                bext.fg('blue')
                print(WATER, end='')
            else:
                print(EMPTY, end='')
        print()
    bext.fg('reset')
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
