import pandas as pd
import matplotlib.pyplot as plt
import datetime

class Visualizer:

    @staticmethod
    def tasks_by_priority(df):

        colors_palette_priority = {
            0: 'lightgrey',
            1: 'green',
            2: 'yellow',
            3: 'red'
        }       

        priority_counts = df['Priority'].value_counts().sort_index()
        colors = [colors_palette_priority[priority] for priority in priority_counts.index]

        plt.figure(figsize=(10, 6))
        bars = plt.bar(priority_counts.index, priority_counts.values, color=colors)
        plt.title('Number of Tasks by Priority')
        plt.xlabel('Priority')
        plt.ylabel('Number of Tasks')
        plt.xticks(rotation=0)
        plt.grid(axis='y')

        plt.show()

    def tasks_by_Category(df):


        colors_palette_category = {
            'Study' : 'limegreen',
            'Home' : 'forestgreen',
            'Health' : 'lightgreen',
            'Personal' : 'darkgreen',
            'Work' : 'darkolivegreen'
        }

        category_counts = df['Category'].value_counts().sort_index()
        colors = [colors_palette_category[category] for category in category_counts.index]

        plt.figure(figsize=(10, 6))
        bars = plt.bar(category_counts.index, category_counts.values, color=colors)
        plt.title('Number of Tasks by Category')
        plt.xlabel('Priority')
        plt.ylabel('Number of Tasks')
        plt.xticks(rotation=0)
        plt.grid(axis='y')

        plt.show()

    def upcoming_deadlines(df):

        df['Deadline'] = pd.to_datetime(df['Deadline'])

        deadline_counts = df['Deadline'].value_counts().sort_index()

        date_range = pd.date_range(start=deadline_counts.index.min(), end=deadline_counts.index.max())
        full_counts = deadline_counts.reindex(date_range, fill_value=0)

        plt.figure(figsize=(12, 6))

        plt.stem(full_counts.index, full_counts.values, linefmt='k-', markerfmt='ro', basefmt="k-")
        plt.title('Upcoming Deadlines')
        plt.xlabel('Date')
        plt.ylabel('Number of Deadlines')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()

        plt.show()       