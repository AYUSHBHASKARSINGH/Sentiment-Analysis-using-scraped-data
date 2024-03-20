import csv
csv_file_path = 'Combined.csv'
output_file_path = 'output_sentences.txt'  # Path to the output text file

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        
        # Assuming "Content" is the column containing the sentences
        for row in csv_reader:
            content = row['Content']
            sentences = content.split('.')  # Split content into sentences based on period (you may use a more sophisticated sentence tokenizer here)
            
            # Write each sentence to the output file
            for sentence in sentences:
                output_file.write(sentence.strip() +'\n\n')  # Write sentence followed by a new line

# Print a message indicating the process is done
print("Sentences extracted and saved to:", output_file_path)
