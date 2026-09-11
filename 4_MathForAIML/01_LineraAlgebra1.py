import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import interactive

df = pd.read_csv('C:\\Users\\hp\\Desktop\\Coding\\AIML\\4_MathForAIML\\Data1.csv')
print(df.head(10))

def plot_line(m, c):
    x = np.linspace(2, 5, num=100)  # generate x values
    y = m*x + c  # calculate y values
    # plt.plot(x, y)  # plot the line
    sns.scatterplot(x='weight', y = 'diameter', hue='fruit', data=df)
    plt.plot(x, y)  # plot the line
    # plt.ylim(-50, 50)  # set y-axis limits
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'y = {m}x + {c}')
    plt.show()

interactive_plot = interactive(plot_line, m=(-1, 5, 0.1), c=(-5, 5, 1))
print(interactive_plot)