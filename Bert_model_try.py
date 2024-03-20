# import torch
# import numpy as np
# import pandas as pd
# import transformers as ppb
# import pickle

# # Load the trained logistic regression model
# with open('logistic_regression_model.pkl', 'rb') as f:
#     loaded_model = pickle.load(f)

# # Load pretrained model/tokenizer
# tokenizer_class = ppb.DistilBertTokenizer
# pretrained_weights = 'distilbert-base-uncased'
# tokenizer = tokenizer_class.from_pretrained(pretrained_weights)
# model_class = ppb.DistilBertModel
# model = model_class.from_pretrained(pretrained_weights)

# # Define the scraper data
# scraper_data = [
#     "This is a positive sentence.",
#     "I'm feeling happy today.",
#     "This is a negative sentence.",
#     "I'm not satisfied with the service."
# ]

# # Tokenize and preprocess the new text data
# tokenized_scraper_data = [tokenizer.encode(text, add_special_tokens=True) for text in scraper_data]
# max_len = max(len(token_ids) for token_ids in tokenized_scraper_data)
# padded_scraper_data = np.array([ids + [0]*(max_len-len(ids)) for ids in tokenized_scraper_data])
# attention_mask_scraper_data = np.where(padded_scraper_data != 0, 1, 0)

# # Convert the preprocessed data to PyTorch tensors
# input_ids_scraper_data = torch.tensor(padded_scraper_data)
# attention_mask_scraper_data = torch.tensor(attention_mask_scraper_data)

# # Get the last hidden states from the DistilBERT model
# with torch.no_grad():
#     last_hidden_states_scraper_data = model(input_ids_scraper_data, attention_mask=attention_mask_scraper_data)

# # Extract features from the last hidden states
# features_scraper_data = last_hidden_states_scraper_data[0][:, 0, :].numpy()

# # Use the loaded logistic regression model to predict sentiment
# predicted_sentiments = loaded_model.predict(features_scraper_data)

# # Print the predicted sentiments
# for text, sentiment in zip(scraper_data, predicted_sentiments):
#     print(f'Text: {text} | Predicted Sentiment: {"Positive" if sentiment == 1 else "Negative"}')






import torch
import numpy as np
import pandas as pd
import transformers as ppb
import pickle

# Load the trained logistic regression model
with open('logistic_regression_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Load pretrained model/tokenizer
tokenizer_class = ppb.DistilBertTokenizer
pretrained_weights = 'distilbert-base-uncased'
tokenizer = tokenizer_class.from_pretrained(pretrained_weights)
model_class = ppb.DistilBertModel
model = model_class.from_pretrained(pretrained_weights)

# Load the CSV file into a DataFrame
df = pd.read_csv('modified_file.csv')
# df = df.dropna()
print(df.head)
# Tokenize and preprocess the text data
tokenized_data = df['CONTENT'].apply(lambda x: tokenizer.encode(x, add_special_tokens=True))

max_len = max(len(token_ids) for token_ids in tokenized_data)
padded_data = np.array([ids + [0]*(max_len-len(ids)) for ids in tokenized_data])
attention_mask_data = np.where(padded_data != 0, 1, 0)

# Convert the preprocessed data to PyTorch tensors
input_ids_data = torch.tensor(padded_data)
attention_mask_data = torch.tensor(attention_mask_data)

# Get the last hidden states from the DistilBERT model
with torch.no_grad():
    last_hidden_states_data = model(input_ids_data, attention_mask=attention_mask_data)

# Extract features from the last hidden states
features_data = last_hidden_states_data[0][:, 0, :].numpy()

# Use the loaded logistic regression model to predict sentiment
predicted_sentiments = loaded_model.predict(features_data)

# Update the label column with the predicted sentiments
# df['Label'] = ['Positive' if sentiment == 1 else 'Negative' for sentiment in predicted_sentiments]

df['LABEL'] = ['Positive' if sentiment == 1 else 'Neutral' if sentiment == 0 else 'Negative' for sentiment in predicted_sentiments]

# Save the modified DataFrame back to a new CSV file
df.to_csv('Combined_with_sentiments.csv', index=False)

actual_labels = df['LABEL'].values

# Convert the actual labels to numerical format for comparison with predictions
label_map = {"Positive": 1, "Negative": -1, "Neutral": 0}
actual_labels_numeric = np.array([label_map[label] for label in actual_labels])

# Calculate the accuracy of the model
accuracy = (predicted_sentiments == actual_labels_numeric).mean()

print("Accuracy:", accuracy)