from dash import dcc, html
import dash_bootstrap_components as dbc

"""
All titles and subtitles that are used in the application.
"""

# Title declaration:
TITLE = "Mathematical model of photodynamic therapy"
SUBTITLE = "including photobleaching and the photoproduct Ppp"

SUBTITLE_INPUT = "Input"
EXPLANATION_INPUT = "Please change those experimental conditions according to your desired setup."

SUBTITLE_X_AXIS = "Change x-axis"
EXPLANATION_X_AXIS = "The x-axis (either Time or Energy Dose) for the data visualization plots can be defined here."

SUBTITLE_VAR_PARAM = "Variable parameter setup"

SUBTITLE_VISUALIZATION = "Data Visualization"

SUBTITLE_DATA_UPLOAD = "Upload mass spectrometry data here"
EXPLANATION_DATA_UPLOAD = "Please upload the mass spectrometry files here, by simply pressing the button and selecting the files or via drag and drop. \
    Make sure that all files are named the correct way. Also, give your dataset an individual name. If data with the same name has already be uploaded, the \
    information will be overritten."

SUBTITLE_DATA_OPT = "Automatical optimization"
EXPLANATION_DATA_OPT = "The opitmization goal is to minimize the difference between the selected data points and the simulated curve by varying the \
    value of μ for PpIX and Ppp. The range in which a solution for μ is searched for can be altered according to former optimization results. The opimization is a Bayesian \
        search algorithm wiht 100 iterations. Please note that it may take a while. After optimization, new plot options appear in the visualization dropdown menu."

# Title component creation
title = html.H1(children=TITLE, style={'textAlign': 'center',})

subtitle_input = html.H2(children=SUBTITLE_INPUT, style={'textAlign': 'center',}, id="subtitle_input")
explanation_input = dbc.Tooltip(EXPLANATION_INPUT, target = "subtitle_input", placement = "bottom")

subtitle_x_axis = html.H2(children=SUBTITLE_X_AXIS, style={'textAlign': 'center',}, id ="subtitle_x_axis")
explanation_x_axis = dbc.Tooltip(EXPLANATION_X_AXIS, target="subtitle_x_axis", placement="bottom")

subtitle_variable_parameter = html.H2(children=SUBTITLE_VAR_PARAM, style={'textAlign': 'center',})

subtitle_visualization = html.H2(children=SUBTITLE_VISUALIZATION, style={'textAlign': 'center',})

subtitle_data_upload = html.H2(children=SUBTITLE_DATA_UPLOAD, style={'textAlign': 'center',}, id="subtitle_data_upload")
explanation_data_upload = dbc.Tooltip(EXPLANATION_DATA_UPLOAD, target="subtitle_data_upload", placement="bottom")

subtitle_data_opt = html.H2(children=SUBTITLE_DATA_OPT, style={'textAlign': 'center',}, id="subtitle_data_opt")
explanation_data_opt = dbc.Tooltip(EXPLANATION_DATA_OPT, target="subtitle_data_opt", placement="bottom")
