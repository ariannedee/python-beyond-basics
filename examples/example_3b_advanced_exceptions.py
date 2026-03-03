num = input("Number: ")

try:
    inverse = 1 / int(num)
except (ZeroDivisionError, ValueError):
    inverse = "not defined"

print(f"Inverse of {num} is {inverse}")


try:
    inverse = 1 / int(num)
except ZeroDivisionError:  # Catch multiple error types with different behaviour
    inverse = "+/- infinity"
except ValueError:
    inverse = "not defined"
except Exception as e:
    print(repr(e))


try:
    int("5")
except ValueError:
    print("Fail!")
else:
    print("Everything worked")    # Runs after try block finishes without errors
finally:
    print("This always happens")  # Runs after everything, even if there was an error


class MyCustomError(Exception):
    pass


raise MyCustomError("Here's an error message")
