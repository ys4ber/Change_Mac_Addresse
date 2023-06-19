#!/usr/bin/python3

import os
import random
import string


# Set Here Your Interface Name :


interface = 'INTERFACE'

def random_mac():


    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00,0x7f),
           random.randint(0x00,0xff),
           random.randint(0x00,0xff)]
    return ':'.join(format(x, '02x') for x in mac)

new_mac = random_mac()

os.system(f"sudo ifconfig {interface} hw ether {new_mac}")
