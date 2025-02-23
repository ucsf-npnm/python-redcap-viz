""" Organize your private tokens here
"""

# Standard Libraries #
import pandas as pd

# Custom functions #
def adjust_for_vas(df):
    new_df = df.loc[:,'vas_anxiety':'stanford_sleepiness']
    new_df.insert(0, 'start_local_timestamp', pd.to_datetime(df.start_local_timestamp))
    new_df['vas_energy_reversed'] = 100 - df['vas_energy']
    new_df['hamd_rescaled'] = df['hamd_total'] * (100 / 22)
    new_df['standford_sleepiness_rescaled'] = df['stanford_sleepiness'] * (100 / 7)
    print('vas_energy reversed in new column vas_energy_reversed')
    print('')
    print('hamd rescaled in new column hamd_rescaled')
    print('')
    print('standford_sleepiness rescaled in new column standford_sleepiness_rescaled')
    return new_df

def get_daily_mean(df):
    new_df = df.set_index('start_local_timestamp').resample('1D').mean().reset_index()
    return new_df

""" End of code """
