from application.layout_components.visualization_components import *
from application.callback.upload_data_functions import *
from dash import html

from application.callback.data_optimization_functions import optimize_mu
from config import *
from dash import ctx, dash_table
from dash.exceptions import PreventUpdate

def starting_concentration_callback(starting_concentration, plot_1_dropdown, plot_2_dropdown):
    """ Updates the starting concentration for the displayed data plots."""

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Update the experimental setup with the new starting concentration
    experimental_setup.set_S__t0_PpIX(starting_concentration)
    
    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)
    
    # Return the updated data plots to be displayed
    return (plot_1, plot_2)

def wavelength_callback(wavelength, plot_1_dropdown, plot_2_dropdown):
    """
    Updates the irradiation wavelength and therefore the number of absorbed photons
    for the displayed data plots.
    """
    
    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Update the experimental setup with the new wavelength
    experimental_setup.set_wavelength(wavelength)

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the updated data plots to be displayed
    return (plot_1, plot_2)

def power_density_callback(power_density, x_label, plot_1_dropdown, plot_2_dropdown):
    """ 
    Updates the irradiation laser power density for the displayed data plots.
    """
    
    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Update the experimental setup with the new power density
    experimental_setup.set_power_density(power_density)

    # If Energy Dose is displayed, change the time vs power density factor accordingly
    if (x_label == "Energy Dose"):
        visualization_setup.set_x_factor(power_density * pow(10, -3))

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the updated data plots to be displayed
    return (plot_1, plot_2)

def x_label_callback(x_label, power_density, plot_1_dropdown, plot_2_dropdown):
    """ 
    Updates the x label (either Time or Power Dose) for the displayed data plots.
    """

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Toggle Time or Power Dose visualization for all data plots
    if (x_label == 'Time'):
        # Update the visualization setup with the time factor and time label
        visualization_setup.set_x_factor(1)
        visualization_setup.set_x_label(TIME_LABEL)
    elif (x_label == "Energy Dose"):
        # Update the visualization setup with the power density dependent power
        # dose factor and power dose label
        visualization_setup.set_x_factor(power_density * pow(10, -3))
        visualization_setup.set_x_label(ENERGY_DOSE_LABEL)

     # Update the experimental setup with the current power density and updated visualization setup
    experimental_setup.set_power_density(power_density)

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the updated data plots to be displayed
    return (plot_1, plot_2)

def mu_PpIX_callback(plot_1_dropdown, plot_2_dropdown):
    """ 
    Updates the value of the variable mu for PpIX.
    """

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Extract the value of either the slider or textbox, whichever has been changed
    mu = ctx.triggered[0]['value']

    # Update the specific parameter setup with the new value for mu of PpIX
    specific_parameter_setup.set_mu_PpIX(mu)

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the updated data plotsand the new value of mu synching the displayed value of slider and textbox
    return (plot_1, plot_2, mu, mu)

def mu_Ppp_callback(plot_1_dropdown, plot_2_dropdown):
    """ 
    Updates the value of the variable mu for Ppp.
    """

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Extract the value of either the slider or textbox, whichever has been changed
    mu = ctx.triggered[0]['value']

    # Update the specific parameter setup with the new value for mu of Ppp
    specific_parameter_setup.set_mu_Ppp(mu)

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)
    
    # Return the updated data plots and the new value of mu synching the displayed value of slider and textbox
    return (plot_1, plot_2, mu, mu)

def xi_PpIX_callback(plot_1_dropdown, plot_2_dropdown):
    """ 
    Updates the value of the variable xi for PpIX.
    """

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Extract the value of either the slider or textbox, whichever has been changed
    xi = ctx.triggered[0]['value']

    # Update the specific parameter setup with the new value for mu of PpIX
    specific_parameter_setup.set_xi_PpIX(xi)

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the updated data plotsand the new value of mu synching the displayed value of slider and textbox
    return (plot_1, plot_2, xi, xi)

def xi_Ppp_callback(plot_1_dropdown, plot_2_dropdown):
    """ 
    Updates the value of the variable xi for PpIX.
    """

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Extract the value of either the slider or textbox, whichever has been changed
    xi = ctx.triggered[0]['value']

    # Update the specific parameter setup with the new value for mu of PpIX
    specific_parameter_setup.set_xi_Ppp(xi)

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the updated data plotsand the new value of mu synching the displayed value of slider and textbox
    return (plot_1, plot_2, xi, xi)

