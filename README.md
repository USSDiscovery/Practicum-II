# Practicum-II

### NCAA Men's Basketball Game Winning Prediction

Basketball is a sport that involves 10 players on a hardwood surface at one time. In the college game, 5 players from each team attempt to get a ball in a basket while trying to prevent the other team from doing so. In college, the basketball court is 94 feet long and 50 feet wide. The basketball hoop is 10 feet above the ground with a 6 foot wide, 42 inch tall backboard. The basketball rim is 18 inches in diameter. There are five positions in basketball. There is the guard, shooting guard, small forward, forward, and center positions. These positions are also referred to as positions 1 through 5. Usually the 1 (guard) position is the shortest player on the team, and best ball handler. The 1 usually handles the ball the most and runs the teams offense. Positions 4 and 5 are usually the tallest players on the team and collect the most rebounds.

The above is an oversimplification of the game as a team is made up of approximately 15 players, at varying positions, with varying skills, making varying contributions to the game. Every year, hundreds of Men's college basketball teams play at least 25 games in a season. As one can imagine, the playing of these games creates a multitude of stats that can be analyzed. The objective of this experiment is to determine, with what accuracy, a machine learning model can predict a win or a loss between two Men's NCAA basketball teams given historical measures. This experiment will be broken as follows:

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Model Building (Decision Tree, Random Forest, K Nearest Neighbors, Support Vector Machines, Artificial Neural Networks)
5. Model Analysis
6. Summary

#### Data Collection

All data has been gathered from the NCAA Men's Basketball Archived Statistics website

![alt tag](Images/Basketball-Archived-Statistics.png "Basketball Archived Statistics")

There are 3 divisions in Men's NCAA Basketball. These division and there respective teams are illustrated below:

### Division 1 - 353 Teams

![alt tag](Images/Division-I.png "Division 1")

### Division 2 - 309 Teams

![alt tag](Images/Division-II.png "Division 2")

### Division 3 - 427 Teams

![alt tag](Images/Division-III.png "Division 3")

The initial thought was to simply download the needed statistics from the NCAA Statistics website. However, upon further investigation, it was determined that this would not yield a statistical dataset rich enough with predictors. As a result, Python along with the BeautifulSoup library is used to scrape the website. Scraping the website allows for the collection of a dataset rich with predictors. It also allows for the data to be cleansed as it is collected and in a preferable, comma-separated, format. The BeautifulSoup library allows for quick data extraction from a nested HTML data structure through code. The data extraction is broken down into Team Statistics, Team Results, and Player Statistics.

### Team statistics

![alt tag](Images/Team-Statistics.png "Team Statistics")

From the initial Division page above, each team is iterated through, using Python and BeautifulSoup, and it's team's statistics are recorded to a file. The following is the Team Statistics file header as extracted from code:

header = 'year_id' + delimiter +\
         'year_nm' + delimiter +\
         'team_id' + delimiter +\
         'team_nm' + delimiter +\
         'division' + delimiter +\
         'scoring_offense_rank' + delimiter +\
         'scoring_offense_value' + delimiter +\
         'scoring_defence_rank' + delimiter +\
         'scoring_defence_value' + delimiter +\
         'scoring_margin_rank' + delimiter +\
         'scoring_margin_value' + delimiter +\
         'rebound_margin_rank' + delimiter +\
         'rebound_margin_value' + delimiter +\
         'assists_per_game_rank' + delimiter +\
         'assists_per_game_value' + delimiter +\
         'blocked_shots_per_game_rank' + delimiter +\
         'blocked_shots_per_game_value' + delimiter +\
         'steals_per_game_rank' + delimiter +\
         'steals_per_game_value' + delimiter +\
         'turnover_margin_rank' + delimiter +\
         'turnover_margin_value' + delimiter +\
         'assist_turnover_ratio_rank' + delimiter +\
         'assist_turnover_ratio_value' + delimiter +\
         'field_goal_per_rank' + delimiter +\
         'field_goal_per_value' + delimiter +\
         'field_goal_per_defense_rank' + delimiter +\
         'field_goal_per_defense_value' + delimiter +\
         'three_pt_field_goals_per_rank' + delimiter +\
         'three_pt_field_goals_per_value' + delimiter +\
         'three_pt_field_goal_per_rank' + delimiter +\
         'three_pt_field_goal_per_value' + delimiter +\
         'free_throw_per_rank' + delimiter +\
         'free_throw_per_value' + delimiter +\
         'won_lost_per_rank' + delimiter +\
         'won_lost_per_value'

### Team Results

![alt tag](Images/Team-Results.png "Team Results")

As the Python code iterates through teams, each team's results are recorded to a file. The following is the Team Results file header as extracted from code:

