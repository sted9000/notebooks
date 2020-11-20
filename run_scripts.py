import pyautogui as gui
from time import sleep
from config import screen_positions
from sims import sims
import json
gui.PAUSE = 1


"""
WHAT SIM ARE YOU RUNNING?
THIS IS THE ONLY THING TO EDIT
"""
sim = 'sb_bn_3bp'


def click(button_name):
    gui.click(x=screen_positions[button_name][0], y=screen_positions[button_name][1])
    sleep(1)


# load imported data
sim_data = json.load(open('sim_data.json'))
trimmed_tree_dict = sim_data[sim]['trimmed_trees']
iterations = sims[sim]['iterations']
reset_average = sims[sim]['reset_average']

# loop through scripts
for script, flops_array in trimmed_tree_dict.items():
    tree_to_load = sim + '_' + script + '.tree'
    flops_string = ', '.join(flops_array)

    # click the scripts button
    click('script_button')

    # select correct tree (tab, enter, paste, enter)
    click('Tree_file_Select')
    gui.typewrite(tree_to_load)
    gui.press('enter')

    # enter the list of flops (tab, paste)
    click('List_of_boards')
    gui.hotkey('ctrl', 'a')
    gui.typewrite(flops_string)

    # iterations (tab, tab, paste)
    click('Run_to')
    gui.hotkey('ctrl', 'a')
    gui.typewrite(iterations)

    # reset point (tab, paste)
    click('Reset_avg_after')
    gui.hotkey('ctrl', 'a')
    gui.typewrite(reset_average)

    # save to folder (tab, tab, tab, tab, enter, paste, enter)
    save_run_folder = 'C:\\Users\\sted9\\Desktop\\MonkerSolver\\savedRuns\\3bp_sb_bn_trimmed'
    click('Save_to_folder_Select')
    gui.typewrite(save_run_folder)
    gui.press('enter')

    # start (tab, enter)
    click('Start_script')

    # wait until all flops are done until running the next script
    sleep(len(flops_array * 5 * 60 * 60))
