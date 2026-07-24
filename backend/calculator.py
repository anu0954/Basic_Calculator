import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def add(a, b):
    logging.info(f"Adding {a} + {b}")
    return a + b


def sub(a, b):
    logging.info(f"Subtracting {a} - {b}")
    return a - b


def mul(a, b):
    logging.info(f"Multiplying {a} * {b}")
    return a * b


def div(a, b):
    logging.info(f"Dividing {a} / {b}")

    try:
        return a / b

    except ZeroDivisionError:
        logging.error("Division by zero attempted")
        return "Error: Cannot divide by zero"