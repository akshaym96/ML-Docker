import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np

class TitanicClassificationModel:
    
    def __init__(self, classifier='decision_tree'):
        self.classifier = classifier
        self.clf = None
        
    def train_model(self, X_train, y_train):
        
        if self.classifier == 'decision_tree':
            self.clf = DecisionTreeClassifier(random_state=39)
        elif self.classifier == 'random_forest':
            self.clf = RandomForestClassifier(random_state=39)
        else:
            raise ValueError("Invalid classifier type.")
            
        self.clf.fit(X_train, y_train)
        
    def save_model(self, filename):
        if self.clf is None:
            raise ValueError("Model has not been trained yet.")
        with open(filename, 'wb') as file:
            pickle.dump(self.clf, file)
        print("Model saved as", filename)

def load_dataset():
    # Load the CSV file into a Pandas DataFrame
    csv_file = "train.csv"  # Replace with the path to your CSV file
    df = pd.read_csv(csv_file)

    df = df.dropna()

    # Specify the column index for the label column (second column)
    label_column_index = 1  # Indexing starts from 0

    # Specify the list of column names to include in X_train
    feature_column_names = ["Pclass", "Age", "SibSp"]  # Replace with your desired column names

    # Filter out columns that are strings and exclude the label column
    non_string_columns = df.columns[(df.dtypes != object) | (df.columns == df.columns[label_column_index])]
    selected_feature_columns = [col for col in feature_column_names if col in non_string_columns]

    # Extract the selected features (X_train)
    X_train = df[selected_feature_columns]

    # Extract labels (Y_train) from the second column
    Y_train = df.iloc[:, label_column_index]


    return X_train, Y_train


if __name__ == "__main__":

    X_train, Y_train = load_dataset()

    #initiating class
    pred_model = TitanicClassificationModel(classifier='random_forest')

    # train model
    pred_model.train_model(X_train, Y_train)

    # Save the trained model
    pred_model.save_model('titanic_prediction_v1.pkl')

