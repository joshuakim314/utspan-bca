
# coding: utf-8

# In[24]:


import pandas as pd
from math import pi
import seaborn as sns
import matplotlib.pyplot as plt
import statistics


class Game:
    home_team = str
    away_team = str
    competetion = str
    home_score = int
    away_score = int
    home_win = bool
    nba_present = bool

    def __init__(self, home_team: str, away_team: str, comp: str, home_score: int, away_score: int):
        self.home_team = home_team
        self.away_team = away_team
        self.competition = comp
        self.home_score = home_score
        self.away_score = away_score
        if home_score>away_score:
            home_win = True
        else:
            home_win = False
        self.nba_present = None

    def team_played(self, team: str) -> int:
        """

        :param team:
        :return:
        2 if home
        1 if away
        0 if not played
        """
        if team == self.home_team:
            return 2
        elif team == self.away_team:
            return 1
        else:
            return 0



class Player:
    name = str
    team = str
    field_goal_attempts = int
    _2pt_attempts = int
    _2pt_made = int
    _3pt_attempts = int
    _3pt_made = int
    free_attempts = int
    free_made = int


    def __init__(self, name: str, team: str):
        self.name = name
        self.team = team
        self.field_goal_attempts = 0
        self._2pt_attempts = 0
        self._2pt_made = 0
        self._3pt_attempts = 0
        self._3pt_made = 0
        self.free_attempts = 0
        self.free_made = 0

    def _2pt(self, made: bool):
        self.field_goal_attempts += 1
        self._2pt_attempts += 1
        if made:
            self._2pt_made += 1

    def _3pt(self, made: bool):
        self.field_goal_attempts += 1
        self._3pt_attempts += 1
        if made:
            self._3pt_made += 1

    def _free(self, made: bool):
        self.free_attempts += 1
        if made:
            self.free_made += 1

    def shot(self, pts: int, made: bool):
        if pts == 1:
            self._free(made)
        elif pts == 2:
            self._2pt(made)
        elif pts == 3:
            self._3pt(made)

    def __eq__(self, name: str):
        if name == self.name:
            return True
        else:
            return False

    def __str__(self):
        return str(self.name)


