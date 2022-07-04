#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        divide = fct(*args)
        return divide
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
