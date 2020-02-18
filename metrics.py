#!/usr/bin/env python
# -*- coding: utf-8 -*-

import signal
import sys
import time
from datetime import datetime, timedelta

from selfupdate import *
from userconfig import INTERVAL

known_states = 0

web3 = Web3(Web3.HTTPProvider(NODE_ADDRESS))  # your node


# NUM_OF_STATES = 446266045  # Actual for Feb, 15 2020

def signal_handler(signal, frame):
    print('Stopping...')
    updater(known_states, NUM_OF_STATES)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def measure(interval=INTERVAL):
    remain = 1
    period = interval
    known_states = web3.eth.syncing['knownStates']
    max_speed = min_speed = 0
    while remain:
        remain = NUM_OF_STATES - web3.eth.syncing['knownStates']
        time.sleep(interval)
        speed = (web3.eth.syncing['knownStates'] - known_states) / period
        if speed > max_speed:
            max_speed = speed
        if speed < min_speed or not min_speed:
            min_speed = speed

        period += interval
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
              'avg:', round(speed), 'max:', round(max_speed), 'min:', round(min_speed), 'states/s',
              '\tremain:', remain, 'states\t', web3.net.peerCount, 'peers',
              '\teta@', timedelta(seconds=remain / speed))


measure(INTERVAL)
