#!/usr/bin/env python
'''
$Id: __init__.py,v 1.1 2004-09-24 15:24:40 jdh2358 Exp $

datetime.tzinfo timezone definitions generated from the
Olson timezone database:

    ftp://elsie.nci.nih.gov/pub/tz*.tar.gz

See the datetime section of the Python Library Reference for information
on how to use these modules.
'''

__rcs_id__  = '$Id: __init__.py,v 1.1 2004-09-24 15:24:40 jdh2358 Exp $'
__version__ = '$Revision: 1.1 $'[11:-2]

# The Olsen database has historically been updated about 4 times a year
OLSEN_VERSION = '2004b'
VERSION = OLSEN_VERSION + '.2'

__all__ = ['timezone', 'all_timezones', 'common_timezones']

import sys

from tzinfo import AmbiguousTimeError

def timezone(zone):
    ''' Return a datetime.tzinfo implementation for the given timezone 
    
    >>> from datetime import datetime, timedelta
    >>> utc = timezone('UTC')
    >>> eastern = timezone('US/Eastern')
    >>> utc_dt = datetime(2002, 10, 27, 6, 0, 0, tzinfo=utc)
    >>> loc_dt = utc_dt.astimezone(eastern)
    >>> fmt = '%Y-%m-%d %H:%M:%S %Z (%z)'
    >>> loc_dt.strftime(fmt)
    '2002-10-27 01:00:00 EST (-0500)'
    >>> (loc_dt - timedelta(minutes=10)).strftime(fmt)
    '2002-10-27 00:50:00 EST (-0500)'
    >>> eastern.normalize(loc_dt - timedelta(minutes=10)).strftime(fmt)
    '2002-10-27 01:50:00 EDT (-0400)'
    >>> (loc_dt + timedelta(minutes=10)).strftime(fmt)
    '2002-10-27 01:10:00 EST (-0500)'
    '''
    zone = _munge_zone(zone)
    zone_bits = ['zoneinfo'] + zone.split('/')

    # Load zone's module
    module_name = '.'.join(zone_bits)
    try:
        module = __import__(module_name, globals(), locals())
    except ImportError:
        raise KeyError, zone
    rv = module
    for bit in zone_bits[1:]:
        rv = getattr(rv, bit)

    # Return instance from that module
    rv = getattr(rv, zone_bits[-1])
    assert type(rv) != type(sys)
    return rv

def _munge_zone(zone):
    ''' Convert a zone into a string suitable for use as a Python identifier 
    '''
    return zone.replace('+', '_plus_').replace('-', '_minus_')

def _test():
    import doctest, os, sys
    sys.path.insert(0, os.pardir)
    import pytz
    return doctest.testmod(pytz)

if __name__ == '__main__':
    _test()

