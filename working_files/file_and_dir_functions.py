'''Functions responsible for performing file and directory operations.

Exported functions:
create_budget -- used in request_processor.py.
save_budget -- used in request_processor.py.
get_budget -- used in request_processor.py.
'''

import os
import pickle

import Budget

CONFIG_DIRECTORY = "~/.budtrack/"


def create_budget(budget_name, reset_period_type, move_leftover):
    '''Create a budget object and then save it to a file.'''
    created_budget = Budget.Budget(budget_name, reset_period_type,
                                   move_leftover)
    save_budget(created_budget)


def remove_budget(budget_name):
    '''Remove a file that represents a budget.'''
    budget_file_path = _get_budget_file_path(budget_name)
    os.remove(budget_file_path)


def save_budget(budget_object):
    '''Save a budget instance to a file.'''
    _pickle_to_file(budget_object)


def get_budget(budget_name):
    '''Return Budget object after unpickling it from a file.'''
    budget_object = _unpickle_from_file(budget_name)
    return budget_object

def list_budgets():
    '''Return a list of budget names.'''
    list_of_budgets = os.listdir(os.path.expanduser(CONFIG_DIRECTORY))
    list_of_budget_names = [file_name.replace(".pickle", "") for
                            file_name in list_of_budgets]
    return list_of_budget_names


def _unpickle_from_file(budget_name):
    '''Return an 'unpickled' Budget object from a given file.'''
    budget_file_path = _get_budget_file_path(budget_name)
    with open(budget_file_path, "rb") as file_object:
        budget_object = pickle.load(file_object)
    return budget_object


def _pickle_to_file(budget_object):
    '''Pickle a Budget object to a file.'''
    CHOSEN_PICKLE_PROTOCOL = 4
    budget_name = budget_object.get_budget_name()
    budget_file_path = _get_budget_file_path(budget_name)
    with open(budget_file_path, "wb") as file_object:
        pickle.dump(budget_object, file_object, CHOSEN_PICKLE_PROTOCOL)


def _get_budget_file_path(budget_name):
    '''Return an absolute path with a formatted budget file name.'''
    expanded_path = os.path.expanduser(CONFIG_DIRECTORY)
    budget_file_name = budget_name + ".pickle"
    expanded_path += budget_file_name
    return expanded_path
