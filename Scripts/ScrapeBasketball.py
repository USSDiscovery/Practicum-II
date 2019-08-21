import requests
import urllib.request
import time
import re
from bs4 import BeautifulSoup

delimiter = ','

na = ''

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

headerPlayerStatistics = 'year_id' + delimiter +\
                         'year_nm' + delimiter +\
                         'team_id' + delimiter +\
                         'team_nm' + delimiter +\
                         'division' + delimiter +\
                         'num_teams' + delimiter +\
                         'jersey' + delimiter +\
                         'player' + delimiter +\
                         'year' + delimiter +\
                         'position' + delimiter +\
                         'height' + delimiter +\
                         'games_played' + delimiter +\
                         'games_started' + delimiter +\
                         'games' + delimiter +\
                         'minutes_played' + delimiter +\
                         'field_goals_made' + delimiter +\
                         'field_goals_attempted' + delimiter +\
                         'field_goal_percent' + delimiter +\
                         'three_point' + delimiter +\
                         'three_point_attempt' + delimiter +\
                         'three_point_percent' + delimiter +\
                         'free_throw' + delimiter +\
                         'free_throw_attempt' + delimiter +\
                         'free_throw_percent' + delimiter +\
                         'points' + delimiter +\
                         'average' + delimiter +\
                         'offensive_rebounds' + delimiter +\
                         'defensive_rebounds' + delimiter +\
                         'total_rebounds' + delimiter +\
                         'average_rebounds' + delimiter +\
                         'assists' + delimiter +\
                         'turn_overs' + delimiter +\
                         'steals' + delimiter +\
                         'blocked_shots' + delimiter +\
                         'fouls' + delimiter +\
                         'double_double' + delimiter +\
                         'triple_double' + delimiter +\
                         'disqualify'