common_timezones = \
['Africa/Abidjan',
 'Africa/Accra',
 'Africa/Addis_Ababa',
 'Africa/Algiers',
 'Africa/Asmera',
 'Africa/Bamako',
 'Africa/Bangui',
 'Africa/Banjul',
 'Africa/Bissau',
 'Africa/Blantyre',
 'Africa/Brazzaville',
 'Africa/Bujumbura',
 'Africa/Cairo',
 'Africa/Casablanca',
 'Africa/Ceuta',
 'Africa/Conakry',
 'Africa/Dakar',
 'Africa/Dar_es_Salaam',
 'Africa/Djibouti',
 'Africa/Douala',
 'Africa/El_Aaiun',
 'Africa/Freetown',
 'Africa/Gaborone',
 'Africa/Harare',
 'Africa/Johannesburg',
 'Africa/Kampala',
 'Africa/Khartoum',
 'Africa/Kigali',
 'Africa/Kinshasa',
 'Africa/Lagos',
 'Africa/Libreville',
 'Africa/Lome',
 'Africa/Luanda',
 'Africa/Lubumbashi',
 'Africa/Lusaka',
 'Africa/Malabo',
 'Africa/Maputo',
 'Africa/Maseru',
 'Africa/Mbabane',
 'Africa/Mogadishu',
 'Africa/Monrovia',
 'Africa/Nairobi',
 'Africa/Ndjamena',
 'Africa/Niamey',
 'Africa/Nouakchott',
 'Africa/Ouagadougou',
 'Africa/Porto-Novo',
 'Africa/Sao_Tome',
 'Africa/Timbuktu',
 'Africa/Tripoli',
 'Africa/Tunis',
 'Africa/Windhoek',
 'America/Adak',
 'America/Anchorage',
 'America/Anguilla',
 'America/Antigua',
 'America/Araguaina',
 'America/Aruba',
 'America/Asuncion',
 'America/Atka',
 'America/Bahia',
 'America/Barbados',
 'America/Belem',
 'America/Belize',
 'America/Boa_Vista',
 'America/Bogota',
 'America/Boise',
 'America/Buenos_Aires',
 'America/Cambridge_Bay',
 'America/Campo_Grande',
 'America/Cancun',
 'America/Caracas',
 'America/Catamarca',
 'America/Cayenne',
 'America/Cayman',
 'America/Chicago',
 'America/Chihuahua',
 'America/Cordoba',
 'America/Costa_Rica',
 'America/Cuiaba',
 'America/Curacao',
 'America/Danmarkshavn',
 'America/Dawson',
 'America/Dawson_Creek',
 'America/Denver',
 'America/Detroit',
 'America/Dominica',
 'America/Edmonton',
 'America/Eirunepe',
 'America/El_Salvador',
 'America/Ensenada',
 'America/Fort_Wayne',
 'America/Fortaleza',
 'America/Glace_Bay',
 'America/Godthab',
 'America/Goose_Bay',
 'America/Grand_Turk',
 'America/Grenada',
 'America/Guadeloupe',
 'America/Guatemala',
 'America/Guayaquil',
 'America/Guyana',
 'America/Halifax',
 'America/Havana',
 'America/Hermosillo',
 'America/Indianapolis',
 'America/Inuvik',
 'America/Iqaluit',
 'America/Jamaica',
 'America/Jujuy',
 'America/Juneau',
 'America/Knox_IN',
 'America/La_Paz',
 'America/Lima',
 'America/Los_Angeles',
 'America/Louisville',
 'America/Maceio',
 'America/Managua',
 'America/Manaus',
 'America/Martinique',
 'America/Mazatlan',
 'America/Mendoza',
 'America/Menominee',
 'America/Merida',
 'America/Mexico_City',
 'America/Miquelon',
 'America/Monterrey',
 'America/Montevideo',
 'America/Montreal',
 'America/Montserrat',
 'America/Nassau',
 'America/New_York',
 'America/Nipigon',
 'America/Nome',
 'America/Noronha',
 'America/Panama',
 'America/Pangnirtung',
 'America/Paramaribo',
 'America/Phoenix',
 'America/Port-au-Prince',
 'America/Port_of_Spain',
 'America/Porto_Acre',
 'America/Porto_Velho',
 'America/Puerto_Rico',
 'America/Rainy_River',
 'America/Rankin_Inlet',
 'America/Recife',
 'America/Regina',
 'America/Rio_Branco',
 'America/Rosario',
 'America/Santiago',
 'America/Santo_Domingo',
 'America/Sao_Paulo',
 'America/Scoresbysund',
 'America/Shiprock',
 'America/St_Johns',
 'America/St_Kitts',
 'America/St_Lucia',
 'America/St_Thomas',
 'America/St_Vincent',
 'America/Swift_Current',
 'America/Tegucigalpa',
 'America/Thule',
 'America/Thunder_Bay',
 'America/Tijuana',
 'America/Toronto',
 'America/Tortola',
 'America/Vancouver',
 'America/Virgin',
 'America/Whitehorse',
 'America/Winnipeg',
 'America/Yakutat',
 'America/Yellowknife',
 'Antarctica/Casey',
 'Antarctica/Davis',
 'Antarctica/DumontDUrville',
 'Antarctica/Mawson',
 'Antarctica/McMurdo',
 'Antarctica/Palmer',
 'Antarctica/Rothera',
 'Antarctica/South_Pole',
 'Antarctica/Syowa',
 'Antarctica/Vostok',
 'Arctic/Longyearbyen',
 'Asia/Aden',
 'Asia/Almaty',
 'Asia/Amman',
 'Asia/Anadyr',
 'Asia/Aqtau',
 'Asia/Aqtobe',
 'Asia/Ashgabat',
 'Asia/Ashkhabad',
 'Asia/Baghdad',
 'Asia/Bahrain',
 'Asia/Baku',
 'Asia/Bangkok',
 'Asia/Beirut',
 'Asia/Bishkek',
 'Asia/Brunei',
 'Asia/Calcutta',
 'Asia/Choibalsan',
 'Asia/Chongqing',
 'Asia/Chungking',
 'Asia/Colombo',
 'Asia/Dacca',
 'Asia/Damascus',
 'Asia/Dhaka',
 'Asia/Dili',
 'Asia/Dubai',
 'Asia/Dushanbe',
 'Asia/Gaza',
 'Asia/Harbin',
 'Asia/Hong_Kong',
 'Asia/Hovd',
 'Asia/Irkutsk',
 'Asia/Istanbul',
 'Asia/Jakarta',
 'Asia/Jayapura',
 'Asia/Jerusalem',
 'Asia/Kabul',
 'Asia/Kamchatka',
 'Asia/Karachi',
 'Asia/Kashgar',
 'Asia/Katmandu',
 'Asia/Krasnoyarsk',
 'Asia/Kuala_Lumpur',
 'Asia/Kuching',
 'Asia/Kuwait',
 'Asia/Macao',
 'Asia/Macau',
 'Asia/Magadan',
 'Asia/Makassar',
 'Asia/Manila',
 'Asia/Muscat',
 'Asia/Nicosia',
 'Asia/Novosibirsk',
 'Asia/Omsk',
 'Asia/Oral',
 'Asia/Phnom_Penh',
 'Asia/Pontianak',
 'Asia/Pyongyang',
 'Asia/Qatar',
 'Asia/Qyzylorda',
 'Asia/Rangoon',
 'Asia/Riyadh',
 'Asia/Saigon',
 'Asia/Sakhalin',
 'Asia/Samarkand',
 'Asia/Seoul',
 'Asia/Shanghai',
 'Asia/Singapore',
 'Asia/Taipei',
 'Asia/Tashkent',
 'Asia/Tbilisi',
 'Asia/Tehran',
 'Asia/Tel_Aviv',
 'Asia/Thimbu',
 'Asia/Thimphu',
 'Asia/Tokyo',
 'Asia/Ujung_Pandang',
 'Asia/Ulaanbaatar',
 'Asia/Ulan_Bator',
 'Asia/Urumqi',
 'Asia/Vientiane',
 'Asia/Vladivostok',
 'Asia/Yakutsk',
 'Asia/Yekaterinburg',
 'Asia/Yerevan',
 'Atlantic/Azores',
 'Atlantic/Bermuda',
 'Atlantic/Canary',
 'Atlantic/Cape_Verde',
 'Atlantic/Faeroe',
 'Atlantic/Jan_Mayen',
 'Atlantic/Madeira',
 'Atlantic/Reykjavik',
 'Atlantic/South_Georgia',
 'Atlantic/St_Helena',
 'Atlantic/Stanley',
 'Australia/ACT',
 'Australia/Adelaide',
 'Australia/Brisbane',
 'Australia/Broken_Hill',
 'Australia/Canberra',
 'Australia/Darwin',
 'Australia/Hobart',
 'Australia/LHI',
 'Australia/Lindeman',
 'Australia/Lord_Howe',
 'Australia/Melbourne',
 'Australia/NSW',
 'Australia/North',
 'Australia/Perth',
 'Australia/Queensland',
 'Australia/South',
 'Australia/Sydney',
 'Australia/Tasmania',
 'Australia/Victoria',
 'Australia/West',
 'Australia/Yancowinna',
 'Brazil/Acre',
 'Brazil/DeNoronha',
 'Brazil/East',
 'Brazil/West',
 'Canada/Atlantic',
 'Canada/Central',
 'Canada/East-Saskatchewan',
 'Canada/Eastern',
 'Canada/Mountain',
 'Canada/Newfoundland',
 'Canada/Pacific',
 'Canada/Saskatchewan',
 'Canada/Yukon',
 'Chile/Continental',
 'Chile/EasterIsland',
 'Europe/Amsterdam',
 'Europe/Andorra',
 'Europe/Athens',
 'Europe/Belfast',
 'Europe/Belgrade',
 'Europe/Berlin',
 'Europe/Bratislava',
 'Europe/Brussels',
 'Europe/Bucharest',
 'Europe/Budapest',
 'Europe/Chisinau',
 'Europe/Copenhagen',
 'Europe/Dublin',
 'Europe/Gibraltar',
 'Europe/Helsinki',
 'Europe/Istanbul',
 'Europe/Kaliningrad',
 'Europe/Kiev',
 'Europe/Lisbon',
 'Europe/Ljubljana',
 'Europe/London',
 'Europe/Luxembourg',
 'Europe/Madrid',
 'Europe/Malta',
 'Europe/Mariehamn',
 'Europe/Minsk',
 'Europe/Monaco',
 'Europe/Moscow',
 'Europe/Nicosia',
 'Europe/Oslo',
 'Europe/Paris',
 'Europe/Prague',
 'Europe/Riga',
 'Europe/Rome',
 'Europe/Samara',
 'Europe/San_Marino',
 'Europe/Sarajevo',
 'Europe/Simferopol',
 'Europe/Skopje',
 'Europe/Sofia',
 'Europe/Stockholm',
 'Europe/Tallinn',
 'Europe/Tirane',
 'Europe/Tiraspol',
 'Europe/Uzhgorod',
 'Europe/Vaduz',
 'Europe/Vatican',
 'Europe/Vienna',
 'Europe/Vilnius',
 'Europe/Warsaw',
 'Europe/Zagreb',
 'Europe/Zaporozhye',
 'Europe/Zurich',
 'GMT',
 'Indian/Antananarivo',
 'Indian/Chagos',
 'Indian/Christmas',
 'Indian/Cocos',
 'Indian/Comoro',
 'Indian/Kerguelen',
 'Indian/Mahe',
 'Indian/Maldives',
 'Indian/Mauritius',
 'Indian/Mayotte',
 'Indian/Reunion',
 'Mexico/BajaNorte',
 'Mexico/BajaSur',
 'Mexico/General',
 'Pacific/Apia',
 'Pacific/Auckland',
 'Pacific/Chatham',
 'Pacific/Easter',
 'Pacific/Efate',
 'Pacific/Enderbury',
 'Pacific/Fakaofo',
 'Pacific/Fiji',
 'Pacific/Funafuti',
 'Pacific/Galapagos',
 'Pacific/Gambier',
 'Pacific/Guadalcanal',
 'Pacific/Guam',
 'Pacific/Honolulu',
 'Pacific/Johnston',
 'Pacific/Kiritimati',
 'Pacific/Kosrae',
 'Pacific/Kwajalein',
 'Pacific/Majuro',
 'Pacific/Marquesas',
 'Pacific/Midway',
 'Pacific/Nauru',
 'Pacific/Niue',
 'Pacific/Norfolk',
 'Pacific/Noumea',
 'Pacific/Pago_Pago',
 'Pacific/Palau',
 'Pacific/Pitcairn',
 'Pacific/Ponape',
 'Pacific/Port_Moresby',
 'Pacific/Rarotonga',
 'Pacific/Saipan',
 'Pacific/Samoa',
 'Pacific/Tahiti',
 'Pacific/Tarawa',
 'Pacific/Tongatapu',
 'Pacific/Truk',
 'Pacific/Wake',
 'Pacific/Wallis',
 'Pacific/Yap',
 'US/Alaska',
 'US/Aleutian',
 'US/Arizona',
 'US/Central',
 'US/East-Indiana',
 'US/Eastern',
 'US/Hawaii',
 'US/Indiana-Starke',
 'US/Michigan',
 'US/Mountain',
 'US/Pacific',
 'US/Pacific-New',
 'US/Samoa',
 'UTC']

