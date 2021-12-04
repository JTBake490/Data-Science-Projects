import numpy as np
import pandas as pd

def lowercase_str_cols(dataframe: pd.DataFrame) -> pd.DataFrame:
    for col in dataframe.columns[:]:
        if dataframe[col].dtype == 'O':
            dataframe[col] = dataframe[col].str.lower()
    return dataframe

# Bulk Data
initial_cols = (
    'name', 'status', 'type_1', 'type_2', 'height_m', 'weight_kg', 'ability_1', 'ability_2', 
    'ability_hidden', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense','speed', 'catch_rate',
    'base_friendship', 'base_experience', 'growth_rate', 'egg_type_1', 'egg_type_2', 'percentage_male', 'egg_cycles')

df = pd.read_csv('../../ML Datasets/pokemon/pokedex.csv', usecols=initial_cols)
df = lowercase_str_cols(df)
# df.status = df.status.map(status_map)

# Partner Pikachu has a missing egg_type_2 dispite having an egg_type_2
df.loc[(df.name == 'partner pikachu'), 'egg_type_2'] = 'fairy'

# Several columns have sveral hundred missing values - shortening these to "has" categories
# df['has_type_2'] = df.type_2.notna()
df['has_ability_2'] = df.ability_2.notna()
df['has_hidden_ability'] = df.ability_hidden.notna()
df['has_egg_type_2'] = df.egg_type_2.notna()

# From playing the games I know that a pokemon that is genderless has a pretty good change a being legendary
df['is_genderless'] = df.percentage_male.isna()

# # weight_kg, growth_rate, and egg_cycles only have one missing value each
df.weight_kg.fillna(950.0, inplace=True) # Eternatus
df.growth_rate.fillna('medium slow', inplace=True) # Galarian Darmanitan Zen Mode
df.egg_cycles.fillna(20.0, inplace=True) # Galarian Darmanitan Zen Mode

# Three pokemon missing ability_1
df.loc[(df.name == 'partner pikachu'), 'ability_1'] = 'static'
df.loc[(df.name == 'partner eevee'), 'ability_1'] = 'run away'
df.loc[(df.name == 'eternatus eternamax'), 'ability_1'] = 'pressure'

# Eighteen pokemon missing catch_rate
df.loc[(df.name == 'galarian meowth'), 'catch_rate'] = 255.0
df.loc[(df.name == 'galarian ponyta'), 'catch_rate'] = 190.0
df.loc[(df.name == 'galarian rapidash'), 'catch_rate'] = 60.0
df.loc[(df.name == "galarian farfetch'd"), 'catch_rate'] = 45.0
df.loc[(df.name == 'galarian weezing'), 'catch_rate'] = 60.0
df.loc[(df.name == 'galarian mr. mime'), 'catch_rate'] = 45.0
df.loc[(df.name == 'galarian corsola'), 'catch_rate'] = 60.0
df.loc[(df.name == 'galarian zigzagoon'), 'catch_rate'] = 255.0
df.loc[(df.name == 'galarian linoone'), 'catch_rate'] = 90.0
df.loc[(df.name == 'galarian darumaka'), 'catch_rate'] = 120.0
df.loc[(df.name == 'galarian darmanitan standard mode'), 'catch_rate'] = 60.0
df.loc[(df.name == 'galarian darmanitan zen mode'), 'catch_rate'] = 60.0
df.loc[(df.name == 'galarian yamask'), 'catch_rate'] = 190.0
df.loc[(df.name == 'galarian stunfisk'), 'catch_rate'] = 75.0
df.loc[(df.name == 'morpeko hangry mode'), 'catch_rate'] = 180.0
df.loc[(df.name == 'zacian hero of many battles'), 'catch_rate'] = 10.0
df.loc[(df.name == 'zamazenta hero of many battles'), 'catch_rate'] = 10.0
df.loc[(df.name == 'eternatus eternamax'), 'catch_rate'] = 255.0

# Three missing values for egg_type_1
df.egg_type_1.fillna('field', inplace=True) # Partner Pikachu, Partner Eevee, Galarian Darmanitan Zen Mode

