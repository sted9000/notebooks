#  MAKE SURE THE DEFAULT SAVED RUN FOLDER IN MONKER IS CORRECT

# This is the actual script, but I will run it on my windows os so that pyautogui has access to mouse object
import pyautogui as gui
from time import sleep
from config import sims, screen_positions
from os import listdir, makedirs
from os.path import isfile, join, exists


def response_click(res_position):
    gui.click(x=screen_positions['responses'][res_position][0], y=screen_positions['responses'][res_position][1])
    sleep(1)


sim = 'sb_bn_3bp'

# for each flop
saved_runs_dir = sims[sim]['saved_runs_dir']
list_of_flops = [f.strip('.mkr') for f in listdir(saved_runs_dir) if isfile(join(saved_runs_dir, f))]
for i, flop in enumerate(list_of_flops):

    # click the load button
    gui.click(x=screen_positions['load_sim'][0], y=screen_positions['load_sim'][1])
    sleep(1)
    # down twice to first flop
    gui.press('down', 2 + i)
    sleep(1)

    # click load one street
    gui.click(x=screen_positions['load_one_street'][0], y=screen_positions['load_one_street'][1])
    sleep(5)
    # each part step in the hand
    for step in sims[sim]['steps']:

        # if the step needs to be trimmed
        if step['trim']:

            # create dir to hold screenshots
            flop_dir = join(sims[sim]['save_screenshots'], flop)
            if not exists(flop_dir):
                makedirs(flop_dir)

            # if you need to setup monker before the screenshot
            if step['setup']:
                for click in step['setup']:
                    if click[0] == 'response':
                        response_click(click[1])

            # each image to be captured
            for j, capture in enumerate(step['captures']):

                # take the screenshot
                gui.screenshot(f"{flop_dir}/{step['ss_prefix']}_{str(j)}.png",
                               region=screen_positions['range_percent'][len(step['captures'])][j])

