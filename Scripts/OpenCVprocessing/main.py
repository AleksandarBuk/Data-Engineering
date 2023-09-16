import cv2
import json
import os
from tqdm import tqdm


# Load and Extract Frames

target_width = 120  # Set your desired width
target_height = 120  # Set your desired height

def main(video_path, output_json_file):
    try:
        # Open the video file for reading
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print("Error: Could not open video file.")
            return

        frame_list = []  # List to store frame dictionaries

        # Create the output directory if it doesn't exist
        # if not os.path.exists(output_dir):
        #     os.makedirs(output_dir)

        frame_number = 0
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Get total number of frames

        # Progress bar
        progress_bar = tqdm(total=total_frames, desc="Processing Frames", unit="frames")

        while True:
            ret, frame = cap.read()

            if not ret:
                break  # Reached the end of the video

            frame = cv2.resize(frame, (target_width, target_height))


            # Get the timestamp of the frame (in milliseconds)
            timestamp_ms = int(cap.get(cv2.CAP_PROP_POS_MSEC))

            # Convert the frame to a list of pixel values
            frame_data = frame.tolist()

            # Create a dictionary to store frame information
            frame_info = {
                "frame_number": frame_number,
                "timestamp_ms": timestamp_ms,
                "frame_data": frame_data
            }

            frame_list.append(frame_info)

            # Save the frame data as a JSON file
            # frame_json_path = os.path.join(output_dir, f"frame_{frame_number}.json")
            try:
                with open(output_json_file, "w") as json_file:
                    json.dump(frame_list, json_file, indent=4)

            except IOError as e:
                print(f"Error saving frame {frame_number} as JSON: {e}")

            frame_number += 1
            progress_bar.update(1)  # Update Progress Bar

        # Close Progress Bar
        progress_bar.close()

        # Release the video capture object and close the video file
        cap.release()
        cv2.destroyAllWindows()

        print(f"Frames saved as JSON files in {output_json_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    video_path = "./mp4/test.mp4"  # Replace with your video file path
    output_json_file = "frames.json"  # JSON file to save all frames

    main(video_path, output_json_file)