headerResults = 'year_id' + delimiter +\
                'year_nm' + delimiter +\
                'team_id' + delimiter +\
                'team_nm' + delimiter +\
                'division' + delimiter +\
                'date' + delimiter +\
                'opposing_team_id' + delimiter +\
                'opposing_team_nm' + delimiter +\
                'home_or_away' + delimiter +\
                'overtime' + delimiter +\
                'result' + delimiter +\
                'team_score' + delimiter +\
                'opposing_team_score'

### Player Statistics

As the Python code iterates through teams, each team's player statistics are recorded to a file. The following is the Team Player Statistic's file header as extracted from code:

headerPlayerStatisticsPivot = 'year_id' + delimiter +\
                              'year_nm' + delimiter +\
                              'team_id' + delimiter +\
                              'team_nm' + delimiter +\
                              'division' + delimiter +\
                              'num_players' + delimiter +\
                              'jersey_01' + delimiter + \
                              'player_01' + delimiter + \
                              'year_01' + delimiter + \
                              'position_01' + delimiter + \
                              'height_01' + delimiter + \
                              'games_played_01' + delimiter + \
                              'games_started_01' + delimiter + \
                              'games_01' + delimiter + \
                              'minutes_played_01' + delimiter + \
                              'field_goals_made_01' + delimiter + \
                              'field_goals_attempted_01' + delimiter + \
                              'field_goal_percent_01' + delimiter + \
                              'three_point_01' + delimiter + \
                              'three_point_attempt_01' + delimiter + \
                              'three_point_percent_01' + delimiter + \
                              'free_throw_01' + delimiter + \
                              'free_throw_attempt_01' + delimiter + \
                              'free_throw_percent_01' + delimiter + \
                              'points_01' + delimiter + \
                              'average_01' + delimiter + \
                              'offensive_rebounds_01' + delimiter + \
                              'defensive_rebounds_01' + delimiter + \
                              'total_rebounds_01' + delimiter + \
                              'average_rebounds_01' + delimiter + \
                              'assists_01' + delimiter + \
                              'turn_overs_01' + delimiter + \
                              'steals_01' + delimiter + \
                              'blocked_shots_01' + delimiter + \
                              'fouls_01' + delimiter + \
                              'double_double_01' + delimiter + \
                              'triple_double_01' + delimiter + \
                              'disqualify_01' + delimiter +\

#### Data Cleansing

Teams have a varied number of players on their roster. Some team have 12 players while other teams have 17 players. Within this dataset, each team will be represented by 15 players. The above header portion represents 1 of the 15 players on a teams roster. If a team has less then 15 players, the missing players will be populated with zero stats. This will ensure that each roster is uniform. The model will decide if a team gets penalized for having less then 15 players on its roster. A team's roster can be made up of a different combination of positions. For example, a team can carry 10 guards and 5 forwards or 10 forwards, 2 guards, and 3 centers. In order to give the model every opportunity to discover patterns in the data the players on a roster must be ordered. The players could be ordered by any number of attributes. For the purpose of this experiment, each roster's players are ordered by the number of field goals the player made. The stats at position '01' will belong to the player that made the most field goals. The stats at position '02' will belong to the player that made the second most field goals. This order is maintained all the way through the 15th player. The ordering of the players on a single record is handled by the Python web-scraping script.                             

The following is a snapshot of output taken from the Python web-scraping script. It represents the 'AM-CORPUS-CHRISTI' team results from 2018:

![alt tag](Images/Team-Results-Python.png "Team Results Python")

The following is a snapshot of output taken from the Python web-scraping script. It represents the 'AM-CORPUS-CHRISTI' player statistics from 2018:

![alt tag](Images/Player-Statistics-Python-Unsorted.png "Player Statistics Python Unsorted")

The following is a snapshot of output taken from the Python web-scraping script. It represents the 'AM-CORPUS-CHRISTI' sorted player statistics from 2018. Due to this roster only containing 13 players, it has been padded with 2 additional players with null stats:

![alt tag](Images/Player-Statistics-Python-Sorted.png "Player Statistics Python Sorted")

Lastly, the web-scraping script pivots the players to a single record maintaining order:

![alt tag](Images/Player-Statistics-Python-Sorted-Pivot.png "Player Statistics Python Sorted Pivot")

The Python script outputs three files. Additional data cleansing and bringing together 3 files to 1 file was done using an Oracle Cloud instance. This was used for its simplicity, power, and speed. Web scraping produced nulls for a small fraction of attributes. In addition, teams without at least 15 players on their roster were padded with null players. Oracle's data definition language was used to  default null columns to zero. Once the data was read into Oracle the three tables were joined by division, year, team in order to produce dataset records that contained team results, team statistics, and player statistics, again all on a single record. With cleansed data we can now move on to the next step.

#### Exploratory Data Analysis

The desktop, student, version of Tableau was chosen to explore this rich dataset full of basketball statistics. The dataset contains 247,933 records each with 966 variables from three divisions of Men's college basketball, spanning years 2010 to 2018.
