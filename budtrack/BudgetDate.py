'''A class to have time operations.'''

import constants as constants
from datetime import date, timedelta


class BudgetDate():
    '''A class to represent time and have some useful operations.

    Attributes:
        reset_period_type: A string period to indicate how often to
                           reset topic's limits.
        creation_date: Creation date of a budget.
        previous_reset_date: a date to indicate when topics were reset.
        reset_period_type: a date to represent
    '''

    def __init__(self, reset_period_type):
        self.creation_date = date.today()
        self.previous_reset_date = self.creation_date
        self.reset_period_type = reset_period_type

    def change_reset_type(self, new_reset_period_type):
        '''Change reset period type.'''
        self.reset_period_type = new_reset_period_type

    def get_string_reset_date(self):
        '''Return a string date of a reset date.'''
        reset_date = self._get_reset_date()
        str_date = reset_date.strftime("%d/%m/%y")
        return str_date

    def has_reached_reset_period_end(self):
        '''Check if a budget reached reset period and return boolean'''
        end_of_reset_period = self._get_reset_date()
        today = date.today()
        time_diff = end_of_reset_period - today
        num_of_days = time_diff.days
        if num_of_days <= 0:
            return True
        else:
            return False

    def update_reset_date(self):
        '''Update a reset date.'''
        today = date.today()
        self.previous_reset_date = today

    def _get_reset_date(self):
        '''Return date of an end for a current period before reset.'''
        time_diff = self._get_time_diff_based_on_reset_type()
        end_of_reset_period_date = self.previous_reset_date + time_diff
        return end_of_reset_period_date

    def _get_time_diff_based_on_reset_type(self):
        '''Return timedelta object with a certain time difference.'''
        reset_period_type = self.reset_period_type
        if reset_period_type == constants.WEEKLY_RESET_TYPE:
            time_diff = timedelta(weeks=1)
        elif reset_period_type == constants.MONTHLY_RESET_TYPE:
            time_diff = timedelta(weeks=4)
        return time_diff