headerPlayerStatisticsPivot = \
'year_id' + delimiter +\
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
'jersey_02' + delimiter + \
'player_02' + delimiter + \
'year_02' + delimiter + \
'position_02' + delimiter + \
'height_02' + delimiter + \
'games_played_02' + delimiter + \
'games_started_02' + delimiter + \
'games_02' + delimiter + \
'minutes_played_02' + delimiter + \
'field_goals_made_02' + delimiter + \
'field_goals_attempted_02' + delimiter + \
'field_goal_percent_02' + delimiter + \
'three_point_02' + delimiter + \
'three_point_attempt_02' + delimiter + \
'three_point_percent_02' + delimiter + \
'free_throw_02' + delimiter + \
'free_throw_attempt_02' + delimiter + \
'free_throw_percent_02' + delimiter + \
'points_02' + delimiter + \
'average_02' + delimiter + \
'offensive_rebounds_02' + delimiter + \
'defensive_rebounds_02' + delimiter + \
'total_rebounds_02' + delimiter + \
'average_rebounds_02' + delimiter + \
'assists_02' + delimiter + \
'turn_overs_02' + delimiter + \
'steals_02' + delimiter + \
'blocked_shots_02' + delimiter + \
'fouls_02' + delimiter + \
'double_double_02' + delimiter + \
'triple_double_02' + delimiter + \
'disqualify_02' + delimiter +\
'jersey_03' + delimiter + \
'player_03' + delimiter + \
'year_03' + delimiter + \
'position_03' + delimiter + \
'height_03' + delimiter + \
'games_played_03' + delimiter + \
'games_started_03' + delimiter + \
'games_03' + delimiter + \
'minutes_played_03' + delimiter + \
'field_goals_made_03' + delimiter + \
'field_goals_attempted_03' + delimiter + \
'field_goal_percent_03' + delimiter + \
'three_point_03' + delimiter + \
'three_point_attempt_03' + delimiter + \
'three_point_percent_03' + delimiter + \
'free_throw_03' + delimiter + \
'free_throw_attempt_03' + delimiter + \
'free_throw_percent_03' + delimiter + \
'points_03' + delimiter + \
'average_03' + delimiter + \
'offensive_rebounds_03' + delimiter + \
'defensive_rebounds_03' + delimiter + \
'total_rebounds_03' + delimiter + \
'average_rebounds_03' + delimiter + \
'assists_03' + delimiter + \
'turn_overs_03' + delimiter + \
'steals_03' + delimiter + \
'blocked_shots_03' + delimiter + \
'fouls_03' + delimiter + \
'double_double_03' + delimiter + \
'triple_double_03' + delimiter + \
'disqualify_03' + delimiter +\
'jersey_04' + delimiter + \
'player_04' + delimiter + \
'year_04' + delimiter + \
'position_04' + delimiter + \
'height_04' + delimiter + \
'games_played_04' + delimiter + \
'games_started_04' + delimiter + \
'games_04' + delimiter + \
'minutes_played_04' + delimiter + \
'field_goals_made_04' + delimiter + \
'field_goals_attempted_04' + delimiter + \
'field_goal_percent_04' + delimiter + \
'three_point_04' + delimiter + \
'three_point_attempt_04' + delimiter + \
'three_point_percent_04' + delimiter + \
'free_throw_04' + delimiter + \
'free_throw_attempt_04' + delimiter + \
'free_throw_percent_04' + delimiter + \
'points_04' + delimiter + \
'average_04' + delimiter + \
'offensive_rebounds_04' + delimiter + \
'defensive_rebounds_04' + delimiter + \
'total_rebounds_04' + delimiter + \
'average_rebounds_04' + delimiter + \
'assists_04' + delimiter + \
'turn_overs_04' + delimiter + \
'steals_04' + delimiter + \
'blocked_shots_04' + delimiter + \
'fouls_04' + delimiter + \
'double_double_04' + delimiter + \
'triple_double_04' + delimiter + \
'disqualify_04' + delimiter +\
'jersey_05' + delimiter + \
'player_05' + delimiter + \
'year_05' + delimiter + \
'position_05' + delimiter + \
'height_05' + delimiter + \
'games_played_05' + delimiter + \
'games_started_05' + delimiter + \
'games_05' + delimiter + \
'minutes_played_05' + delimiter + \
'field_goals_made_05' + delimiter + \
'field_goals_attempted_05' + delimiter + \
'field_goal_percent_05' + delimiter + \
'three_point_05' + delimiter + \
'three_point_attempt_05' + delimiter + \
'three_point_percent_05' + delimiter + \
'free_throw_05' + delimiter + \
'free_throw_attempt_05' + delimiter + \
'free_throw_percent_05' + delimiter + \
'points_05' + delimiter + \
'average_05' + delimiter + \
'offensive_rebounds_05' + delimiter + \
'defensive_rebounds_05' + delimiter + \
'total_rebounds_05' + delimiter + \
'average_rebounds_05' + delimiter + \
'assists_05' + delimiter + \
'turn_overs_05' + delimiter + \
'steals_05' + delimiter + \
'blocked_shots_05' + delimiter + \
'fouls_05' + delimiter + \
'double_double_05' + delimiter + \
'triple_double_05' + delimiter + \
'disqualify_05' + delimiter +\
'jersey_06' + delimiter + \
'player_06' + delimiter + \
'year_06' + delimiter + \
'position_06' + delimiter + \
'height_06' + delimiter + \
'games_played_06' + delimiter + \
'games_started_06' + delimiter + \
'games_06' + delimiter + \
'minutes_played_06' + delimiter + \
'field_goals_made_06' + delimiter + \
'field_goals_attempted_06' + delimiter + \
'field_goal_percent_06' + delimiter + \
'three_point_06' + delimiter + \
'three_point_attempt_06' + delimiter + \
'three_point_percent_06' + delimiter + \
'free_throw_06' + delimiter + \
'free_throw_attempt_06' + delimiter + \
'free_throw_percent_06' + delimiter + \
'points_06' + delimiter + \
'average_06' + delimiter + \
'offensive_rebounds_06' + delimiter + \
'defensive_rebounds_06' + delimiter + \
'total_rebounds_06' + delimiter + \
'average_rebounds_06' + delimiter + \
'assists_06' + delimiter + \
'turn_overs_06' + delimiter + \
'steals_06' + delimiter + \
'blocked_shots_06' + delimiter + \
'fouls_06' + delimiter + \
'double_double_06' + delimiter + \
'triple_double_06' + delimiter + \
'disqualify_06' + delimiter +\
'jersey_07' + delimiter + \
'player_07' + delimiter + \
'year_07' + delimiter + \
'position_07' + delimiter + \
'height_07' + delimiter + \
'games_played_07' + delimiter + \
'games_started_07' + delimiter + \
'games_07' + delimiter + \
'minutes_played_07' + delimiter + \
'field_goals_made_07' + delimiter + \
'field_goals_attempted_07' + delimiter + \
'field_goal_percent_07' + delimiter + \
'three_point_07' + delimiter + \
'three_point_attempt_07' + delimiter + \
'three_point_percent_07' + delimiter + \
'free_throw_07' + delimiter + \
'free_throw_attempt_07' + delimiter + \
'free_throw_percent_07' + delimiter + \
'points_07' + delimiter + \
'average_07' + delimiter + \
'offensive_rebounds_07' + delimiter + \
'defensive_rebounds_07' + delimiter + \
'total_rebounds_07' + delimiter + \
'average_rebounds_07' + delimiter + \
'assists_07' + delimiter + \
'turn_overs_07' + delimiter + \
'steals_07' + delimiter + \
'blocked_shots_07' + delimiter + \
'fouls_07' + delimiter + \
'double_double_07' + delimiter + \
'triple_double_07' + delimiter + \
'disqualify_07' + delimiter +\
'jersey_08' + delimiter + \
'player_08' + delimiter + \
'year_08' + delimiter + \
'position_08' + delimiter + \
'height_08' + delimiter + \
'games_played_08' + delimiter + \
'games_started_08' + delimiter + \
'games_08' + delimiter + \
'minutes_played_08' + delimiter + \
'field_goals_made_08' + delimiter + \
'field_goals_attempted_08' + delimiter + \
'field_goal_percent_08' + delimiter + \
'three_point_08' + delimiter + \
'three_point_attempt_08' + delimiter + \
'three_point_percent_08' + delimiter + \
'free_throw_08' + delimiter + \
'free_throw_attempt_08' + delimiter + \
'free_throw_percent_08' + delimiter + \
'points_08' + delimiter + \
'average_08' + delimiter + \
'offensive_rebounds_08' + delimiter + \
'defensive_rebounds_08' + delimiter + \
'total_rebounds_08' + delimiter + \
'average_rebounds_08' + delimiter + \
'assists_08' + delimiter + \
'turn_overs_08' + delimiter + \
'steals_08' + delimiter + \
'blocked_shots_08' + delimiter + \
'fouls_08' + delimiter + \
'double_double_08' + delimiter + \
'triple_double_08' + delimiter + \
'disqualify_08' + delimiter +\
'jersey_09' + delimiter + \
'player_09' + delimiter + \
'year_09' + delimiter + \
'position_09' + delimiter + \
'height_09' + delimiter + \
'games_played_09' + delimiter + \
'games_started_09' + delimiter + \
'games_09' + delimiter + \
'minutes_played_09' + delimiter + \
'field_goals_made_09' + delimiter + \
'field_goals_attempted_09' + delimiter + \
'field_goal_percent_09' + delimiter + \
'three_point_09' + delimiter + \
'three_point_attempt_09' + delimiter + \
'three_point_percent_09' + delimiter + \
'free_throw_09' + delimiter + \
'free_throw_attempt_09' + delimiter + \
'free_throw_percent_09' + delimiter + \
'points_09' + delimiter + \
'average_09' + delimiter + \
'offensive_rebounds_09' + delimiter + \
'defensive_rebounds_09' + delimiter + \
'total_rebounds_09' + delimiter + \
'average_rebounds_09' + delimiter + \
'assists_09' + delimiter + \
'turn_overs_09' + delimiter + \
'steals_09' + delimiter + \
'blocked_shots_09' + delimiter + \
'fouls_09' + delimiter + \
'double_double_09' + delimiter + \
'triple_double_09' + delimiter + \
'disqualify_09' + delimiter +\
'jersey_10' + delimiter + \
'player_10' + delimiter + \
'year_10' + delimiter + \
'position_10' + delimiter + \
'height_10' + delimiter + \
'games_played_10' + delimiter + \
'games_started_10' + delimiter + \
'games_10' + delimiter + \
'minutes_played_10' + delimiter + \
'field_goals_made_10' + delimiter + \
'field_goals_attempted_10' + delimiter + \
'field_goal_percent_10' + delimiter + \
'three_point_10' + delimiter + \
'three_point_attempt_10' + delimiter + \
'three_point_percent_10' + delimiter + \
'free_throw_10' + delimiter + \
'free_throw_attempt_10' + delimiter + \
'free_throw_percent_10' + delimiter + \
'points_10' + delimiter + \
'average_10' + delimiter + \
'offensive_rebounds_10' + delimiter + \
'defensive_rebounds_10' + delimiter + \
'total_rebounds_10' + delimiter + \
'average_rebounds_10' + delimiter + \
'assists_10' + delimiter + \
'turn_overs_10' + delimiter + \
'steals_10' + delimiter + \
'blocked_shots_10' + delimiter + \
'fouls_10' + delimiter + \
'double_double_10' + delimiter + \
'triple_double_10' + delimiter + \
'disqualify_10' + delimiter +\
'jersey_11' + delimiter + \
'player_11' + delimiter + \
'year_11' + delimiter + \
'position_11' + delimiter + \
'height_11' + delimiter + \
'games_played_11' + delimiter + \
'games_started_11' + delimiter + \
'games_11' + delimiter + \
'minutes_played_11' + delimiter + \
'field_goals_made_11' + delimiter + \
'field_goals_attempted_11' + delimiter + \
'field_goal_percent_11' + delimiter + \
'three_point_11' + delimiter + \
'three_point_attempt_11' + delimiter + \
'three_point_percent_11' + delimiter + \
'free_throw_11' + delimiter + \
'free_throw_attempt_11' + delimiter + \
'free_throw_percent_11' + delimiter + \
'points_11' + delimiter + \
'average_11' + delimiter + \
'offensive_rebounds_11' + delimiter + \
'defensive_rebounds_11' + delimiter + \
'total_rebounds_11' + delimiter + \
'average_rebounds_11' + delimiter + \
'assists_11' + delimiter + \
'turn_overs_11' + delimiter + \
'steals_11' + delimiter + \
'blocked_shots_11' + delimiter + \
'fouls_11' + delimiter + \
'double_double_11' + delimiter + \
'triple_double_11' + delimiter + \
'disqualify_11' + delimiter +\
'jersey_12' + delimiter + \
'player_12' + delimiter + \
'year_12' + delimiter + \
'position_12' + delimiter + \
'height_12' + delimiter + \
'games_played_12' + delimiter + \
'games_started_12' + delimiter + \
'games_12' + delimiter + \
'minutes_played_12' + delimiter + \
'field_goals_made_12' + delimiter + \
'field_goals_attempted_12' + delimiter + \
'field_goal_percent_12' + delimiter + \
'three_point_12' + delimiter + \
'three_point_attempt_12' + delimiter + \
'three_point_percent_12' + delimiter + \
'free_throw_12' + delimiter + \
'free_throw_attempt_12' + delimiter + \
'free_throw_percent_12' + delimiter + \
'points_12' + delimiter + \
'average_12' + delimiter + \
'offensive_rebounds_12' + delimiter + \
'defensive_rebounds_12' + delimiter + \
'total_rebounds_12' + delimiter + \
'average_rebounds_12' + delimiter + \
'assists_12' + delimiter + \
'turn_overs_12' + delimiter + \
'steals_12' + delimiter + \
'blocked_shots_12' + delimiter + \
'fouls_12' + delimiter + \
'double_double_12' + delimiter + \
'triple_double_12' + delimiter + \
'disqualify_12' + delimiter +\
'jersey_13' + delimiter + \
'player_13' + delimiter + \
'year_13' + delimiter + \
'position_13' + delimiter + \
'height_13' + delimiter + \
'games_played_13' + delimiter + \
'games_started_13' + delimiter + \
'games_13' + delimiter + \
'minutes_played_13' + delimiter + \
'field_goals_made_13' + delimiter + \
'field_goals_attempted_13' + delimiter + \
'field_goal_percent_13' + delimiter + \
'three_point_13' + delimiter + \
'three_point_attempt_13' + delimiter + \
'three_point_percent_13' + delimiter + \
'free_throw_13' + delimiter + \
'free_throw_attempt_13' + delimiter + \
'free_throw_percent_13' + delimiter + \
'points_13' + delimiter + \
'average_13' + delimiter + \
'offensive_rebounds_13' + delimiter + \
'defensive_rebounds_13' + delimiter + \
'total_rebounds_13' + delimiter + \
'average_rebounds_13' + delimiter + \
'assists_13' + delimiter + \
'turn_overs_13' + delimiter + \
'steals_13' + delimiter + \
'blocked_shots_13' + delimiter + \
'fouls_13' + delimiter + \
'double_double_13' + delimiter + \
'triple_double_13' + delimiter + \
'disqualify_13' + delimiter +\
'jersey_14' + delimiter + \
'player_14' + delimiter + \
'year_14' + delimiter + \
'position_14' + delimiter + \
'height_14' + delimiter + \
'games_played_14' + delimiter + \
'games_started_14' + delimiter + \
'games_14' + delimiter + \
'minutes_played_14' + delimiter + \
'field_goals_made_14' + delimiter + \
'field_goals_attempted_14' + delimiter + \
'field_goal_percent_14' + delimiter + \
'three_point_14' + delimiter + \
'three_point_attempt_14' + delimiter + \
'three_point_percent_14' + delimiter + \
'free_throw_14' + delimiter + \
'free_throw_attempt_14' + delimiter + \
'free_throw_percent_14' + delimiter + \
'points_14' + delimiter + \
'average_14' + delimiter + \
'offensive_rebounds_14' + delimiter + \
'defensive_rebounds_14' + delimiter + \
'total_rebounds_14' + delimiter + \
'average_rebounds_14' + delimiter + \
'assists_14' + delimiter + \
'turn_overs_14' + delimiter + \
'steals_14' + delimiter + \
'blocked_shots_14' + delimiter + \
'fouls_14' + delimiter + \
'double_double_14' + delimiter + \
'triple_double_14' + delimiter + \
'disqualify_14' + delimiter +\
'jersey_15' + delimiter + \
'player_15' + delimiter + \
'year_15' + delimiter + \
'position_15' + delimiter + \
'height_15' + delimiter + \
'games_played_15' + delimiter + \
'games_started_15' + delimiter + \
'games_15' + delimiter + \
'minutes_played_15' + delimiter + \
'field_goals_made_15' + delimiter + \
'field_goals_attempted_15' + delimiter + \
'field_goal_percent_15' + delimiter + \
'three_point_15' + delimiter + \
'three_point_attempt_15' + delimiter + \
'three_point_percent_15' + delimiter + \
'free_throw_15' + delimiter + \
'free_throw_attempt_15' + delimiter + \
'free_throw_percent_15' + delimiter + \
'points_15' + delimiter + \
'average_15' + delimiter + \
'offensive_rebounds_15' + delimiter + \
'defensive_rebounds_15' + delimiter + \
'total_rebounds_15' + delimiter + \
'average_rebounds_15' + delimiter + \
'assists_15' + delimiter + \
'turn_overs_15' + delimiter + \
'steals_15' + delimiter + \
'blocked_shots_15' + delimiter + \
'fouls_15' + delimiter + \
'double_double_15' + delimiter + \
'triple_double_15' + delimiter + \
'disqualify_15'

