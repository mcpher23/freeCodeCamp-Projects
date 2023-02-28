import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# Import data
df = pd.read_csv('medical_examination.csv')


# Add 'overweight' column
df['overweight'] = (df['weight'] / ((df['height']/100)**2) > 25).astype('int64')


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['overweight'] == True, 'overweight'] = 1

df.loc[df['overweight'] == False, 'overweight'] = 0

df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0

df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1

df.loc[df['gluc'] == 1, 'gluc'] = 0

df.loc[df['gluc'] > 1, 'gluc'] = 1


# Draw Categorical Plot
def draw_cat_plot():

    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'active', 'overweight', 'alco'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'])['cardio'].count().reset_index(name='total')
    

    # Draw the catplot with 'sns.catplot()'
    sns.catplot(data=df_cat, x='variable',hue='value', y='total', kind='bar', col='cardio', height=6, aspect=0.8, errorbar=None)


    # Get the figure for the output
    fig = sns.catplot(data=df_cat, x='variable',hue='value', y='total', kind='bar', col='cardio', height=6, aspect=0.8, errorbar=None).fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():

    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]


    # Calculate the correlation matrix
    corr = df_heat.corr()


    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr))


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,12))


    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, fmt='.1f',vmin=-.1, vmax=.3, square=True, linewidths=1, mask=mask, center=0, cbar_kws={'ticks': [-0.08, 0.00, 0.08, 0.16, 0.24]})


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
