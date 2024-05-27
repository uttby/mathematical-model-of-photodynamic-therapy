from dash import dcc, html
import dash_bootstrap_components as dbc
import numpy as np

from config import specific_parameter_setup

MU_EXPLANATION = (html.P("μ = k_os/(k_oa*[A])"),
                  html.P("k_os : rate of reaction between singlet oxygen and ground state photosensitizer (photobleaching)"),
                  html.P("k_oa : rate of reaction between singlet oxygen and acceptor (cancer cell)"),
                  html.P("[A] : Acceptor cell concentration"),
                  html.P("Since experiments have shown that the photobleaching rate is power density dependent, this model assumes μ to be power density dependent."))

"""
Component utility functions
"""

def slider_component(id, min=0.0, max=1.0, step=0.01,  value=0.5, marks=[0, 1, 11], int_marks = False):
    """
    Utility function that creates a slider object:
        Args:
            id(String): the id of the slider object
            min(Float): optional, minimal possible value on the slider scale
            max(Float): optional, maximal possible value on the slider scale
            step(Float): optional, scale steps
            value(Float): optional, inital value
            marks([Int, Int, Int]): marks on the slider scale
            int_marks(Boolean): Set to true if the marks on the scale should be rounded to be Integer values
    """

    if int_marks:
       marks = {int(i): '{}'.format(int(i)) for i in np.linspace(marks[0],marks[1], marks[2], True)} 
    else:
        marks = {round(i, 5): '{}'.format(round(i, 5)) for i in np.linspace(marks[0],marks[1], marks[2], True)}

    # Create and return the slider object
    return (html.Div([
        dcc.Slider(
            min=min,
            max=max,
            step=step,
            marks=marks,
            value=value,
            id=id,
            updatemode='drag',
            tooltip={"placement": "top", "always_visible": True} 
        ),
    ], style={}))

def textbox_component(id, min=0.0, max=1.0, step=0.001, value=0.5):
    """
    Utility function that creates a textbox object:
        Args:
            id(String): the id of the textbox object
            min(Float): optional, minimal possible value
            max(Float): optional, maximal possible value
            step(Float): optional, scale steps
    """

    # Create and return the textbox object
    return (html.Div([
        dcc.Input(value=value, type='number', id=id, min=min, max=max, step=step, style={'textAlign': 'center',}),
    ], style={}))


"""
Components
"""

# Introduction including the explanation for μ for the variable parameter component
variable_parameter_introduction = html.Div(
    [
        html.H4("μ (power dose dependent)", id = "mu", style={'textAlign': 'left',}),
        dbc.Tooltip(MU_EXPLANATION, target = "mu", placement = "top"),
    ]
)

# Component that allows to change μ PpIX via slider or textbox 
set_mu_PpIX = html.Div(
    [
        html.Div("PpIX"), 
        textbox_component('textbox_mu_PpIX', value=specific_parameter_setup.get_mu_PpIX(), max = 1e-3, step = 1e-6), 
        slider_component('slider_mu_PpIX', value=specific_parameter_setup.get_mu_Ppp(), max = 1e-3, step = 1e-6, marks=[0, 1e-3, 3]), 

    ]
)

# Component that allows to change μ Ppp via slider or textbox 
set_mu_Ppp = html.Div(
    [
        html.Div("Ppp"), 
        textbox_component('textbox_mu_Ppp', value=specific_parameter_setup.get_mu_PpIX(), max = 1e-3, step = 1e-6), 
        slider_component('slider_mu_Ppp', value=specific_parameter_setup.get_mu_Ppp(), max = 1e-3, step = 1e-6, marks=[0, 1e-3, 3]),
    ]
)

# Introduction including the explanation for xi for the variable parameter component
xi_dash_introduction = html.Div(
    [
        html.H4("xi_dash", id = "xi_dash", style={'textAlign': 'left',}),
    ]
)

# Component that allows to change xi_dash PpIX via slider or textbox 
set_xi_dash_PpIX = html.Div(
    [
        html.Div("PpIX"), 
        textbox_component('textbox_xi_dash_PpIX', value=specific_parameter_setup.get_xi_dash_PpIX(), max = 0.05, step = 1e-6), 
        slider_component('slider_xi_dash_PpIX', value=specific_parameter_setup.get_xi_dash_Ppp(), max = 0.05, step = 1e-6, marks=[0, 1e-3, 3]), 

    ]
)

# Component that allows to change xi_dash Ppp via slider or textbox 
set_xi_dash_Ppp = html.Div(
    [
        html.Div("Ppp"), 
        textbox_component('textbox_xi_dash_Ppp', value=specific_parameter_setup.get_xi_dash_PpIX(), max = 0.05, step = 1e-6), 
        slider_component('slider_xi_dash_Ppp', value=specific_parameter_setup.get_xi_dash_Ppp(), max = 0.05, step = 1e-6, marks=[0, 1e-3, 3]),
    ]
)

# Introduction including the explanation for xi for the variable parameter component
beta_introduction = html.Div(
    [
        html.H4("beta", id = "beta", style={'textAlign': 'left',}),
    ]
)

# Component that allows to change beta PpIX via slider or textbox 
set_beta_PpIX = html.Div(
    [
        html.Div("PpIX"), 
        textbox_component('textbox_beta_PpIX', value=specific_parameter_setup.get_beta_PpIX(), max = 10, step = 1e-4), 
        slider_component('slider_beta_PpIX', value=specific_parameter_setup.get_beta_Ppp(), max = 10, step = 1e-4, marks=[0, 1e-3, 3]), 

    ]
)

