import os
import json
import click


@click.command()
@click.argument('directory', type=click.Path(exists=True), metavar='DIRECTORY')
def process_json_files(directory):
    output_directory = f"{directory}_counted"
    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)

            with open(file_path, 'r') as json_file:
                data = json.load(json_file)

                segments = data['segments']

                segment_chains = []
                segment_counts = []
                current_chain = 0
                segment_count = 0

                for segment in segments:
                    segment_type = segment['type']

                    if segment_type == 'TV':
                        segment_count += 1
                    else:
                        if segment_count > 0:
                            segment_chains.append(segment_count)
                            current_chain += 1
                            segment_count = 0

                if segment_count > 0:
                    segment_chains.append(segment_count)

                segment_counts.append(len(segment_chains))

            result = {
                filename: {
                    'frames': segment_chains,
                    'segments-chained': segment_counts
                }
            }

            output_filename = os.path.join(
                output_directory, f"{os.path.splitext(filename)[0]}_output.json")
            with open(output_filename, 'w') as output_file:
                json.dump(result, output_file)


if __name__ == '__main__':
    process_json_files()
