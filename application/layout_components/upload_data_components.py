from dash import dcc, html
import dash_bootstrap_components as dbc

import plotly.graph_objects as go
import numpy as np
from config import experimental_setup
from model.concentration_equations import *
from config import visualization_setup, solvent_tag

"""
Components for the mass spectrometry data upload
"""

set_solvent_data_label = html.Div([
    html.Label('Enter solvent data tag:'),
    dcc.Input(value=solvent_tag, type='text', id='solvent_data_label', style={'textAlign': 'center',}),
])

set_data_label = html.Div([
    html.Label('Enter data label:'),
    dcc.Input(value="MS Data", type='text', id='concentration_data_label', style={'textAlign': 'center',}),
])

create_datapoints_button = html.Div([
    html.Button('Preview Datapoints', id='MS_data_submit', n_clicks=0, style={'textAlign': 'center',}),
])

upload_mass_spectrometry_data = html.Div([
    dcc.Upload(
        id='upload_mass_spectrometry_data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    dcc.Loading(id="upload_data_feedback", children = [""], type = "default"),
])

