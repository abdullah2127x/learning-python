# def greet(name: str) -> str:
#     return f"Hello, {name}"

# result = greet("42")  # Type checker: ERROR! 42 is not a str

# #  uv run pyright .\pyright_file.py
#
#


# def get_count() -> int:
#     return 5  # ERROR: returns str, not int



def process(data: str | None) -> int:
    return len(data) if data else 0