from langchain.tools import tool
from datetime import datetime


@tool
def get_current_time() -> str:
    """Returns the current time."""
    return datetime.now().strftime("%H:%M:%S")


@tool
def calculator(expression: str) -> str:
    """Evaluate a mathematical expression."""
    return str(eval(expression))


@tool
def count_words(text: str) -> int:
    """Count the number of words in a text."""
    return len(text.split())


@tool
def count_characters(text: str) -> int:
    """Count the number of characters in a text."""
    return len(text)


@tool
def reverse_text(text: str) -> str:
    """Reverse a string."""
    return text[::-1]


@tool
def to_uppercase(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()


@tool
def to_lowercase(text: str) -> str:
    """Convert text to lowercase."""
    return text.lower()


@tool
def is_even(number: int) -> bool:
    """Check if a number is even."""
    return number % 2 == 0


@tool
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


@tool
def greet(name: str) -> str:
    """Generate a greeting message."""
    return f"Hello {name}, welcome to LangChain!"



tools = [
    get_current_time,
    calculator,
    count_words,
    count_characters,
    reverse_text,
    to_uppercase,
    to_lowercase,
    is_even,
    celsius_to_fahrenheit,
    greet,
]