Fraser Gehrig 
==================

[![PyPI version](https://badge.fury.io/py/fraser_gehrig.svg)](https://badge.fury.io/py/fraser_gehrig) [![GitHub version](https://badge.fury.io/gh/jacaranda-analytics%2Ffraser-gehrig.svg)](https://badge.fury.io/gh/jacaranda-analytics%2Ffraser-gehrig)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
`master` ![master ci status](https://github.com/jacaranda-analytics/fraser_gehrig/actions/workflows/python-package.yml/badge.svg?branch=main)

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Fraser Gehrig ](#fraser-gehrig)
- [Description](#description)
- [Kaggle](#kaggle)
- [Installation](#installation)
    - [GitHub](#github)
    - [Pip](#pip)
- [Examples](#examples)
    - [Get player stats for a single year](#get--player-stats-for-a-single-year)
    - [Get game stats For a single year](#get-game-stats-for-a-single-year)
    - [Get game by game results for a single year](#get--game-by-game-results-for-a-single-year)
- [License](#license)

<!-- markdown-toc end -->

![Fraser Gehrig](https://i.ytimg.com/vi/fvE6R92tTG0/sddefault.jpg)

# Description 

This is a small webscraper package to scrap AFL player and game statistics data from [AFL Tables](https://afltables.com/afl/afl_index.html). 

This package is named after the famous St Kilda forward Fraser Gehrig because, why not? 


# Kaggle 

A kaggle dataset of the entire set of scraped table data, using this package, is available [here](https://www.kaggle.com/datasets/gabrieldennis/afl-player-and-game-data-and-statistics18972022). 
The script which was used to scrape the set of tables and package up the dataset for kaggle is located [here](examples/kaggle_data.py). 


- A Kaggle notebook which uses this data to predict the 2021 Brownlow medal counts can be seen [here](https://www.kaggle.com/gabrieldennis/2021-brownlow-prediction-mlp)

# Installation 

Currently, there are various ways this package can be installed. 
These include 

- GitHub 
- pip

## GitHub 

To install from GitHub there are two options, 
the first option is to clone the repository and do a local installation from the cloned directory. 

```sh
git clone git@github.com:jacaranda-analytics/fraser_gehrig.git
cd fraser_gehrig/ && pip install . 
```

The second option is to install from GitHub without first cloning the repository, 
to install the latest master branch, run the command. 

```sh
pip install https://github.com/jacaranda-analytics/fraser_gehrig/archive/master.zip
```

## Pypi 

To install through Pypi, simply run 

```python 
pip install fraser-gehrig
```


# Examples 

The following section shows some example usages for this tool 


```python 

>>>> import  fraser_gehrig.fraser_gehrig as fg 

```

## Get player stats for a single year 


```python 

>>> fg.get_player_stats(year = 2020)
Loading Data:
                  jumper games_played kicks marks
Crouch, Matt           5           16   162    44
Laird, Rory           29           17   186    46
Smith, Brodie         33           16   203    58
Keays, Ben            28           16   147    47
Crouch, Brad           2           12   136    20
...                  ...          ...   ...   ...
Schache, Josh         13            2     8     3
Porter, Callum        28            1     4    NA
Trengove, Jackson      8            1     2     1
Dickson, Tory         29            1    NA    NA
Young, Lewis           2            1     3     3

[650 rows x 27 columns]

```

## Get game stats For a single year 


```python 
 
>>> fg.get_game_by_game_stats(year = 2020)
.
.
.
         index        player       team  round opponents       stat value
0            0  Atkins, Rory   adelaide      0        SY  disposals    14
1            1  Atkins, Rory   adelaide      1        PA  disposals    10
2            2  Atkins, Rory   adelaide      2        GC  disposals     3
3            3  Atkins, Rory   adelaide      3        BL  disposals    NA
4            4  Atkins, Rory   adelaide      4        FR  disposals    NA
...        ...           ...        ...    ...       ...        ...   ...
267600  267600  Young, Lewis  bullldogs     13        GE   %_played    NA
267601  267601  Young, Lewis  bullldogs     14        WC   %_played    NA
267602  267602  Young, Lewis  bullldogs     15        HW   %_played    NA
267603  267603  Young, Lewis  bullldogs     16        FR   %_played    NA
267604  267604  Young, Lewis  bullldogs     17        SK   %_played    NA

[267605 rows x 7 columns]


```

## Get game by game results for a single year


```python 
>>> fg.get_game_by_game_results(year = 2020)
            team   round       opponent  kicks  ... marks_inside_50 one_percenters bounces goal_assist
0           Adelaide   R1          Sydney  142-200  ...             6-8          38-47     7-0         7-7
1           Adelaide   R2   Port Adelaide  138-226  ...            4-13          41-45      NA         5-9
2           Adelaide   R3      Gold Coast  145-196  ...            2-10          33-36     2-4         2-7
3           Adelaide   R4  Brisbane Lions  162-199  ...            5-19          34-42     1-3         5-9
4           Adelaide   R5       Fremantle  170-197  ...            6-15          32-29     2-6         2-7
..               ...  ...             ...      ...  ...             ...            ...     ...         ...
13  Western Bulldogs  R14         Geelong  146-183  ...            10-7          49-40     1-5         7-7
14  Western Bulldogs  R16      West Coast  157-175  ...            8-10          38-35     1-4         3-7
15  Western Bulldogs  R17        Hawthorn  192-140  ...             9-5          61-50     0-1         9-4
16  Western Bulldogs  R18       Fremantle  162-172  ...            12-8          55-31     6-3         8-5
17  Western Bulldogs   EF        St Kilda  175-184  ...            9-12          48-44     3-6         4-7

[324 rows x 25 columns]
```


# License 

- [MIT](LICENSE.md)






