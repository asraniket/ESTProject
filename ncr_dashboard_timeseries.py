import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import random

# Load the dataset
df = pd.read_csv(r'ncr_merged_data_up_with_access_score.csv')

# Convert 'Year' to datetime for plotting
df['Year'] = pd.to_datetime(df['Year'], format='%Y')

# Initialize the Dash app
app = Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    # Header with India-themed gradient
    html.Div([
        html.H1('NCR Dataset Dashboard', className='title'),
    ], className='header'),
    
    html.Div([
        html.Label('Select State:', className='label'),
        dcc.Dropdown(
            id='state-dropdown',
            options=[{'label': state, 'value': state} for state in df['State'].unique()],
            value=df['State'].unique()[0],
            multi=False,
            className='dropdown'
        ),
    ], className='dropdown-container'),
    
    html.Div([
        html.Label('Select District:', className='label'),
        dcc.Dropdown(
            id='district-dropdown',
            multi=False,
            className='dropdown'
        ),
    ], className='dropdown-container'),
    
    html.Div([
        html.Label('Select Metric:', className='label'),
        dcc.Dropdown(
            id='metric-dropdown',
            options=[
                {'label': 'Mean NDVI', 'value': 'mean_ndvi'},
                {'label': 'Wheat Data', 'value': 'wheat_data'},
                {'label': 'Tomato Data', 'value': 'tomato_data'},
                {'label': 'Potato Data', 'value': 'potato_data'},
                {'label': 'Per Capita Income', 'value': 'Percapita_Income'},
                {'label': 'Population Density', 'value': 'Population_density'},
                {'label': 'Total Markets', 'value': 'total_markets'},
                {'label': 'Malnutrition Rate', 'value': 'Malnutrition_Rate'},
                {'label': 'Anemia Rate', 'value': 'Anemia_Rate'},
                {'label': 'BMI Average', 'value': 'BMI_Avg'},
                {'label': 'Access Score', 'value': 'access_score'}
            ],
            value='access_score',
            multi=False,
            className='dropdown'
        ),
    ], className='dropdown-container'),
    
    dcc.Graph(id='time-series-graph', className='graph'),
    
    html.H2('Additional Visualizations', className='subtitle'),
    dcc.Graph(id='scatter-plot', className='graph'),
    
    # Hidden div to store state for CSS update
    html.Div(id='state-background', style={'display': 'none'})
], className='container', id='main-container')

# Callback to update district dropdown based on state
@app.callback(
    Output('district-dropdown', 'options'),
    Input('state-dropdown', 'value')
)
def update_districts(selected_state):
    filtered_df = df[df['State'] == selected_state]
    districts = [{'label': district, 'value': district} for district in filtered_df['District'].unique()]
    return districts

# Callback to update the time-series graph
@app.callback(
    Output('time-series-graph', 'figure'),
    [Input('state-dropdown', 'value'),
     Input('district-dropdown', 'value'),
     Input('metric-dropdown', 'value')]
)
def update_time_series(selected_state, selected_district, selected_metric):
    if selected_district:
        filtered_df = df[(df['State'] == selected_state) & (df['District'] == selected_district)]
    else:
        filtered_df = df[df['State'] == selected_state]
    
    fig = px.line(
        filtered_df,
        x='Year',
        y=selected_metric,
        color='District' if not selected_district else None,
        title=f'Time Series of {selected_metric} in {selected_state} ({selected_district if selected_district else "All Districts"})'
    )
    fig.update_layout(
        plot_bgcolor='rgba(255, 255, 255, 0.95)',
        paper_bgcolor='rgba(255, 255, 255, 0.95)',
        font=dict(color='#1a3c34'),
        title_font=dict(size=22, color='#c0392b'),
        xaxis_title_font=dict(size=16, color='#1a3c34'),
        yaxis_title_font=dict(size=16, color='#1a3c34'),
        margin=dict(l=50, r=50, t=80, b=50)
    )
    return fig

# Callback for scatter plot (Access Score vs Malnutrition Rate)
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('state-dropdown', 'value'),
     Input('district-dropdown', 'value')]
)
def update_scatter(selected_state, selected_district):
    if selected_district:
        filtered_df = df[(df['State'] == selected_state) & (df['District'] == selected_district)]
    else:
        filtered_df = df[df['State'] == selected_state]
    
    fig = px.scatter(
        filtered_df,
        x='access_score',
        y='Malnutrition_Rate',
        color='Year',
        size='Population_density',
        hover_data=['District'],
        title=f'Scatter Plot: Access Score vs Malnutrition Rate in {selected_state} ({selected_district if selected_district else "All Districts"})'
    )
    fig.update_layout(
        plot_bgcolor='rgba(255, 255, 255, 0.95)',
        paper_bgcolor='rgba(255, 255, 255, 0.95)',
        font=dict(color='#1a3c34'),
        title_font=dict(size=22, color='#c0392b'),
        xaxis_title_font=dict(size=16, color='#1a3c34'),
        yaxis_title_font=dict(size=16, color='#1a3c34'),
        margin=dict(l=50, r=50, t=80, b=50)
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)