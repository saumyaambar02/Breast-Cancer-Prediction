import seaborn as sns
import matplotlib.pyplot as plt

def generate_pairplot(df):
    sns.pairplot(df, hue='target', vars=[
        'mean radius', 'mean texture', 'mean area',
        'mean perimeter', 'mean smoothness'
    ])

def plot_target_distribution(df):
    sns.histplot(df['target'], label="Count")

def scatter_plot(df):
    sns.scatterplot(x='mean area', y='mean smoothness', hue='target', data=df)

def correlation_heatmap(df):
    plt.figure(figsize=(20, 10))
    sns.heatmap(df.corr(), annot=True)
