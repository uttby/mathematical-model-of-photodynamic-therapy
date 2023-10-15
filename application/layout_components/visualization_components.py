from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import plotly.express as px

from config import experimental_setup
from model.concentration_equations import *
from config import visualization_setup, uploaded_data

def create_figure(title, x, y, x_label = "time [s]", y_label = "concentration [uM]", legend = ["PpIX", "Ppp", "total"], colors = ["#00CED1", "orange", "green"], ):
    """
    Utility function that creates a plotly.graph_object.go.Figure object using the speficied title, data, labels, colors and legend.
        Args:
            title(String): Title of the figure
            x(List): x data 
            y(List): y data
            x_label(String): optional, label of the x axis
            y_lable(String): optional, label of the y axis
            legend(List[String]): optional, legend for the y data traces
            colors(List): optional, colors of the y data traces
        Returns:
            Initalized figure object
    """

    fig = go.Figure(layout=go.Layout(title=go.layout.Title(text=title)))
    
    fig.update_xaxes(
            title_text = x_label,
            title_standoff = 25)
    
    fig.update_yaxes(
        title_text = y_label,
        title_standoff = 25)   

    for i in range(len(y)):     
        fig.add_trace(
            go.Scatter(
                visible=True,
                line=dict(color=colors[i], width=4),
                name=legend[i],
                x=x,
                y=y[i]))
    
    return fig

def create_ground_state_PS_figure():
    """
    Creates the visualization of the simulated ground state concentration for PpIX and Ppp.
    """

    t = np.linspace(0, experimental_setup.get_irradiation_time(), 10001)
    plot = create_figure( 
                title = "Ground State photosensitizer concentration", 
                x = t * visualization_setup.get_x_factor(),   
                y = ground_state_concentration(t),
                x_label = visualization_setup.get_x_label()
        )
    # add all saved uploaded data traces
    for key in uploaded_data:
        concentration_data = uploaded_data[key]
        x = concentration_data['tag'] * (visualization_setup.get_x_factor() / (experimental_setup.get_power_density() * pow(10, -3)))

        trace_PpIX = go.Scatter(x=x, y=concentration_data['PpIX_value'], mode='markers', name = f"{key}_PpIX")
        trace_Ppp = go.Scatter(x=x, y=concentration_data['Ppp_value'], mode='markers', name = f"{key}_Ppp")

        plot.add_trace(trace_PpIX)
        plot.add_trace(trace_Ppp)

    return (plot)

def create_singlet_oxygen_figure():
    """
    Creates the visualization of the simulated singlet oxygen concentration produced by PpIX, Ppp and both combined.
    """
        
    t = np.linspace(0, experimental_setup.get_irradiation_time(), 10001)
    return (
        create_figure(
                x = t * visualization_setup.get_x_factor(), 
                x_label = visualization_setup.get_x_label(), 
                title = "Singlet oxygen concentration * k__oa[A]", 
                y  = singlet_oxygen_concentration(t)
        )
    )

def create_emitted_oxygen_figure():
    """
    Creates the visualization of the simulated emitted singlet oxygen concentration produced by PpIX, Ppp and both combined.
    """

    t = np.linspace(0, experimental_setup.get_irradiation_time(), 10001)
    return (
        create_figure(
                x = t * visualization_setup.get_x_factor(), 
                x_label = visualization_setup.get_x_label(),
                title = "Emitted singlet oxygen concentration", 
                y  = emitted_singlet_oxygen(t)
        )
    )

def create_reactive_oxygen_figure():
    """
    Creates the visualization of the simulated reactive singlet oxygen concentration produced by PpIX, Ppp and both combined.
    """

    t = np.linspace(0, experimental_setup.get_irradiation_time(), 10001)
    return (
        create_figure(
                x = t * visualization_setup.get_x_factor(), 
                x_label = visualization_setup.get_x_label(),
                title = "Reactive singlet oxygen concentration", 
                y  = reactive_singlet_oxygen(t)
        )
    )

def create_opt_scoring_figure():
    """
    Creates the visualization of the score history for that has been achieved by using different values for 
    µ PpIX and µ Ppp during automatical parameter optimization.
    """

    # Extract the mean test score from the optimization results that have been stored inside the visualization setup.
    score = pd.DataFrame({"mean test score" : visualization_setup.get_opt_results()['mean_test_score']})
    
    return(
        px.line(score, 
            title="Optimization history: Mean test score",
        ).update_layout(xaxis_title ="Iteration", yaxis_title="Negative Mean Squared Error")
    )

def create_opt_PpIX_value_score_figure():  
    """
    Creates the visualization of the score history for different values for 
    µ PpIX during automatical parameter optimization.
    """

    # Extract the mean test score and µ PpIX values from the optimization results that have been stored inside the visualization setup.
    score = pd.DataFrame(data={
        'mu_PpIX': visualization_setup.get_opt_results()['param_mu_PpIX'].tolist(),
        'mean test score': visualization_setup.get_opt_results()['mean_test_score'].tolist(),
    })

    return(
        px.scatter(score, 
            y="mu_PpIX",
            color="mean test score",
            title="Optimization history: µ PpIX",
        ).update_layout(xaxis_title ="Iteration")
    )

def create_opt_Ppp_value_score_figure():
    """
    Creates the visualization of the score history for different values for 
    µ Ppp during automatical parameter optimization.
    """

    # Extract the mean test score and µ Ppp values from the optimization results that have been stored inside the visualization setup.    
    score = pd.DataFrame(data={
        'mu_Ppp': visualization_setup.get_opt_results()['param_mu_Ppp'].tolist(),
        'mean test score': visualization_setup.get_opt_results()['mean_test_score'].tolist(),
    })

    return(
        px.scatter(score, 
            y="mu_Ppp",
            color="mean test score",
            title="Optimization history: µ Ppp",
        ).update_layout(xaxis_title ="Iteration")
    )

"""
Application layout components
"""

# Dropdown menu for choosing the first figure
plot_1_dropdown = html.Div(children=[
    dcc.Dropdown(['Ground State Photosensitizer', 'Singlet oxygen concentration', 'Emitted singelt oxygen concentration', 'Reactive singlet oxygen concentration'], 
                 'Ground State Photosensitizer', 
                 id="plot_1_dropdown")
])

# Dropdown menu for choosing the second figure
plot_2_dropdown = html.Div(children=[
    dcc.Dropdown(['Ground State Photosensitizer', 'Singlet oxygen concentration', 'Emitted singelt oxygen concentration', 'Reactive singlet oxygen concentration'], 
                 'Emitted singelt oxygen concentration', 
                 id="plot_2_dropdown")
])

# First figure (initally: ground state concentration)
plot_1 = html.Div(children=[
    dcc.Graph(
        id='plot_1',
        figure = create_ground_state_PS_figure()
    ),
]) 

# Second figure (initially: emitted oxygen figure)
plot_2 = html.Div(children=[
    dcc.Graph(
        id='plot_2',
        figure = create_emitted_oxygen_figure()
    ),
]) 
