import datetime

import pytest

from src.date_functions import first_sunday

# TODO parameterize, mock 

@pytest.mark.parametrize(
    "year,month,expected",
    [
        (2002, 2, "2002-02-03"),
        (2006, 5, "2006-05-07"),
        (2020, 11, "2020-11-01"),
        (2029, 7, "2029-07-01"),
        (2036, 6, "2036-06-01"),
    ]
)
def test_first_sunday_returns_the_first_sunday_of_the_month(year, month, expected):
    result = first_sunday(year, month)
    assert result == datetime.datetime.strptime(expected, "%Y-%m-%d").date()

     

# TODO parameterize, mock 
def test_this_year_info_returns_first_sundays_for_whole_year():
    pass