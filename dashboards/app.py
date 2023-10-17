import dash
from dash import dcc, html
import random  # For generating random data (replace with your data source)
import plotly.graph_objs as go
import time  # For real-time updates

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Racing Telemetry Dashboard'),
    dcc.Graph(id='real-time-chart'),
    dcc.Interval(
        id='interval-component',
        interval=10,  # Update every second (adjust as needed)
        n_intervals=0
    )
])

@app.callback(
    dash.dependencies.Output('real-time-chart', 'figure'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_chart(n_intervals):
    x_data = list(range(1000))  # Replace with your x-axis data
    y_data = [random.uniform(40, 55) for _ in x_data]  # Replace with your y-axis data
    
    figure = go.Figure(data=[
        go.Scatter(x=x_data, y=y_data, mode='lines', line=dict(color='red'))
    ])
    figure.update_yaxes(range=[0, 100])
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