# 115 missing values for base_friendship
df.loc[(df.name == 'galarian meowth'), 'base_friendship'] = 50.0
df.loc[(df.name == 'galarian ponyta'), 'base_friendship'] = 50.0
df.loc[(df.name == 'galarian rapidash'), 'base_friendship'] = 50.0
df.loc[(df.name == "galarian farfetch'd"), 'base_friendship'] = 50.0
df.loc[(df.name == 'galarian weezing'), 'base_friendship'] = 50.0
df.loc[(df.name == 'galarian mr. mime'), 'base_friendship'] = 50.0
df.loc[(df.name == 'galarian corsola'), 'base_friendship'] = 50.0
df.loc[(df.name == 'galarian zigzagoon'), 'base_friendship'] = 50.0
df.loc[(df.name == 'galarian linoone'), 'base_friendship'] = 50.0
df.loc[(df.name == 'galarian darumaka'), 'base_friendship'] = 50.0
df.loc[(df.name == 'galarian darmanitan standard mode'), 'base_friendship'] = 50.0
df.loc[(df.name == 'galarian darmanitan zen mode'), 'base_friendship'] = 50.0
df.loc[(df.name == 'galarian yamask'), 'base_friendship'] = 50.0
df.loc[(df.name == 'galarian stunfisk'), 'base_friendship'] = 50.0
df.loc[(df.name == 'meltan'), 'base_friendship'] = 0.0
df.loc[(df.name == 'melmetal'), 'base_friendship'] = 0.0
df.loc[(df.name == 'grookey'), 'base_friendship'] = 50.0
df.loc[(df.name == 'thwackey'), 'base_friendship'] = 50.0
df.loc[(df.name == 'rillaboom'), 'base_friendship'] = 50.0
df.loc[(df.name == 'scorbunny'), 'base_friendship'] = 50.0
df.loc[(df.name == 'raboot'), 'base_friendship'] = 50.0
df.loc[(df.name == 'cinderace'), 'base_friendship'] = 50.0
df.loc[(df.name == 'sobble'), 'base_friendship'] = 50.0
df.loc[(df.name == 'drizzile'), 'base_friendship'] = 50.0
df.loc[(df.name == 'inteleon'), 'base_friendship'] = 50.0
df.loc[(df.name == 'skwovet'), 'base_friendship'] = 50.0
df.loc[(df.name == 'greedent'), 'base_friendship'] = 50.0
df.loc[(df.name == 'rookidee'), 'base_friendship'] = 50.0
df.loc[(df.name == 'corvisquire'), 'base_friendship'] = 50.0
df.loc[(df.name == 'corviknight'), 'base_friendship'] = 50.0
df.loc[(df.name == 'blipbug'), 'base_friendship'] = 50.0
df.loc[(df.name == 'dottler'), 'base_friendship'] = 50.0
df.loc[(df.name == 'orbeetle'), 'base_friendship'] = 50.0
df.loc[(df.name == 'nickit'), 'base_friendship'] = 50.0
df.loc[(df.name == 'thievul'), 'base_friendship'] = 50.0
df.loc[(df.name == 'gossifleur'), 'base_friendship'] = 50.0
df.loc[(df.name == 'eldegoss'), 'base_friendship'] = 50.0
df.loc[(df.name == 'wooloo'), 'base_friendship'] = 50.0
df.loc[(df.name == 'dubwool'), 'base_friendship'] = 50.0
df.loc[(df.name == 'chewtle'), 'base_friendship'] = 50.0
df.loc[(df.name == 'drednaw'), 'base_friendship'] = 50.0
df.loc[(df.name == 'yamper'), 'base_friendship'] = 50.0
df.loc[(df.name == 'boltund'), 'base_friendship'] = 50.0
df.loc[(df.name == 'rolycoly'), 'base_friendship'] = 50.0
df.loc[(df.name == 'carkol'), 'base_friendship'] = 50.0
df.loc[(df.name == 'coalossal'), 'base_friendship'] = 50.0
df.loc[(df.name == 'applin'), 'base_friendship'] = 50.0
df.loc[(df.name == 'flapple'), 'base_friendship'] = 50.0
df.loc[(df.name == 'appletun'), 'base_friendship'] = 50.0
df.loc[(df.name == 'silicobra'), 'base_friendship'] = 50.0
df.loc[(df.name == 'sandaconda'), 'base_friendship'] = 50.0
df.loc[(df.name == 'cramorant'), 'base_friendship'] = 50.0
df.loc[(df.name == 'arrokuda'), 'base_friendship'] = 50.0
df.loc[(df.name == 'barraskewda'), 'base_friendship'] = 50.0
df.loc[(df.name == 'toxel'), 'base_friendship'] = 50.0
df.loc[(df.name == 'toxtricity low key form'), 'base_friendship'] = 50.0
df.loc[(df.name == 'toxtricity amped form'), 'base_friendship'] = 50.0
df.loc[(df.name == 'sizzlipede'), 'base_friendship'] = 50.0
df.loc[(df.name == 'centiskorch'), 'base_friendship'] = 50.0
df.loc[(df.name == 'clobbopus'), 'base_friendship'] = 50.0
df.loc[(df.name == 'grapploct'), 'base_friendship'] = 50.0
df.loc[(df.name == 'sinistea'), 'base_friendship'] = 50.0
df.loc[(df.name == 'polteageist'), 'base_friendship'] = 50.0
df.loc[(df.name == 'hatenna'), 'base_friendship'] = 50.0
df.loc[(df.name == 'hattrem'), 'base_friendship'] = 50.0
df.loc[(df.name == 'hatterene'), 'base_friendship'] = 50.0
df.loc[(df.name == 'impidimp'), 'base_friendship'] = 50.0
df.loc[(df.name == 'morgrem'), 'base_friendship'] = 50.0
df.loc[(df.name == 'grimmsnarl'), 'base_friendship'] = 50.0
df.loc[(df.name == 'obstagoon'), 'base_friendship'] = 50.0
df.loc[(df.name == 'perrserker'), 'base_friendship'] = 50.0
df.loc[(df.name == 'cursola'), 'base_friendship'] = 50.0
df.loc[(df.name == "sirfetch'd"), 'base_friendship'] = 50.0
df.loc[(df.name == 'mr. rime'), 'base_friendship'] = 50.0
df.loc[(df.name == 'runerigus'), 'base_friendship'] = 50.0
df.loc[(df.name == 'milcery'), 'base_friendship'] = 50.0
df.loc[(df.name == 'alcremie'), 'base_friendship'] = 50.0
df.loc[(df.name == 'falinks'), 'base_friendship'] = 50.0
df.loc[(df.name == 'pincurchin'), 'base_friendship'] = 50.0
df.loc[(df.name == 'snom'), 'base_friendship'] = 50.0
df.loc[(df.name == 'frosmoth'), 'base_friendship'] = 50.0
df.loc[(df.name == 'stonjourner'), 'base_friendship'] = 50.0
df.loc[(df.name == 'eiscue ice face'), 'base_friendship'] = 50.0
df.loc[(df.name == 'eiscue noice face'), 'base_friendship'] = 50.0
df.loc[(df.name == 'indeedee male'), 'base_friendship'] = 140.0
df.loc[(df.name == 'indeedee female'), 'base_friendship'] = 140.0
df.loc[(df.name == 'morpeko full belly mode'), 'base_friendship'] = 50.0
df.loc[(df.name == 'morpeko hangry mode'), 'base_friendship'] = 50.0
df.loc[(df.name == 'cufant'), 'base_friendship'] = 50.0
df.loc[(df.name == 'copperajah'), 'base_friendship'] = 50.0
df.loc[(df.name == 'dracozolt'), 'base_friendship'] = 50.0
df.loc[(df.name == 'arctozolt'), 'base_friendship'] = 50.0
df.loc[(df.name == 'dracovish'), 'base_friendship'] = 50.0
df.loc[(df.name == 'arctovish'), 'base_friendship'] = 50.0
df.loc[(df.name == 'duraludon'), 'base_friendship'] = 50.0
df.loc[(df.name == 'dreepy'), 'base_friendship'] = 50.0
df.loc[(df.name == 'drakloak'), 'base_friendship'] = 50.0
df.loc[(df.name == 'dragapult'), 'base_friendship'] = 50.0
df.loc[(df.name == 'zacian crowned sword'), 'base_friendship'] = 0.0
df.loc[(df.name == 'zacian hero of many battles'), 'base_friendship'] = 0.0
df.loc[(df.name == 'zamazenta crowned shield'), 'base_friendship'] = 0.0
df.loc[(df.name == 'zamazenta hero of many battles'), 'base_friendship'] = 0.0
df.loc[(df.name == 'eternatus'), 'base_friendship'] = 0.0
df.loc[(df.name == 'eternatus eternamax'), 'base_friendship'] = 0.0
df.loc[(df.name == 'kubfu'), 'base_friendship'] = 50.0
df.loc[(df.name == 'urshifu single strike style'), 'base_friendship'] = 50.0
df.loc[(df.name == 'urshifu rapid strike style'), 'base_friendship'] = 50.0
df.loc[(df.name == 'zarude'), 'base_friendship'] = 0.0
df.loc[(df.name == 'regieleki'), 'base_friendship'] = 35.0
df.loc[(df.name == 'regidrago'), 'base_friendship'] = 35.0
df.loc[(df.name == 'glastrier'), 'base_friendship'] = 35.0
df.loc[(df.name == 'spectrier'), 'base_friendship'] = 35.0
df.loc[(df.name == 'calyrex'), 'base_friendship'] = 100.0
df.loc[(df.name == 'calyrex ice rider'), 'base_friendship'] = 100.0
df.loc[(df.name == 'calyrex shadow rider'), 'base_friendship'] = 100.0

