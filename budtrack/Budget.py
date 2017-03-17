'''Contain a class for containing and maintaining a budget.'''

import BudgetDate as BudgetDate


class Budget():
    '''Class to represent a budget.

    Attributes:
        budget_name: Budget's name.
        move_leftover: A boolean to indicate whether to move unspent
                       spending to another period iteration in a topic.
        topics: A dictionary to contain sub-dictionaries of topics.
        budget_date_object: A BudgetDate object to indicate creation of
                            budget.
    '''

    def __init__(self, budget_name, reset_period_type, move_leftover):
        '''Budget constructor.'''
        self.budget_name = budget_name
        self.move_leftover = move_leftover
        self.budget_date_object = BudgetDate.BudgetDate(
            reset_period_type)
        self.topics = {}

    def add_topic(self, topic_name, limit):
        '''Add a topic to a budget.

        Args:
            topic_name: A string value for a topic name.
            limit: A float value to represent a limit on total spending.
        '''
        topic = {'current_spending': 0.0, 'limit': limit,
                 'original_limit': limit}
        self.topics[topic_name] = topic

    def remove_topic(self, topic_name):
        '''Remove a topic from a budget.'''
        del(self.topics[topic_name])

    def get_budget_name(self):
        '''Return a string that represents a budget name.'''
        return self.budget_name

    def change_reset_type(self, new_reset_type):
        '''Change a period reset type.'''
        self.budget_date_object.change_reset_type(new_reset_type)

    def increment_current_spending_in_topic(self, topic_name, amount):
        '''Increase current spending in a certain topic.'''
        self._check_and_perform_reset_operation()
        topic = self.topics[topic_name]
        topic['current_spending'] += amount

    def get_current_topic_status(self, topic_name):
        '''Return a string representing topic's attributes.'''
        topic = self.topics[topic_name]
        date_obj = self.budget_date_object
        str_date = date_obj.get_string_reset_date()
        str_current_spending = "{:.2f}".format(topic['current_spending'])
        str_current_limit = "{:.2f}".format(topic['limit'])
        message = "Budget's topic reset date: {0}\n" \
                  "Current '{1}' topic's status:\n" \
                  "Current Spending: {2}\n"  \
                  "Current Limit: {3}"
        message = message.format(str_date, topic_name,
                                 str_current_spending,
                                 str_current_limit)
        return message

    def generate_summary_of_topics_attributes(self):
        '''Return a string that lists topics and their attributes.

        Return an empty string if the self.topics has got no topics.
        '''
        if not self.topics:
            return ""
        topic_name_list = sorted(self.topics.keys())
        summary_header = "Topic Name  Current Spending  Current Limit"
        output_format = "{0:10}  {1:16.2f}  {2:13.2f}"
        formatted_string_list = [summary_header]
        for topic_name in topic_name_list:
            topic = self.topics[topic_name]
            formatted_string = output_format.format(topic_name,
                                            topic['current_spending'],
                                            topic['limit'])
            formatted_string_list.append(formatted_string)
        generated_summary = "\n".join(formatted_string_list)
        return generated_summary


    def _check_and_perform_reset_operation(self):
        '''Check if a budget reached end period and perform reset.'''
        date_obj = self.budget_date_object
        reached_end = date_obj.has_reached_reset_period_end()
        if reached_end:
            self._reset_topics_current_spending()
            date_obj.update_reset_date()

    def _reset_topics_current_spending(self):
        '''Reset every topic's current spending.'''
        topic_list = self.topics.values()
        for topic in topic_list:
            if self.move_leftover:
                limit = topic['limit']
                current_spending = topic['current_spending']
                spending_difference = limit - current_spending
                if spending_difference <= 0.0:
                    topic['limit'] = topic['original_limit']
                else:
                    new_limit = limit + spending_difference
                    topic['limit'] = new_limit
            topic['current_spending'] = 0.0
