# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 20:59:04 2022
NBA players heights
@author: Luis Miguel Ramirez Sandoval
"""

from PlayersClass import *
players_class_instance = PlayersClass()

if __name__ == "__main__":

    desired_height = int(input("Enter the desired height: ") or 139)
    
    if desired_height == 0:
        print("Height cannot be 0.")
        print("No matches found.")
    
    matches_combinations = players_class_instance.find_players_matches(desired_height)
    
    if len(matches_combinations) == 0:
        print("No matches found.")
    else:
        print("\n")
        print(*(match for match in matches_combinations), sep = "\n")


