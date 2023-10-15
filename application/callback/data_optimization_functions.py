from config import *
import numpy as np

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import LeaveOneOut
from skopt import BayesSearchCV

from sklearn.base import BaseEstimator, ClassifierMixin
import matplotlib.pyplot as plt
from model.concentration_equations import ground_state_concentration

import matplotlib.pyplot as plt

class GroundState_ExperimentalFit(BaseEstimator, ClassifierMixin):
    def __init__(self, mu_PpIX, mu_Ppp):
        """
        This Estimator is used to optimize the values of mu PpIX and mu Ppp by fitting the simulation to 
        the uploaded experimental data. 

            Args:
                mu_PpIX (Float),
                mu_Ppp (Float)
        """
        self.mu_PpIX = mu_PpIX
        self.mu_Ppp = mu_Ppp

        self.t = np.linspace(0, 10000, 10001)
        # set inside the fit function
        self.model= None

    def fit(self, X, y):
        """
        Prepare the simulated ground state concentration for given time steps t
        """

        self.model = ground_state_concentration(self.t)
        return self
    
    def apply_parameters(self):
        """
        Apply the parameters of the estimator globally to the model
        """
        
        self.mu_PpIX = round(self.mu_PpIX, 5)
        self.mu_Ppp = round(self.mu_Ppp, 5)

        specific_parameter_setup.set_mu_PpIX(self.mu_PpIX)
        specific_parameter_setup.set_mu_Ppp(self.mu_Ppp)

    def predict(self, X):
        """
        Predict the ground state concentration of PpIX and Ppp using the simulation and the entered time step(s).
        """
        
        # set all parameters so that they are used inside the model
        self.apply_parameters()

        
        # check whether the input has multiple dimensions or not
        if (len(X) > 1):
            prediction_PpIX = np.array([])
            prediction_Ppp  = np.array([])

            # Predict the ground state concentration for every time step and add the prediction to the prediction_array.
            for time_step in X:
                index = np.argwhere(self.t == time_step)[0][0]
                prediction_PpIX = np.append(prediction_PpIX, self.model[0][index])
                prediction_Ppp  = np.append(prediction_Ppp, self.model[1][index])
        
        # Predict the ground state concentration for the given time step. 
        elif (len(X) == 1):
            index = np.argwhere(self.t == X)[0][0]
            prediction_PpIX = self.model[0][index]
            prediction_Ppp  = self.model[1][index]

        # Return the predicted concentration 
        return prediction_PpIX, prediction_Ppp

    def score(self, X, y):
        """
        Calculate and return the negative squared mean error of the prediction.
        """

        PpIX, Ppp = self.predict(X)
        target_PpIX, target_Ppp = y[:,0], y[:,1]

        return (- (pow(abs(PpIX - target_PpIX), 2).mean() + pow(abs(Ppp - target_Ppp), 2).mean()))

    def get_optimized_mu(self):
        """
        Returns the optimized values for mu PpIX and mu Ppp
        """
        
        return (self.mu_PpIX, self.mu_Ppp)

def optimize_mu (x, y, min_PpIX, max_PpIX, min_Ppp, max_Ppp, n_iter = 100):
    """
    Optimize mu PpIX and Ppp to fit best to the uploaded experimental data
        Args:
            x : uploaded x data (ground state concentration of PpIX and Ppp)
            y: uploaded y data (time steps)
            min_PpIX(Float), max_PpIX(Float): Interval in which a solution for mu PpIX is seeked
            min_Ppp(Float), max_Ppp(Float): Interval in which a solution for mu Ppp is seeked
            n_iter(Int): optional, number of interations for the optimization
    """

    # Extract specific parameters for PpIX and Ppp from the specific parameter setup
    parameters = {'mu_PpIX':[min_PpIX, max_PpIX], 'mu_Ppp':[min_Ppp, max_Ppp]}

    # Create the estimator for the optimization
    estimator = GroundState_ExperimentalFit(
            specific_parameter_setup.get_mu_PpIX(), 
            specific_parameter_setup.get_mu_Ppp()
        )

    #  Create a GridSearchCV object
    grid_search = BayesSearchCV(estimator, parameters, cv=LeaveOneOut(), verbose = 1, n_iter=n_iter)

    # Fit the GridSearchCV object to your data
    grid_search.fit(x, y)

    # Predict
    grid_search.predict(x)

    # Access the best estimator found during the grid search
    best_estimator = grid_search.best_estimator_

    # Apply the optimized parameters globally
    best_estimator.apply_parameters()

    # Store the optimization results inside the visualization setup
    visualization_setup.set_opt_results(grid_search.cv_results_)

    # Return the optimized value for mu PpIX and mu Ppp
    return (best_estimator.get_optimized_mu())