import re
import numpy as np
import pandas as pd
import base64, io
from config import *

def prepare_raw_data(raw_data, filename, solvent_label):
    """ 
    Read and decode raw mass spectronemtry data, and convert the data points into concentration units. 
    The element mass as well as the factor and bias specified in the config file is used for the data preparation.
    """
    
    # Check if the function was called with an empty input
    if raw_data is None:
        return "None", []

    # Create an empty dataframe which will later store the PpIX and Ppp values and their corresponding
    # Energy Dose ("tag")
    unsorted_itensity_data = pd.DataFrame(columns = ["tag", "PpIX_value", "Ppp_value"])

    index = 0
    for element in raw_data:
        # Decode the raw mass spectrometry data and store it in the decoded_data dataframe
        decoded = base64.b64decode(element.split(',')[1])
        decoded_data = pd.read_csv(io.StringIO(decoded.decode('utf-8')),  delimiter='\t', names=['mass', 'value']).astype(float)
        
        # Extract PpIX and Ppp values (using the element mass and factor/bias which has been setup in the config.py file)
        value_PpIX = extract_PpIX_intensity(decoded_data)
        value_Ppp =  extract_Ppp_intensity(decoded_data)

        # Set the corresponding tag for the solvent data to -1
        if (solvent_label in filename[index]):
            tag = -1

        # Set the corresponding tag for PpIX and Ppp data equal to there Energy Density which is specified in the filename
        # Note that the datafile naming specification is set in the config file
        else:
            energy_dose = float(re.findall(data_file_naming_specification, filename[index])[0])
            tag = energy_dose 
        
        # increase the data location index by one
        index = index + 1

        # Add the values for PpIX and Ppp as new row to the unsorted data dataframe
        unsorted_itensity_data.loc[len(unsorted_itensity_data.index)] = [tag, value_PpIX, value_Ppp] 

    # Create a new dataframe with the mean values for each tag, so that there are no duplicates per energy dose
    sorted_itensity_data = pd.DataFrame(unsorted_itensity_data.groupby('tag').mean()).reset_index()

    # Get the solvent values
    solvent_values = sorted_itensity_data.loc[0, ['PpIX_value', 'Ppp_value']].values

    # Subtract the solvent from all values and remove the solvent row from the dataframe
    sorted_itensity_data[['PpIX_value', 'Ppp_value']] = sorted_itensity_data[['PpIX_value', 'Ppp_value']].sub(solvent_values)
    prepared_intensity_data = sorted_itensity_data.drop(0)

    # Copy the intensity data into a new dataframe
    concentration_data = prepared_intensity_data.copy()

    # Convert the intensity values into concentration unit using the bias and factor that has been speficied 
    # in the config file
    concentration_data['PpIX_value'] =(prepared_intensity_data['PpIX_value'] - bias_PpIX) / factor_PpIX
    concentration_data['Ppp_value'] = (prepared_intensity_data['Ppp_value'] - bias_Ppp) / factor_Ppp 
    # Return the prepared concentration data with updated column names
    return concentration_data


def extract_PpIX_intensity(data):
    """ 
    Extract the maximal intensity value that is occuring in a specified interval around the element mass
    specified in the config file.
    """
    # Create a upper and lower mass thresh for the extraction interval
    upper_thresh = element_mass_PpIX + interval_length/2 
    lower_thresh = element_mass_PpIX - interval_length/2

     # Check if threshholds are in range of the data
    if (data['mass'].max()>element_mass_PpIX and  data['mass'].min() < element_mass_PpIX):
        # Find the location of the mass value that is included into the data closest to the threshhold
        up = np.argwhere(np.array(data["mass"])>upper_thresh).min()
        low = np.argwhere(np.array(data["mass"])<lower_thresh).max()
        # Get the maximum value inside the specified interval around the element mass
        value_PpIX = data.iloc[low:up, :]['value'].max()
    # Return the maximal intensity value inside the extraction interval
    return value_PpIX

def extract_Ppp_intensity(data):
    """ 
    Extract the maximal intensity value that is occuring in a specified interval around the element mass
    specified in the config file.
    """

    # Create a upper and lower mass thresh for the extraction interval
    upper_thresh = element_mass_Ppp + interval_length/2 
    lower_thresh = element_mass_Ppp - interval_length/2

     # Check if threshholds are in range of the data
    if (data['mass'].max()>element_mass_Ppp and  data['mass'].min() < element_mass_Ppp):

        # Find the location of the mass value that is included into the data closest to the threshhold
        up = np.argwhere(np.array(data["mass"])>upper_thresh).min()
        low = np.argwhere(np.array(data["mass"])<lower_thresh).max()
        
        # Get the maximum value inside the specified interval around the element mass
        value_Ppp = data.iloc[low:up, :].max()['value']
    # Return the maximal intensity value inside the extraction interval
    return value_Ppp
