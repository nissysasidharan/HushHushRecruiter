import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Scoring Algorithm/utils')

import pandas as pd
import utils

print(utils.Select_Candidate.step_1(table='Stack',id_column='UserID',name_column='UserName',email_column='UserEmail',score_column='Average'))
print(utils.Select_Candidate.step_1(table='Github',id_column='user_list',name_column='user_name',email_column='user_email',score_column='score'))
print(utils.Select_Candidate.step_1(table='Kaggle',id_column='TeamId',name_column='TeamName',email_column='user_email',score_column='Score_normalised'))