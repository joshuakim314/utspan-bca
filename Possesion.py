import pandas as pd
from math import pi
import seaborn as sns
import matplotlib.pyplot as plt
import statistics

class Team:

    country = str

    def __init__(self, team_name):

        self.tendency = [[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]
        self.defense = [[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]
        self.country = team_name
        self.SA = {"Spot-Up":0, "Transition":1, "ISO":2, "Cut":3, "Post-Up":4, "P&R Ball Handler":5, "P&R Roll Man":6}
        self.Play = {"Miss 3 Pts":0, "Make 3 Pts":3, "Miss 2 Pts":0, "Make 2 Pts":2, "Foul":2}

    def scoring_action(self):

        for i in range(0,num_row):

            if data.iloc[i,6] == self.country and (data.iloc[i,5] in self.Play): #Was the country involved in a a scoring action
                tempstring = (data.iloc[i,10]).split(' > ') #Splice the scoring action
                for j in range (0,len(tempstring)): #Check scoring action appears, reverse to find most recent
                    if tempstring[len(tempstring)-(1+j)] in self.SA: #Should be changed to decrement
                        self.tendency[self.SA[tempstring[len(tempstring)-(1+j)]]][0] += 1
                        self.tendency[self.SA[tempstring[len(tempstring)-(1+j)]]][1] += self.Play[data.iloc[i,5]]
                        break

        return True

    def normalize_tendency(self):

        accum = 0
        for i in range (0,len(self.tendency)):
            accum = accum + self.tendency[i][0]
        for i in range (0,len(self.tendency)):
            self.tendency[i][1] = (self.tendency[i][1])/(self.tendency[i][0])
            self.tendency[i][1] = (self.tendency[i][1]) * 1000
            self.tendency[i][1] = int(self.tendency[i][1])
            self.tendency[i][1] = (self.tendency[i][1]) / 1000

            self.tendency[i][0] = self.tendency[i][0]/accum
            self.tendency[i][0] = (self.tendency[i][0]) * 1000
            self.tendency[i][0] = int(self.tendency[i][0])
            self.tendency[i][0] = (self.tendency[i][0]) / 1000

        return True

    def defense_action(self):

        for i in range(0, num_row):
            group = []
            other_group = []
            group.append(data.iloc[i, 3])
            group.append(data.iloc[i, 4])
            if group[0] == self.country:
                other_group = group[1]
            if group[1] == self.country:
                other_group = group[0]

            if data.iloc[i, 6] == other_group and (data.iloc[i, 5] in self.Play):  # Was the country involved in a a scoring action
                tempstring = (data.iloc[i, 10]).split(' > ')  # Splice the string
                for j in range (0,len(tempstring)): #Check scoring action appears, revers to find most recent
                    if tempstring[len(tempstring)-(1+j)] in self.SA:
                        if tempstring[len(tempstring) - (1 + j)] in self.SA:  # Should be changed to decrement
                            self.defense[self.SA[tempstring[len(tempstring) - (1 + j)]]][0] += 1
                            self.defense[self.SA[tempstring[len(tempstring) - (1 + j)]]][1] += self.Play[data.iloc[i, 5]]
                            break

        return True

    def normalize_defense(self):

        accum = 0
        for i in range (0,len(self.defense)):
            accum = accum + self.defense[i][0]
        for i in range (0,len(self.defense)):
            self.defense[i][1] = (self.defense[i][1])/(self.defense[i][0])
            self.defense[i][1] = (self.defense[i][1]) * 1000
            self.defense[i][1] = int(self.defense[i][1])
            self.defense[i][1] = (self.defense[i][1]) / 1000


            self.defense[i][0] = self.defense[i][0]/accum
            self.defense[i][0] = (self.defense[i][0]) * 1000
            self.defense[i][0] = int(self.defense[i][0])
            self.defense[i][0] = (self.defense[i][0]) / 1000


        return True







num_row = 196657 - 1    # -1 for the header row
excel_file = "Data.xlsx"
data = pd.read_excel(excel_file, encoding='latin-1')
teams = []
final_scores = pd.DataFrame()
previous_index = 0
counter = 0

USA = Team("USA")
USA.scoring_action()
USA.defense_action()
USA.normalize_tendency()
USA.normalize_defense()

df = pd.DataFrame({
    "group": ["Offense","Defense"],
    "Spot_Up": [USA.tendency[0][1],USA.defense[0][1]],
    "Transition": [USA.tendency[1][1],USA.defense[1][1]],
    "ISO": [USA.tendency[2][1],USA.defense[2][1]],
    "Cut": [USA.tendency[3][1],USA.defense[3][1]],
    "Post-Up": [USA.tendency[4][1],USA.defense[4][1]],
    "P&R Ball Handler": [USA.tendency[5][1],USA.defense[5][1]],
    "P&R Roll Man": [USA.tendency[6][1],USA.defense[6][1]]
})

# number of variable
categories = list(df)[1:]
N = len(categories)

# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:
values = df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
values

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the spider plot
ax = plt.subplot(111, polar=True)

# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories, color='grey', size=8)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([1,2], ["1", "2"], color="grey", size=7)
plt.ylim(0, 2)

# Plot data
ax.plot(angles, values, linewidth=1, linestyle='solid')

# Fill area
ax.fill(angles, values, 'b', alpha=0.1)

plt.show()

"""for i in range(0,num_row):
    if data.iloc[i, 6] not in teams:
        teams.append(data.iloc[i, 6])
print(teams)

print(teams[1])

A = Team(teams[1])

print(A.tendency)
print(A.country)"""

"""for i in range(0,(len(teams)-1)):
    J = Team(teams[i])
    J.scoring_action()
    J.defense_action()
    J.normalize_tendency()
    J.normalize_defense()
    print(J.country + " Scoring Tendencies: " + str(J.tendency))
    print(J.country + " Defense Tendencies: " + str(J.defense))"""






