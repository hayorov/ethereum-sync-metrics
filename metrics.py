#!/usr/bin/env python
# -*- coding: utf-8 -*-
import signal
import sys
import time
from datetime import datetime, timedelta

from selfupdate import *
from userconfig import INTERVAL
from knownstates import NUM_OF_STATES
from knownstates import NUM_OF_STATES_AS_OF

known_states = 0

web3 = Web3(Web3.HTTPProvider(NODE_ADDRESS))  # your node


# NUM_OF_STATES = 446266045  # Actual for Feb, 15 2020

def signal_handler(signal, frame):
    print('Stopping...')
    updater(known_states, NUM_OF_STATES)
    ##TODO: PUSH STATE TOTAL FILE TO SERVER MAYBE?
    sys.exit(3)


signal.signal(signal.SIGINT, signal_handler)


def measure(interval=INTERVAL):
    if web3.eth.syncing == False:
        print('NOT SYNCING')
        sys.exit(1)

    if isinstance(web3.eth.syncing, object):
        remain = 1
        period = interval
        known_states = web3.eth.syncing['knownStates']
        max_speed = min_speed = 0
        print('Calculating...')
        while remain:
            remain = NUM_OF_STATES - web3.eth.syncing['knownStates']
            pulled = web3.eth.syncing['pulledStates']
            time.sleep(interval)
            if web3.eth.syncing != False:
                speed = (web3.eth.syncing['knownStates'] - known_states) / period
                if speed > max_speed:
                    max_speed = speed
                if speed < min_speed or not min_speed:
                    min_speed = speed

                period += interval
                if NUM_OF_STATES > known_states:
                    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                          'avg:', round(speed), 'max:', round(max_speed), 'min:', round(min_speed), 'states/s',
                          '\tremain:', remain, 'states\t', web3.net.peerCount, 'peers',
                          '\teta@', timedelta(seconds=remain / speed))
                if NUM_OF_STATES < known_states:
                    updater(known_states, NUM_OF_STATES)
                    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                          'avg:', round(speed), 'max:', round(max_speed), 'min:', round(min_speed), 'states/s',
                          '\tremaining best guess:', (NUM_OF_STATES_AS_OF - pulled), 'states\t', web3.net.peerCount,
                          'peers',
                          '\teta@', timedelta(seconds=(NUM_OF_STATES_AS_OF - pulled) / speed))

measure(INTERVAL)
