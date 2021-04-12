import random
import string


def generate_codes(number_of_codes: int, code_length: int):
    """Generates X number of random codes based on the provided length.

    Pramas:
    -------
        number_of_codes (int): The number of the random codes that shall be
            created which should be unique also.
        code_length (int): The length of the code which will be generated.
    """
    codes = set()
    choices = string.ascii_uppercase + string.digits
    while len(codes) < number_of_codes:
        code = ''.join(random.SystemRandom().choice(choices) for _ in range(code_length))
        codes.add(code)
    return codes
