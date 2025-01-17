import os
import pandas as pd

class DataCheck:
    
    def __init__(self):
        self.data = [os.path.join("./data", filename) for filename in os.listdir("./data")]
        self.map = {}
        print("Starting the Data Integration Test \n")
        
    def run(self):
        for file in self.data:
            try:
                # Read CSV file
                csv = pd.read_csv(file)

                # Check if any column contains list-like values
                for column in csv.columns:
                   
                    if csv[column].apply(lambda x: isinstance(x, list)).any():
                        print(f"File {file} contains list-like data in column: {column} \n")
                        break

                # Check if there are any empty cells in the CSV
                if csv.isnull().values.any():
                    print(f"File {file} contains empty cells. \n")
                    
                if str(csv) in self.map : 
                    print(f"Duplicate DataSet {file} : {self.map[str(csv)]} \n")
                
                self.map[str(csv)] = file
                    
                
                
            except Exception as e:
                print(f"Error reading file {file}: {e} \n")
        print("Data Integration is Over")