def scrapeStat(stat, statsarray):

    if len(stat) >= 3:

        if stat[0].get_text() == 'Scoring Offense':

            statsarray[0][0] = stat[1].get_text().strip()

            statsarray[0][1] = stat[2].get_text().strip()

        elif stat[0].get_text() == 'Scoring Defense':

            statsarray[1][0] = stat[1].get_text().strip()

            statsarray[1][1] = stat[2].get_text().strip()

        elif stat[0].get_text() == 'Scoring Margin':

            statsarray[2][0] = stat[1].get_text().strip()

            statsarray[2][1] = stat[2].get_text().strip()

        elif stat[0].get_text() == 'Rebound Margin':

            statsarray[3][0] = stat[1].get_text().strip()

            statsarray[3][1] = stat[2].get_text().strip()

        elif stat[0].get_text() == 'Assists Per Game':

            statsarray[4][0] = stat[1].get_text().strip()

            statsarray[4][1] = stat[2].get_text().strip()

        elif stat[0].get_text() == 'Blocked Shots Per Game':


            statsarray[5][0] = stat[1].get_text().strip()

            statsarray[5][1] = stat[2].get_text().strip()

        elif stat[0].get_text() == 'Steals Per Game':

            statsarray[6][0] = stat[1].get_text().strip()

            statsarray[6][1] = stat[2].get_text().strip()

        elif stat[0].get_text() == 'Turnover Margin':

            statsarray[7][0] = stat[1].get_text().strip()

            statsarray[7][1] = stat[2].get_text().strip()

        elif stat[0].get_text() == 'Assist Turnover Ratio':

            statsarray[8][0] = stat[1].get_text().strip()

            statsarray[8][1] = stat[2].get_text().strip()

        elif stat[0].get_text() == 'Field-Goal Percentage':

            statsarray[9][0] = stat[1].get_text().strip()

            statsarray[9][1] = stat[2].get_text().strip()

        elif stat[0].get_text() == 'Field-Goal Percentage Defense':

            statsarray[10][0] = stat[1].get_text().strip()

            statsarray[10][1] = stat[2].get_text().strip()

        elif stat[0].get_text() == 'Three-Point Field Goals Per Game':

            statsarray[11][0] = stat[1].get_text().strip()

            statsarray[11][1] = stat[2].get_text().strip()

        elif stat[0].get_text() == 'Three-Point Field-Goal Percentage':

            statsarray[12][0] = stat[1].get_text().strip()

            statsarray[12][1] = stat[2].get_text().strip()

        elif stat[0].get_text() == 'Free-Throw Percentage':

            statsarray[13][0] = stat[1].get_text().strip()

            statsarray[13][1] = stat[2].get_text().strip()

        elif stat[0].get_text() == 'Won-Lost Percentage':

            statsarray[14][0] = stat[1].get_text().strip()

            statsarray[14][1] = stat[2].get_text().strip()

    return statsarray

