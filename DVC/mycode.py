import os 
import pandas as pd 

data={
    "Name":["Alice", "Bob","Charlie"],
    "Age":[21,23,45],
    "City":["New York","Chicago","San Francisco"]
}

df=pd.DataFrame(data)

#add new row to the data 
new_data={"Name":"Priyank","Age":29,"City":"Ayodhya"}
df.loc[len(df.index)]=new_data



#file path
direc_path='data'
os.makedirs(direc_path,exist_ok=True)

file_path=os.path.join(direc_path,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f"CSV file saved to path {file_path}")
