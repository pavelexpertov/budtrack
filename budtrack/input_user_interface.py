'''
Budtrack

Usage:
    budtrack add budget <budget-name> (weekly|monthly)
    (move_leftover|discard_leftover)
    budtrack add topic <budget-name> <topic-name> <spending-limit>
    budtrack remove budget <budget-name>
    budtrack remove topic <budget-name> <topic-name>
    budtrack change reset_type <budget-name> (weekly|monthly)
    budtrack update spending <budget-name> <topic-name>
    <spending-amount>
    budtrack list budgets
    budtrack list topics <budget-name>
'''

import constants as cs

from docopt import docopt


def get_parsed_user_input():
    '''Returns a dict with user input.

    Each 'if' block calls an appropriate function for a given command.
    These functions return a parsed dictionary that contain user
    arguments and then it's returned to a calling function.
    '''
    user_arguments = docopt(__doc__, version='Budtrack 0.1')

    if user_arguments['remove']:
        parsed_arguments = _get_dict_for_remove_command(user_arguments)
    elif user_arguments['add']:
        parsed_arguments = _get_dict_for_add_command(user_arguments)
    elif user_arguments['change']:
        parsed_arguments = _get_dict_for_change_command(user_arguments)
    elif user_arguments['update']:
        parsed_arguments = _get_dict_for_update_command(user_arguments)
    elif user_arguments['list']:
        parsed_arguments = _get_dict_for_list_command(user_arguments)

    return parsed_arguments


# PARSING FUNCTIONS FOR EACH AVAILABLE COMMAND


def _get_dict_for_remove_command(user_arguments):
    '''Return a dict with parsed user arguments for remove command'''
    ua = user_arguments
    parsed_values = {}

    parsed_values[cs.BUDGET_NAME] = ua['<budget-name>']
    # If removing a budget's topic
    if ua['topic']:
        parsed_values[cs.COMMAND_NAME] = cs.REMOVE_TOPIC_COMMAND
        parsed_values[cs.TOPIC_NAME] = ua['<topic-name>']
    elif ua['budget']:
        parsed_values[cs.COMMAND_NAME] = cs.REMOVE_BUDGET_COMMAND

    return parsed_values


def _get_dict_for_add_command(user_arguments):
    '''Return a dict with parsed user arguments for add command'''
    ua = user_arguments
    parsed_values = {}

    parsed_values[cs.BUDGET_NAME] = ua['<budget-name>']
    # If adding a topic to a budget
    if ua['topic']:
        parsed_values[cs.COMMAND_NAME] = cs.ADD_TOPIC_COMMAND
        parsed_values[cs.TOPIC_NAME] = ua['<topic-name>']
        casted_amount = _convert_string_to_float(ua['<spending-limit>'])
        parsed_values[cs.SPENDING_LIMIT] = casted_amount
    elif ua['budget']:
        parsed_values[cs.COMMAND_NAME] = cs.ADD_BUDGET_COMMAND
        if ua['weekly']:
            parsed_values[cs.RESET_TYPE] = cs.WEEKLY_RESET_TYPE
        elif ua['monthly']:
            parsed_values[cs.RESET_TYPE] = cs.MONTHLY_RESET_TYPE

        if ua['move_leftover']:
            parsed_values[cs.MOVE_LEFTOVER] = True
        elif ua['discard_leftover']:
            parsed_values[cs.MOVE_LEFTOVER] = False

    return parsed_values


def _get_dict_for_change_command(user_arguments):
    '''Return a dict with parsed user arguments for change command.'''
    ua = user_arguments
    parsed_values = {}

    if ua['reset_type']:
        parsed_values[cs.COMMAND_NAME] = cs.CHANGE_RESET_TYPE_COMMAND
        parsed_values[cs.BUDGET_NAME] = ua['<budget-name>']
        if ua['weekly']:
            parsed_values[cs.RESET_TYPE] = cs.WEEKLY_RESET_TYPE
        elif ua['monthly']:
            parsed_values[cs.RESET_TYPE] = cs.MONTHLY_RESET_TYPE

    return parsed_values


def _get_dict_for_update_command(user_arguments):
    '''Return a dict with parsed user arguments for update command.'''
    ua = user_arguments
    parsed_values = {}

    parsed_values[cs.BUDGET_NAME] = ua['<budget-name>']
    if ua['spending']:
        parsed_values[cs.COMMAND_NAME] = cs.UPDATE_SPENDING_COMMAND
        string_amount = ua['<spending-amount>']
        casted_amount = _convert_string_to_float(string_amount)
        parsed_values[cs.SPENDING_UPDATE] = casted_amount
        parsed_values[cs.TOPIC_NAME] = ua['<topic-name>']

    return parsed_values


def _get_dict_for_list_command(user_arguments):
    '''Returns a dict with parsed user arguments for list command.'''
    ua = user_arguments
    parsed_values = {}

    if ua['budgets']:
        parsed_values[cs.COMMAND_NAME] = cs.LIST_BUDGETS_COMMAND
    elif ua['topics']:
        parsed_values[cs.BUDGET_NAME] = ua['<budget-name>']
        parsed_values[cs.COMMAND_NAME] = cs.LIST_TOPICS_COMMAND

    return parsed_values


# UTILITY FUNCTIONS


def _convert_string_to_float(string_amount):
    '''Cast a string to a float type.'''
    try:
        casted_amount = float(string_amount)
        casted_amount = round(casted_amount, 2)
        return casted_amount
    except ValueError:
        error_message = "You have entered something that's not a " \
                        "number for a field that takes a decimal " \
                        "number. Please enter a legit number for the " \
                        "previous command you have just executed."
        exception = ValueError(error_message)
        raise exception
