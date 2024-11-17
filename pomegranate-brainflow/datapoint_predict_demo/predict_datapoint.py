import keras
import numpy as np
import pandas as pd

filepath = 'custom_model.keras'
model = keras.saving.load_model(filepath)

# TEST DATA
data = pd.read_csv('test_data.csv')
# CUSTOM DATA
# data = pd.read_csv('custom_emotions.csv')
# data = data.iloc[:10, :-1]
print(data)

# ALL AT ONCE
X_test = data.values 
X_test = X_test.reshape(data.shape[0], data.shape[1], 1) 
predictions = model.predict(X_test)
# For softmax (multiclass classification):
predicted_labels = predictions.argmax(axis=1)
print("Predicted labels:", predicted_labels)

# # ONE AT A TIME (BROKEN)
# for i, row in data.iterrows():
#     if i==0:
#         continue
#     if i > 10:
#         break
#     sample = row.iloc[:-1].values.reshape(1, -1, 1)  # Reshape a single sample
#     prediction = model.predict(sample)
#     predicted_label = prediction.argmax(axis=1)  # For multiclass
#     print(f"Row {i} predicted label: {predicted_label}")

