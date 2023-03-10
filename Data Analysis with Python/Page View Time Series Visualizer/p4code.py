import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=[0], index_col='date')


# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = df.plot(kind='line', figsize=(16,5), color='darkred', legend=None, xlabel='Date', ylabel='Page Views', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig = fig.figure
    
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    df_bar['Months'] = pd.Categorical(df_bar.index.strftime('%B'), categories=months, ordered=True)

    df_bar = pd.pivot_table(data=df_bar, index=df_bar.index.year, columns='Months', values='value')

    # Draw bar plot
    fig = df_bar.plot(kind='bar', figsize=(12, 8), ylabel='Average Page Views', xlabel='Years', rot=0)

    plt.legend(loc = "upper left", title='Months')

    # Save image and return fig (don't change this part)
    fig = fig.figure

    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['month'] = pd.Categorical(df_box['month'], categories=months, ordered=True)

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15,5))

    sns.boxplot(ax=ax1, x = 'year', y='value', data=df_box, fliersize=1)

    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_ylabel('Page Views')
    ax1.set_xlabel('Year')
    ax1.set_yticks([0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000])

    sns.boxplot(ax=ax2, x = 'month', y='value', data=df_box, fliersize=1)

    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_ylabel('Page Views')
    ax2.set_xlabel('Month')
    ax2.set_yticks([0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000])

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig