import json
import country_codes

with open('accents.json', 'r') as accent_file:
    no_accents = json.load(accent_file)

with open('directions.json', 'r') as direct_file:
    direct_map = json.load(direct_file)

def remove_accents(word, accents_map=no_accents):
    table = str.maketrans(accents_map)
    return word.translate(table)

def abbrev_directions(direction, direction_map=direct_map):
    result = []
    direction_map = {key.upper() : value for key, value in direction_map.items()}

    for word in direction.split():
        upper_word = word.upper()
        if upper_word in direction_map:
            result.append(direction_map[upper_word])
        else:
            result.append(word)
    
    return ' '.join(result)

def abbrev_country(country, abbrev='ISO2', country_map=country_codes.countries):
    '''
    Converts a given country to an abbreviated form.
    abbrev : {'ISO2', 'ISO3', 'UN_CODE'}, default='ISO2'
    '''
    if abbrev.upper() not in ('ISO2', 'ISO3', 'UN_CODE'):
        raise ValueError('abbrev must be ISO2, ISO3, or UN_CODE')

    country = country.upper()
    abbrev = abbrev.upper()
    if abbrev == 'ISO2':
        return country_map[country].ISO2
    elif abbrev == 'ISO3':
        return country_map[country].ISO3
    elif abbrev == 'UN_CODE':
        return country_map[country].UN_CODE