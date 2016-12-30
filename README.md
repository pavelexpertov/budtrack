# budtrack
A simple cmd-based budget tracker

# Why?
I wanted to track my personal weekly budget and I know I could have
probably used open-source alternatives to make my life much easier, but
I wanted to do some practicing with designing software architecture.

# USAGE
The usage of the program can be found as a string in
input_user_interface module, but I will provide the following here:
```
Usage:
    budtrack add budget <budget-name> (weekly|monthly) (move_leftover|discard_leftover)
    budtrack add topic <budget-name> <topic-name> <spending-limit>
    budtrack remove budget <budget-name>
    budtrack remove topic <budget-name> <topic-name>
    budtrack change reset_type <budget-name> (weekly|monthly)
    budtrack update spending <budget-name> <topic-name> <spending-amount>
    budtrack list budgets
    budtrack list topics <budget-name>
```
whereas **budtrack** is _budtrack.py_. Well, you supposed to make the
file executable by using `chmod +x budtrack.py` and then run it by
typing it `./budtrack.py blah blah`. Hope this helps ;).
