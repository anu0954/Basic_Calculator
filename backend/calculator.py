import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def add(a, b):
    logging.info(f"Addition requested: {a} + {b}")
    return a + b


def sub(a, b):
    logging.info(f"Subtraction requested: {a} - {b}")
    return a - b


def mul(a, b):
    logging.info(f"Multiplication requested: {a} * {b}")
    return a * b


def div(a, b):
    logging.info(f"Division requested: {a} / {b}")

    if b == 0:
        logging.warning("Attempted division by zero")
        return "Cannot divide by zero"

    return a / b