all_timezones = \
['Africa/Abidjan',
 'Africa/Accra',
 'Africa/Addis_Ababa',
 'Africa/Algiers',
 'Africa/Asmera',
 'Africa/Bamako',
 'Africa/Bangui',
 'Africa/Banjul',
 'Africa/Bissau',
 'Africa/Blantyre',
 'Africa/Brazzaville',
 'Africa/Bujumbura',
 'Africa/Cairo',
 'Africa/Casablanca',
 'Africa/Ceuta',
 'Africa/Conakry',
 'Africa/Dakar',
 'Africa/Dar_es_Salaam',
 'Africa/Djibouti',
 'Africa/Douala',
 'Africa/El_Aaiun',
 'Africa/Freetown',
 'Africa/Gaborone',
 'Africa/Harare',
 'Africa/Johannesburg',
 'Africa/Kampala',
 'Africa/Khartoum',
 'Africa/Kigali',
 'Africa/Kinshasa',
 'Africa/Lagos',
 'Africa/Libreville',
 'Africa/Lome',
 'Africa/Luanda',
 'Africa/Lubumbashi',
 'Africa/Lusaka',
 'Africa/Malabo',
 'Africa/Maputo',
 'Africa/Maseru',
 'Africa/Mbabane',
 'Africa/Mogadishu',
 'Africa/Monrovia',
 'Africa/Nairobi',
 'Africa/Ndjamena',
 'Africa/Niamey',
 'Africa/Nouakchott',
 'Africa/Ouagadougou',
 'Africa/Porto-Novo',
 'Africa/Sao_Tome',
 'Africa/Timbuktu',
 'Africa/Tripoli',
 'Africa/Tunis',
 'Africa/Windhoek',
 'America/Adak',
 'America/Anchorage',
 'America/Anguilla',
 'America/Antigua',
 'America/Araguaina',
 'America/Argentina/Buenos_Aires',
 'America/Argentina/Catamarca',
 'America/Argentina/ComodRivadavia',
 'America/Argentina/Cordoba',
 'America/Argentina/Jujuy',
 'America/Argentina/La_Rioja',
 'America/Argentina/Mendoza',
 'America/Argentina/Rio_Gallegos',
 'America/Argentina/San_Juan',
 'America/Argentina/Tucuman',
 'America/Argentina/Ushuaia',
 'America/Aruba',
 'America/Asuncion',
 'America/Atka',
 'America/Bahia',
 'America/Barbados',
 'America/Belem',
 'America/Belize',
 'America/Boa_Vista',
 'America/Bogota',
 'America/Boise',
 'America/Buenos_Aires',
 'America/Cambridge_Bay',
 'America/Campo_Grande',
 'America/Cancun',
 'America/Caracas',
 'America/Catamarca',
 'America/Cayenne',
 'America/Cayman',
 'America/Chicago',
 'America/Chihuahua',
 'America/Cordoba',
 'America/Costa_Rica',
 'America/Cuiaba',
 'America/Curacao',
 'America/Danmarkshavn',
 'America/Dawson',
 'America/Dawson_Creek',
 'America/Denver',
 'America/Detroit',
 'America/Dominica',
 'America/Edmonton',
 'America/Eirunepe',
 'America/El_Salvador',
 'America/Ensenada',
 'America/Fort_Wayne',
 'America/Fortaleza',
 'America/Glace_Bay',
 'America/Godthab',
 'America/Goose_Bay',
 'America/Grand_Turk',
 'America/Grenada',
 'America/Guadeloupe',
 'America/Guatemala',
 'America/Guayaquil',
 'America/Guyana',
 'America/Halifax',
 'America/Havana',
 'America/Hermosillo',
 'America/Indiana/Indianapolis',
 'America/Indiana/Knox',
 'America/Indiana/Marengo',
 'America/Indiana/Vevay',
 'America/Indianapolis',
 'America/Inuvik',
 'America/Iqaluit',
 'America/Jamaica',
 'America/Jujuy',
 'America/Juneau',
 'America/Kentucky/Louisville',
 'America/Kentucky/Monticello',
 'America/Knox_IN',
 'America/La_Paz',
 'America/Lima',
 'America/Los_Angeles',
 'America/Louisville',
 'America/Maceio',
 'America/Managua',
 'America/Manaus',
 'America/Martinique',
 'America/Mazatlan',
 'America/Mendoza',
 'America/Menominee',
 'America/Merida',
 'America/Mexico_City',
 'America/Miquelon',
 'America/Monterrey',
 'America/Montevideo',
 'America/Montreal',
 'America/Montserrat',
 'America/Nassau',
 'America/New_York',
 'America/Nipigon',
 'America/Nome',
 'America/Noronha',
 'America/North_Dakota/Center',
 'America/Panama',
 'America/Pangnirtung',
 'America/Paramaribo',
 'America/Phoenix',
 'America/Port-au-Prince',
 'America/Port_of_Spain',
 'America/Porto_Acre',
 'America/Porto_Velho',
 'America/Puerto_Rico',
 'America/Rainy_River',
 'America/Rankin_Inlet',
 'America/Recife',
 'America/Regina',
 'America/Rio_Branco',
 'America/Rosario',
 'America/Santiago',
 'America/Santo_Domingo',
 'America/Sao_Paulo',
 'America/Scoresbysund',
 'America/Shiprock',
 'America/St_Johns',
 'America/St_Kitts',
 'America/St_Lucia',
 'America/St_Thomas',
 'America/St_Vincent',
 'America/Swift_Current',
 'America/Tegucigalpa',
 'America/Thule',
 'America/Thunder_Bay',
 'America/Tijuana',
 'America/Toronto',
 'America/Tortola',
 'America/Vancouver',
 'America/Virgin',
 'America/Whitehorse',
 'America/Winnipeg',
 'America/Yakutat',
 'America/Yellowknife',
 'Antarctica/Casey',
 'Antarctica/Davis',
 'Antarctica/DumontDUrville',
 'Antarctica/Mawson',
 'Antarctica/McMurdo',
 'Antarctica/Palmer',
 'Antarctica/Rothera',
 'Antarctica/South_Pole',
 'Antarctica/Syowa',
 'Antarctica/Vostok',
 'Arctic/Longyearbyen',
 'Asia/Aden',
 'Asia/Almaty',
 'Asia/Amman',
 'Asia/Anadyr',
 'Asia/Aqtau',
 'Asia/Aqtobe',
 'Asia/Ashgabat',
 'Asia/Ashkhabad',
 'Asia/Baghdad',
 'Asia/Bahrain',
 'Asia/Baku',
 'Asia/Bangkok',
 'Asia/Beirut',
 'Asia/Bishkek',
 'Asia/Brunei',
 'Asia/Calcutta',
 'Asia/Choibalsan',
 'Asia/Chongqing',
 'Asia/Chungking',
 'Asia/Colombo',
 'Asia/Dacca',
 'Asia/Damascus',
 'Asia/Dhaka',
 'Asia/Dili',
 'Asia/Dubai',
 'Asia/Dushanbe',
 'Asia/Gaza',
 'Asia/Harbin',
 'Asia/Hong_Kong',
 'Asia/Hovd',
 'Asia/Irkutsk',
 'Asia/Istanbul',
 'Asia/Jakarta',
 'Asia/Jayapura',
 'Asia/Jerusalem',
 'Asia/Kabul',
 'Asia/Kamchatka',
 'Asia/Karachi',
 'Asia/Kashgar',
 'Asia/Katmandu',
 'Asia/Krasnoyarsk',
 'Asia/Kuala_Lumpur',
 'Asia/Kuching',
 'Asia/Kuwait',
 'Asia/Macao',
 'Asia/Macau',
 'Asia/Magadan',
 'Asia/Makassar',
 'Asia/Manila',
 'Asia/Muscat',
 'Asia/Nicosia',
 'Asia/Novosibirsk',
 'Asia/Omsk',
 'Asia/Oral',
 'Asia/Phnom_Penh',
 'Asia/Pontianak',
 'Asia/Pyongyang',
 'Asia/Qatar',
 'Asia/Qyzylorda',
 'Asia/Rangoon',
 'Asia/Riyadh',
 'Asia/Saigon',
 'Asia/Sakhalin',
 'Asia/Samarkand',
 'Asia/Seoul',
 'Asia/Shanghai',
 'Asia/Singapore',
 'Asia/Taipei',
 'Asia/Tashkent',
 'Asia/Tbilisi',
 'Asia/Tehran',
 'Asia/Tel_Aviv',
 'Asia/Thimbu',
 'Asia/Thimphu',
 'Asia/Tokyo',
 'Asia/Ujung_Pandang',
 'Asia/Ulaanbaatar',
 'Asia/Ulan_Bator',
 'Asia/Urumqi',
 'Asia/Vientiane',
 'Asia/Vladivostok',
 'Asia/Yakutsk',
 'Asia/Yekaterinburg',
 'Asia/Yerevan',
 'Atlantic/Azores',
 'Atlantic/Bermuda',
 'Atlantic/Canary',
 'Atlantic/Cape_Verde',
 'Atlantic/Faeroe',
 'Atlantic/Jan_Mayen',
 'Atlantic/Madeira',
 'Atlantic/Reykjavik',
 'Atlantic/South_Georgia',
 'Atlantic/St_Helena',
 'Atlantic/Stanley',
 'Australia/ACT',
 'Australia/Adelaide',
 'Australia/Brisbane',
 'Australia/Broken_Hill',
 'Australia/Canberra',
 'Australia/Darwin',
 'Australia/Hobart',
 'Australia/LHI',
 'Australia/Lindeman',
 'Australia/Lord_Howe',
 'Australia/Melbourne',
 'Australia/NSW',
 'Australia/North',
 'Australia/Perth',
 'Australia/Queensland',
 'Australia/South',
 'Australia/Sydney',
 'Australia/Tasmania',
 'Australia/Victoria',
 'Australia/West',
 'Australia/Yancowinna',
 'Brazil/Acre',
 'Brazil/DeNoronha',
 'Brazil/East',
 'Brazil/West',
 'CET',
 'CST6CDT',
 'Canada/Atlantic',
 'Canada/Central',
 'Canada/East-Saskatchewan',
 'Canada/Eastern',
 'Canada/Mountain',
 'Canada/Newfoundland',
 'Canada/Pacific',
 'Canada/Saskatchewan',
 'Canada/Yukon',
 'Chile/Continental',
 'Chile/EasterIsland',
 'Cuba',
 'EET',
 'EST',
 'EST5EDT',
 'Egypt',
 'Eire',
 'Etc/GMT',
 'Etc/GMT+0',
 'Etc/GMT+1',
 'Etc/GMT+10',
 'Etc/GMT+11',
 'Etc/GMT+12',
 'Etc/GMT+2',
 'Etc/GMT+3',
 'Etc/GMT+4',
 'Etc/GMT+5',
 'Etc/GMT+6',
 'Etc/GMT+7',
 'Etc/GMT+8',
 'Etc/GMT+9',
 'Etc/GMT-0',
 'Etc/GMT-1',
 'Etc/GMT-10',
 'Etc/GMT-11',
 'Etc/GMT-12',
 'Etc/GMT-13',
 'Etc/GMT-14',
 'Etc/GMT-2',
 'Etc/GMT-3',
 'Etc/GMT-4',
 'Etc/GMT-5',
 'Etc/GMT-6',
 'Etc/GMT-7',
 'Etc/GMT-8',
 'Etc/GMT-9',
 'Etc/GMT0',
 'Etc/Greenwich',
 'Etc/UCT',
 'Etc/UTC',
 'Etc/Universal',
 'Etc/Zulu',
 'Europe/Amsterdam',
 'Europe/Andorra',
 'Europe/Athens',
 'Europe/Belfast',
 'Europe/Belgrade',
 'Europe/Berlin',
 'Europe/Bratislava',
 'Europe/Brussels',
 'Europe/Bucharest',
 'Europe/Budapest',
 'Europe/Chisinau',
 'Europe/Copenhagen',
 'Europe/Dublin',
 'Europe/Gibraltar',
 'Europe/Helsinki',
 'Europe/Istanbul',
 'Europe/Kaliningrad',
 'Europe/Kiev',
 'Europe/Lisbon',
 'Europe/Ljubljana',
 'Europe/London',
 'Europe/Luxembourg',
 'Europe/Madrid',
 'Europe/Malta',
 'Europe/Mariehamn',
 'Europe/Minsk',
 'Europe/Monaco',
 'Europe/Moscow',
 'Europe/Nicosia',
 'Europe/Oslo',
 'Europe/Paris',
 'Europe/Prague',
 'Europe/Riga',
 'Europe/Rome',
 'Europe/Samara',
 'Europe/San_Marino',
 'Europe/Sarajevo',
 'Europe/Simferopol',
 'Europe/Skopje',
 'Europe/Sofia',
 'Europe/Stockholm',
 'Europe/Tallinn',
 'Europe/Tirane',
 'Europe/Tiraspol',
 'Europe/Uzhgorod',
 'Europe/Vaduz',
 'Europe/Vatican',
 'Europe/Vienna',
 'Europe/Vilnius',
 'Europe/Warsaw',
 'Europe/Zagreb',
 'Europe/Zaporozhye',
 'Europe/Zurich',
 'GB',
 'GB-Eire',
 'GMT',
 'GMT+0',
 'GMT-0',
 'GMT0',
 'Greenwich',
 'HST',
 'Hongkong',
 'Iceland',
 'Indian/Antananarivo',
 'Indian/Chagos',
 'Indian/Christmas',
 'Indian/Cocos',
 'Indian/Comoro',
 'Indian/Kerguelen',
 'Indian/Mahe',
 'Indian/Maldives',
 'Indian/Mauritius',
 'Indian/Mayotte',
 'Indian/Reunion',
 'Iran',
 'Israel',
 'Jamaica',
 'Japan',
 'Kwajalein',
 'Libya',
 'MET',
 'MST',
 'MST7MDT',
 'Mexico/BajaNorte',
 'Mexico/BajaSur',
 'Mexico/General',
 'NZ',
 'NZ-CHAT',
 'Navajo',
 'PRC',
 'PST8PDT',
 'Pacific/Apia',
 'Pacific/Auckland',
 'Pacific/Chatham',
 'Pacific/Easter',
 'Pacific/Efate',
 'Pacific/Enderbury',
 'Pacific/Fakaofo',
 'Pacific/Fiji',
 'Pacific/Funafuti',
 'Pacific/Galapagos',
 'Pacific/Gambier',
 'Pacific/Guadalcanal',
 'Pacific/Guam',
 'Pacific/Honolulu',
 'Pacific/Johnston',
 'Pacific/Kiritimati',
 'Pacific/Kosrae',
 'Pacific/Kwajalein',
 'Pacific/Majuro',
 'Pacific/Marquesas',
 'Pacific/Midway',
 'Pacific/Nauru',
 'Pacific/Niue',
 'Pacific/Norfolk',
 'Pacific/Noumea',
 'Pacific/Pago_Pago',
 'Pacific/Palau',
 'Pacific/Pitcairn',
 'Pacific/Ponape',
 'Pacific/Port_Moresby',
 'Pacific/Rarotonga',
 'Pacific/Saipan',
 'Pacific/Samoa',
 'Pacific/Tahiti',
 'Pacific/Tarawa',
 'Pacific/Tongatapu',
 'Pacific/Truk',
 'Pacific/Wake',
 'Pacific/Wallis',
 'Pacific/Yap',
 'Poland',
 'Portugal',
 'ROC',
 'ROK',
 'Singapore',
 'SystemV/AST4',
 'SystemV/AST4ADT',
 'SystemV/CST6',
 'SystemV/CST6CDT',
 'SystemV/EST5',
 'SystemV/EST5EDT',
 'SystemV/HST10',
 'SystemV/MST7',
 'SystemV/MST7MDT',
 'SystemV/PST8',
 'SystemV/PST8PDT',
 'SystemV/YST9',
 'SystemV/YST9YDT',
 'Turkey',
 'UCT',
 'US/Alaska',
 'US/Aleutian',
 'US/Arizona',
 'US/Central',
 'US/East-Indiana',
 'US/Eastern',
 'US/Hawaii',
 'US/Indiana-Starke',
 'US/Michigan',
 'US/Mountain',
 'US/Pacific',
 'US/Pacific-New',
 'US/Samoa',
 'UTC',
 'Universal',
 'W-SU',
 'WET',
 'Zulu',
 'posixrules']
