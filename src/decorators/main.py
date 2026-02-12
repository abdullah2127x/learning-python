# Decorator function to wrap another function
def greet(fc):
    def mfx():
        print("Good Morning!")  # Pre-function execution message
        fc()  # Calling the original function
        print("Good Bye")  # Post-function execution message
    return mfx

# Applying the decorator using @ syntax
@greet
def hello():
    print("Hello World!")  # Main function logic

# Calling the function
hello()

print("====================")

# Decorator function that supports arguments
def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning!")  # Pre-function execution message
        fx(*args, **kwargs)  # Calling the original function with arguments
        print("Good Bye")  # Post-function execution message
    return mfx

# Applying the decorator to a function that accepts arguments
@greet
def hello(name, age):
    print(f"Hello {name}! You are {age} years old.")  # Main function logic

# Calling the function with arguments
hello("Abdullah", 18)
