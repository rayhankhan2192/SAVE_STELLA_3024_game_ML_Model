import pandas as pd

# Define the function to determine the plant type
def determine_plant_type(row):
    try:
        do = float(row['Dissolved_Oxygen'])
        temp = float(row['Temperature'])
        ph = float(row['pH'])
        
        if 1 <= do <= 5 and 25 <= temp <= 30 and 7.5 <= ph <= 8.0:
            return 'Warm, Slightly Alkaline Lake with Low Oxygen'
        elif 5 <= do <= 7 and 8 <= temp <= 15 and 5.5 <= ph <= 6.0:
            return 'Cool, Acidic River with Moderate Oxygen'
        elif 7.1 <= do <= 10 and 20 <= temp <= 30 and 6.8 <= ph <= 7.2:
            return 'Hot, Neutral Pond with High Oxygen'
        elif 1 <= do <= 3 and 5 <= temp <= 10 and 8.1 <= ph <= 8.5:
            return 'Cold, Alkaline Stream with Very Low Oxygen'
        elif 10.1 <= do <= 15 and 10 <= temp <= 20 and 6.0 <= ph <= 6.5:
            return 'Temperate, Slightly Acidic Wetland with Very High Oxygen'
        elif 4 <= do <= 7 and 22 <= temp <= 30 and 6.5 <= ph <= 7.5:
            return 'Tropical, Neutral Lake with Moderate Oxygen'
        elif 8 <= do <= 12 and 10 <= temp <= 15 and 6.8 <= ph <= 7.5:
            return 'Cool, Neutral Stream with High Oxygen'
        elif 3 <= do <= 6 and 20 <= temp <= 30 and 6.0 <= ph <= 6.5:
            return 'Warm, Slightly Acidic Pond with Low to Moderate Oxygen'
        elif 5 <= do <= 7 and 5 <= temp <= 10 and 6.5 <= ph <= 7.2:
            return 'Cold, Neutral River with Moderate Oxygen'
        elif 2 <= do <= 5 and 10 <= temp <= 20 and 7.0 <= ph <= 7.8:
            return 'Temperate, Slightly Alkaline Lake with Low Oxygen'
        else:
            return 'unknown'
    except (ValueError, KeyError):
        return 'unknown'

# Load the CSV file
try:
    df = pd.read_csv('.\\datasets\\sampled_data_Model_2.csv')
except FileNotFoundError:
    print("Error: The file 'input_data.csv' was not found.")
    exit()

# Apply the function to each row
df['Plant Type'] = df.apply(determine_plant_type, axis=1)

# Save the updated CSV file
df.to_csv('.\\datasets\\output_data_with_plants_2.csv', index=False)

print("Processing complete. The updated file is 'output_data_with_plants.csv'.")
