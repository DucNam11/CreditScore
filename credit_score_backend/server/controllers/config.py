import numpy as np
import pandas as pd
from joblib import load
import os


#---------------------- Functions ----------------------#
def convert_types(df, print_info = False):
    
    original_memory = df.memory_usage().sum()
    
    # Iterate through each column
    for c in df:
        
        # Convert ids and booleans to integers
        if ('SK_ID' in c):
            df[c] = df[c].fillna(0).astype(np.int32)
            
        # Convert objects to category
        elif (df[c].dtype == 'object') and (df[c].nunique() < df.shape[0]):
            df[c] = df[c].astype('category')
        
        # Booleans mapped to integers
        elif list(df[c].unique()) == [1, 0]:
            df[c] = df[c].astype(bool)
        
        # Float64 to float32
        elif df[c].dtype == float:
            df[c] = df[c].astype(np.float32)
            
        # Int64 to int32
        elif df[c].dtype == int:
            df[c] = df[c].astype(np.int32)
        
    new_memory = df.memory_usage().sum()
    
    if print_info:
        print(f'Original Memory Usage: {round(original_memory / 1e9, 2)} gb.')
        print(f'New Memory Usage: {round(new_memory / 1e9, 2)} gb.')
        
    return df

def load_csv_file(file_path):
    '''
        Load a .csv file from the specified file path
        and transforms it into a pandas df
    '''
    df = pd.read_csv(file_path)
    df = df.drop(df.columns[0], axis=1)  # Drop the first column if necessary
    return convert_types(df)

#---------------------- Variables ----------------------#


data_dir = os.getenv('DATA_DIR', '/app/data')




#-------------------------------------------------------#

# Loading the original data that has been transformed and used to train
# the model on.

print("Loading training data into dataframes...")

SAVED_APP_DATA = load_csv_file(os.path.join(data_dir, "application_test.csv"))
SAVED_BUREAU_DATA = load_csv_file(os.path.join(data_dir, "bureau.csv"))
SAVED_BUREAU_BALANCE_DATA = load_csv_file(os.path.join(data_dir, "bureau_balance.csv"))
SAVED_CASH_DATA = load_csv_file(os.path.join(data_dir, "POS_CASH_balance.csv"))
SAVED_CARD_DATA = load_csv_file(os.path.join(data_dir, "credit_card_balance.csv"))
SAVED_INSTALLMENTS_DATA = load_csv_file(os.path.join(data_dir, "installments_payments.csv"))
SAVED_PREV_APP_DATA = load_csv_file(os.path.join(data_dir, "previous_application.csv"))
CREDIT_SCORE_DATA = load_csv_file(os.path.join(data_dir, "predictions_test.csv"))
print("Training data loaded.")

# Loading the model 

# print("Loading model...")

# MODEL = load(data_dir+"lgbm_trained_model_whole_dataset.joblib")

# print("Model loaded.")