# 120 missing values for base_experience
df.loc[(df.name == 'galarian meowth'), 'base_experience'] = 58.0
df.loc[(df.name == 'galarian ponyta'), 'base_experience'] = 82.0
df.loc[(df.name == 'galarian rapidash'), 'base_experience'] = 175.0
df.loc[(df.name == 'galarian slowbro'), 'base_experience'] = 172.0
df.loc[(df.name == "galarian farfetch'd"), 'base_experience'] = 132.0
df.loc[(df.name == 'galarian weezing'), 'base_experience'] = 172.0
df.loc[(df.name == 'galarian mr. mime'), 'base_experience'] = 161.0
df.loc[(df.name == 'galarian articuno'), 'base_experience'] = 290.0
df.loc[(df.name == 'galarian zapdos'), 'base_experience'] = 290.0
df.loc[(df.name == 'galarian moltres'), 'base_experience'] = 290.0
df.loc[(df.name == 'galarian slowking'), 'base_experience'] = 172.0
df.loc[(df.name == 'galarian corsola'), 'base_experience'] = 144.0
df.loc[(df.name == 'galarian zigzagoon'), 'base_experience'] = 56.0
df.loc[(df.name == 'galarian linoone'), 'base_experience'] = 147.0
df.loc[(df.name == 'galarian darumaka'), 'base_experience'] = 63.0
df.loc[(df.name == 'galarian darmanitan standard mode'), 'base_experience'] = 168.0
df.loc[(df.name == 'galarian darmanitan zen mode'), 'base_experience'] = 189.0
df.loc[(df.name == 'galarian yamask'), 'base_experience'] = 61.0
df.loc[(df.name == 'galarian stunfisk'), 'base_experience'] = 165.0
df.loc[(df.name == 'meltan'), 'base_experience'] = 150.0
df.loc[(df.name == 'melmetal'), 'base_experience'] = 300.0
df.loc[(df.name == 'grookey'), 'base_experience'] = 62.0
df.loc[(df.name == 'thwackey'), 'base_experience'] = 147.0
df.loc[(df.name == 'rillaboom'), 'base_experience'] = 265.0
df.loc[(df.name == 'scorbunny'), 'base_experience'] = 62.0
df.loc[(df.name == 'raboot'), 'base_experience'] = 147.0
df.loc[(df.name == 'cinderace'), 'base_experience'] = 265.0
df.loc[(df.name == 'sobble'), 'base_experience'] = 62.0
df.loc[(df.name == 'drizzile'), 'base_experience'] = 147.0
df.loc[(df.name == 'inteleon'), 'base_experience'] = 265.0
df.loc[(df.name == 'skwovet'), 'base_experience'] = 55.0
df.loc[(df.name == 'greedent'), 'base_experience'] = 161.0
df.loc[(df.name == 'rookidee'), 'base_experience'] = 49.0
df.loc[(df.name == 'corvisquire'), 'base_experience'] = 128.0
df.loc[(df.name == 'corviknight'), 'base_experience'] = 248.0
df.loc[(df.name == 'blipbug'), 'base_experience'] = 36.0
df.loc[(df.name == 'dottler'), 'base_experience'] = 117.0
df.loc[(df.name == 'orbeetle'), 'base_experience'] = 253.0
df.loc[(df.name == 'nickit'), 'base_experience'] = 49.0
df.loc[(df.name == 'thievul'), 'base_experience'] = 159.0
df.loc[(df.name == 'gossifleur'), 'base_experience'] = 50.0
df.loc[(df.name == 'eldegoss'), 'base_experience'] = 161.0
df.loc[(df.name == 'wooloo'), 'base_experience'] = 122.0
df.loc[(df.name == 'dubwool'), 'base_experience'] = 172.0
df.loc[(df.name == 'chewtle'), 'base_experience'] = 57.0
df.loc[(df.name == 'drednaw'), 'base_experience'] = 170.0
df.loc[(df.name == 'yamper'), 'base_experience'] = 54.0
df.loc[(df.name == 'boltund'), 'base_experience'] = 172.0
df.loc[(df.name == 'rolycoly'), 'base_experience'] = 48.0
df.loc[(df.name == 'carkol'), 'base_experience'] = 144.0
df.loc[(df.name == 'coalossal'), 'base_experience'] = 255.0
df.loc[(df.name == 'applin'), 'base_experience'] = 52.0
df.loc[(df.name == 'flapple'), 'base_experience'] = 170.0
df.loc[(df.name == 'appletun'), 'base_experience'] = 170.0
df.loc[(df.name == 'silicobra'), 'base_experience'] = 63.0
df.loc[(df.name == 'sandaconda'), 'base_experience'] = 179.0
df.loc[(df.name == 'cramorant'), 'base_experience'] = 166.0
df.loc[(df.name == 'arrokuda'), 'base_experience'] = 56.0
df.loc[(df.name == 'barraskewda'), 'base_experience'] = 172.0
df.loc[(df.name == 'toxel'), 'base_experience'] = 48.0
df.loc[(df.name == 'toxtricity low key form'), 'base_experience'] = 176.0
df.loc[(df.name == 'toxtricity amped form'), 'base_experience'] = 176.0
df.loc[(df.name == 'sizzlipede'), 'base_experience'] = 61.0
df.loc[(df.name == 'centiskorch'), 'base_experience'] = 184.0
df.loc[(df.name == 'clobbopus'), 'base_experience'] = 62.0
df.loc[(df.name == 'grapploct'), 'base_experience'] = 168.0
df.loc[(df.name == 'sinistea'), 'base_experience'] = 62.0
df.loc[(df.name == 'polteageist'), 'base_experience'] = 178.0
df.loc[(df.name == 'hatenna'), 'base_experience'] = 53.0
df.loc[(df.name == 'hattrem'), 'base_experience'] = 130.0
df.loc[(df.name == 'hatterene'), 'base_experience'] = 255.0
df.loc[(df.name == 'impidimp'), 'base_experience'] = 53.0
df.loc[(df.name == 'morgrem'), 'base_experience'] = 130.0
df.loc[(df.name == 'grimmsnarl'), 'base_experience'] = 255.0
df.loc[(df.name == 'obstagoon'), 'base_experience'] = 260.0
df.loc[(df.name == 'perrserker'), 'base_experience'] = 154.0
df.loc[(df.name == 'cursola'), 'base_experience'] = 179.0
df.loc[(df.name == "sirfetch'd"), 'base_experience'] = 177.0
df.loc[(df.name == 'mr. rime'), 'base_experience'] = 182.0
df.loc[(df.name == 'runerigus'), 'base_experience'] = 169.0
df.loc[(df.name == 'milcery'), 'base_experience'] = 54.0
df.loc[(df.name == 'alcremie'), 'base_experience'] = 173.0
df.loc[(df.name == 'falinks'), 'base_experience'] = 165.0
df.loc[(df.name == 'pincurchin'), 'base_experience'] = 152.0
df.loc[(df.name == 'snom'), 'base_experience'] = 37.0
df.loc[(df.name == 'frosmoth'), 'base_experience'] = 166.0
df.loc[(df.name == 'stonjourner'), 'base_experience'] = 165.0
df.loc[(df.name == 'eiscue ice face'), 'base_experience'] = 165.0
df.loc[(df.name == 'eiscue noice face'), 'base_experience'] = 165.0
df.loc[(df.name == 'indeedee male'), 'base_experience'] = 166.0
df.loc[(df.name == 'indeedee female'), 'base_experience'] = 166.0
df.loc[(df.name == 'morpeko full belly mode'), 'base_experience'] = 153.0
df.loc[(df.name == 'morpeko hangry mode'), 'base_experience'] = 153.0
df.loc[(df.name == 'cufant'), 'base_experience'] = 66.0
df.loc[(df.name == 'copperajah'), 'base_experience'] = 175.0
df.loc[(df.name == 'dracozolt'), 'base_experience'] = 177.0
df.loc[(df.name == 'arctozolt'), 'base_experience'] = 177.0
df.loc[(df.name == 'dracovish'), 'base_experience'] = 177.0
df.loc[(df.name == 'arctovish'), 'base_experience'] = 177.0
df.loc[(df.name == 'duraludon'), 'base_experience'] = 187.0
df.loc[(df.name == 'dreepy'), 'base_experience'] = 54.0
df.loc[(df.name == 'drakloak'), 'base_experience'] = 144.0
df.loc[(df.name == 'dragapult'), 'base_experience'] = 300.0
df.loc[(df.name == 'zacian crowned sword'), 'base_experience'] = 360.0
df.loc[(df.name == 'zacian hero of many battles'), 'base_experience'] = 335.0
df.loc[(df.name == 'zamazenta crowned shield'), 'base_experience'] = 360.0
df.loc[(df.name == 'zamazenta hero of many battles'), 'base_experience'] = 335.0
df.loc[(df.name == 'eternatus'), 'base_experience'] = 345.0
df.loc[(df.name == 'eternatus eternamax'), 'base_experience'] = 563.0
df.loc[(df.name == 'kubfu'), 'base_experience'] = 77.0
df.loc[(df.name == 'urshifu single strike style'), 'base_experience'] = 275.0
df.loc[(df.name == 'urshifu rapid strike style'), 'base_experience'] = 275.0
df.loc[(df.name == 'zarude'), 'base_experience'] = 300.0
df.loc[(df.name == 'regieleki'), 'base_experience'] = 290.0
df.loc[(df.name == 'regidrago'), 'base_experience'] = 290.0
df.loc[(df.name == 'glastrier'), 'base_experience'] = 290.0
df.loc[(df.name == 'spectrier'), 'base_experience'] = 290.0
df.loc[(df.name == 'calyrex'), 'base_experience'] = 250.0
df.loc[(df.name == 'calyrex ice rider'), 'base_experience'] = 340.0
df.loc[(df.name == 'calyrex shadow rider'), 'base_experience'] = 340.0

# Drop Replaced Columns
df.drop(columns=['ability_2', 'ability_hidden', 'egg_type_2', 'percentage_male'], inplace=True)
