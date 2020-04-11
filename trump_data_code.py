import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns

# Read in fivethirtyeight Trump polling data
data = pd.read_csv('approval_polllist.csv', sep=',')

# Reformat createddate column into date type
data['createddate'] =  pd.to_datetime(data['createddate'], format='%m/%d/%Y')

# Arrange data by 'createddate' in ascending order
data_rev = data.sort_values(by = 'createddate')

# Create dstart variable, which is earliest date
dstart = np.min(data_rev['createddate'])

# Create dend variable, which is latest date
dend = np.max(data_rev['createddate'])

# Create data_fox dataframe, which only includes Fox News polls
data_fox = data_rev[data_rev['pollster']=='Fox News']

# Create data_gl dataframe, which only includes Gallup polls
data_gl = data_rev[data_rev['pollster']=='Gallup']

# Create data_cbs dataframe, which only includes CBS News polls
data_cbs = data_rev[data_rev['pollster']=='CBS News']

# Create line plots for each pollster, indicating reported
# disapproval percentage of polls about Trump over time
plt.plot(data_fox['createddate'], data_fox['disapprove'], label = "Fox News")
plt.plot(data_gl['createddate'], data_gl['disapprove'], label = "Gallup")
plt.plot(data_cbs['createddate'], data_cbs['disapprove'], label = "CBS News")

# Set location of legend
plt.legend(loc="upper right")

# Set title
plt.title("Comparing Trump Disapproval Percentages Across Polls from Fox, Gallup, and CBS")

# Set x range
plt.xlim(dstart, dend)

# Rotate x axis ticks to clean plot
plt.xticks(rotation = 70)

# Show plot
plt.show()