def scrapeTeamResults(tr_fh, year_id, year_nm, team_id, college, division, tableResults):

    borderTable = list(tableResults.children)[3]


    resultsBody = list(borderTable.children)[3]

    # Step through results

    resultTR = resultsBody.findAll('tr')


    for i in range(0, len(list(resultTR)), 2):

        results = year_id + delimiter + year_nm[:4] + delimiter + team_id + delimiter + college + delimiter + str(division) + delimiter

        resultTD = resultTR[i].findAll('td')

        if (len(list(resultTD)) == 3):

            for j in range(0, len(list(resultTD))):

                # Get Data

                resultTData = resultTD[j]

                if j == 0:

                    resultDate = ''

                    resultDate = resultTData.get_text()

                    resultDate = resultDate.split('/')

                    resultDate = resultDate[2] + resultDate[0] + resultDate[1]

                    results = results + resultDate

                if j == 1:

                    resultTeamID = ''

                    resultBR = ''

                    resultTeamID = resultTData.findAll('a')

                    # Code for missing a tag

                    if len(resultTeamID) > 0:

                        resultTeamName = resultTeamID[0].get_text()

                        resultTeamName = resultTeamName.strip()

                        if resultTeamName.find('#') > -1:

                            resultTeamName = resultTeamName[resultTeamName.find(' ') + 1:]

                        resultTeamName = resultTeamName.replace('&', '')

                        resultTeamName = resultTeamName.replace('&amp;', '')

                        resultTeamName = resultTeamName.replace(' ', '_')

                        resultTeamName = resultTeamName.replace('.', '')

                        resultTeamName = resultTeamName.replace('(', '')

                        resultTeamName = resultTeamName.replace(')', '')

                        resultTeamName = resultTeamName.replace('\'', '')

                        resultTeamName = resultTeamName.upper()

                        # resultTeamNameREG = re.compile(r'([A-Z]+[_]*[A-Z]*)*')

                        resultTeamID = resultTeamID[0]['href']

                        resultTeamID = resultTeamID.split('/')

                        resultTeamID = resultTeamID[2]

                        results = results + delimiter + resultTeamID + delimiter + resultTeamName

                        # 0 represents a home game 1 represents an away game

                        resultBR = str(resultTD[j]).find('@')

                        if resultBR == -1:

                            resultBR = 'HOME'

                        else:

                            resultBR = 'AWAY'

                        results = results + delimiter + resultBR

                    else:

                        resultTeamName = resultTData.get_text()

                        resultBR = resultTeamName.find('@')

                        if resultBR == -1:

                            resultBR = 'HOME'

                        else:

                            resultBR = 'AWAY'

                        resultTeamName = resultTeamName.split('@')

                        resultTeamName = resultTeamName[0]

                        resultTeamName = resultTeamName.strip()

                        resultTeamName = resultTeamName.replace('&', '')

                        resultTeamName = resultTeamName.replace('&amp;', '')

                        resultTeamName = resultTeamName.replace(' ', '_')

                        resultTeamName = resultTeamName.replace('.', '')

                        resultTeamName = resultTeamName.replace('(', '')

                        resultTeamName = resultTeamName.replace(')', '')

                        resultTeamName = resultTeamName.replace('\'', '')

                        resultTeamName = resultTeamName.upper()

                        if resultTeamName.find('#') > -1:

                            resultTeamName = resultTeamName[3:]

                        results = results + delimiter + '' + delimiter + resultTeamName + delimiter + resultBR

                if j == 2:

                    resultTDValue = ''

                    resultWL = []

                    resultScore = []

                    resultOvertime = []

                    resultTDValue = resultTData.findAll('a')

                    resultTDValue = resultTDValue[0].get_text()

                    resultWL = re.compile(r'[WL]')

                    resultWL = resultWL.findall(resultTDValue)[0]

                    resultScore = re.compile(r'\d+-\d+')

                    resultScore = resultScore.findall(resultTDValue)[0]

                    resultScore = resultScore.split('-')

                    resultScoreTeam = resultScore[0]

                    resultScoreTeamOppose = resultScore[1]

                    resultOvertime = re.compile(r'OT')

                    if len(resultOvertime.findall(resultTDValue)) > 0:

                        resultOvertime = resultOvertime.findall(resultTDValue)[0]

                        if resultOvertime == 'OT':

                            resultOvertime = 1

                        else:

                            resultOvertime = 0

                    else:

                        resultOvertime = 0

                    results = results + delimiter + str(resultOvertime) + delimiter + resultWL + delimiter + resultScoreTeam + delimiter + resultScoreTeamOppose

        print(results)

        tr_fh.write(str(results) + '\n')

