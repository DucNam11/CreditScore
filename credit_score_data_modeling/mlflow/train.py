import lightgbm as lgb
import pandas as pd
import numpy as np
from scipy.stats import randint
import re
from sklearn.metrics import roc_auc_score, make_scorer
import mlflow
import mlflow.lightgbm
from utils import fetch_logged_data
from pprint import pprint

# Load data
train_features = pd.read_csv("train.csv")
train_labels = pd.read_csv("y_train.csv")
test_features = pd.read_csv("test.csv")
test_labels = pd.read_csv("y_test.csv")

# Data preprocessing
train_features = train_features.drop(columns="Unnamed: 0").rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x))
train_labels = train_labels.drop(columns="Unnamed: 0").rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x))
test_features = test_features.drop(columns="Unnamed: 0").rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x))
test_labels = test_labels.drop(columns="Unnamed: 0").rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x))

def main():
    mlflow.set_tracking_uri("http://localhost:5000")

    # Enable MLflow autologging
    mlflow.lightgbm.autolog()

  
    # Start a new MLflow run
    with mlflow.start_run():
          # Initialize LightGBM classifier
        model = lgb.LGBMClassifier(n_estimators=30, reg_alpha=1.0,reg_lambda=1.0)
        model.fit(train_features, train_labels['TARGET'])
    
        y_pred = model.predict(test_features)
        
        # Calculate and log the AUC score
        auc = roc_auc_score(test_labels[:2000], y_pred)
        mlflow.log_metric("ROC AUC", auc)
        

        print(f"ROC AUC on test data: {auc}")

        # Log the run ID for future reference
        run_id = mlflow.active_run().info.run_id
        print(f"Logged data and model in run {run_id}")

        # show logged data
        for key, data in fetch_logged_data(run_id).items():
            print(f"\n---------- logged {key} ----------")
            pprint(data)

if __name__ == "__main__":
    main()
