
# coding: utf-8

# In[24]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

num_row = 196657 - 1    # -1 for the header row
csv_file = "CanadaBasketballHackathonData.csv"
data = pd.read_csv(csv_file, encoding='latin-1')
num_row = 196657 - 1

player_list = []

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
        
        
class Country:
    name = str
    record = []
    
    def __init__(self, name: str):
        self.name = name
    
    def game_played(self, home_team: str, away_team: str, comp: str, home_score: int, away_score: int):
        game = Game(home_team, away_team, comp, home_score, away_score)
        record += [game]
                
    def ppg(self):
        total_points = 0
        g = 0
        for game in self.record:
            g += 1
            if self.name == game.home_team:
                total_points += game.home_score
            else:
                total_points += game.away_score
        if g != 0:
            return total_points/g
        else:
            return 0
    
    def win_percent(self):
        w = 0
        g = 0
        for game in record:
            g += 1
            if country.name == game.home_team:
                if game.home_win:
                    w += 1
            else:
                if not game.home_win:
                    w += 1
        if g != 0:
            return w/g
        else:
            return 0
    
    

class Player:
    name = str
    team = str
    region = str
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
            
    def __cmp__(self, name: str):
        if name == self.name:
            return true
        else:
            return false
        
    def fgp(self):
        num = 0
        try:
            num = (self._2pt_made + self._3pt_made)/(self._2pt_attempts + self._3pt_attempts)
        except:
            pass
        return num
    
    def ftp(self):
        return self.free_made / self.free_attempts
    
    def efgp(self):
        return (self._2pt_made + 1.5*self._3pt_made)/(self._2pt_attempts + self._3pt_attempts)
    
    def _2fgp(self):
        return self._2pt_made / self._2pt_attempts
    
    def _3fgp(self):
        return self._3pt_made / self._3pt_attempts
    
    def tsp(self):
        pts = 2*self._2pt_made + 3*self._3pt_made + 1*self.free_made
        den = 2*(self._2pt_attempts + self._3pt_attempts + 0.44*self.free_attempts)
        if den != 0:
            return pts/den
        else:
            return 0
    
    def __str__(self):
        return str(self.name) + "||eFGP: " + str(self.efgp())
    

    
for row in range(0, 10000 - 1): ##CHANGE TO ALL ROWS LATER
    player_name = data.iloc[row][9]
    player_country = data.iloc[row][6]
    result = data.iloc[row][5]
    before_score = int(data.iloc[row-1][11]) + int(data.iloc[row-1][12])
    after_score = int(data.iloc[row][11]) + int(data.iloc[row][12])
    
    player_in_list = False
    for p in player_list:
        if p.name == player_name:
            player = p
            player_in_list = True
            
    if not player_in_list:
        player = Player(player_name, player_country)    
        player_list += [player]
        
    if result == 'Miss 2 Pts':
        player.shot(2, False)
    elif result == 'Make 2 Pts':
        player.shot(2, True)
    elif result == 'Miss 3 Pts':
        player.shot(3, False)
    elif result == 'Make 3 Pts':
        player.shot(3, True)
    elif result == 'Free Throw':
        if before_score == after_score:
            player.shot(1, False)
        else:
            player.shot(1, True)
    #print(player)
    

    
num_row = 196657 - 1    # -1 for the header row
csv_file = "CanadaBasketballHackathonData.csv"
data = pd.read_csv(csv_file, encoding='latin-1')
games_list = []
final_scores = pd.DataFrame()
previous_index = 0
counter = 0
for i in range(num_row - 1):
    if data.iloc[i, 7] > data.iloc[i+1, 7]:
        counter += 1
        games_list.append(data.iloc[previous_index:i+1])
        previous_index = i+1
games_list.append(data.iloc[previous_index:num_row-1])
games = []
for game in games_list:
    games.append(Game(game.iloc[-1, 4], game.iloc[-1, 3], game.iloc[-1, 1], game.iloc[-1, 12], game.iloc[-1, 11]))
    
print('hi')
countries = []
for g in games:
    home_country_found = False
    away_country_found = False
    for c in countries:
        if g.home_team == c.name and not home_country_found:
            c.record += [g]
            home_country_found = True
        if g.away_team == c.name and not away_country_found:
            c.record += [g]
            away_country_found = True
            
    if not home_country_found:
        a = Country(g.home_team)
        a.record += [g]
        countries += [a]
        
    if not away_country_found:
        a = Country(g.away_team)
        a.record += [g]
        countries += [a]
    
    
goal_team_analysis = 'Cuba'

for c in countries:
    if c.name == goal_team_analysis:
        mean_ppg = c.ppg()
        print(mean_ppg)
        for current_game in c.record:
            if c.name == current_game.home_team:
                print(current_game.away_team + ": " + str(current_game.home_score - mean_ppg))
            else:
                print(current_game.home_team + ": " + str(current_game.away_score - mean_ppg))
        break
    
    
            

