import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog
from collections import Counter
from datetime import datetime


# Function to read XLSX files from a directory and display them as DataFrames
def read_xlsx_files(directory_path):
    dataframes = {}

    # Check if the directory exists
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        # List all files in the directory
        files = os.listdir(directory_path)

        # Filter for XLSX files
        xlsx_files = [file for file in files if file.endswith(".xlsx")]

        if not xlsx_files:
            print("No XLSX files found in the directory.")
            return dataframes

        # Loop through XLSX files and read them into DataFrames
        for file_name in xlsx_files:
            xlsx_file_path = os.path.join(directory_path, file_name)

            try:
                df = pd.read_excel(xlsx_file_path)
                dataframes[file_name] = df
                print(f"Loaded {file_name} into a DataFrame.")
            except Exception as e:
                print(f"An error occurred while reading {file_name}: {e}")

    else:
        print("Directory does not exist.")

    return dataframes


# Function to extract most frequent words from titles
# Function to extract words with 3 or more appearances from titles and save to CSV and XLSX
def extract_most_frequent_words(dataframes):
    titles = []

    for df_name, df in dataframes.items():
        if 'title' in df.columns:
            titles.extend(df['title'])

    all_titles = ' '.join(titles)
    words = all_titles.split()
    word_counts = Counter(words)

    # Extract words with lengths between 4 and 10 characters (inclusive) and at least 3 appearances
    filtered_words = [word for word in word_counts if 4 <= len(word) <= 10 and word_counts[word] >= 3]

    if not filtered_words:
        print("No words with 3 or more appearances found.")
        return

    # Create a DataFrame from the filtered words
    words_df = pd.DataFrame(
        {'list of words': filtered_words, 'number of occurrence': [word_counts[word] for word in filtered_words]})

    # Get the current date for the file names
    today_date = datetime.now().strftime("%Y-%m-%d")

    # Save the DataFrame to CSV and XLSX files
    csv_file_name = f"{today_date}.csv"
    xlsx_file_name = f"{today_date}.xlsx"
    words_df.to_csv(csv_file_name, index_label='index')
    words_df.to_excel(xlsx_file_name, index_label='index')

    print(f"Filtered words (with 3 or more appearances) saved to '{csv_file_name}' and '{xlsx_file_name}'.")


# Function to create the main application window
def create_app_window():
    # Create a tkinter root window (GUI)
    root = tk.Tk()
    root.withdraw()  # Hide the main root window

    # Ask the user to select a directory using a file dialog
    directory_path = filedialog.askdirectory(title="Select a directory containing XLSX files")

    if not directory_path:
        print("No directory selected. Exiting.")
    else:
        loaded_dataframes = read_xlsx_files(directory_path)

        # Check if any DataFrames were loaded
        if loaded_dataframes:
            # Display the loaded DataFrames
            for file_name, df in loaded_dataframes.items():
                print(f"DataFrame for {file_name}:")
                print(df.head())

            # Extract and save most frequent words from titles
            extract_most_frequent_words(loaded_dataframes)
        else:
            print("No valid data was loaded.")


# Main function
def main():
    create_app_window()


if __name__ == "__main__":
    main()
