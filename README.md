# advent
Advent of Code Python solutions

![Build](https://github.com/crerwin/advent/actions/workflows/build.yaml/badge.svg)

These are solutions for http://adventofcode.com/

I've checked in my inputs so I can work on this without redownloading them, but they are technically per-user.

## Setup
```
poetry install
```

## Test Example
```
poetry run pytest tests/test_2022day1.py
```

## Executing
```
poetry run advent run -y 2021 -d 1 -p 1
```

## Show

The Show command shows a list of implemented days:
```
$ poetry run advent show
Legend: Not yet implemented     Neither part    Part 1 only     Part 2 only     Both parts      Star total for year

2015: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ⭐ 19
2016: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ⭐ 0
2017: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ⭐ 9
2018: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ⭐ 6
2019: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ⭐ 0
2020: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ⭐ 6
2021: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ⭐ 4
2022: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ⭐ 4
```

## Stubbing out a new day
`poetry run advent stubout --year 2022 --day 3`