def sortPlayerStatistics(pss_fh, pssp_fh, year_id, year_nm, team_id, college, division, playerLists):

    # The following will be used to ensure at least 15 roster spots per team

    defaultPlayerList = [str(year_id), str(year_nm[:4]), str(team_id), college, str(division), '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

    for i in range(len(playerLists), 15):

        playerLists.append(defaultPlayerList)

    # Sort player list

    playerLists = sorted(playerLists, key = lambda x: int(x[15] or 0), reverse = True)

    print(playerLists)

    # Pivot roster to single line

    playerListsLinePivot = ''

    # Take first 15 roster spots

    for i in range(0, 15):

        playerListsLine = ''

        # The following line will be for the pivot line header on the first record

        playerListsLineHeader = ''

        for j in range(0, len(playerLists[i])):

            if j == 0:

                playerListsLine = playerListsLine + playerLists[i][j]

            else:

                playerListsLine = playerListsLine + delimiter + playerLists[i][j]

            # Build line with header

            if i == 0:

                if j == 0:

                    playerListsLineHeader = playerListsLineHeader + playerLists[i][j]

                else:

                    playerListsLineHeader = playerListsLineHeader + delimiter + playerLists[i][j]

            else:

                if j == 6:
                    playerListsLineHeader = playerListsLineHeader + playerLists[i][j]

                elif j > 6:

                    playerListsLineHeader = playerListsLineHeader + delimiter + playerLists[i][j]

        print(playerListsLine)

        pss_fh.write(playerListsLine + '\n')

        if i == 0:

            playerListsLinePivot = playerListsLinePivot + playerListsLineHeader

        else:

            playerListsLinePivot = playerListsLinePivot + delimiter + playerListsLineHeader

    print(playerListsLinePivot)

    pssp_fh.write(playerListsLinePivot + '\n')

def buildPlayerStatsLine(headerIndexDict):

    playerStatsLine = ''

    # print(headerIndexDict)

    for j in range(1, 33):

        if j == 1:

            playerStatsLine = playerStatsLine + headerIndexDict.get('Jersey', na)

        elif j == 2:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('Player', na)

        elif j == 3:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('Yr', na)

        elif j == 4:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('Pos', na)

        elif j == 5:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('Ht', na)

        elif j == 6:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('GP', na)

        elif j == 7:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('GS', na)

        elif j == 8:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('G', na)

        elif j == 9:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('MP', na)

        elif j == 10:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('FGM', na)

        elif j == 11:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('FGA', na)

        elif j == 12:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('FG%', na)

        elif j == 13:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('3FG', na)

        elif j == 14:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('3FGA', na)

        elif j == 15:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('3FG%', na)

        elif j == 16:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('FT', na)

        elif j == 17:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('FTA', na)

        elif j == 18:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('FT%', na)

        elif j == 19:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('PTS', na)

        elif j == 20:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('Avg', na)

        elif j == 21:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('ORebs', na)

        elif j == 22:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('DRebs', na)

        elif j == 23:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('Tot Reb', na)

        elif j == 24:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('Avg_R', na)

        elif j == 25:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('AST', na)

        elif j == 26:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('TO', na)

        elif j == 27:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('STL', na)

        elif j == 28:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('BLK', na)

        elif j == 29:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('Fouls', na)

        elif j == 30:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('Dbl Dbl', na)

        elif j == 31:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('Trpl Dbl', na)

        elif j == 32:

            playerStatsLine = playerStatsLine + delimiter + headerIndexDict.get('DQ', na)

    return playerStatsLine

def scrapePlayerStatistics(ps_fh, pss_fh, pssp_fh, year_id, year_nm, team_id, college, division, rosterDataLink):

    playerLists = []

    url = 'https://stats.ncaa.org' + rosterDataLink

    # print(url)

    response = requests.get(url)

    playerStatistics = BeautifulSoup(response.text, 'html.parser')

    html = list(playerStatistics.children)[2]

    # print(html)

    head = list(html.children)[1]

    # print(head)

    body = list(html.children)[5]

    # print(body)

    div = list(body.children)[3]

    # print(div)

    # Check if player statistics available

    if len(div) >= 25:

        fieldset = list(div.children)[25]

        # print(fieldset)

        fieldsetDiv = list(fieldset.children)[7]

        # print(fieldsetDiv)

        fieldsetDivHeader = list(fieldsetDiv.children)[1]

        # print(fieldsetDivHeader)

        fieldsetDivHeaderThread = list(fieldsetDivHeader)[1]

        # print(fieldsetDivHeaderThread)

        th = fieldsetDivHeaderThread.findAll('th')

        fieldsetDivForm = list(fieldsetDiv.children)[3]

        # print(fieldsetDivForm)

        tr = fieldsetDivForm.findAll('tr')

        # print(tr)

        # print(len(tr))

        for i in range(0, len(tr)):

            # print(tr[i])

            # Roster Number

            headerIndex = []

            for l in range(0, len(th)):

                headerIndexText = th[l].get_text()

                if headerIndexText == 'MIN':

                    headerIndex.append('MP')

                elif headerIndexText == 'Avg' and l >= 21:

                    headerIndex.append('Avg_R')

                else:

                    headerIndex.append(headerIndexText)

            # print(headerIndex)

            playerStatsLine = year_id + delimiter + year_nm[:4] + delimiter + team_id + delimiter + college + delimiter + str(division) + delimiter + str(len(tr))

            td = tr[i].findAll('td')

            # print(td)

            for j in range(0, len(td)):

                stat = td[j].get_text()

                stat = stat.strip()

                stat = stat.replace(',', '')

                # Convert hours minutes to decimal

                stat = stat.replace(':', '.')

                # Convert height to inches

                if j == 4:

                    resultHT = stat.find('-')

                    if resultHT != -1:

                        stat = stat.split('-')

                        if stat[0] == '':

                            stat = ''

                        else:

                            stat = str((int(stat[0]) * 12) + int(stat[1]))

                headerIndex[j] = tuple([headerIndex[j], stat.strip()])

                # print(headerIndex[j])

            # print(headerIndex)

            headerIndexDict = dict(headerIndex)

            # print(headerIndexDict)

            playerStatsLine = playerStatsLine + delimiter + buildPlayerStatsLine(headerIndexDict)

            print(playerStatsLine)

            ps_fh.write(playerStatsLine + '\n')

            playerList = playerStatsLine.split(',')

            playerLists.append(playerList)

        sortPlayerStatistics(pss_fh, pssp_fh, year_id, year_nm, team_id, college, division, playerLists)

def scrapeTeamStatistics(ts_fh, tr_fh, ps_fh, pss_fh, pssp_fh, year_id, year_nm, team_id, college, division):

    statsArray = [['' for x in range(2)] for y in range(15)]

    url = 'https://stats.ncaa.org/teams/' + year_id + '?utf8=%E2%9C%93&year_id=' + year_id + '&sport_id=1&commit=Submit&org_sport_name=&org_id='

    response = requests.get(url)

    teamStatistics = BeautifulSoup(response.text, 'html.parser')

    # print(teamStatistics)

    html = list(teamStatistics.children)[2]

    # print(html)

    head = list(html.children)[1]

    # print(head)

    body = list(html.children)[5]

    # print(body)

    div = list(body.children)[3]

    # print(div)

    fieldset = list(div.children)[7]

    # print(fieldset)

    fieldsetDiv = list(fieldset.children)[3]

    # print(fieldsetDiv)

    fieldsetDivForm = list(fieldsetDiv.children)[1]

    # print(fieldsetDivForm)

    fieldsetDivFormSelect = list(fieldsetDivForm)[2]

    # print(fieldsetDivFormSelect)

    teamStatsLine = year_id + delimiter + year_nm[:4] + delimiter + team_id + delimiter + college + delimiter + str(division)

    try:
        table = list(div.children)[21]

        # print(table)

        tableBody = list(table.children)[3]

        # print(tableBody)

        tableBodyRecord = list(tableBody.children)[1]

        # print(tableBodyRecord)

        # Schedule - Results Data

        tableResults = list(tableBodyRecord)[1]

        scrapeTeamResults(tr_fh, year_id, year_nm, team_id, college, division, tableResults)

        # Team Stats Data

        tableData = list(tableBodyRecord)[3]

        # print(tableData)

        tableDataTable = list(tableData)[1]

        # print(tableDataTable)

        # Scoring Offense

        for i in range(5, len(list(tableDataTable)), 2):

            tableRecord = list(tableDataTable)[i]

            # print(tableRecord)

            stat = tableRecord.findAll('td')

            statsArray = scrapeStat(stat, statsArray)

        teamStatsLine = teamStatsLine +\
                        delimiter + statsArray[0][0].translate({ord(i):None for i in 'T-'}) + delimiter + statsArray[0][1] +\
                        delimiter + statsArray[1][0].translate({ord(i):None for i in 'T-'}) + delimiter + statsArray[1][1] +\
                        delimiter + statsArray[2][0].translate({ord(i):None for i in 'T-'}) + delimiter + statsArray[2][1] +\
                        delimiter + statsArray[3][0].translate({ord(i):None for i in 'T-'}) + delimiter + statsArray[3][1] +\
                        delimiter + statsArray[4][0].translate({ord(i):None for i in 'T-'}) + delimiter + statsArray[4][1] +\
                        delimiter + statsArray[5][0].translate({ord(i):None for i in 'T-'}) + delimiter + statsArray[5][1] +\
                        delimiter + statsArray[6][0].translate({ord(i):None for i in 'T-'}) + delimiter + statsArray[6][1] +\
                        delimiter + statsArray[7][0].translate({ord(i):None for i in 'T-'}) + delimiter + statsArray[7][1] +\
                        delimiter + statsArray[8][0].translate({ord(i):None for i in 'T-'}) + delimiter + statsArray[8][1] +\
                        delimiter + statsArray[9][0].translate({ord(i):None for i in 'T-'}) + delimiter + statsArray[9][1] +\
                        delimiter + statsArray[10][0].translate({ord(i):None for i in 'T-'}) + delimiter + statsArray[10][1] +\
                        delimiter + statsArray[11][0].translate({ord(i):None for i in 'T-'}) + delimiter + statsArray[11][1] +\
                        delimiter + statsArray[12][0].translate({ord(i):None for i in 'T-'}) + delimiter + statsArray[12][1] +\
                        delimiter + statsArray[13][0].translate({ord(i):None for i in 'T-'}) + delimiter + statsArray[13][1] +\
                        delimiter + statsArray[14][0].translate({ord(i):None for i in 'T-'}) + delimiter + statsArray[14][1]

        print(teamStatsLine)

        ts_fh.write(teamStatsLine + '\n')

    except:

        teamStatsLine = teamStatsLine + \
                        delimiter + statsArray[0][0].translate({ord(i): None for i in 'T-'}) + delimiter + statsArray[0][1] + \
                        delimiter + statsArray[1][0].translate({ord(i): None for i in 'T-'}) + delimiter + statsArray[1][1] + \
                        delimiter + statsArray[2][0].translate({ord(i): None for i in 'T-'}) + delimiter + statsArray[2][1] + \
                        delimiter + statsArray[3][0].translate({ord(i): None for i in 'T-'}) + delimiter + statsArray[3][1] + \
                        delimiter + statsArray[4][0].translate({ord(i): None for i in 'T-'}) + delimiter + statsArray[4][1] + \
                        delimiter + statsArray[5][0].translate({ord(i): None for i in 'T-'}) + delimiter + statsArray[5][1] + \
                        delimiter + statsArray[6][0].translate({ord(i): None for i in 'T-'}) + delimiter + statsArray[6][1] + \
                        delimiter + statsArray[7][0].translate({ord(i): None for i in 'T-'}) + delimiter + statsArray[7][1] + \
                        delimiter + statsArray[8][0].translate({ord(i): None for i in 'T-'}) + delimiter + statsArray[8][1] + \
                        delimiter + statsArray[9][0].translate({ord(i): None for i in 'T-'}) + delimiter + statsArray[9][1] + \
                        delimiter + statsArray[10][0].translate({ord(i): None for i in 'T-'}) + delimiter + statsArray[10][1] + \
                        delimiter + statsArray[11][0].translate({ord(i): None for i in 'T-'}) + delimiter + statsArray[11][1] + \
                        delimiter + statsArray[12][0].translate({ord(i): None for i in 'T-'}) + delimiter + statsArray[12][1] + \
                        delimiter + statsArray[13][0].translate({ord(i): None for i in 'T-'}) + delimiter + statsArray[13][1] + \
                        delimiter + statsArray[14][0].translate({ord(i): None for i in 'T-'}) + delimiter + statsArray[14][1]

        print(teamStatsLine)

        ts_fh.write(teamStatsLine + '\n')

    # Build Roster Statistics for current year

    rosterData = div.findAll('a')

    rosterDataLink = ''

    for l in range(0, len(rosterData)):

        if rosterData[l].get_text() == 'Team Statistics':

            rosterDataLink = rosterData[l]['href']

            # print(rosterDataLink)

            scrapePlayerStatistics(ps_fh, pss_fh, pssp_fh, year_id, year_nm, team_id, college, division, rosterDataLink)

def divisionStats(ts_fh, tr_fh, ps_fh, pss_fh, pssp_fh, url, teamFrom, teamTo, division):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    for x in range(teamFrom, teamTo):

        tag = soup.findAll('a')[x]

        link = tag['href']

        # print(link)

        line = str(tag)

        # remove ' from team name

        line = line.replace('\'', '')

        title = re.compile(r'[\w+\&*\w*\;*\.*\w*\-*\s*\(*\w*\s*]+')

        team_id = str(title.findall(line)[2])

        college = title.findall(line)[4]

        college = college.replace('&amp;', '')

        college = college.replace(' ', '_')

        college = college.replace('.', '')

        college = college.replace('(', '')

        college = college.replace(')', '')

        college = college.upper()

        # print(college)

        url = 'https://stats.ncaa.org' + link

        # print('PROBLEM BEFORE')

        response = requests.get(url)

        # print('PROBLEM AFTER')

        teamStatistics = BeautifulSoup(response.text, 'html.parser')

        # print(teamStatistics)

        try:

            html = list(teamStatistics.children)[2]

            # print(html)

            head = list(html.children)[1]

            # print(head)

            body = list(html.children)[5]

            # print(body)

            div = list(body.children)[3]

            # print(div)

            fieldset = list(div.children)[7]

            # print(fieldset)

            fieldsetDiv = list(fieldset.children)[3]

            # print(fieldsetDiv)

            fieldsetDivForm = list(fieldsetDiv.children)[1]

            # print(fieldsetDivForm)

            fieldsetDivFormSelect = list(fieldsetDivForm)[2]

            # print(fieldsetDivFormSelect)

            # This will iterate through years for the current team

            fieldsetYears = fieldsetDivFormSelect.findAll('option')

            for i in range(0, len(list(fieldsetYears))):

                # for i in range(0, 1):

                year_id = fieldsetYears[i].get('value')

                year_nm = fieldsetYears[i].get_text()

                scrapeTeamStatistics(ts_fh, tr_fh, ps_fh, pss_fh, pssp_fh, year_id, year_nm, team_id, college, division)

                # Nine years per team of stats

                if i == 8:

                    break

                time.sleep(3)

        except:

            break

start = time.time()

output_file_dir = 'C:\\Richard\\Regis\\1_MSDS696_X70_Data_Science_Practicum_II\\Data\\'

ts_fh = open(output_file_dir + 'teamStatistics.txt', "w", encoding = 'utf-8')

ts_fh.write(header + '\n')

tr_fh = open(output_file_dir + 'teamResults.txt', "w", encoding = 'utf-8')

tr_fh.write(headerResults + '\n')

ps_fh = open(output_file_dir + 'playerStatistics.txt', "w", encoding = 'utf-8')

ps_fh.write(headerPlayerStatistics + '\n')

pss_fh = open(output_file_dir + 'playerStatisticsSorted.txt', "w", encoding = 'utf-8')

pss_fh.write(headerPlayerStatistics + '\n')

pssp_fh = open(output_file_dir + 'playerStatisticsPivot.txt', "w", encoding = 'utf-8')

pssp_fh.write(headerPlayerStatisticsPivot + '\n')

# Division 1 for x in range(191, 544):

# Division 2 for x in range(184, 493):

# Division 3 for x in range(205, 632):

# Division 1

division = 1

url = 'https://stats.ncaa.org/team/inst_team_list?sport_code=MBB&division=' + str(division)

teamFrom = 191

teamTo = 544

divisionStats(ts_fh, tr_fh, ps_fh, pss_fh, pssp_fh, url, teamFrom, teamTo, division)

# Division 2

division = 2

url = 'https://stats.ncaa.org/team/inst_team_list?sport_code=MBB&division=' + str(division)

teamFrom = 184

teamTo = 493

# divisionStats(ts_fh, tr_fh, ps_fh, pss_fh, pssp_fh, url, teamFrom, teamTo, division)

# Division 3

division = 3

url = 'https://stats.ncaa.org/team/inst_team_list?sport_code=MBB&division=' + str(division)

teamFrom = 205

teamTo = 632

# divisionStats(ts_fh, tr_fh, ps_fh, pss_fh, pssp_fh, url, teamFrom, teamTo, division)

ts_fh.close()

tr_fh.close()

ps_fh.close()

pss_fh.close()

pssp_fh.close()

end = time.time()

print(end - start)
