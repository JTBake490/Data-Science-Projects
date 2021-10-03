# Notes Regrading Pokemon EDA

## Objective
* Perform a basic EDA using as much of the Python Standard Library as possible

## Web Scraping
* The data was webscraped from pokemondb.net/pokedex/all on December 2020
* Since the Pokemon video games are continuing to be made, the database may continue to expand. The techniques used to scrape the data should continute to work provided the HTML structure of the website remain contant

## Database
* SQLite
    - Since using the Python Standard Library is part of the objective, SQLite was chosen as the database.

## Parsing
* HTMLParser
    - Python has its own html parser which meets the critera for the objective

## Queries
* Two sample queries are given at the end of the notebook
    - Query all scraped stats from "Mega Pokemon"
    - Query the pokemon with the highest base HP stat