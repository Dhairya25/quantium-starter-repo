import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load the data from final.csv
df = pd.read_csv('final.csv')

# Initialize the Dash application
app = dash.Dash(__name__)

# Define custom styles for the radio button and chart
radio_style = {
    'marginBottom': '20px',
    'color': '#333',  # Text color
    'fontFamily': 'Arial, sans-serif',  # Font family
}

hover_effect = {
    'transition': 'background-color 0.3s',
    'cursor': 'pointer',
}

# Define the layout of the application with custom styles
app.layout = html.Div([
    html.H1("Sales Data Visualizer", style={'textAlign': 'center', 'marginBottom': '20px'}),
    dcc.RadioItems(
        id='region-selector',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all',  # Default value
        labelStyle={'display': 'block', **radio_style},
        style={'marginBottom': '20px'}
    ),
    dcc.Graph(id='sales-chart', style={'height': '400px', 'marginBottom': '50px'})
])

# Define the callback to update the chart based on the selected region
@app.callback(
    Output('sales-chart', 'figure'),
    [Input('region-selector', 'value')]
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(filtered_df, x='date', y='sales', title='Sales Data Visualization')
    return fig

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
