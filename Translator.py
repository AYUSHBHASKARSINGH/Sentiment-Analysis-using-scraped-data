# pip install googletrans==3.1.0a0

import pandas as pd
from googletrans import Translator

df = pd.read_csv('/content/Combined_with_sentiments - Combined_with_sentiments.csv.csv')
translator = Translator()
def translate_to_english(text):
    translation = translator.translate(text, dest='en')
    return translation.text

df['content_english'] = df['Content'].apply(translate_to_english)
df.to_csv('translated_file.csv', index=False)

