# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 10:21:26 2020

@author: Jawad K. Mohammed Hussein
"""
import time

print("""
████████╗██╗░░██╗███████╗  ░██████╗░░█████╗░██████╗░██████╗░███████╗███╗░░██╗  ░█████╗░███████╗
╚══██╔══╝██║░░██║██╔════╝  ██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗░██║  ██╔══██╗██╔════╝
░░░██║░░░███████║█████╗░░  ██║░░██╗░███████║██████╔╝██║░░██║█████╗░░██╔██╗██║  ██║░░██║█████╗░░
░░░██║░░░██╔══██║██╔══╝░░  ██║░░╚██╗██╔══██║██╔══██╗██║░░██║██╔══╝░░██║╚████║  ██║░░██║██╔══╝░░
░░░██║░░░██║░░██║███████╗  ╚██████╔╝██║░░██║██║░░██║██████╔╝███████╗██║░╚███║  ╚█████╔╝██║░░░░░
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚══╝  ░╚════╝░╚═╝░░░░░

██████╗░███████╗██╗░░░░░██╗░██████╗░██╗░░██╗████████╗░██████╗
██╔══██╗██╔════╝██║░░░░░██║██╔════╝░██║░░██║╚══██╔══╝██╔════╝
██║░░██║█████╗░░██║░░░░░██║██║░░██╗░███████║░░░██║░░░╚█████╗░
██║░░██║██╔══╝░░██║░░░░░██║██║░░╚██╗██╔══██║░░░██║░░░░╚═══██╗
██████╔╝███████╗███████╗██║╚██████╔╝██║░░██║░░░██║░░░██████╔╝
╚═════╝░╚══════╝╚══════╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░

By Jade Maitre""")

pointer = ''
pointer1 = ''
player = input("What's your name? ")
player_name = player.capitalize()
gender = input("Male/Female? (M/F)")
if gender.lower() == 'm':
    pointer = 'he'
    pointer1 = 'his'
elif gender.lower() == 'f':
    pointer = 'she'
    pointer1 = 'her'
else:
    pointer = 'they'
    
def printing(line):
    for a in line:
        print(a, end='')
        time.sleep(.02)


line_2 = f'When {player_name} went to bed,\nAll kind of things crept in {pointer1} head.\n\n'
printing (line_2)
time.sleep(2)

line_3 = (f'It seemed as though {pointer} felt cocooned\nIn light from stardust, birdcall, moon...\n\n')
printing (line_3)
time.sleep(2)

line_4 = f"""And then, in rumpled sheets and pillows,\n{pointer}'d heard the call of breezy billows...\n\n"""
printing (line_4)
time.sleep(2)

line_5 = ('Outside the glass, beyond the trees,\nTiptoeing lawn-wet high trapeze\n\n')
printing (line_5)
time.sleep(2)

line_6 = (f'Ants and butterflies, insects all,\nInviting {pointer1} to attend a ball.\n\n')
printing (line_6)
time.sleep(2)

line_7 = (f'{player_name} kicked {pointer1} legs\nEmerged from sheets, outside the bed.\n\n')
printing (line_7)
time.sleep(2)

line_8 =(f'And stepped onto the calm wood floor,\nAnd put {pointer1} fingers to the door,\n\n')
printing (line_8)
time.sleep(2)

line_9 =('And turning the handle, crept away,\nThrough darkling night and towards the day.\n\n')
printing (line_9)
time.sleep(2)

line_10 =('The night-time garden was cool and wan,\nThings were so different whithout the sun.\n\n')
printing (line_10)
time.sleep(2)

line_11 =(f'The trees watched over little {player_name}\n{pointer} breathed in deeply, eager, dozy.\n\n')
printing (line_11)
time.sleep(2)

line_12 =(f'The wonders held {pointer1} gripped with awe.\nAbove were stars. Below, {pointer} saw...\n\n')
printing (line_12)
time.sleep(2)

line_13 =('A praying mantis held his heart,\nA tiger crept through shadowed park.\n\n')
printing (line_13)
time.sleep(2)

line_14 =('A crane crept lightly through the bowers.\nWhile everywhere, laughed miles of flowers.\n\n')
printing (line_14)
time.sleep(2)

line_15 =('Roses here and iris there,\nLotus pushing towards the air.\n\n')
printing (line_15)
time.sleep(2)

line_16 =(""" "The music had started slowly now;\nA dog's dreaming noises; a cat's miaow.\n\n""")
printing (line_16)
time.sleep(2)

line_17 =('The sound of whispers between two friends;\nA baddling river where it wends.\n\n')
printing (line_17)
time.sleep(2)

line_18 =('The moon above, high out of reach\nInvited her to a secret beach,\n\n')
printing (line_18)
time.sleep(2)

line_19 =('A sandy spot where, come the dawn\nThe roses would shake off their thorns\n\n')
printing (line_19)
time.sleep(2)

line_20 =('And open to the wildling sin,\nAnd smooth the sand, for everyone.\n\n')
printing (line_20)
time.sleep(2)

line_21 =('And by the tunes of night-time dreaming,\nReplace moonbeams with dancing, beaming.\n\n')
printing (line_21)
time.sleep(2)

