import os
import json

# Directory containing JSON files
json_directory = "JSONS"

# Initialize variables
highest_end_frame = 0
total_end_frame_sum = 0

# List all JSON files in the directory
json_files = [f for f in os.listdir(json_directory) if f.endswith('.json')]

for json_file in json_files:
    with open(os.path.join(json_directory, json_file), 'r') as file:
        try:
            data = json.load(file)
            scenes_and_segments = data.get('scenes[]', 'segments[]')
            get_max = 0
            print(scenes_and_segments)
            for scene_segment in scenes_and_segments:
                frame_end = scene_segment.get("frame_end")
                print(frame_end)
                if frame_end > get_max:
                    get_max = frame_end

            highest_end_frame = get_max

            max_frame = highest_end_frame
            total_end_frame_sum += max_frame
        except Exception as e:
            print(f"Error processing {json_file}: {e}")

print("Total sum of highest end_frame values:", total_end_frame_sum)