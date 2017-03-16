'''Functions responsible for outputing messages to a user.'''


def output_successful_budget_creation(budget_name):
    '''Print a message after creating a budget file successfully'''
    message = "New budget called '{0}' has been " \
              "created.".format(budget_name)
    print(message)


def output_successful_topic_creation(budget_name, topic_name):
    '''Print a message after crating a topic for a budget successfully'''
    message = "New topic called '{1}' has been created in '{0}' " \
              "budget.".format(budget_name, topic_name)
    print(message)


def output_successful_budget_removal(budget_name):
    '''Print a message after deleting a budget successfully.'''
    message = "Successfully removed a budget " \
              "called '{0}'.".format(budget_name)
    print(message)


def output_successful_topic_removal(budget_name, topic_name):
    '''Print a message after deleting a topic successfully.'''
    message = "Successfully removed '{1}' topic from " \
              "'{0}' budget.".format(budget_name, topic_name)
    print(message)


def output_successful_change_reset_period(budget_name, reset_type):
    '''Print a message after changing reset type in a budget.'''
    message = "Successfully changes a reset period to " \
              "{1} in {0} budget".format(budget_name, reset_type)
    print(message)


def output_incremented_spending_amount_for_topic(budget_name,
                                                 topic_name,
                                                 current_topic_status):
    '''Print a message after updating current spending for a topic.

    Args:
        budget_name: A budget's name in string type.
        budget_topic: A budget's topic's name in string type.
        current_status_string: A string that shows the topic's current
                               spending and its spending limit.
    '''
    message = "Successfully updated current spending for '{1}' topic " \
              "in '{0}' budget.\nCurrent status of '{1}' is:\n" \
              "{2}".format(budget_name, topic_name,
                           current_topic_status)
    print(message)


def print_list_of_budgets_topic(budget_name, topics_summary_string):
    '''Print a list of a budget's topics and their attributes.'''
    if topics_summary_string:
        message = "{0}'s topics:\n{1}".format(budget_name,
                                              topics_summary_string)
    else:
        message = "Unfortunately, '{0}' doesn't have " \
                  "any topics".format(budget_name)
    print(message)
