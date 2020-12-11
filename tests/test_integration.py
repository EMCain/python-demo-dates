import datetime
import unittest

import pytest

from src.info_string import this_year_info_string


class TestThisYearInfoString:
    def test_this_year_info_string(self, mock_today):
        info = this_year_info_string()
        assert info == """Today is Tuesday, May 20, 2014
The first Sundays for 2014 are: 
Sunday, January  5, 2014
Sunday, February  2, 2014
Sunday, March  2, 2014
Sunday, April  6, 2014
Sunday, May  4, 2014
Sunday, June  1, 2014
Sunday, July  6, 2014
Sunday, August  3, 2014
Sunday, September  7, 2014
Sunday, October  5, 2014
Sunday, November  2, 2014
Sunday, December  7, 2014
"""

    @pytest.fixture
    def mock_today(self, mocker):
        class MyDate(datetime.date):
            @classmethod
            def today(cls, **kwargs):
                return datetime.datetime(2014, 5, 20).date()

        patched_date = mocker.patch("src.date_functions.datetime.date", MyDate)