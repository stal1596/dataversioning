import pandas as pd
import os

#Create a sample dataframe with column names

data = {
    'Name': ['Alice','Bob','Charlie'],
    'Age': [25,30,35],
    'City': ['Margao','Quepem','Tilamol']
    }

df = pd.DataFrame(data)

# # Adding new row to df for V2
new_row_loc = {'Name': 'Tanya', 'Age': 22, 'City': 'Bangalore'}
df.loc[len(df.index)] = new_row_loc

# # Adding new row to df for V3
new_row_loc2 = {'Name': 'Udita', 'Age': 30, 'City': 'Pune'}
df.loc[len(df.index)] = new_row_loc2


#Ensure data directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

#Define the file path
file_path = os.path.join(data_dir,'sample_data.csv')

#Save the dataframe to a csv file including column names
df.to_csv(file_path,index=False)

print(f'CSV file saved to {file_path}')

