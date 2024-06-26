import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

# Load the dataset
file_path = '../data/all-ages.csv'
df = pd.read_csv(file_path, usecols=['P25th', 'P75th', 'Median'])

# Drop rows with missing values
df = df.dropna()

# Split features and target
x_df = df.drop(columns=['Median'], axis=1)
y_df = df['Median']

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.25, random_state=42)

# Train the model
model = LinearRegression()
model.fit(x_train, y_train)

# Make predictions on the testing set
prediction_test = model.predict(x_test)

# Save the trained model
with open('modelSalary.pkl', 'wb') as file:
    pickle.dump(model, file)

model = pickle.load(open('modelSalary.pkl', 'rb'))