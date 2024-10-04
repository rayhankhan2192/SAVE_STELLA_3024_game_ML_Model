import pickle
import json
import numpy as np
from sklearn.preprocessing import LabelEncoder

__model = None
__data_columns = None
__label_encoder = None  # Label encoder for decoding

def get_predicted_aquatic_environment(Dissolved_Oxygen, salinities):
    if Dissolved_Oxygen < 1.0 or Dissolved_Oxygen > 20.0:
        return 'Invalid Dissolved Oxygen value!'
    if salinities < 0 or salinities > 60.0:
        return 'Invalid salinity value!'

    x = np.array([Dissolved_Oxygen, salinities]).reshape(1, -1)
    predicted_index = __model.predict(x)[0]

    if __label_encoder is not None:
        predicted_label = __label_encoder.inverse_transform([predicted_index])
        return predicted_label[0]
    else:
        return 'Label encoder not loaded properly.'

def load_saved_artifacts():
    global __data_columns, __label_encoder

    with open('E:\\Python\\Machile Learning\\Nasa Space App\\Game Model\\server\\serverAppHydroSphere\\artifacts_Hydro\\columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        with open('E:\\Python\\Machile Learning\\Nasa Space App\\Game Model\\server\\serverAppHydroSphere\\artifacts_Hydro\\hydrosphere_model.pickle', 'rb') as f:
            __model = pickle.load(f)

    with open('E:\\Python\\Machile Learning\\Nasa Space App\\Game Model\\server\\serverAppHydroSphere\\artifacts_Hydro\\label_encoder.pickle', 'rb') as f:
        __label_encoder = pickle.load(f)

def get_data_columns():
    return __data_columns

# Load artifacts on module import
load_saved_artifacts()
