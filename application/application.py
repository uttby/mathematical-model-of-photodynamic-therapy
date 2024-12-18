from dash import html
import dash_bootstrap_components as dbc
import dash
from dash import html, Input, Output, State, callback


from application.layout_components.title_components import *
from application.layout_components.experiment_setup_components import *
from application.layout_components.variable_parameter_components import *
from application.layout_components.visualization_components import *
from application.layout_components.upload_data_components import *
from application.layout_components.optimize_data_components import *

from application.callback.callback_functions import *

# Generate the app object
app = dash.Dash(external_stylesheets=[dbc.themes.COSMO])

setup_width = 2

"""
Application layout
"""

# Application layout components for accessing the experimental setup and visualization settings
setup_layout =  dbc.Col(
                    [
                        subtitle_input, explanation_input,
                        starting_concentration_setup, 
                        wavelength_setup,
                        power_density_setup,
                        html.Br(),

                        subtitle_x_axis, explanation_x_axis,
                        time_energy_dose_toggle, 
                        irradiation_time_setup, 
                        irradiation_dose_setup,
                        html.Br(),
                    ], style={'textAlign': 'center',}
                )

# Application layout components for altering the value for mu_PpIX and mu_Ppp
variable_parameter = dbc.Col(
                    [
                        subtitle_variable_parameter,
                        variable_parameter_introduction,
                        set_mu_PpIX, set_mu_Ppp
                    ], style={'textAlign': 'center',}
                )

# Application layout components for uploading mass spectrometry data
data_upload = dbc.Col(
                    [
                        subtitle_data_upload, explanation_data_upload,
                        set_solvent_data_label,
                        set_data_label,
                        upload_mass_spectrometry_data,
                    ], style={'textAlign': 'center',}
                )

# Application layout components for configuring and starting the automatical data optimization algorithm
param_opt = dbc.Col(
                    [
                        subtitle_data_opt, explanation_data_opt,
                        set_min_max_PpIX,
                        set_min_max_Ppp,
                        choose_opt_dataset,
                        param_opt_button,
                    ], style={'textAlign': 'center',}
                )

# Enables adjusting all the other parameters for PDT
xi = dbc.Col([xi_introduction, set_xi_PpIX, set_xi_Ppp], style={'textAlign': 'center',})
beta = dbc.Col([beta_introduction, set_beta_PpIX, set_beta_Ppp], style={'textAlign': 'center',})
delta = dbc.Col([delta_introduction, set_delta_PpIX, set_delta_Ppp], style={'textAlign': 'center',})
Phi_t = dbc.Col([Phi_t_introduction, set_Phi_t_PpIX, set_Phi_t_Ppp], style={'textAlign': 'center',})
S_Delta = dbc.Col([S_Delta_introduction, set_S_Delta_PpIX, set_S_Delta_Ppp], style={'textAlign': 'center',})
gamma = dbc.Col([gamma_introduction, set_gamma_PpIX, set_gamma_Ppp], style={'textAlign': 'center',})

# Combined layout for the simulation application
app.layout = html.Div(children=[
    html.Div([
        title, 
        dbc.Row(
            [
                # Setup
                setup_layout, 
                # change mu_PpIX and mu_Ppp
                variable_parameter,
                # Automatical parameters optimization
                param_opt,
            ]
        ), 

        # Data visualization 
        subtitle_visualization,
        dbc.Row(
            [
                dbc.Col([plot_1_dropdown, plot_1]),
                dbc.Col([plot_2_dropdown, plot_2]),
            ]
        ),
        # Data upload
        data_upload, 
        html.Br(),
        # Additional variable parameter setup
        dbc.Row([
            xi,
            beta,
            delta,
            S_Delta,
            gamma, 
            Phi_t,
        ])
    ])
])

"""
User interaction callback
"""

