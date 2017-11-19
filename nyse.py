from datetime import time
import pandas as pd
import pandas_market_calendars as mcal
import datetime as dt

from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, nearest_workday, \
    USMartinLutherKingJr, USPresidentsDay, GoodFriday, USMemorialDay, \
    USLaborDay, USThanksgivingDay


def print_nyse_cal():
    nyse = mcal.get_calendar('NYSE')
    print(nyse.holidays().holidays[-5:])
    pandas_only()

def pandas_only():
    print(get_trading_close_holidays(2016))


class USTradingCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday('NewYearsDay', month=1, day=1, observance=nearest_workday),
        USMartinLutherKingJr,
        USPresidentsDay,
        GoodFriday,
        USMemorialDay,
        Holiday('USIndependenceDay', month=7, day=4, observance=nearest_workday),
        USLaborDay,
        USThanksgivingDay,
        Holiday('Christmas', month=12, day=25, observance=nearest_workday)
    ]


def get_trading_close_holidays(year):
    inst = USTradingCalendar()

    return inst.holidays(dt.datetime(year-1, 12, 31), dt.datetime(year, 12, 31))

if __name__ == '__main__':
    print_nyse_cal();