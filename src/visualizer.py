import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib.dates as mdates
from IPython.display import display
import plotly.graph_objects as go
import plotly.io as pio

class Visualizer:

    @staticmethod
    def tasks_by_priority_and_category_pie(df):
        colors_palette_priority = {
            0: 'lightgrey',
            1: 'green',
            2: 'yellow',
            3: 'red'
        }

        colors_palette_category = {
            'Study': 'limegreen',
            'Home': 'forestgreen',
            'Health': 'lightgreen',
            'Personal': 'darkgreen',
            'Work': 'darkolivegreen'
        }

        priority_counts = df['Priority'].value_counts().sort_index()
        category_counts = df['Category'].value_counts().sort_index()

        colors_priority = [colors_palette_priority[priority] for priority in priority_counts.index]
        colors_category = [colors_palette_category[category] for category in category_counts.index]

        fig, axs = plt.subplots(1, 2, figsize=(12, 6))

        axs[0].pie(priority_counts.values, labels=priority_counts.index, colors=colors_priority, autopct='%1.1f%%')
        axs[0].set_title('Number of Tasks by Priority')

        axs[1].pie(category_counts.values, labels=category_counts.index, colors=colors_category, autopct='%1.1f%%')
        axs[1].set_title('Number of Tasks by Category')

        plt.tight_layout()
        plt.show()

    @staticmethod
    def tasks_by_priority_and_category(df):
        colors_palette_priority = {
            0: 'lightgrey',
            1: 'green',
            2: 'yellow',
            3: 'red'
        }

        colors_palette_category = {
            'Study': 'limegreen',
            'Home': 'forestgreen',
            'Health': 'lightgreen',
            'Personal': 'darkgreen',
            'Work': 'darkolivegreen'
        }

        priority_category_counts = df.groupby(['Priority', 'Category']).size().unstack().fillna(0)

        fig, ax = plt.subplots(figsize=(12, 6))
        for i, priority in enumerate(priority_category_counts.index):
            ax.bar(priority_category_counts.columns, priority_category_counts.loc[priority],
                   bottom=priority_category_counts.iloc[:i].sum(), label=f'Priority {priority}',
                   color=colors_palette_priority[priority])

        ax.set_title('Number of Tasks by Priority and Category')
        ax.set_xlabel('Category')
        ax.set_ylabel('Number of Tasks')
        ax.legend(title='Priority', loc='upper right')
        plt.tight_layout()
        plt.grid(True)
        plt.show()


    @staticmethod
    def upcoming_deadlines(df):
        df['Deadline'] = pd.to_datetime(df['Deadline'])

        deadline_counts = df['Deadline'].value_counts().sort_index()

        date_range = pd.date_range(start=deadline_counts.index.min(), end=deadline_counts.index.max())
        full_counts = deadline_counts.reindex(date_range, fill_value=0)

        # Omitting 0 values
        full_counts = full_counts[full_counts != 0]

        # Create the plotly figure
        fig = go.Figure()

        # Add the deadlines line
        fig.add_trace(go.Scatter(
            x=full_counts.index, y=full_counts.values,
            mode='lines+markers+text',
            name='Deadlines',
            line=dict(color='royalblue', width=2),
            marker=dict(size=6),
            text=[", ".join(df[df['Deadline'] == date]['Title'].values) for date in full_counts.index],
            textposition="top center",
            hoverinfo='text'
        ))

        # Customize the layout
        fig.update_layout(
            title='Upcoming Deadlines',
            xaxis_title='Date',
            yaxis_title='Number of Deadlines',
            template='plotly_white',
            xaxis=dict(
                tickformat='%Y-%m-%d',
                tickangle=-45,
                rangeslider=dict(visible=True),
            ),
            yaxis=dict(gridcolor='lightgrey'),
            legend=dict(x=0.01, y=0.99, bordercolor='Black', borderwidth=1)
        )

        # Show the plot in local window
        fig.show()
        

    @staticmethod
    def points_over_time(df):
        df['Deadline'] = pd.to_datetime(df['Deadline'])
        
        points_over_time = df.groupby('Deadline')['Points'].sum().sort_index().cumsum().reset_index()

        # Calculate the moving average
        points_over_time['Moving Average'] = points_over_time['Points'].rolling(window=7).mean()

        # Create the plot
        fig = go.Figure()

        # Add the cumulative points line
        fig.add_trace(go.Scatter(
            x=points_over_time['Deadline'], y=points_over_time['Points'],
            mode='lines+markers', name='Cumulative Points',
            line=dict(color='royalblue', width=2),
            marker=dict(size=6)
        ))

        # Add the moving average line
        fig.add_trace(go.Scatter(
            x=points_over_time['Deadline'], y=points_over_time['Moving Average'],
            mode='lines', name='7-Day Moving Average',
            line=dict(color='firebrick', width=2, dash='dash')
        ))

        # Add annotations for key points
        max_point = points_over_time['Points'].idxmax()
        fig.add_annotation(x=points_over_time['Deadline'][max_point], y=points_over_time['Points'][max_point],
                        text=f"Max: {points_over_time['Points'][max_point]}",
                        showarrow=True, arrowhead=1)

        # Customize the layout
        fig.update_layout(
            title='Cumulative Points Over Time',
            xaxis_title='Date',
            yaxis_title='Cumulative Points',
            template='plotly_white',
            xaxis=dict(
                tickformat='%Y-%m-%d',
                tickangle=-45,
                rangeslider=dict(visible=True),
            ),
            yaxis=dict(gridcolor='lightgrey'),
            legend=dict(x=0.01, y=0.99, bordercolor='Black', borderwidth=1)
        )

        # Show the plot
        fig.show()







# #show all the plots
# #load in the tasklist
# tasklist = pd.read_csv('tasklist.csv')
# Visualizer.tasks_by_priority(tasklist)
# Visualizer.tasks_by_category(tasklist)
# Visualizer.upcoming_deadlines(tasklist)
# Visualizer.points_over_time(tasklist)
# Visualizer.tasks_by_priority_and_category(tasklist)