# Update starting concentration
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Input('starting_concentration', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_starting_concentration(starting_concentration, plot_1_dropdown, plot_2_dropdown):
    return (starting_concentration_callback(starting_concentration, plot_1_dropdown, plot_2_dropdown))

# Update irradiation wavelenght
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Input('wavelength', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_wavelength(wavelength, plot_1_dropdown, plot_2_dropdown):
    return (wavelength_callback(wavelength, plot_1_dropdown, plot_2_dropdown))

# Update power density
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Input('power_density', 'value'),
    State('time_energy_dose_toggle', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_power_density(power_density, x_label, plot_1_dropdown, plot_2_dropdown):
    return (power_density_callback(power_density, x_label, plot_1_dropdown, plot_2_dropdown))

# Update x axis label
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Input('time_energy_dose_toggle', 'value'),
    State('power_density', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_x_label(x_label, power_density, plot_1_dropdown, plot_2_dropdown):
    return (x_label_callback(x_label, power_density, plot_1_dropdown, plot_2_dropdown))

# Update the changed irradiation time interval, calculate and update the corresponding irradiation energy dose interval
@callback(
    Output('irradiation_dose', 'value', allow_duplicate=True), Output('irradiation_time', 'value', allow_duplicate=True), 
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'), State('power_density', 'value'),
    Input('irradiation_time', 'value'),
    prevent_initial_call=True
)
def update_irradiation_time(
    plot_1_dropdown, 
    plot_2_dropdown, 
    power_density,
    irradiation_time):

    return (irradiation_time_callback(plot_1_dropdown, plot_2_dropdown, power_density, irradiation_time))

# Update the changed irradiation energy dose interval, calculate and update the corresponding irradiation time interval
@callback(
    Output('irradiation_dose', 'value', allow_duplicate=True), Output('irradiation_time', 'value', allow_duplicate=True), 
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'), State('power_density', 'value'),
    Input('irradiation_dose', 'value'),
    prevent_initial_call=True
)
def update_irradiation_time(
    plot_1_dropdown, 
    plot_2_dropdown, 
    power_density,
    irradiation_time):

    return (irradiation_dose_callback(plot_1_dropdown, plot_2_dropdown, power_density, irradiation_time))

# Update mu for PpIX
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Output('textbox_mu_PpIX', 'value', allow_duplicate=True), Output('slider_mu_PpIX', 'value', allow_duplicate=True),
    Input('textbox_mu_PpIX', 'value'),
    Input('slider_mu_PpIX', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_mu_PpIX(textbox, slider, plot_1_dropdown, plot_2_dropdown):
    return (mu_PpIX_callback(plot_1_dropdown, plot_2_dropdown))

# Update mu for Ppp
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Output('textbox_mu_Ppp', 'value', allow_duplicate=True), Output('slider_mu_Ppp', 'value', allow_duplicate=True),
    Input('textbox_mu_Ppp', 'value'),
    Input('slider_mu_Ppp', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_mu_Ppp(textbox, slider, plot_1_dropdown, plot_2_dropdown):
    return (mu_Ppp_callback(plot_1_dropdown, plot_2_dropdown))

# Update all other param
# Update xi for PpIX
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Output('textbox_xi_PpIX', 'value', allow_duplicate=True), Output('slider_xi_PpIX', 'value', allow_duplicate=True),
    Input('textbox_xi_PpIX', 'value'),
    Input('slider_xi_PpIX', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_xi_PpIX(textbox, slider, plot_1_dropdown, plot_2_dropdown):
    return (xi_PpIX_callback(plot_1_dropdown, plot_2_dropdown))

# Update xi for Ppp
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Output('textbox_xi_Ppp', 'value', allow_duplicate=True), Output('slider_xi_Ppp', 'value', allow_duplicate=True),
    Input('textbox_xi_Ppp', 'value'),
    Input('slider_xi_Ppp', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_xi_Ppp(textbox, slider, plot_1_dropdown, plot_2_dropdown):
    return (xi_Ppp_callback(plot_1_dropdown, plot_2_dropdown))

# Update beta for PpIX
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Output('textbox_beta_PpIX', 'value', allow_duplicate=True), Output('slider_beta_PpIX', 'value', allow_duplicate=True),
    Input('textbox_beta_PpIX', 'value'),
    Input('slider_beta_PpIX', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_beta_PpIX(textbox, slider, plot_1_dropdown, plot_2_dropdown):
    return (beta_PpIX_callback(plot_1_dropdown, plot_2_dropdown))

# Update beta for Ppp
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Output('textbox_beta_Ppp', 'value', allow_duplicate=True), Output('slider_beta_Ppp', 'value', allow_duplicate=True),
    Input('textbox_beta_Ppp', 'value'),
    Input('slider_beta_Ppp', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_beta_Ppp(textbox, slider, plot_1_dropdown, plot_2_dropdown):
    return (beta_Ppp_callback(plot_1_dropdown, plot_2_dropdown))

# Update delta for PpIX
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Output('textbox_delta_PpIX', 'value', allow_duplicate=True), Output('slider_delta_PpIX', 'value', allow_duplicate=True),
    Input('textbox_delta_PpIX', 'value'),
    Input('slider_delta_PpIX', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_delta_PpIX(textbox, slider, plot_1_dropdown, plot_2_dropdown):
    return (delta_PpIX_callback(plot_1_dropdown, plot_2_dropdown))

# Update delta for Ppp
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Output('textbox_delta_Ppp', 'value', allow_duplicate=True), Output('slider_delta_Ppp', 'value', allow_duplicate=True),
    Input('textbox_delta_Ppp', 'value'),
    Input('slider_delta_Ppp', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_delta_Ppp(textbox, slider, plot_1_dropdown, plot_2_dropdown):
    return (delta_Ppp_callback(plot_1_dropdown, plot_2_dropdown))

# Update S_Delta for PpIX
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Output('textbox_S_Delta_PpIX', 'value', allow_duplicate=True), Output('slider_S_Delta_PpIX', 'value', allow_duplicate=True),
    Input('textbox_S_Delta_PpIX', 'value'),
    Input('slider_S_Delta_PpIX', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_S_Delta_PpIX(textbox, slider, plot_1_dropdown, plot_2_dropdown):
    return (S_Delta_PpIX_callback(plot_1_dropdown, plot_2_dropdown))

# Update S_Delta for Ppp
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Output('textbox_S_Delta_Ppp', 'value', allow_duplicate=True), Output('slider_S_Delta_Ppp', 'value', allow_duplicate=True),
    Input('textbox_S_Delta_Ppp', 'value'),
    Input('slider_S_Delta_Ppp', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_S_Delta_Ppp(textbox, slider, plot_1_dropdown, plot_2_dropdown):
    return (S_Delta_Ppp_callback(plot_1_dropdown, plot_2_dropdown))

# Update gamma for PpIX
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Output('textbox_gamma_PpIX', 'value', allow_duplicate=True), Output('slider_gamma_PpIX', 'value', allow_duplicate=True),
    Input('textbox_gamma_PpIX', 'value'),
    Input('slider_gamma_PpIX', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_gamma_PpIX(textbox, slider, plot_1_dropdown, plot_2_dropdown):
    return (gamma_PpIX_callback(plot_1_dropdown, plot_2_dropdown))

# Update gamma for Ppp
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Output('textbox_gamma_Ppp', 'value', allow_duplicate=True), Output('slider_gamma_Ppp', 'value', allow_duplicate=True),
    Input('textbox_gamma_Ppp', 'value'),
    Input('slider_gamma_Ppp', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_gamma_Ppp(textbox, slider, plot_1_dropdown, plot_2_dropdown):
    return (gamma_Ppp_callback(plot_1_dropdown, plot_2_dropdown))

# Update Phi_t for PpIX
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Output('textbox_Phi_t_PpIX', 'value', allow_duplicate=True), Output('slider_Phi_t_PpIX', 'value', allow_duplicate=True),
    Input('textbox_Phi_t_PpIX', 'value'),
    Input('slider_Phi_t_PpIX', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_Phi_t_PpIX(textbox, slider, plot_1_dropdown, plot_2_dropdown):
    return (Phi_t_PpIX_callback(plot_1_dropdown, plot_2_dropdown))

# Update Phi_t for Ppp
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Output('textbox_Phi_t_Ppp', 'value', allow_duplicate=True), Output('slider_Phi_t_Ppp', 'value', allow_duplicate=True),
    Input('textbox_Phi_t_Ppp', 'value'),
    Input('slider_Phi_t_Ppp', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_Phi_t_Ppp(textbox, slider, plot_1_dropdown, plot_2_dropdown):
    return (Phi_t_Ppp_callback(plot_1_dropdown, plot_2_dropdown))

# Upload mass spectrometry data
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Output('upload_data_feedback', 'children'),
    Output('choose_opt_dataset', 'options'),
    Input('upload_mass_spectrometry_data', 'contents'),
    State('upload_mass_spectrometry_data', 'filename'),
    State('concentration_data_label', 'value'),
    State('solvent_data_label', 'value'),
    State('plot_1_dropdown', 'value'), State('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_upload_mass_spectrometry_data(data, filename, label, solvent_label, plot_1_dropdown, plot_2_dropdown):
    return (upload_mass_spectrometry_data_callback(data, filename, label, solvent_label, plot_1_dropdown, plot_2_dropdown))

@callback(
    Output('opt_feedback', 'children'),
    Output('textbox_mu_PpIX', 'value', allow_duplicate=True), Output('slider_mu_PpIX', 'value', allow_duplicate=True),
    Output('textbox_mu_Ppp', 'value', allow_duplicate=True), Output('slider_mu_Ppp', 'value', allow_duplicate=True),
    Output('plot_1_dropdown', 'options'), Output('plot_2_dropdown', 'options'),
    Input('param_opt_button', 'n_clicks'),
    State('choose_opt_dataset', 'value'),
    State('min_mu_PpIX_opt', 'value'), State('max_mu_PpIX_opt', 'value'),
    State('min_mu_Ppp_opt', 'value'), State('max_mu_Ppp_opt', 'value'),
    prevent_initial_call=True
)
# Optimize mu_PpIx and mu_Ppp in order to fit best to the uploaded data
def optimization(n_clicks, opt_dataset, min_PpIX, max_PpIX, min_Ppp, max_Ppp):
    return (optimization_callback(opt_dataset, min_PpIX, max_PpIX, min_Ppp, max_Ppp))

# Update the visualization ouput caused by dropdown choice
@callback(
    Output('plot_1', 'figure', allow_duplicate=True), Output('plot_2', 'figure', allow_duplicate=True),
    Input('plot_1_dropdown', 'value'), Input('plot_2_dropdown', 'value'),
    prevent_initial_call=True
)
def update_visualization_output(plot_1_dropdown, plot_2_dropdown):
    return (dropdown_figure_callback(plot_1_dropdown), dropdown_figure_callback(plot_2_dropdown))
