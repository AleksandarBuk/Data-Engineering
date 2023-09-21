# Sort Continuous Ad Segments

import os
import json
import click

@click.command()
@click.argument('directory', type=click.Path(exists=True), metavar='DIRECTORY', required=False)
def process_json_files(directory):
    if directory is None:
        directory = 'Files'

    output_directory = f"{directory}"
    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)

            with open(file_path, 'r') as json_file:
                data = json.load(json_file)

                segments = data['segments']

                segment_chains = []
                frame_counts = []
                current_chain = 0
                segment_count = 0
                segment_length = 0

                for segment in segments:
                    segment_type = segment['type']
                    segment_start = segment['start_frame']
                    segment_end = segment['end_frame']

                    if segment_type == 'Ad':
                        segment_length = segment_end - segment_start
                        segment_count += 1
                        frame_counts.append(segment_length)

                    else:
                        if segment_count > 0:
                            segment_chains.append(segment_count)
                            current_chain += 1
                            segment_count = 0

                if segment_count > 0:
                    segment_chains.append(segment_count)

            # Modify frame_counts to accumulate frames within chained segments
            updated_frame_counts = []
            current_chain_frame_count = 0
            for i, chain_count in enumerate(segment_chains):
                chain_frames = frame_counts[current_chain_frame_count:current_chain_frame_count + chain_count]
                total_frames_in_chain = sum(chain_frames)
                updated_frame_counts.append(total_frames_in_chain)
                current_chain_frame_count += chain_count

            result = {
                filename: {
                    'frames': updated_frame_counts,
                    'count_tv': segment_chains
                }
            }

            # Create a new output directory with _CAS suffix
            new_output_directory = f"{directory}_CAS"
            os.makedirs(new_output_directory, exist_ok=True)

            output_filename = os.path.join(
                new_output_directory, f"{os.path.splitext(filename)[0]}_output.json")
            with open(output_filename, 'w') as output_file:
                json.dump(result, output_file)

if __name__ == '__main__':
    process_json_files()
