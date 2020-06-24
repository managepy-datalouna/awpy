""" Data cleaning functions
"""

import numpy as np
import pandas as pd
import textdistance

from csgo.analytics.distance import point_distance


def clean_footsteps(df, max_dist=500):
    """ A function to clean a dataframe of footsteps, as created by the match_parser
    """
    for r in range(0, df.RoundNum.max() + 1):
        for p in df.SteamID.unique():
            player_df = df[(df["RoundNum"] == r) & (df["SteamID"] == p)]
            player_pos = []
            player_pos_clean = []
            for i, row in player_df.iterrows():
                player_pos.append((row["X"], row["Y"], row["Z"]))
            for i, pos in enumerate(player_pos):
                if i == 0:
                    player_pos_clean.append(0)
                else:
                    player_pos_clean.append(
                        distance.euclidean(list(pos), list(player_pos[i - 1]))
                    )
    return NotImplementedError


def associate_players(game_names=[], player_names=[]):
    """ A function to return a dict of player names. Uses longest common subsequence distance.

    Args:
        game_names (list)   : A list of names generated by the demofile
        player_names (list) : A list of names

    Returns:
        player_dict (dict) : A dictionary where the keys are entries in game_names
    """
    if len(game_names) != len(player_names):
        raise ValueError("Need both player lists to only have 5 entries each.")
    player_dict = {}
    for p in player_names:
        name_distances = []
        for gn in game_names:
            name_distances.append(textdistance.lcsseq.distance(p, gn))
        player_dict[game_names[np.argmin(name_distances)]] = p
    return player_dict