def beta_PpIX_callback(plot_1_dropdown, plot_2_dropdown):
    """ 
    Updates the value of the variable beta for PpIX.
    """

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Extract the value of either the slider or textbox, whichever has been changed
    beta = ctx.triggered[0]['value']

    # Update the specific parameter setup with the new value for mu of PpIX
    specific_parameter_setup.set_beta_PpIX(beta)

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the updated data plotsand the new value of mu synching the displayed value of slider and textbox
    return (plot_1, plot_2, beta, beta)

def beta_Ppp_callback(plot_1_dropdown, plot_2_dropdown):
    """ 
    Updates the value of the variable beta for PpIX.
    """

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Extract the value of either the slider or textbox, whichever has been changed
    beta = ctx.triggered[0]['value']

    # Update the specific parameter setup with the new value for mu of PpIX
    specific_parameter_setup.set_beta_Ppp(beta)

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the updated data plotsand the new value of mu synching the displayed value of slider and textbox
    return (plot_1, plot_2, beta, beta)

def delta_PpIX_callback(plot_1_dropdown, plot_2_dropdown):
    """ 
    Updates the value of the variable delta for PpIX.
    """

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Extract the value of either the slider or textbox, whichever has been changed
    delta = ctx.triggered[0]['value']

    # Update the specific parameter setup with the new value for mu of PpIX
    specific_parameter_setup.set_delta_PpIX(delta)

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the updated data plotsand the new value of mu synching the displayed value of slider and textbox
    return (plot_1, plot_2, delta, delta)

def delta_Ppp_callback(plot_1_dropdown, plot_2_dropdown):
    """ 
    Updates the value of the variable delta for PpIX.
    """

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Extract the value of either the slider or textbox, whichever has been changed
    delta = ctx.triggered[0]['value']

    # Update the specific parameter setup with the new value for mu of PpIX
    specific_parameter_setup.set_delta_Ppp(delta)

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the updated data plotsand the new value of mu synching the displayed value of slider and textbox
    return (plot_1, plot_2, delta, delta)

def Phi_t_PpIX_callback(plot_1_dropdown, plot_2_dropdown):
    """ 
    Updates the value of the variable Phi_t for PpIX.
    """

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Extract the value of either the slider or textbox, whichever has been changed
    Phi_t = ctx.triggered[0]['value']

    # Update the specific parameter setup with the new value for mu of PpIX
    specific_parameter_setup.set_Phi_t_PpIX(Phi_t)

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the updated data plotsand the new value of mu synching the displayed value of slider and textbox
    return (plot_1, plot_2, Phi_t, Phi_t)

def Phi_t_Ppp_callback(plot_1_dropdown, plot_2_dropdown):
    """ 
    Updates the value of the variable Phi_t for PpIX.
    """

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Extract the value of either the slider or textbox, whichever has been changed
    Phi_t = ctx.triggered[0]['value']

    # Update the specific parameter setup with the new value for mu of PpIX
    specific_parameter_setup.set_Phi_t_Ppp(Phi_t)

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the updated data plotsand the new value of mu synching the displayed value of slider and textbox
    return (plot_1, plot_2, Phi_t, Phi_t)

def S_Delta_PpIX_callback(plot_1_dropdown, plot_2_dropdown):
    """ 
    Updates the value of the variable S_Delta for PpIX.
    """

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Extract the value of either the slider or textbox, whichever has been changed
    S_Delta = ctx.triggered[0]['value']

    # Update the specific parameter setup with the new value for mu of PpIX
    specific_parameter_setup.set_S_Delta_PpIX(S_Delta)

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the updated data plotsand the new value of mu synching the displayed value of slider and textbox
    return (plot_1, plot_2, S_Delta, S_Delta)

def S_Delta_Ppp_callback(plot_1_dropdown, plot_2_dropdown):
    """ 
    Updates the value of the variable S_Delta for PpIX.
    """

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Extract the value of either the slider or textbox, whichever has been changed
    S_Delta = ctx.triggered[0]['value']

    # Update the specific parameter setup with the new value for mu of PpIX
    specific_parameter_setup.set_S_Delta_Ppp(S_Delta)

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the updated data plotsand the new value of mu synching the displayed value of slider and textbox
    return (plot_1, plot_2, S_Delta, S_Delta)

def gamma_PpIX_callback(plot_1_dropdown, plot_2_dropdown):
    """ 
    Updates the value of the variable gamma for PpIX.
    """

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Extract the value of either the slider or textbox, whichever has been changed
    gamma = ctx.triggered[0]['value']

    # Update the specific parameter setup with the new value for mu of PpIX
    specific_parameter_setup.set_gamma_PpIX(gamma)

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the updated data plotsand the new value of mu synching the displayed value of slider and textbox
    return (plot_1, plot_2, gamma, gamma)

