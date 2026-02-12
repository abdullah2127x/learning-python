# import click

# @click.command()
# @click.option("--count", default=1, help="Number of times to print the message")
# @click.argument("name")
# def hello(count, name):
#     """Prints 'Hello' multiple times."""
#     for _ in range(count):
#         click.echo(f"Hello, {name}!")

# if __name__ == "__main__":
#     hello()


# ========
# import click

# @click.command()
# @click.argument("name", required=False)
# def hello(name):
#     if not name:
#         name = click.prompt("What is your name?")
#     click.echo(f"Hello, {name}!")

# if __name__ == "__main__":
#     hello()

# =================


# import click

# @click.command()
# # @click.option("--name", default="Guest", help="Enter your name")  # Add an option
# @click.option("--name", required=True, help="Enter your name")  # Add an option
# def hello(name):
#     """Greets the user with their name."""
#     click.echo(f"Hello, {name}!")

# if __name__ == "__main__":
#     hello()

# =====================
# select the given city only
# import click

# @click.command()
# @click.option("--city", type=click.Choice(["Karachi", "Lahore", "Islamabad"], case_sensitive=False), help="Choose your city")
# def select_city(city):
#     """Displays the selected city."""
#     click.echo(f"You selected: {city}")

# if __name__ == "__main__":
#     select_city()
# ==============


# import click

# @click.command()
# @click.option("--name", required=True, help="Enter your name")
# @click.option("--age", type=int, required=True, help="Enter your age")
# def user_info(name, age):
#     """Displays user information."""
#     click.echo(f"Name: {name}, Age: {age}")

# if __name__ == "__main__":
#     user_info()
# ==========true/false =============================
# import click

# @click.command()
# @click.option("--hobby", multiple=True, help="Enter your hobbies")
# def show_hobbies(hobby):
#     """Displays hobbies."""
#     click.echo(f"Your hobbies: {', '.join(hobby)}")

# if __name__ == "__main__":
#     show_hobbies()
# ===============
# 1
# import click

# @click.command()
# @click.option("--debug/--no-debug", default=False, help="Enable or disable debug mode")
# def run(debug):
#     """Runs the program with debug mode."""
#     if debug:
#         click.echo("Debug mode is ON 🛠️")
#     else:
#         click.echo("Debug mode is OFF 📴")

# if __name__ == "__main__":
#     run()
# =======================================
# 2
# import click

# @click.command()
# @click.option("--debug", is_flag=True, help="Enable debug mode")
# def run(debug):
#     """Runs the program with debug mode."""
#     if debug:
#         click.echo("Debug mode is ON 🛠️")
#     else:
#         click.echo("Debug mode is OFF 📴")

# if __name__ == "__main__":
#     run()
# ============================
# 3
# import click

# @click.command()
# @click.option("--debug", type=bool, help="Enable debug mode")
# def run(debug):
#     """Runs the program with debug mode."""
#     if debug:
#         click.echo("Debug mode is ON 🛠️")
#     else:
#         click.echo("Debug mode is OFF 📴")

# if __name__ == "__main__":
#     run()

# ===============practice boolean =================
# Modify the following Click program to add a --debug option.
# ✅ If --debug is used, print "Debug mode is ON 🛠️"
# ✅ If --debug is not used, print "Debug mode is OFF 📴"
# import click

# @click.command()
# # Add an option here for debug mode
# @click.option("--debug", is_flag=True, help="Enable debug mode")
# def run(debug):
#     """Runs the program."""
#     # Print debug mode ON/OFF based on user input
#     if debug:
#         click.echo("Debug mode is ON 🛠️")
#     else:
#         click.echo("Debug mode is OFF 📴")

# if __name__ == "__main__":
#     run()
# ====
# Modify your program to: ✅ Add an extra name for --debug (use -d)
# ✅ Add an extra name for --verbose (use --log)
# import click

# @click.command()
# @click.option("--debug", "-d", is_flag=True, help="Enable debug mode")  # Added "-d"
# @click.option("--verbose", "-v", "--log", is_flag=True, help="Enable verbose mode")  # Added "--log"
# def run(debug, verbose):
#     """Runs the program."""

#     if debug:
#         click.echo("Debug mode is ON 🛠️")
#     else:
#         click.echo("Debug mode is OFF 📴")

#     if verbose:
#         click.echo("Verbose mode is ON 📢 (Showing extra details)")
#     else:
#         click.echo("Verbose mode is OFF 🤫 (Only basic output)")

# if __name__ == "__main__":
#     run()
# ================
# import click


# @click.command()
# @click.option("--debug", "-d", is_flag=True, help="Enable debug mode")
# @click.option("--verbose", "-v", "--log", is_flag=True, help="Enable verbose mode")

# @click.option("--name","-n",default="Guest" ,type=str, help="Name of the option")
# def run(debug, verbose, name):
#     """Runs the program."""

#     if debug:
#         click.echo("Debug mode is ON 🛠️")
#     else:
#         click.echo("Debug mode is OFF 📴")

#     if verbose:
#         click.echo("Verbose mode is ON 📢 (Showing extra details)")
#     else:
#         click.echo("Verbose mode is OFF 🤫 (Only basic output)")

#     click.echo(f"Hello, {name}!")


# if __name__ == "__main__":
#     run()

# ============================learning again====================================
# import click

# @click.command()
# @click.option("--name", default = "Guest", help="Enter your name")
# @click.option("--role", "-r",  type=click.Choice(['admin', 'user', "guest"]),default="guest", help="Enable verbose mode")
# def run(name, role):
#     """Runs the program."""
#     click.echo(f"Hello, {name}!")

#     if role == "admin":
#         click.echo("Welcome, Admin! 🔑")
#     elif role == "user":
#         click.echo("Hello, User! 👋")
#     else:
#         click.echo("Enjoy as a Guest! 🎉")

# if __name__ == "__main__":
#     run()

# ===========multiple arguments============
# import click

# @click.command()
# @click.argument("num1", type=int, default=0)
# @click.argument("num2",type=int, default=0)

# def add(num1, num2):
#     """Adds two numbers and prints the result."""
    
#     result = num1 + num2
#     click.echo(f"The sum of {num1} and {num2} is {result}")

# if __name__ == "__main__":
#     add()
# =============
# import click

# @click.command()
# @click.argument("numbers", type=int, nargs=-1)


# def add(numbers):
#     """add all the numbers"""

    
#     result = sum(numbers)
#     click.echo(f"The sum of all numbers is {result}")

# if __name__ == "__main__":
#     add()
