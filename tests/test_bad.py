import datetime
import re

from src.info_string import this_year_info_string


class TestThisYearInfoStringBadExample:
    # This is bad because we don't learn anything meaningful about how the date is used 
    def test_this_year_info_string_pattern(self):
        info = this_year_info_string()
        assert re.match(
            r"Today is \w+day, \w+ \d+, \d{4}\nThe first \w+days for \d{4} are:",
            info
        ) is not None

    # This is bad because it duplicates the function logic and is hard to read
    def test_this_year_info_string_formatted(self):
        info = this_year_info_string()
        today = datetime.date.today()
        assert info.startswith(
            f"Today is {today.strftime('%A, %B %e, %Y')}\nThe first Sundays for {today.year} are:"
        )
    # Also, neither test asserts anything about the entire output, just the start