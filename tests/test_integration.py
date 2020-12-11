import datetime

import pytest

from src.info_string import this_year_info_string


class TestThisYearInfoString:
    def test_this_year_info_string(self, mock_today):
        info = this_year_info_string()
        import pdb; pdb.set_trace
        print(info)

    @pytest.fixture
    def mock_today(self, monkeypatch):
        class MyDate(datetime.date):
            @classmethod
            def today(cls, **kwargs):
                return datetime.datetime(2014, 5, 20)

        patched_date = monkeypatch.setattr(datetime, "date", MyDate)