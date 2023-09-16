import cv2
import json
from tqdm import tqdm

# Set your desired target resolution
target_width = 120
target_height = 120
frames_per_second = 30  # Frames per second in the video

def main(video_path, output_json_file):
    try:
        # Open the video file for reading
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print("Error: Could not open video file.")
            return

        frame_number = 0
        frame_list = []

        # Get the total number of frames and frames per second
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Create a progress bar
        progress_bar = tqdm(total=total_frames, desc="Processing Frames", unit="frames")

        while True:
            ret, frame = cap.read()

            if not ret:
                break  # Reached the end of the video

            # Resize the frame to the target resolution
            frame = cv2.resize(frame, (target_width, target_height))

            # Calculate the frame timestamp in milliseconds
            timestamp_ms = (frame_number * 1000) / fps

            # Calculate the second in which the frame appears
            frame_second = timestamp_ms / 1000.0

            # Create a dictionary to represent the frame
            frame_info = {
                "frame_number": frame_number,
                "second": frame_second,
                "timestamp_ms": timestamp_ms
            }

            frame_list.append(frame_info)

            frame_number += 1
            progress_bar.update(1)  # Update Progress Bar

        # Close Progress Bar
        progress_bar.close()

        # Release the video capture object and close the video file
        cap.release()

        # Create a JSON object with "frames" containing the frame list
        json_data = {"frames": frame_list}

        # Save the JSON data to the output file
        with open(output_json_file, "w") as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"Frames saved as JSON file: {output_json_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_path = "./mp4/test.mp4"  # Replace with your video file path
    output_json_file = "frames.json"  # JSON file to save all frames

    main(video_path, output_json_file)
