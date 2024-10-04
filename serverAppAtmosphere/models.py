from django.db import models
import pickle
import json
import numpy as np

__model = None
__data_columns = None


def get_predicted_land_type(air_temp, aerosols):
   if air_temp < -10 or air_temp > 50:  # Example reasonable range
       return 'Invalid air temperature value'
   if aerosols < -999 or aerosols > 4:
       return 'Invalid aerosols value'

   # Prepare the input for the model
   x = np.array([air_temp, aerosols]).reshape(1, -1)

   # Predict the land type directly from the model output
   predicted_index = __model.predict(x)[0]  # This should return the land type as a string directly

   return predicted_index  # Return the predicted land type directly



def load_saved_artifacts():
   print("Loading saved artifacts... start")
   global __data_columns


   with open('E:\\Python\\Machile Learning\\Nasa Space App\\Game Model\\server\\serverAppAtmosphere\\artifacts_Atmos\\columns.json', 'r') as f:
       __data_columns = json.load(f)['data_columns']


   global __model
   if __model is None:
       with open('E:\\Python\\Machile Learning\\Nasa Space App\\Game Model\\server\\serverAppAtmosphere\\artifacts_Atmos\\atmosphere_model.pickle', 'rb') as f:
           __model = pickle.load(f)


   print("Loading saved artifacts... done")




def get_data_columns():
   return __data_columns
