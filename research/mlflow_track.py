import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import urllib

csv_url = "https://raw.githubusercontent.com/shrikant-temburwar/Wine-Quality-Dataset/master/winequality-red.csv"
df = pd.read_csv(csv_url, sep=';')
x = df.drop('quality', axis=1)
y = df['quality']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=33)

alpha = 0.5
l1_ratio = 0.5

print("MLflow_version = ", mlflow.__version__)
print("MLflow_tracking URI = ", mlflow.get_tracking_uri())
print("MLflow experiment name = ", mlflow.get_experiment_by_name("mihir"))



mlflow.set_experiment("LoanApproval-1")
with mlflow.start_run(run_name="Loan_runname-1"):
    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio)
    lr.fit(x_train, y_train)

    y_pred = lr.predict(x_test)

    def eval_metrics(actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    (rmse, mae, r2) = eval_metrics(y_test, y_pred)

    print("Elasticnet model (alpha={:f}, l1_ratio={:f}):".format(alpha, l1_ratio))
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)

    mlflow.log_param("alpha", alpha)
    mlflow.log_param("l1_ration", l1_ratio)
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("mae", mae)
    mlflow.log_metric("r2_score", r2)

    mlflow.sklearn.log_model(lr, "model-1-2", registered_model_name="ElasticModel-1-2")