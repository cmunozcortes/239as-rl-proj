import os
import glob
import re
import pandas as pd
import matplotlib.pyplot as plt

# Set style sheet
plt.style.use(['seaborn-muted','seaborn-talk'])

mean_scores = {}

# Visit each subdir recursively looking for log files
for root, dirs, files in os.walk('.'):
    for file in glob.glob(os.path.join(root, '*.log')):

        # Open file as read only
        with open(file, 'r') as reader:

            # Read the first line
            line = reader.readline()

            # Continue reading until eof (empty string)
            while line != '':
                if 'Average Score' in line:

                    # Expect the mean score to be the fifth item
                    mean_score = float(line.split()[5].replace(';', ''))
                    algo = re.split('\W+', file)[2]
                    game = re.split('\W+', file)[3]

                    # Initialize list for each game in the dict
                    if algo not in mean_scores:
                        mean_scores[algo] = dict()

                    # Append to list of scores for game
                    mean_scores[algo][game] = mean_score

                # Read the next line
                line = reader.readline()

# Create df from dict with human and random scores
scores = {
    'Games': ['breakout', 'boxing', 'road_runner', 'video_pinball'],
    'Random': [1.70, 0.10, 11.50, 16256.90],
    'Human': [31.80, 4.30, 7845.00, 17297.60],
}
df = pd.DataFrame(scores)
df = df.set_index('Games')

# Create df from mean_scores dict
algo_scores_df = pd.DataFrame(mean_scores)

# Concatenate both dataframes
df = pd.concat([df, algo_scores_df], axis=1)

# Create df with normalized scores
cols = df.columns.values.tolist()[2:]
for col in cols:
    new_col = col + '_norm'
    df[new_col] = (df[col] - df['Random']) / (df['Human'] - df['Random']) * 100

# Generate a bar plot with the scores for each game
plot_cols = df.columns.values.tolist()[-3:]
df[plot_cols].plot.barh(figsize=(13,5))
plt.title('Normalized scores')

# Show on screen and save plot
plt.tight_layout()
plt.savefig('norm_scores.png', dpi=600)
plt.show()
