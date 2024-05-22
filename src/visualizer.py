import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib.dates as mdates

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
        plt.xticks(priority_counts.index, labels=[f'Priority {i}' for i in priority_counts.index], rotation=0)
        plt.grid(axis='y')
        plt.show()

    @staticmethod
    def tasks_by_category(df):
        colors_palette_category = {
            'Study': 'limegreen',
            'Home': 'forestgreen',
            'Health': 'lightgreen',
            'Personal': 'darkgreen',
            'Work': 'darkolivegreen'
        }

        category_counts = df['Category'].value_counts().sort_index()
        colors = [colors_palette_category[category] for category in category_counts.index]

        plt.figure(figsize=(10, 6))
        bars = plt.bar(category_counts.index, category_counts.values, color=colors)
        plt.title('Number of Tasks by Category')
        plt.xlabel('Category')
        plt.ylabel('Number of Tasks')
        plt.xticks(rotation=0)
        plt.grid(axis='y')
        plt.show()

    @staticmethod
    def upcoming_deadlines(df):

        df['Deadline'] = pd.to_datetime(df['Deadline'])

        deadline_counts = df['Deadline'].value_counts().sort_index()

        date_range = pd.date_range(start=deadline_counts.index.min(), end=deadline_counts.index.max())
        full_counts = deadline_counts.reindex(date_range, fill_value=0)

        # Omitting 0 values
        full_counts = full_counts[full_counts != 0]

        plt.figure(figsize=(12, 6))

        # Using a simple line plot
        plt.plot(full_counts.index, full_counts.values, marker='o')
        plt.title('Upcoming Deadlines')
        plt.xlabel('Date')
        plt.ylabel('Number of Deadlines')
        plt.xticks(rotation=45)
        plt.yticks(range(int(full_counts.min()), int(full_counts.max()) + 1))
        plt.grid(True)
        plt.tight_layout()

        # Labeling each value with the task title
        for date, count in zip(full_counts.index, full_counts.values):
            task_titles = df[df['Deadline'] == date]['Title'].values
            for i, title in enumerate(task_titles):
                if i % 2 == 0:
                    plt.text(date, count, title, ha='center', va='bottom')
                else:
                    plt.text(date, count, title, ha='center', va='top')

        plt.show()
