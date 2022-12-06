from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import requests
import pandas as pd
from typing import List


def get_player_stats(year: int = 2021) -> pd.DataFrame:
    """Retrieves the year by year player stats from
       https://afltables.com/afl/stats/

    Args:
        year (int, optional): Year to retrieve stats from. Acceptable range (1897-2021).
         Defaults to 2021.

    Raises:
        HTTPError:
        Exception

    Returns:
        pd.DataFramet: A data frame with player names as the index and statistics as the column names
    """
    min_year, max_year = 1897, 2022
    if not (min_year <= year <= max_year):
        raise ValueError(f"{year=} is not in range: {min_year} - {max_year}")

    try:
        r = requests.get(f"https://afltables.com/afl/stats/{year}.html")
    except HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except Exception as e:
        print(f"Exception: {e}")
    else:
        print("Loading Data:")

    html_content = BeautifulSoup(r.content, features="html.parser")

    stats_keys = parse_table_headers(html_content, player_index=1)

    players = {}
    for row in html_content.find_all("tr"):
        player_stats = {
            stats_keys[i]: data.string for i, data in enumerate(row.find_all("td"))
        }
        if player_stats and player_stats.get("player") is not None:
            players[player_stats["player"]] = {
                key: (value if value != "\xa0" else "NA")
                for key, value in player_stats.items()
                if key != "player"
            }

    return pd.DataFrame.from_dict(players, orient="index")


def parse_table_headers(html_content, player_index: int = 1) -> List[str]:
    """Parses the table headers

    Args:
        html_content ([type]): html content
        player_index (int, optional): Index which to insert  the player name as a column header. Defaults to 1.

    Returns:
        List[str]: List of parsed table headers
    """
    table_header = html_content.find_all("span")
    parsed_table_headers = [
        a.split("=")[1].lower().replace(" ", "_")
        for a in table_header[1].stripped_strings
    ]
    parsed_table_headers.insert(player_index, "player")

    return parsed_table_headers


def get_game_by_game_stats(year: int = 2021) -> pd.DataFrame:
    """Retrieves the detailed game by game afl player statistics for a year
       between 1965 and 2021 available from
       https://afltables.com/afl/stats/teams/{team}/{year}_gbg.html

    Args:
        year (int, optional): Year to retrieve stats from.
        Acceptable range (1965-2021). Defaults to 2021.

    Raises:
        ValueError: if year is outside the range 1965-2021

    Returns:
        pd.DataFrame: A pandas data frame which
        has columns array([player, team, round, opponent, statistic, value])
    """
    min_year, max_year = 1965, 2022
    if not (min_year <= year <= max_year):
        raise ValueError(f"{year=} is not in range: {min_year}-{max_year}")

    teams = [
        "adelaide",
        "brisbaneb",
        "brisbanel",
        "carlton",
        "collingwood",
        "essendon",
        "fitzroy",
        "fremantle",
        "geelong",
        "goldcoast",
        "gws",
        "hawthorn",
        "melbourne",
        "kangaroos",
        "padelaide",
        "richmond",
        "stkilda",
        "swans",
        "westcoast",
        "bullldogs",
    ]

    URL = "https://afltables.com/afl/stats/teams/"

    def url_func(team):
        return f"{URL}{team}/{year}_gbg.html"

    gbg_content = {}
    for team in teams:
        r = requests.get(url_func(team))
        if r.status_code != 200:
            continue
        html_content = BeautifulSoup(r.content, features="html.parser")
        opponents = [
            s.string
            for s in html_content.find("tfoot").find_all("tr")[1].find_all("th")
        ]
        opponents = opponents[1:-1]
        for body, header in zip(
            html_content.find_all("tbody"), html_content.find_all("thead")
        ):
            table_name = header.find("tr").find("th").string
            table_name = table_name.lower().replace(" ", "_")
            for table_row in body.find_all("tr"):
                table_content = [
                    s.string.replace("\xa0", "NA").replace("-", "NA")
                    for s in table_row.find_all("td")
                ]

                if table_content[0] not in gbg_content.keys():
                    gbg_content[table_content[0]] = {
                        table_name: table_content[1:-1]}
                    gbg_content[table_content[0]]["opponents"] = opponents
                    gbg_content[table_content[0]]["team"] = [
                        team for _ in range(len(opponents))
                    ]
                else:
                    gbg_content[table_content[0]
                                ][table_name] = table_content[1:-1]
    # Turn into pandas
    for key, values in gbg_content.items():
        if "df" not in locals():

            df = pd.DataFrame.from_dict(values)
            df["player"] = key
            df["round"] = df.index.values
        else:
            try:
                dat = pd.DataFrame.from_dict(values)
            except ValueError as ve:
                print("Unable to parse values")
                continue
            dat["player"] = key
            dat["round"] = dat.index.values
            df = pd.concat([df, dat], axis=0)

    return df.melt(
        id_vars=["player", "team", "round", "opponents"],
        value_name="value",
        var_name="stat",
    ).reset_index()


