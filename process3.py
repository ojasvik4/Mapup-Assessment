# -*- coding: utf-8 -*-
"""Process3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/129o7BUfYIBA5_1WTeOhrAF3zQBbf1LUV

**Process 3: Extracting Toll Information from JSON Files**
"""

import os
import json

def process_toll_information(input_directory):
    # Check if the input directory exists
    if not os.path.exists(input_directory):
        print(f"Error: The specified directory '{input_directory}' does not exist.")
        return

    # Process each file in the input directory
    for filename in os.listdir(input_directory):
        # Check if the file has a JSON extension
        if filename.endswith(".json"):
            file_path = os.path.join(input_directory, filename)
            print(f"Processing file: {file_path}")

            # Read and parse the JSON file
            with open(file_path, "r") as file:
                try:
                    trip_data = json.load(file)
                    # Process the toll information as needed
                    process_trip_data(trip_data)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in file {file_path}: {e}")

def process_trip_data(trip_data):
    # Implement your logic to process the toll information
    # For example, you can print the details of each trip
    print("Trip Details:")
    print(f"Start Location: {trip_data['start_location']}")
    print(f"End Location: {trip_data['end_location']}")
    print(f"Toll Amount: {trip_data['toll_amount']}")
    print("\n")

input_directory = "/transformed_data.csv"

"""**Members as collaborators** venkateshn@mapup.ai namanjeetsingh@mapup.ai saranshj@mapup.ai varuna@mapup.ai"""