def gamma_Ppp_callback(plot_1_dropdown, plot_2_dropdown):
    """ 
    Updates the value of the variable gamma for PpIX.
    """

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Extract the value of either the slider or textbox, whichever has been changed
    gamma = ctx.triggered[0]['value']

    # Update the specific parameter setup with the new value for mu of PpIX
    specific_parameter_setup.set_gamma_Ppp(gamma)

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the updated data plotsand the new value of mu synching the displayed value of slider and textbox
    return (plot_1, plot_2, gamma, gamma)

def upload_mass_spectrometry_data_callback(data, filename, label, solvent_label, plot_1_dropdown, plot_2_dropdown):
    """ 
    Prepares and stores the uploaded concentration data. 
    """

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    try:
        # Read and decode the data and convert into concentration units
        concentration_data = prepare_raw_data(data, filename, solvent_label)
        
        # Assert a non-emtpy data list for the uploaded data.
        assert(not concentration_data.empty)
        
        # Add the prepared concentration data into the uploaded data dictionary 
        # (using the specified label as data label, and replacing old data if the label already exists)
        uploaded_data[label] = concentration_data

        mean_10mW = pd.DataFrame([
            [0.0, 9.889152391, 0.331949941],
            [10.0, 7.660342549, 0.437022391],
            [20.0, 6.931313123, 0.590843221],
            [30.0, 5.877294684, 0.731818182],
            [40.0, 5.231488794, 0.869664032],
            [50.0, 5.131357055, 0.953985514],
            [60.0, 4.77342996, 0.984782609],
            [70.0, 3.68076417, 0.933069822],
            [80.0, 3.697891957, 0.981653498],
            [90.0, 3.478524368, 1.278425553],
            [100.0, 3.232806324, 1.258662708]
        ], columns=['tag', 'PpIX_value', 'Ppp_value'])

        mean_100mW = pd.DataFrame([
            [0.0, 9.786605178, 0.237198063],
            [10.0, 6.39486166, 0.25256917],
            [20.0, 5.068994289, 0.327448399],
            [30.0, 4.123891087, 0.292973202],
            [40.0, 4.193280632, 0.274967055],
            [50.0, 3.954589368, 0.296047431],
            [60.0, 3.84918753, 0.343917431],
            [70.0, 3.401229684, 0.362582352],
            [80.0, 3.413526561, 0.368511206],
            [90.0, 2.981379012, 0.351602984],
            [100.0, 2.837110237, 0.433728597]
        ], columns=['tag', 'PpIX_value', 'Ppp_value'])
        
        #uploaded_data["10mW"] = mean_10mW
        #uploaded_data["100mW"] = mean_100mW

        # Create a feedback message including a table of the uploaded data
        message = [
            html.Div(
                f"The data {label} has been successfully uploaded.",
                style={"color" : "green"}),
            dash_table.DataTable(
                concentration_data.to_dict('records'), 
                [{"name": i, "id": i} for i in concentration_data.columns])
            ]
    # In case the data preparation has failed
    except:
        # Create a feedback message including possible reasons for failure
        message = html.Div(
            f"The data {label} cannot be uploaded.\
            Are the data files named correctly? Have you selected all necessary files (data as well as solvent files)? \
            Has the solvent name tag been specified correctly?", 
            style={"color" : "red"})

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the updated data plots, a feedback message and the uploaded data dictionary 
    # to be updated for the optimization options
    return (plot_1, plot_2, message, [key for key in uploaded_data])
    
