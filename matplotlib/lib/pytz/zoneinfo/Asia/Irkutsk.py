'''tzinfo timezone information for Asia/Irkutsk.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Irkutsk(DstTzInfo):
    '''Asia/Irkutsk timezone definition. See datetime.tzinfo for details'''

    _zone = 'Asia/Irkutsk'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1920,1,24,17,2,40),
d(1930,6,20,17,0,0),
d(1981,3,31,16,0,0),
d(1981,9,30,15,0,0),
d(1982,3,31,16,0,0),
d(1982,9,30,15,0,0),
d(1983,3,31,16,0,0),
d(1983,9,30,15,0,0),
d(1984,3,31,16,0,0),
d(1984,9,29,18,0,0),
d(1985,3,30,18,0,0),
d(1985,9,28,18,0,0),
d(1986,3,29,18,0,0),
d(1986,9,27,18,0,0),
d(1987,3,28,18,0,0),
d(1987,9,26,18,0,0),
d(1988,3,26,18,0,0),
d(1988,9,24,18,0,0),
d(1989,3,25,18,0,0),
d(1989,9,23,18,0,0),
d(1990,3,24,18,0,0),
d(1990,9,29,18,0,0),
d(1991,3,30,18,0,0),
d(1991,9,28,19,0,0),
d(1992,1,18,19,0,0),
d(1992,3,28,15,0,0),
d(1992,9,26,14,0,0),
d(1993,3,27,18,0,0),
d(1993,9,25,18,0,0),
d(1994,3,26,18,0,0),
d(1994,9,24,18,0,0),
d(1995,3,25,18,0,0),
d(1995,9,23,18,0,0),
d(1996,3,30,18,0,0),
d(1996,10,26,18,0,0),
d(1997,3,29,18,0,0),
d(1997,10,25,18,0,0),
d(1998,3,28,18,0,0),
d(1998,10,24,18,0,0),
d(1999,3,27,18,0,0),
d(1999,10,30,18,0,0),
d(2000,3,25,18,0,0),
d(2000,10,28,18,0,0),
d(2001,3,24,18,0,0),
d(2001,10,27,18,0,0),
d(2002,3,30,18,0,0),
d(2002,10,26,18,0,0),
d(2003,3,29,18,0,0),
d(2003,10,25,18,0,0),
d(2004,3,27,18,0,0),
d(2004,10,30,18,0,0),
d(2005,3,26,18,0,0),
d(2005,10,29,18,0,0),
d(2006,3,25,18,0,0),
d(2006,10,28,18,0,0),
d(2007,3,24,18,0,0),
d(2007,10,27,18,0,0),
d(2008,3,29,18,0,0),
d(2008,10,25,18,0,0),
d(2009,3,28,18,0,0),
d(2009,10,24,18,0,0),
d(2010,3,27,18,0,0),
d(2010,10,30,18,0,0),
d(2011,3,26,18,0,0),
d(2011,10,29,18,0,0),
d(2012,3,24,18,0,0),
d(2012,10,27,18,0,0),
d(2013,3,30,18,0,0),
d(2013,10,26,18,0,0),
d(2014,3,29,18,0,0),
d(2014,10,25,18,0,0),
d(2015,3,28,18,0,0),
d(2015,10,24,18,0,0),
d(2016,3,26,18,0,0),
d(2016,10,29,18,0,0),
d(2017,3,25,18,0,0),
d(2017,10,28,18,0,0),
d(2018,3,24,18,0,0),
d(2018,10,27,18,0,0),
d(2019,3,30,18,0,0),
d(2019,10,26,18,0,0),
d(2020,3,28,18,0,0),
d(2020,10,24,18,0,0),
d(2021,3,27,18,0,0),
d(2021,10,30,18,0,0),
d(2022,3,26,18,0,0),
d(2022,10,29,18,0,0),
d(2023,3,25,18,0,0),
d(2023,10,28,18,0,0),
d(2024,3,30,18,0,0),
d(2024,10,26,18,0,0),
d(2025,3,29,18,0,0),
d(2025,10,25,18,0,0),
d(2026,3,28,18,0,0),
d(2026,10,24,18,0,0),
d(2027,3,27,18,0,0),
d(2027,10,30,18,0,0),
d(2028,3,25,18,0,0),
d(2028,10,28,18,0,0),
d(2029,3,24,18,0,0),
d(2029,10,27,18,0,0),
d(2030,3,30,18,0,0),
d(2030,10,26,18,0,0),
d(2031,3,29,18,0,0),
d(2031,10,25,18,0,0),
d(2032,3,27,18,0,0),
d(2032,10,30,18,0,0),
d(2033,3,26,18,0,0),
d(2033,10,29,18,0,0),
d(2034,3,25,18,0,0),
d(2034,10,28,18,0,0),
d(2035,3,24,18,0,0),
d(2035,10,27,18,0,0),
d(2036,3,29,18,0,0),
d(2036,10,25,18,0,0),
d(2037,3,28,18,0,0),
d(2037,10,24,18,0,0),
        ]

    _transition_info = [
i(25020,0,'IMT'),
i(25200,0,'IRKT'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(28800,0,'IRKST'),
i(25200,0,'IRKT'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
i(32400,3600,'IRKST'),
i(28800,0,'IRKT'),
        ]

Irkutsk = Irkutsk()

