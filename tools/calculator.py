def calculator(expression):

    try:
        return str(eval(expression))

    except Exception as e:
        return str(e)