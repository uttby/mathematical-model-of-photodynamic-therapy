from dash import dcc, html
import dash_bootstrap_components as dbc

from config import experimental_setup

TITLE = 'Experimental conditions setup:'
TOGGLE_EXPLANATION = "Please choose whether the data should be plotted over the time or energy dose."

"""
Components for the experimental condition setup
"""

time_energy_dose_toggle = html.Div(
    [
        dcc.RadioItems(
            ['Time', 'Energy Dose'],
            'Time',
            id = "time_energy_dose_toggle",
            inline = True
        ),
        dbc.Tooltip(TOGGLE_EXPLANATION, target = "time_energy_dose_toggle", placement = "top"),
    ]
)

irradiation_time_setup = html.Div(
    [
        html.Label('Irradiation time range [s]: '),
        dcc.Input(value=experimental_setup.get_irradiation_time(), type='number', id='irradiation_time', min=0.0, max=100000.0, step=1.0, style={'textAlign': 'center',})
    ]
)

irradiation_dose_setup = html.Div(
    [
        html.Label('Irradiation dose range [J/cm^2]: '),
        dcc.Input(value=round(experimental_setup.get_irradiation_time() * experimental_setup.get_power_density() * pow(10, -3)),
                                type='number', id='irradiation_dose', min=0.0, max=10000.0, step=0.1, style={'textAlign': 'center',})
    ]
)

starting_concentration_setup = dbc.Col([
            html.Label('Starting concentration of PpIX [uM]: '),
            dcc.Input(value=experimental_setup.get_S__t0_PpIX(), type='number', id='starting_concentration', min=0.0, max=100.0, step=0.1, style={'textAlign': 'center',})
        ])


wavelength_setup = html.Div(
    [
        html.Label('Irradiation wavelength [nm]: '),
        dcc.Input(value=experimental_setup.get_wavelength(), type='number', id='wavelength', min=350.0, max=1000.0, step=1, style={'textAlign': 'center',})
    ]
)

power_density_setup = html.Div(
    [
        html.Label('Irradiation laser power density [mW/cm^2]:'),
        dcc.Input(value=experimental_setup.get_power_density(), type='number', id='power_density', min=0.0, max=1000.0, step=1, style={'textAlign': 'center',})
    ]
)
