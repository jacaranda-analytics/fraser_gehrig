import os
import numpy as np
import pandas as pd
import asyncio
import fraser_gehrig.fraser_gehrig as fg


"""
This example script generates a kaggle dataset
"""


async def import_data_player_data_year(year, file_name):
    df = fg.get_player_stats(year=year)
    df["year"] = year
    df.to_csv(file_name)
    return


async def import_player_data(years: np.ndarray, output_file: str) -> None:
    """Imports the player data and saves it to the specified output file"""
    await asyncio.gather(
        *[
            import_data_player_data_year(year, f"{output_file}_{year}.csv")
            for year in years
        ]
    )
    return


async def import_game_stats_year(year, file_name):
    df = fg.get_game_by_game_stats(year=year)
    df["year"] = year
    df.to_csv(file_name)
    return


async def import_game_by_game_data(years: np.ndarray, output_file: str) -> None:
    """Imports the game by game data and saves it to the specified output file"""
    await asyncio.gather(
        *[import_game_stats_year(year, f"{output_file}_{year}.csv") for year in years]
    )
    return


async def import_game_results_year(year, file_name):
    df = fg.get_game_by_game_results(year=year)
    df["year"] = year
    df.to_csv(file_name)
    return


async def import_game_by_game_results(years: np.ndarray, output_file: str) -> None:
    """Imports the game by game results and saves it to the specified output file"""
    await asyncio.gather(
        *[import_game_results_year(year, f"{output_file}_{year}.csv") for year in years]
    )
    return


async def main():
    """generates datasets to be uploaded to kaggle using the fraser_gehrig package"""
    await asyncio.gather(
        import_player_data(np.arange(1897, 2022), "data/afl_player_data"),
        import_game_by_game_data(np.arange(1965, 2020), "data/afl_game_by_game_data"),
        import_game_by_game_results(
            np.arange(1965, 2020), "data/afl_game_by_game_results"
        ),
    )

    # Import the data  as year by year files  and write to disk
    files = os.listdir("data/")

    pd.concat(
        [pd.read_csv(f"data/{f}") for f in files if "afl_player_data_" in f], axis=0
    ).to_csv("afl_player_data_1897_2022.csv")
    pd.concat(
        [pd.read_csv(f"data/{f}") for f in files if "afl_game_by_game_data_" in f],
        axis=0,
    ).to_csv("afl_game_by_game_data_1965_2022.csv")
    pd.concat(
        [pd.read_csv(f"data/{f}") for f in files if "afl_game_by_game_results" in f],
        axis=0,
    ).to_csv("afl_game_by_game_results_1965_2022.csv")
    return


if __name__ == "__main__":
    SystemExit(asyncio.run(main()))
