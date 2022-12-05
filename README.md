Fraser Gehrig 
==================

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Fraser Gehrig ](#fraser-gehrig)
- [Description](#description)
- [Installation](#installation)
    - [Github](#github)
- [Examples](#examples)
    - [Get  player stats for a single year](#get--player-stats-for-a-single-year)
    - [Get game stats For a single year](#get-game-stats-for-a-single-year)
    - [Get  game by game results for a single year](#get--game-by-game-results-for-a-single-year)
- [Licence](#licence)

<!-- markdown-toc end -->


# Description 

This is a small webscraper package to scrap AFL player and game statistics data from [AFL Tables](https://afltables.com/afl/afl_index.html). 

This package is named after the famous St Kilda forward Fraser Gehrig because, why not? 


# Installation 

Currently the best way to install this package is directly from github. 

## Github 

To install from github there are two options, 
the first option is to clone the repository  and do a local install 
from the cloned directory. 

```sh
git clone git@github.com:jacaranda-analytics/fraser_gehrig.git
cd fraser_gehrig/ && pip install . 
```

The second option is to install from github without first cloning the repository, 
to install the  latest master branch, run the command. 

```sh
pip install https://github.com/jacaranda-analytics/fraser_gehrig/archive/master.zip
```


# Examples 

The following section shows some example usages for this tool 

```python 

>>>> import  fraser_gehrig.fraser_gehrig as fg 

```

## Get  player stats for a single year 


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

## Get  game by game results for a single year


```python 
>>> fg.get_game_by_game_results(year = 2020)
                team    #        Opponent       KI      MK       HB 
0           Adelaide   R1          Sydney  142-200   41-68  107-113 
1           Adelaide   R2   Port Adelaide  138-226  39-105  121-137 
2           Adelaide   R3      Gold Coast  145-196   56-87  105-124 
3           Adelaide   R4  Brisbane Lions  162-199   71-80    70-86 
4           Adelaide   R5       Fremantle  170-197  79-109   133-88 
..               ...  ...             ...      ...     ...      ... 
13  Western Bulldogs  R14         Geelong  146-183   61-77  136-140 
14  Western Bulldogs  R16      West Coast  157-175   59-80   162-86 
15  Western Bulldogs  R17        Hawthorn  192-140   85-58  158-130 
16  Western Bulldogs  R18       Fremantle  162-172   58-79  125-129 
17  Western Bulldogs   EF        St Kilda  175-184   75-88  122-100 

[324 rows x 25 columns]

```


# Licence 

- [MIT](LICENCE.md)






