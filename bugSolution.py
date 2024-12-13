def function_with_error_handling(x):
    try:
        if x == 0:
            return 0 #or raise a custom exception
        else:
            return x + 5
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"An unexpected error occurred: {e}"