def optimization_callback(opt_dataset_label, min_PpIX, max_PpIX, min_Ppp, max_Ppp):
    """
    Checks if the inputed conditions are valid, then starts the automatical optimization. 
    It will return a feedback message, the optimized values for mu PpIX and mu Ppp as well as new options 
    for the visualization dropdown (which will then include opitmization history plots).
    """

    # Check if an uploaded dataset has been set for the optimization. If not, return an error message and unchanged parameters.
    if (opt_dataset_label is None):
        return (
            html.Div(
                "Please select uploaded data. Please also make sure that the power density, starting concentration and wavelenght are set to the correct value", 
                style={"color" : "red"}
            ), specific_parameter_setup.get_mu_PpIX(), specific_parameter_setup.get_mu_PpIX(), specific_parameter_setup.get_mu_Ppp(), specific_parameter_setup.get_mu_Ppp()
        )

    # Convert power Dose into time steps (since the optimization uses time steps)
    time_steps = uploaded_data[opt_dataset_label]["tag"].values * 1000 / experimental_setup.get_power_density() 

    # Convert the uploaded data in the format used for optimization
    concentration_values = np.transpose(np.array([uploaded_data[opt_dataset_label]["PpIX_value"].values, uploaded_data[opt_dataset_label]["Ppp_value"].values]))

    # Call the opitmization funciton in order to get the optimized value for mu PpIX and mu Ppp
    optimized_mu_PpIX, optimized_mu_Ppp = optimize_mu(time_steps, concentration_values, min_PpIX, max_PpIX, min_Ppp, max_Ppp)
    
    # Add new visualization options to the dropdown menu
    options_dropdown =  [
        'Ground State Photosensitizer', 
        'Singlet oxygen concentration', 
        'Emitted singelt oxygen concentration', 
        'Reactive singlet oxygen concentration', 
        'Optimization history: mean test score', 
        'Optimization history: mu PpIX',
        'Optimization history: mu Ppp'
        ]

    # Return a feedback message as well as the optimized values and the updated dropdown options.
    return (
        html.Div(
            f"Bayesian Optimization sucessfully resulted in: \n{optimized_mu_PpIX} for μ PpIX, {optimized_mu_Ppp} for μ Ppp.\
            experimental data label: ''{opt_dataset_label}'', \
            power density: {experimental_setup.get_power_density()} mW/cm^2, \
            irradiation wavelenght: {experimental_setup.get_wavelength()} nm, \
            starting concentration PpIX: {experimental_setup.get_S__t0_PpIX()} μM",  
            style={"color" : "green"}
        ), optimized_mu_PpIX, optimized_mu_PpIX, optimized_mu_Ppp, optimized_mu_Ppp, options_dropdown, options_dropdown
    )

def dropdown_figure_callback(dropdown):
    """ 
    Updates the displayed data plot according to the dropdown choice.
    """

    # Display the ground state concentration 
    if dropdown=='Ground State Photosensitizer':
        plot = create_ground_state_PS_figure()

    # Display the singlet oxygen concentration 
    elif dropdown=='Singlet oxygen concentration':
        plot = create_singlet_oxygen_figure()

    # Display the singlet oxygen concentration that has been emitted in total
    elif dropdown=='Emitted singelt oxygen concentration': 
        plot = create_emitted_oxygen_figure()

    # Display the singlet oxygen concentration that will react with cancer cells
    elif dropdown=='Reactive singlet oxygen concentration': 
        plot = create_reactive_oxygen_figure()
    
    # Display the optimization score over iteration history
    elif dropdown=='Optimization history: mean test score':
        plot = create_opt_scoring_figure()

    # Display the values of mu PpIX as well as their scores that have been tested during the optimization.
    elif dropdown=='Optimization history: mu PpIX':
        plot = create_opt_PpIX_value_score_figure()

    # Display the values of mu Ppp as well as their scores that have been tested during the optimization.
    elif dropdown=='Optimization history: mu Ppp':
        plot = create_opt_Ppp_value_score_figure()

    # Return the updated data plot
    return plot

def irradiation_time_callback(plot_1_dropdown, plot_2_dropdown, power_density,
    irradiation_time):
    """
    Update the irradiation time that is displayed as x axis in the data plots. 
    Also fits the value of the irradiation dose
    accordingly, using the lasers power density.
    """

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate
    
    # Calculate the corresponding irradiation dose
    irradiation_dose = round(irradiation_time * power_density * pow(10, -3))

    # Update the experimental setup with the new value for the irradiation time
    experimental_setup.set_irradiation_time(irradiation_time)

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the according irradiation dose, the new irradiation time and the updated data dislay plots
    return (irradiation_dose, irradiation_time, plot_1, plot_2)
  
def irradiation_dose_callback(plot_1_dropdown, plot_2_dropdown, power_density,
    irradiation_dose):
    """
    Update the irradiation dose that is displayed as x axis in the data plots. 
    Also fits the value of the irradiation time
    accordingly, using the lasers power density.
    """

    # Check if the callback was triggered by an empty input
    if (ctx.triggered[0]['value'] is None):
        # Prevent updating the plots if the input is empty
        raise PreventUpdate

    # Calculate the corresponding irradiation time
    irradiation_time = round(irradiation_dose /(power_density * pow(10, -3)))

    # Update the experimental setup with the new value for the irradiation time
    experimental_setup.set_irradiation_time(irradiation_time)

    # Call a callback function to update the plot based on the dropdown selection
    plot_1 = dropdown_figure_callback(plot_1_dropdown)
    plot_2 = dropdown_figure_callback(plot_2_dropdown)

    # Return the new irradiation dose, the according irradiation time and the updated data dislay plots
    return (irradiation_dose, irradiation_time, plot_1, plot_2)

