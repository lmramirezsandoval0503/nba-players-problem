# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 20:59:04 2022
NBA players heights
@author: Luis Miguel Ramirez Sandoval
"""

import json
import requests
from itertools import combinations, permutations

class PlayersClass():
    """
        Players class. 
        This class holds the retrieved data (players) from the given url.
    """
    
    
    def __init__(self):
        
        # Get data and save it
        self.data_url = "https://mach-eight.uc.r.appspot.com/"
        self.data_json = requests.get(self.data_url).json()["values"]
        
        # Sort players data by height in in
        self.players_data = sorted(self.data_json, key = lambda player : player["h_in"])
        self.players_combinations = combinations(self.players_data, 2)
    
    
    def find_players_matches(self, desired_height):
        """
        Finds all possible pairs of players for which their heights in inches add up to the value of the desired height argument. This uses combinations to find all possible
        combinations of players then filters out the ones that do not equal the total desired height.

        Parameters
        ----------
        desired_height : INT
            Desired height for which all possible pairs of players heights should be equal to.

        Returns
        -------
        list
            List of pairs of players whose heights add up to the desired height argument.

        """
        return [ self.get_full_pair_names(players_pair[0], players_pair[1]) for players_pair in  self.players_combinations if (int(players_pair[0]["h_in"]) + int(players_pair[1]["h_in"])) == desired_height]

    
    def get_full_name(self, player):
        """
        Returns the full name of the player using the first_name and last_name values from the player object (json)

        Parameters
        ----------
        player : JSON
            Player object (json) with first_name and last_name keys.

        Returns
        -------
        str
            Full name made of first_name and last_name values of the player's object.

        """
        return "{} {}".format(player["first_name"], player["last_name"])
    
    
    def get_full_pair_names(self, player1, player2):
        """
        Returns the full pair of names of the players whose heights meet the desired height

        Parameters
        ----------
        player1 : JSON
            Player 1 object (json) with first_name and last_name keys.
        
        player2 : JSON
            Player 2 object (json) with first_name and last_name keys.

        Returns
        -------
        str
            Full pair names made of player's names

        """
        return "{}    {}\n".format(self.get_full_name(player1), self.get_full_name(player2))
