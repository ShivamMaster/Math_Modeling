from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Training data (assuming sequences of 11 numbers with target at index 11)
training_data = [[7, 8, 9, 5, 6, 4, 1, 4, 3, 2, 2, 0, 0, 8, 0, 4, 8, 4, 0, 6, 8],
                 [1, 2, 3, 4, 5, 6]]  # Example with a shorter sequence

# Function to convert sequence to model input format (one-hot encoding with padding)
def to_model_input(sequence, max_len=11):  # Define max sequence length here
  encoded_sequence = []
  for num in sequence:
    one_hot = [0] * 10
    one_hot[num] = 1
    encoded_sequence.append(one_hot)
  # Pad shorter sequences with zeros
  padded_sequence = pad_sequences([encoded_sequence], maxlen=max_len, padding='post')
  return padded_sequence[0]  # Return the first element (single sequence)

# Define the model
model = Sequential([
  LSTM(128, return_sequences=True, input_shape=(11, 10)),  # Specify input shape here
  LSTM(64),
  Dense(10, activation='softmax')
])

# Compile the model before training (specifying loss, optimizer, and metrics)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Handle potential data structure issues:

# Option 1: Single Long Sequence (modify if your data is different)
if len(training_data[0]) > 11:  # Check if single sequence is longer than 11 elements
  sequence_length = 11  # Number of elements per sequence
  sequences = []
  for i in range(0, len(training_data[0]), sequence_length):
    sequences.append(training_data[0][i:i+sequence_length])  # Extract subsequences
  x_train = np.array([to_model_input(seq) for seq in sequences])  # Convert and reshape

# Option 2: Flattened Data (modify if your data structure is a single list)
else:
  num_sequences = len(training_data)  # Assuming each element in data is a sequence
  x_train = np.array([to_model_input(seq) for seq in training_data])

# Handle sequences with potentially different lengths for target labels
y_train = np.array([seq[11] if len(seq) > 11 else None for seq in training_data])  # Target labels

# Train the model on the prepared data
model.fit(x_train, y_train, epochs=10)

# Function to predict next number (assuming same data format)
def predict_next(sequence):
  input_data = to_model_input(sequence)
  prediction = model.predict(input_data)
  return np.argmax(prediction[0])

# Function to run the test loop (you can modify this as needed)
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
