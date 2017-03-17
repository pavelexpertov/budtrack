'''Functions responsible for handling user's request.'''

import constants
import file_and_dir_functions as file_operations
import output_user_interface as output

# Public function


def process_request(user_input):
    '''Process user's input arguments to perform a certain operation.'''
    _perform_an_operation(user_input)


def _get_budget_object(budget_name):
    '''Return budget object based on an argument that's passed.'''
    budget_object = file_operations.get_budget(budget_name)
    return budget_object


def _save_budget_object(budget_object):
    '''Save budget object to a file.'''
    file_operations.save_budget(budget_object)


def _perform_an_operation(user_input):
    '''Perform an operation on a Budget object based on user's command.

    Most of operation functions perform the following:
    1. Get a Budget object based on a budget name. If it doesn't exist,
    then an exception is thrown.
    2. Perform an operation based on a user's command and then execute
    an appropriate function and pass budget's object and other
    necessary arguments. This will have a function that chooses an
    operation and then handle any errors to output to the user.
    3. Write the Budget object back to a file.
    However, there are other functions that may not follow the above.
    '''
    requested_command = user_input[constants.COMMAND_NAME]
    if requested_command == constants.ADD_BUDGET_COMMAND:
        budget_name = user_input[constants.BUDGET_NAME]
        reset_type = user_input[constants.RESET_TYPE]
        move_leftover = user_input[constants.MOVE_LEFTOVER]
        _create_budget(budget_name, reset_type, move_leftover)
    elif requested_command == constants.ADD_TOPIC_COMMAND:
        budget_name = user_input[constants.BUDGET_NAME]
        topic_name = user_input[constants.TOPIC_NAME]
        limit = user_input[constants.SPENDING_LIMIT]
        _add_new_topic(budget_name, topic_name, limit)
    elif requested_command == constants.REMOVE_BUDGET_COMMAND:
        budget_name = user_input[constants.BUDGET_NAME]
        _remove_budget(budget_name)
    elif requested_command == constants.REMOVE_TOPIC_COMMAND:
        budget_name = user_input[constants.BUDGET_NAME]
        topic_name = user_input[constants.TOPIC_NAME]
        _remove_topic(budget_name, topic_name)
    elif requested_command == constants.CHANGE_RESET_TYPE_COMMAND:
        budget_name = user_input[constants.BUDGET_NAME]
        period_type = user_input[constants.RESET_TYPE]
        _change_reset_period(budget_name, period_type)
    elif requested_command == constants.UPDATE_SPENDING_COMMAND:
        budget_name = user_input[constants.BUDGET_NAME]
        topic_name = user_input[constants.TOPIC_NAME]
        amount = user_input[constants.SPENDING_UPDATE]
        _increment_topics_current_spending(budget_name, topic_name,
                                           amount)
    elif requested_command == constants.LIST_BUDGETS_COMMAND:
        _list_budgets()
    elif requested_command == constants.LIST_TOPICS_COMMAND:
        budget_name = user_input[constants.BUDGET_NAME]
        _list_budget_topics_and_expenditures(budget_name)
    else:
        error_msg = "A command has not been found in a dict that's " \
                    "been passed recently"
        raise Exception(error_msg)


# Set of available operations to execute by _perform_an_operation

def _create_budget(budget_name, reset_type, move_leftover):
    '''Create a brand new budget for the program.'''
    file_operations.create_budget(budget_name, reset_type,
                                  move_leftover)
    output.output_successful_budget_creation(budget_name)


def _add_new_topic(budget_name, topic_name, limit):
    '''Create a topic for a particular budget.'''
    budget_object = _get_budget_object(budget_name)
    budget_object.add_topic(topic_name, limit)
    output.output_successful_topic_creation(budget_name, topic_name)
    _save_budget_object(budget_object)

def _remove_budget(budget_name):
    '''Remove a given budget.'''
    file_operations.remove_budget(budget_name)
    output.output_successful_budget_removal(budget_name)


def _remove_topic(budget_name, topic_name):
    '''Update current spending for a given topic and budget.'''
    budget_object = _get_budget_object(budget_name)
    budget_object.remove_topic(topic_name)
    output.output_successful_topic_removal(budget_name, topic_name)
    _save_budget_object(budget_object)


def _change_reset_period(budget_name, period_type):
    '''Change reset type in a given budget.'''
    budget_object = _get_budget_object(budget_name)
    budget_object.change_reset_type(period_type)
    output.output_successful_change_reset_period(budget_name,
                                                 period_type)
    _save_budget_object(budget_object)


def _increment_topics_current_spending(budget_name, topic_name,
                                       amount):
    '''Update current spending for a given topic and budget.'''
    budget_object = _get_budget_object(budget_name)
    budget_object.increment_current_spending_in_topic(topic_name,
                                                      amount)
    topic_status = budget_object.get_current_topic_status(topic_name)
    output.output_incremented_spending_amount_for_topic(budget_name,
                                                        topic_name,
                                                        topic_status)
    _save_budget_object(budget_object)


def _list_budget_topics_and_expenditures(budget_name):
    '''List budget's topics and their contents.'''
    budget_object = _get_budget_object(budget_name)
    summary = budget_object.generate_summary_of_topics_attributes()
    output.print_list_of_budgets_topic(budget_name, summary)

def _list_budgets():
    '''List all available budgets.'''
    budget_list = file_operations.list_budgets()
    if budget_list:
        print("Here's a list of available budgets:")
        for budget_name in budget_list:
            print(budget_name)
    else:
        print("Unfortunately, there're no available budgets here.")
