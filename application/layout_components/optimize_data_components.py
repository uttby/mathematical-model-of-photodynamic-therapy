from dash import dcc, html
from config import uploaded_data

"""
Components for the automatical optimization
"""

param_opt_button = html.Div([
    html.Button('Optimize parameters', id='param_opt_button', n_clicks=0),
    dcc.Loading
    (
        id="opt_feedback",
        children = ["Please select uploaded data. Please also make sure that the power density, starting concentration and wavelenght are set to the correct value"], 
        type = "default"
    ),
])

choose_opt_dataset = html.Div([
    html.Label('Choose which datapoints should be used in optimization:'),
    dcc.Dropdown(uploaded_data, id="choose_opt_dataset"),
])

set_min_max_PpIX = html.Div(
    [
        html.Label('Set the borders for optimization'),
        html.Br(),
        html.Label('μ PpIX min: '),
        dcc.Input(value=1e-8, type='number', id='min_mu_PpIX_opt', min=1e-8, max=0.001, step=1e-8, style={'textAlign': 'center',}),
        html.Label('μ PpIX max: '),
        dcc.Input(value=1e-3, type='number', id='max_mu_PpIX_opt', min=1e-8, max=0.001, step=1e-8, style={'textAlign': 'center',})
    ]
)

set_min_max_Ppp = html.Div(
    [
        html.Label('μ Ppp min: '),
        dcc.Input(value=1e-8, type='number', id='min_mu_Ppp_opt', min=1e-8, max=0.001, step=1e-8, style={'textAlign': 'center',}),
        html.Label('μ Ppp max: '),
        dcc.Input(value=1e-3, type='number', id='max_mu_Ppp_opt', min=1e-8, max=0.001, step=1e-8, style={'textAlign': 'center',}),
        html.Br(),
        html.Br(),
    ]
)