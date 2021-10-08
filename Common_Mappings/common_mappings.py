import json
from string import punctuation
from Mappings import country_codes

with open('Mappings/accents.json', 'r') as accent_file:
    no_accents_map = json.load(accent_file)
    accent_table = str.maketrans(no_accents_map)
    del no_accents_map

with open('Mappings/directions.json', 'r') as direct_file:
    direct_map = json.load(direct_file)
    direct_map = {key.upper() : value for key, value in direct_map.items()}

def remove_accents(word, accents_table=accent_table):
    '''Remove all accents from a character within a string if there is an ascii equivalent'''
    return word.translate(accents_table)

def remove_punctuation(text, punctuation=punctuation, sep=''):
    '''Remove punctuation from a given text. Punctuation is provided from the string library.'''
    no_punctuation = str.maketrans(dict.fromkeys(punctuation, sep))
    return text.translate(no_punctuation).strip()

def abbrev_directions(direction, direction_map=direct_map):
    '''Replace directions with a common abbreviated form'''
    result = []

    for word in direction.split():
        upper_word = word.upper()
        if upper_word in direction_map:
            result.append(direction_map[upper_word])
        else:
            result.append(word)
    
    return ' '.join(result)

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