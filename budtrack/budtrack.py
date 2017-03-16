#!/usr/bin/env python3
'''This is a main file that needs to be run in order to run the program.'''

from request_processor import process_request
from input_user_interface import get_parsed_user_input


def run():
    '''Main function that starts the whole program'''
    user_input_dict = get_parsed_user_input()
    process_request(user_input_dict)


if __name__ == "__main__":
    run()
