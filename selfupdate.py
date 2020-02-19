#!/usr/bin/env python
# -*- coding: utf-8 -*-

from web3 import Web3
from userconfig import NODE_ADDRESS
import fileinput

web3 = Web3(Web3.HTTPProvider(NODE_ADDRESS))


def updater(known_states, NUM_OF_STATES):
	if known_states > NUM_OF_STATES:
		print('The current known state is higher than config...Updating Config...')
		print('Known States = ', known_states)
		print('Config File States = ', NUM_OF_STATES)
		##TODO: CHECK KNOWN STATES HAVE INCREASED BEFORE MAKING ANOTHER WRITE
		replace_in_file('knownstates.py', str(NUM_OF_STATES), str(known_states))
		print('New state config is now', known_states)
	if known_states < NUM_OF_STATES:
		print('NOT IN SYNC WITH NETWORK YET, COME BACK SOON')


def replace_in_file(file_path, search_text, new_text):
	with fileinput.input(file_path, inplace=True) as f:
		for line in f:
			new_line = line.replace(search_text, new_text)
			print(new_line, end='')
