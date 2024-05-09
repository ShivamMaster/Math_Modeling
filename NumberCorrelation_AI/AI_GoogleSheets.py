from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np

# Training data
training_data = []

# Function to add a sequence to training data
def add_sequence(sequence):
  training_data.append(sequence)

# Function to convert sequence to model input format
def to_model_input(sequence):
  # One-hot encode each number (modify if needed)
  encoded_sequence = []
  for num in sequence:
    one_hot = [0] * 10  # Assuming numbers are 0-9
    one_hot[num] = 1
    encoded_sequence.append(one_hot)
  return np.array([encoded_sequence])

# Define and train the model
model = Sequential()
model.add(LSTM(128, return_sequences=True, input_shape=(11, 10)))
model.add(LSTM(64))
model.add(Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Add your training data here (call add_sequence multiple times)
# ... (replace with your training data)

# Train the model on the provided data
model.fit(np.array([seq[:11] for seq in training_data]), np.array([seq[11] for seq in training_data]), epochs=10)

# Function to predict next number
def predict_next(sequence):
  input_data = to_model_input(sequence)
  prediction = model.predict(input_data)
  return np.argmax(prediction[0])

# Function to run the test loop
def test_sequence():
  sequence = []
  for i in range(11):
    num = int(input(f"Enter number {i+1} of the sequence: "))
    sequence.append(num)

  correct = 0
  for i in range(11, 21):
    prediction = predict_next(sequence[:i])
    print(f"Guess for number {i+1}: {prediction}")
    actual_num = int(input("Enter the actual number: "))
    if prediction == actual_num:
      correct += 1
    sequence.append(actual_num)

  success_rate = correct / 10
  print(f"Success Rate: {success_rate:.2f}")

# Run the test loop
test_sequence()
