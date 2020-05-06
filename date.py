import re

'''short_month_names = (
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

long_month_names = (
    'January', 'February', 'March', 'April', 'May', 'June', 'July',
    'August', 'September', 'October', 'November', 'December')

short_month_cap = '(?:' + '|'.join(short_month_names) + ')'
long_month_cap = '(?:' + '|'.join(long_month_names) + ')'
short_num_month_cap = '(?:[1-9]|1[12])'
long_num_month_cap = '(?:0[1-9]|1[12])'

long_day_cap = '(?:0[1-9]|[12][0-9]|3[01])'
short_day_cap = '(?:[1-9]|[12][0-9]|3[01])'

long_year_cap = '(?:[0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]|[0-9][1-9][0-9]{2}|[1-9][0-9]{3})'
short_year_cap = '(?:[0-9][0-9])'

ordinal_day = '(?:2?1st|2?2nd|2?3rd|[12]?[4-9]th|1[123]th|[123]0th|31st)'

formats = (
    r'(?P<month_0>{lnm}|{snm})/(?P<day_0>{ld}|{sd})/(?P<year_0>{sy}|{ly})',
    r'(?P<month_1>{sm})\-(?P<day_1>{ld}|{sd})\-(?P<year_1>{ly})',
    r'(?P<month_2>{sm}|{lm})(?:\.\s+|\s*)(?P<day_2>{ld}|{sd})(?:,\s+|\s*)(?P<year_2>{ly})',
    r'(?P<day_3>{ld}|{sd})(?:[\.,]\s+|\s*)(?P<month_3>{lm}|{sm})(?:[\.,]\s+|\s*)(?P<year_3>{ly})',
    r'(?P<month_4>{lm}|{sm})\s+(?P<year_4>{ly})',
    r'(?P<month_5>{lnm}|{snm})/(?P<year_5>{ly})',
    r'(?P<year_6>{ly})',
    r'(?P<month_6>{sm})\s+(?P<day_4>(?={od})[0-9][0-9]?)..,\s*(?P<year_7>{ly})'
          )

_pattern = '|'.join(
    i.format(
        sm=short_month_cap, lm=long_month_cap, snm=short_num_month_cap,
        lnm=long_num_month_cap, ld=long_day_cap, sd=short_day_cap,
        ly=long_year_cap, sy=short_year_cap, od=ordinal_day
    ) for i in formats
)

pattern = re.compile(_pattern)'''

def get_pattern():
    short_month_names = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    long_month_names = ('January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November',         
                         'December')
    short_month_cap = '(?:' + '|'.join(short_month_names) + ')'
    long_month_cap = '(?:' + '|'.join(long_month_names) + ')'
    short_num_month_cap = '(?:[1-9]|1[12])'
    long_num_month_cap = '(?:0[1-9]|1[12])'

    long_day_cap = '(?:0[1-9]|[12][0-9]|3[01])'
    short_day_cap = '(?:[1-9]|[12][0-9]|3[01])'

    long_year_cap = '(?:[0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]|[0-9][1-9][0-9]{2}|[1-9][0-9]{3})'
    short_year_cap = '(?:[0-9][0-9])'
    ordinal_day = '(?:2?1st|2?2nd|2?3rd|[12]?[4-9]th|1[123]th|[123]0th|31st)'

    formats = (
    r'(?P<month_0>{lnm}|{snm})/(?P<day_0>{ld}|{sd})/(?P<year_0>{sy}|{ly})',
    r'(?P<month_1>{sm})\-(?P<day_1>{ld}|{sd})\-(?P<year_1>{ly})',
    r'(?P<month_2>{sm}|{lm})(?:\.\s+|\s*)(?P<day_2>{ld}|{sd})(?:,\s+|\s*)(?P<year_2>{ly})',
    r'(?P<day_3>{ld}|{sd})(?:[\.,]\s+|\s*)(?P<month_3>{lm}|{sm})(?:[\.,]\s+|\s*)(?P<year_3>{ly})',
    r'(?P<month_4>{lm}|{sm})\s+(?P<year_4>{ly})',
    r'(?P<month_5>{lnm}|{snm})/(?P<year_5>{ly})',
    r'(?P<year_6>{ly})',
    r'(?P<month_6>{sm})\s+(?P<day_4>(?={od})[0-9][0-9]?)..,\s*(?P<year_7>{ly})'
      
          )

    _pattern = '|'.join(
        i.format(
        sm=short_month_cap, lm=long_month_cap, snm=short_num_month_cap,
        lnm=long_num_month_cap, ld=long_day_cap, sd=short_day_cap,
        ly=long_year_cap, sy=short_year_cap, od=ordinal_day
        ) for i in formats
        )
    pattern = re.compile(_pattern)
    return pattern
pattern = get_pattern()
def get_fields(match):
    if not match:
        return None
    return {
        k[:-2]: v
        for k, v in match.groupdict().items()
        if v is not None
            }






tests=r"""entries are due by January 4, 2017 at 8:00pm created 01/15/2005 by ACME Inc. and associates. 03/23"""
#print('{!r}'.format(get_fields(pattern.fullmatch('January 4, 2017'))))
#print(get_fields(pattern.fullmatch('January 4, 2017')))
'''
for test_line in tests.split('\n'):
    for test in test_line.split('; '):
        print('{!r}: {!r}'.format(test, get_fields(pattern.fullmatch(test))))
    print('')'''
