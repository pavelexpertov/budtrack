'''This module contains a set of constant values.

These constants values are used throughout different modules
to keep certain passed values consistent when some functions
want to use one and keep it consistent.
'''

# RESET TYPES FOR BUDGET CLASS
WEEKLY_RESET_TYPE = 'weekly'
MONTHLY_RESET_TYPE = 'monthly'

# KEY VALUES FOR USER INPUT DICTIONARY

BUDGET_NAME = 'budget_name'
COMMAND_NAME = 'command_name'
TOPIC_NAME = 'topic_name'
RESET_TYPE = 'reset_type'
SPENDING_LIMIT = 'spending_limit'
SPENDING_UPDATE = 'spending_update'
MOVE_LEFTOVER = 'move_leftover'

# COMMAND VALUES FROM COMMAND LINE INTERFACE
ADD_BUDGET_COMMAND = 'add_budget_command'
ADD_TOPIC_COMMAND = 'add_topic_command'
CHANGE_RESET_TYPE_COMMAND = 'change_reset_type_command'
LIST_BUDGETS_COMMAND = 'list_budgets_command'
LIST_TOPICS_COMMAND = 'list_topics_command'
REMOVE_TOPIC_COMMAND = 'remove_topic_command'
REMOVE_BUDGET_COMMAND = 'remove_budget_command'
UPDATE_SPENDING_COMMAND = 'update_spending_command'
