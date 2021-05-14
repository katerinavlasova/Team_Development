import cv2
import numpy as np

def test_images(name_design, name_screen):
    design = cv2.imread(name_design)
    dcols, drows, dchan = design.shape
    screen = cv2.imread(name_screen)
    scols, srows, schan = screen.shape

    if (dcols != scols or drows != srows or dchan != schan):
        return 'FAIL'
    
    fails_count = 0
    for i in range (dcols):
        for j in range (drows):
            for k in range (dchan):
                if design[i][j][k] != screen[i][j][k]:
                    fails_count += 1
    fails_proc = fails_count / (dcols * drows * dchan)
    if fails_proc < 0.01:
        return 'OK'
    else:
        return 'FAIL'
            


name_design_intr = 'img/screen_test/design_intr.png'
name_screen_intr = 'img/screen_test/screen_intr.png'
name_design_game = 'img/screen_test/design_game.png'
name_screen_game = 'img/screen_test/screen_game.png'

test1 = test_images(name_design_intr, name_screen_intr)
print('test1: ', test1)
test2 = test_images(name_design_game, name_screen_game)
print('test2: ', test2)

if test1 == test2 == 'OK':
    print('\nresult: OK')
else:
    print('\nresult: FAIL')
