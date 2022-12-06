import numpy as np
import pandas as pd
import asyncio
import fraser_gehrig.fraser_gehrig as fg


"""
This example script generates a kaggle dataset
"""


def import_data_player_data_year(year):
    df = fg.get_player_stats(year=year)
    df["year"] = year
    return df


async def import_player_data(years: np.ndarray, output_file: str) -> None:
    """Imports the player data and saves it to the specified output file"""
    results = [import_data_player_data_year(year) for year in years]
    df = pd.concat(results, axis=0)
    df.to_csv(output_file)
    return


def import_game_stats_year(year):
    df = fg.get_game_by_game_stats(year=year)
    df["year"] = year
    return df


async def import_game_by_game_data(years: np.ndarray, output_file: str) -> None:
    """Imports the game by game data and saves it to the specified output file"""
    results = [import_game_stats_year(year) for year in years]
    df = pd.concat(results, axis=0)
    df.to_csv(output_file)
    return


def import_game_results_year(year):
    df = fg.get_game_by_game_results(year=year)
    df["year"] = year
    return df


async def import_game_by_game_results(years: np.ndarray, output_file: str) -> None:
    """Imports the game by game results and saves it to the specified output file"""
    results = [import_game_results_year(year) for year in years]
    df = pd.concat(results, axis=0)
    df.to_csv(output_file)
    return


async def main():
    """generates datasets to be uploaded to kaggle using the fraser_gehrig package"""
    await asyncio.gather(
        import_player_data(np.arange(1897, 2022), "afl_player_data.csv"),
        import_game_by_game_data(np.arange(1965, 2020), "afl_game_by_game_data.csv"),
        import_game_by_game_results(
            np.arange(1965, 2020), "afl_game_by_game_results.csv"
        ),
    )
    return


if __name__ == "__main__":
    SystemExit(asyncio.run(main()))
