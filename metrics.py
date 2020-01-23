#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from datetime import datetime, timedelta

from web3 import Web3

web3 = Web3(Web3.HTTPProvider('https://xxxx.chainstack.com'))  # your node

NUM_OF_STATES = 432391041  # Actual for Jan, 17 2020


def measure(interval=30):
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


measure(30)
