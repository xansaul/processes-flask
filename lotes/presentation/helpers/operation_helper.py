import re
import random


def validate_operation(operation):
    try:
        if re.match('^-?\d+[+*/%-]-?\d+$', operation) and '/0' not in operation and '%0' not in operation:
            return True
    except:
        return False


def generate_operation():
    symbols = ['+', '-', '/', '*', '%']
    operation = str(random.randint(0, 100))+random.choice(symbols)+str(random.randint(0, 100))

    return operation


def validate_array_ids(array_to_validate, expected_length):
    if not isinstance(array_to_validate, list) or not all(isinstance(x, int) for x in array_to_validate):
        raise ValueError("ids must be a list of integers")
    if len(array_to_validate) != expected_length:
        raise ValueError("ids array length does not match number of processes")