def get_game_by_game_results(year: int) -> pd.DataFrame:
    """
    Retrieve the detailed game by game afl statistics for each year
    between 1965 and 2021
    available from https://afltables.com/afl/stats/{year}t.html
    Args:
        year (int, optional): Year to retrieve stats from.
                             Acceptable range (1965-2021).
                                Defaults to 2021.

    Raises:
        ValueError: if year is outside the range 1965-2021

    Returns:
        pd.DataFrame:
    """
    if year not in range(1965, 2023):
        raise ValueError(f"{year} outside range (1965, 2023)")

    URL = f"https://afltables.com/afl/stats/{year}t.html"
    r = requests.get(URL)
    html_content = BeautifulSoup(r.content, features="html.parser")

    table_headers: str = []
    for header in html_content.find_all("thead"):
        team_str = header.find("tr").find(
            "th").find("a").previousSibling.string

        table_headers.append(team_str.replace("Team Statistics [", "").strip())
    # Teams are repeated

    # Parse the table headers
    statistics = []
    for ids, stat in enumerate(html_content.find_all("thead")):
        if ids > 1:
            break
        for tr in stat.find_all("tr"):
            for s in tr.find_all("th"):
                if s.string is not None:
                    statistics.append(s.string)

    # Repeats after - So we can break it into two table headers
    column_headers = ["team"]
    column_headers.extend(list(dict.fromkeys(statistics)))

    # Create a Pandas data frame
    game_by_game = pd.DataFrame({s: [] for s in column_headers})

    for idx, tbody in enumerate(html_content.find_all("tbody")):
        if idx % 2 == 0:
            row_content = []
        rowidx = 0
        for row in tbody.find_all("tr"):
            if len(row.find_all("td")) > 0:
                if idx % 2 == 0:
                    team = [table_headers[idx]]
                    team.extend(
                        [
                            data.string.replace("\xa0-", "NA")
                            for data in row.find_all("td")
                        ]
                    )
                    row_content.append(team[:15])
                    rowidx += 1
                else:
                    team = [
                        data.string.replace("\xa0-", "NA")
                        for i, data in enumerate(row.find_all("td"))
                        if i > 1
                    ]
                    row_content[rowidx].extend(team[:10])
                    rowidx += 1
        if idx % 2 == 1:
            team_games = pd.DataFrame(row_content, columns=column_headers)
            game_by_game = pd.concat([game_by_game, team_games], axis=0)

        # Create a dictionary to map columns to
        names_to_dict = {
            "#": "round",
            "KI": "kicks",
            "MK": "marks",
            "HB": "handballs",
            "DI": "disposals",
            "GL": "goals",
            "BH": "behinds",
            "HO": "hit_outs",
            "TK": "tackles",
            "RB": "rebound_50s",
            "IF": "inside_50s",
            "CL": "clearances",
            "CG": "clangers",
            "FF": "freekicks_for",
            "FA": "freekicks_agains",
            "BR": "brownlow_votes",
            "CP": "contested_possesions",
            "UP": "uncontested_possesions",
            "CM": "contested_marks",
            "MI": "marks_inside_50",
            "1%": "one_percenters",
            "BO": "bounces",
            "GA": "goal_assist",
        }

    return game_by_game.rename(names_to_dict, axis=1)
