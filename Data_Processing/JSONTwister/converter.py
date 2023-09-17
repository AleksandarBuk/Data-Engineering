import json
import os
from tqdm import tqdm
from tkinter import Tk, filedialog


# Assign value to the JSON file
def assign_ids(data):
    for idx, scene in enumerate(data["scenes"]):
        scene["id"] = idx + 1

    for idx, segment in enumerate(data["segments"]):
        segment["id"] = idx + 1


# Processes the JSON file through the value assign function
def process_json_file(file_path, output_directory):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        assign_ids(data)

    filename = os.path.basename(file_path)
    output_path = os.path.join(output_directory, filename)

    with open(output_path, "w") as json_file:
        json.dump(data, json_file, indent=4)


# processes directory with JSON files
def process_directory(input_directory, output_directory):
    for filename in tqdm(os.listdir(input_directory), desc="Processing JSON files"):
        if filename.endswith(".json"):
            file_path = os.path.join(input_directory, filename)
            process_json_file(file_path, output_directory)


if __name__ == "__main__":
    root = Tk()
    root.withdraw()

    input_directory = filedialog.askdirectory(title="Select a directory with JSON files")
    if not input_directory:
        print("No input directory selected. Exiting.")
    else:
        output_directory = filedialog.askdirectory(title="Select an output directory")
        if not output_directory:
            print("No output directory selected. Exiting.")
        else:
            process_directory(input_directory, output_directory)
            print("All JSON files processed and saved to the output directory.")
