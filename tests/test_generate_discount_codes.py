import pytest

from app.utils import generate_codes

@pytest.mark.parametrize(
    'number_of_codes,expected',
    [
        (1, 1), (10, 10), (100, 100), (1000, 1000)
    ]
)
def test_generate_codes_creates_same_number_codes(number_of_codes,expected):
    "Test that number of code generated is equal to the number of code requested"
    code_length = 6
    assert len(generate_codes(number_of_codes, code_length)) == expected


@pytest.mark.parametrize(
    'code_length,expected',
    [
        (5, 5), (10, 10), (15, 15), (20, 20)
    ]
)
def test_generate_codes_creates_code_with_requested_length(code_length,expected):
    "Test that number of code generated is equal to the number of code requested"
    number_of_codes = 1
    code = generate_codes(number_of_codes, code_length).pop()
    assert len(code) == expected
