# Sort Segment Types

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

                chain_types = []

                for segment in segments:
                    segment_type = segment['type']

                    chain_types.append(segment_type)

            result = {
                filename: {
                    'types': chain_types,
                }
            }

            # Create a new output directory with _CAS suffix
            new_output_directory = f"{directory}_SST"
            os.makedirs(new_output_directory, exist_ok=True)

            output_filename = os.path.join(
                new_output_directory, f"{os.path.splitext(filename)[0]}_output.json")
            with open(output_filename, 'w') as output_file:
                json.dump(result, output_file)

if __name__ == '__main__':
    process_json_files()
