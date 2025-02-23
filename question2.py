import pandas as pd
import matplotlib.pyplot as plt


# Load the datasets
df_games = pd.read_csv('data/football/clean/epl_games.csv')
df_teams = pd.read_csv('data/football/clean/epl-teams-games.csv')

# Filter for the 2016 and 2017 seasons
df_games_1617 = df_games[(df_games['season'] == 2016) | (df_games['season'] == 2017)]

# Calculate home results
home_wins = (df_games_1617['points_home'] > df_games_1617['points_away']).sum()
home_draws = (df_games_1617['points_home'] == df_games_1617['points_away']).sum()
home_losses = (df_games_1617['points_home'] < df_games_1617['points_away']).sum()

# Away Results
away_wins = home_losses
away_draws = home_draws
away_losses = home_wins

# Calculate average goals scored and loss
home_goals_scored = df_games_1617['points_home'].mean()
home_goals_conceded = df_games_1617['points_away'].mean()
away_goals_scored = df_games_1617['points_away'].mean()
away_goals_conceded = df_games_1617['points_home'].mean()

# Calculate points earned at home vs away (3 for a win, 1 for a draw)
home_points = home_wins * 3 + home_draws
away_points = away_wins * 3 + away_draws

# Summary table
summary_stats = pd.DataFrame({
    'Metric': ['Wins', 'Draws', 'Losses', 'Avg Goals Scored', 'Avg Goals Conceded', 'Total Points'],
    'Home': [home_wins, home_draws, home_losses, home_goals_scored, home_goals_conceded, home_points],
    'Away': [away_wins, away_draws, away_losses, away_goals_scored, away_goals_conceded, away_points]
})

summary_stats.to_excel('results/question2_results/summary_statistics.xlsx')