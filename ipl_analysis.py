import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
ipl = pd.read_csv('D:/CODES/DATASETS/matches.csv')

# Plot 1: Matches Won by Each Team
plt.figure(figsize=(10, 6))
teams = list(ipl['winner'].value_counts().keys())
matches = list(ipl['winner'].value_counts())
plt.barh(teams, matches, color='g')
plt.title('Matches Won by Each Team')
plt.xlabel('Matches')
plt.ylabel('Teams')
plt.xticks(np.arange(0, max(matches) + 10, step=10))  # Adjusted xticks
for i, v in enumerate(matches):
    plt.text(v, teams[i], str(v), va='center', fontsize=10)
plt.tight_layout()  # Prevent overlapping

# Plot 2: Wins by Batting First vs. Batting Second for Top 5 Teams
plt.figure(figsize=(12, 6))
batting_first_wins = ipl[ipl['win_by_runs'] > 0]['winner'].value_counts()
batting_second_wins = ipl[ipl['win_by_wickets'] > 0]['winner'].value_counts()
wins_df = pd.DataFrame({'Batting First Wins': batting_first_wins,
                        'Batting Second Wins': batting_second_wins}).fillna(0)
top_teams = wins_df.sum(axis=1).nlargest(5).index
top_teams_df = wins_df.loc[top_teams]
ax = top_teams_df.plot(kind='bar', figsize=(12, 6), color=['skyblue', 'orange'])
plt.xlabel("Teams", fontsize=12)
plt.ylabel("Number of Matches Won", fontsize=12)
plt.title("Top 5 Teams: Wins by Batting First vs. Batting Second", fontsize=14)
plt.xticks(rotation=30, fontsize=10)
plt.yticks(np.arange(0, 55, step=5),fontsize=10)
plt.legend(title="Win Type", fontsize=10, title_fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
for bar in ax.containers:
    ax.bar_label(bar, fmt='%d', fontsize=10, padding=3)
plt.tight_layout()

# Table: Match Result Counts
print('\nMatch Results:\n')
result_counts = ipl['result'].value_counts()
result_df = pd.DataFrame({'Result': result_counts.index, 'Count': result_counts.values})
print(result_df)

# Plot 3: Top 10 Players with Most Man of the Match Awards
plt.figure(figsize=(10, 5))
names = list(ipl['player_of_match'].value_counts()[:10].keys())
mom_awards = list(ipl['player_of_match'].value_counts()[:10])
plt.bar(names, mom_awards, color='r')
plt.title('Top 10 Players with Most M.O.M. Awards')
plt.xlabel("Player Names")
plt.ylabel("Count of M.O.M. Awards")
plt.xticks(rotation=45, fontsize=10)
plt.yticks(np.arange(0, max(mom_awards) + 5, step=2))
for i, v in enumerate(mom_awards):
    plt.text(i, v + 0.5, str(v), ha='center', fontsize=8)
plt.tight_layout()

# Table: Matches Played in Each City
print('\nMatches across different cities:\n')
city_counts = ipl['city'].value_counts()
city_matches = pd.DataFrame({'City': city_counts.index, 'Number of Matches': city_counts.values})
print(city_matches)

# Plot 4: Number of Matches in Each IPL Season
plt.figure(figsize=(10, 5))
season_counts = ipl['season'].value_counts().sort_index()
season_df = pd.DataFrame({'Season': season_counts.index, 'Number of Matches': season_counts.values})
plt.plot(season_df['Season'], season_df['Number of Matches'], marker='o', linestyle='-', color='b')
plt.xlabel('Season')
plt.ylabel('Number of Matches')
plt.title('Number of Matches in Each IPL Season')
plt.yticks(np.arange(50, max(season_df['Number of Matches']) + 10, step=5))
plt.xticks(season_df['Season'], rotation=45)
plt.grid(True)
for i, txt in enumerate(season_df['Number of Matches']):
    plt.text(season_df['Season'][i], txt + 1, str(txt), ha='center', fontsize=10)
plt.tight_layout()

# Plot 5: Toss Winner Winning Percentage
plt.figure(figsize=(6, 6))
toss_win_match_win = ipl[ipl['toss_winner'] == ipl['winner']].shape[0]
toss_win_match_loss = ipl.shape[0] - toss_win_match_win
plt.pie([toss_win_match_win, toss_win_match_loss], labels=["Toss Winner Won", "Toss Winner Lost"], autopct='%1.1f%%', colors=['lightgreen', 'red'])
plt.title("Winning Percentage of Toss Winners")
plt.tight_layout()

# Plot 6: Toss Decisions Over IPL Seasons
plt.figure(figsize=(12, 6))
toss_decisions = ipl.groupby(['season', 'toss_decision']).size().unstack()
ax = toss_decisions.plot(kind='bar', figsize=(12, 6), colormap='coolwarm')
plt.xlabel("Season")
plt.ylabel("Number of Tosses Won")
plt.title("Toss Decisions Over IPL Seasons")
plt.legend(title="Toss Decision")
plt.xticks(rotation=45)
for container in ax.containers:
    ax.bar_label(container, fmt='%d', label_type='edge', fontsize=10, color='black')
plt.tight_layout()

plt.show()
