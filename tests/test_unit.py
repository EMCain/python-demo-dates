import datetime

import pytest
from freezegun import freeze_time

from src.date_functions import first_sunday, third_tuesday, this_year_info


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



@pytest.mark.parametrize(
    "year,month,expected",
    [
        (2002, 2, "2002-02-19"),
        (2006, 5, "2006-05-16"),
        (2020, 11, "2020-11-17"),
        (2029, 7, "2029-07-17"),
        (2036, 6, "2036-06-17"),
    ]
)
def test_third_tuesday_returns_the_third_tuesday_of_the_month(year, month, expected):
    result = third_tuesday(year, month)
    assert result == datetime.datetime.strptime(expected, "%Y-%m-%d").date()


@pytest.mark.parametrize(
    "year,expected",
    [
        (2002, "2002-02-03"),
        (2006, "2006-05-07"),
        (2020, "2020-11-01"),
        (2029, "2029-07-01"),
        (2036, "2036-06-01"),
    ]
)
def test_this_year_info_returns_first_sundays_for_whole_year(year, expected):
    with freeze_time(lambda : datetime.date(year, 1, 1)):
        info = this_year_info()
        expected_date = datetime.datetime.strptime(expected, "%Y-%m-%d").date()
        assert expected_date in info["first_sundays"]