# Component that allows to change beta Ppp via slider or textbox 
set_beta_Ppp = html.Div(
    [
        html.Div("Ppp"), 
        textbox_component('textbox_beta_Ppp', value=specific_parameter_setup.get_beta_PpIX(), max = 10, step = 1e-4), 
        slider_component('slider_beta_Ppp', value=specific_parameter_setup.get_beta_Ppp(), max = 10, step = 1e-4, marks=[0, 1e-3, 3]),
    ]
)

# Introduction including the explanation for xi for the variable parameter component
delta_introduction = html.Div(
    [
        html.H4("delta", id = "delta", style={'textAlign': 'left',}),
    ]
)

# Component that allows to change delta PpIX via slider or textbox 
set_delta_PpIX = html.Div(
    [
        html.Div("PpIX"), 
        textbox_component('textbox_delta_PpIX', value=specific_parameter_setup.get_delta_PpIX(), max = 100, step = 1e-2), 
        slider_component('slider_delta_PpIX', value=specific_parameter_setup.get_delta_Ppp(), max = 100, step = 1e-2, marks=[0, 1e-3, 3]), 

    ]
)

# Component that allows to change delta Ppp via slider or textbox 
set_delta_Ppp = html.Div(
    [
        html.Div("Ppp"), 
        textbox_component('textbox_delta_Ppp', value=specific_parameter_setup.get_delta_PpIX(), max = 100, step = 1e-2), 
        slider_component('slider_delta_Ppp', value=specific_parameter_setup.get_delta_Ppp(), max = 100, step = 1e-2, marks=[0, 1e-3, 3]),
    ]
)

# Introduction including the explanation for xi for the variable parameter component
Phi_t_introduction = html.Div(
    [
        html.H4("Phi_t", id = "Phi_t", style={'textAlign': 'left',}),
    ]
)

# Component that allows to change Phi_t PpIX via slider or textbox 
set_Phi_t_PpIX = html.Div(
    [
        html.Div("PpIX"), 
        textbox_component('textbox_Phi_t_PpIX', value=specific_parameter_setup.get_Phi_t_PpIX(), max = 2, step = 1e-6), 
        slider_component('slider_Phi_t_PpIX', value=specific_parameter_setup.get_Phi_t_Ppp(), max = 2, step = 1e-6, marks=[0, 1e-3, 3]), 

    ]
)

# Component that allows to change Phi_t Ppp via slider or textbox 
set_Phi_t_Ppp = html.Div(
    [
        html.Div("Ppp"), 
        textbox_component('textbox_Phi_t_Ppp', value=specific_parameter_setup.get_Phi_t_PpIX(), max = 2, step = 1e-6), 
        slider_component('slider_Phi_t_Ppp', value=specific_parameter_setup.get_Phi_t_Ppp(), max = 2, step = 1e-6, marks=[0, 1e-3, 3]),
    ]
)

# Introduction including the explanation for xi for the variable parameter component
S_Delta_introduction = html.Div(
    [
        html.H4("S_Delta", id = "S_Delta", style={'textAlign': 'left',}),
    ]
)

# Component that allows to change S_Delta PpIX via slider or textbox 
set_S_Delta_PpIX = html.Div(
    [
        html.Div("PpIX"), 
        textbox_component('textbox_S_Delta_PpIX', value=specific_parameter_setup.get_S_Delta_PpIX(), max = 2, step = 1e-6), 
        slider_component('slider_S_Delta_PpIX', value=specific_parameter_setup.get_S_Delta_Ppp(), max = 2, step = 1e-6, marks=[0, 1e-3, 3]), 

    ]
)

# Component that allows to change S_Delta Ppp via slider or textbox 
set_S_Delta_Ppp = html.Div(
    [
        html.Div("Ppp"), 
        textbox_component('textbox_S_Delta_Ppp', value=specific_parameter_setup.get_S_Delta_PpIX(), max = 2, step = 1e-6), 
        slider_component('slider_S_Delta_Ppp', value=specific_parameter_setup.get_S_Delta_Ppp(), max = 2, step = 1e-6, marks=[0, 1e-3, 3]),
    ]
)

# Introduction including the explanation for xi for the variable parameter component
gamma_introduction = html.Div(
    [
        html.H4("gamma", id = "gamma", style={'textAlign': 'left',}),
    ]
)

# Component that allows to change gamma PpIX via slider or textbox 
set_gamma_PpIX = html.Div(
    [
        html.Div("PpIX"), 
        textbox_component('textbox_gamma_PpIX', value=specific_parameter_setup.get_gamma_PpIX(), max = 1e-4, step = 1e-6), 
        slider_component('slider_gamma_PpIX', value=specific_parameter_setup.get_gamma_Ppp(), max = 1e-4, step = 1e-6), 

    ]
)

# Component that allows to change gamma Ppp via slider or textbox 
set_gamma_Ppp = html.Div(
    [
        html.Div("Ppp"), 
        textbox_component('textbox_gamma_Ppp', value=specific_parameter_setup.get_gamma_PpIX(), max = 1e-4, step = 1e-6), 
        slider_component('slider_gamma_Ppp', value=specific_parameter_setup.get_gamma_Ppp(), max = 1e-4, step = 1e-6),
    ]
)