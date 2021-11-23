import json
from collections import deque
from string import punctuation
from Mappings import country_codes, roman_numerals

with open('Mappings/accents.json', 'r') as accent_file:
    no_accents_map = json.load(accent_file)
    accent_table = str.maketrans(no_accents_map)
    del no_accents_map

with open('Mappings/directions.json', 'r') as direct_file:
    direct_map = json.load(direct_file)
    direct_map = {key.upper() : value for key, value in direct_map.items()}

with open('Mappings/num_to_words.json', 'r') as num_words_file:
    num_to_words_map = json.load(num_words_file)
    __zero_to_nineteen = {int(key) : value for key, value in num_to_words_map['zero_to_nineteen'].items()}
    __tens = {int(key): value for key, value in num_to_words_map['tens'].items()}

def remove_accents(word, accents_table=accent_table):
    '''Remove all accents from a character within a string if there is an ascii equivalent'''
    return word.translate(accents_table)

def remove_punctuation(text, punctuation=punctuation, sep=''):
    '''Remove punctuation from a given text. Punctuation is provided from the string library.'''
    no_punctuation = str.maketrans(dict.fromkeys(punctuation, sep))
    return text.translate(no_punctuation).strip()

def abbrev_directions(direction, direction_map=direct_map, sep=' '):
    '''Replace directions with a common abbreviated form'''
    result = []

    for word in direction.split():
        upper_word = word.upper()
        if upper_word in direction_map:
            result.append(direction_map[upper_word])
        else:
            result.append(word)
    return sep.join(result)

def abbrev_country(country, abbrev='ISO2', country_map=country_codes.countries):
    '''
    Converts a given country to an abbreviated form
    abbrev : {'ISO2', 'ISO3', 'UN_CODE'}, default='ISO2'
    '''
    country_up = country.upper()
    abbrev = abbrev.upper()

    assert abbrev in ('ISO2', 'ISO3', 'UN_CODE'), 'abbrev must be ISO2, ISO3, or UN_CODE'

    try:
        if abbrev == 'ISO2':
            return country_map[country_up].ISO2
        elif abbrev == 'ISO3':
            return country_map[country_up].ISO3
        elif abbrev == 'UN_CODE':
            return country_map[country_up].UN_CODE
    except KeyError:
        return country

def convert_to_roman(number: int) -> str:
    '''
    Convert an integer to Roman Numerals.
    Number range is accurate from 1 to 3000 inclusive.
    '''
    assert (number >= 1) & (number <= 3_000), 'convert_to_roman is only for 1 to 3_000 inclusive'
    complete = ''
    
    for field in roman_numerals.Symbols._fields:
        numeral = eval(f'roman_numerals.numerals.{field}')
        num = eval(f'roman_numerals.numbers.{field}')
        while number >= num:
            complete += numeral
            number -= num
    return complete

def num_to_words(num, num_to_words_map=num_to_words_map, sep='-'):
    '''
    Return the word form of an integer.
    Numbers must be between 0 inclusive 
    and 1_000_000_000_000_000 (one-quadrillion) exclusive.
    '''
    assert (num >= 0) & (num < 1_000_000_000_000_000), 'number must be between 0 inclusive and one-quadrillion exclusive'

    if num == 0:
        return 'zero'
    elif num <= 19:
        return __zero_to_nineteen[num]
    elif num < 100:
        qtnt, rmdr = divmod(num, 10)
        return sep.join((__tens[qtnt], __zero_to_nineteen[rmdr])) if rmdr != 0 else __tens[qtnt]
    elif num < 1_000:
        qtnt, rmdr = divmod(num, 100)
        if rmdr != 0:
            return sep.join((__zero_to_nineteen[qtnt], 'hundred', num_to_words(rmdr))).strip(sep)
        else:
            return sep.join((__zero_to_nineteen[qtnt], 'hundred')).strip(sep)
    else:
        full = deque()
        places = iter(('', 'thousand', 'million', 'billion', 'trillion'))
        while num >= 1000:
            num, rmdr = divmod(num, 1000)
            place = next(places)
            if rmdr != 0:
                rmdr_words = num_to_words(rmdr)
                full.appendleft(place)
                full.appendleft(rmdr_words)
        full.appendleft(next(places))
        full.appendleft(num_to_words(num))
        return sep.join(full).strip(sep)
