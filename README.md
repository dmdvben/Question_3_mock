# The weekly prize draw

Every week, the marketing team draws two winners of a first prize and two winners of a second prize among
the members of the loyalty club. The draw is made by the course API's endpoint `/getrand`, with the week
number as the seed, so a draw can always be made again and checked.

## Set up

Copy `.env.example` to `.env`, and write the key of the endpoint `/getrand` in `.env`.
Git ignores `.env`, so the key stays on your droplet.

## Run

`draw_prizes.py` draws the winners and saves them in `test_dataframe.csv`.

## Files

- `draw_prizes.py`: the draw, from the API to the CSV file
- `api_functions.py`: the request to the course API
- `example_conflict.py`: the settings of the draw
