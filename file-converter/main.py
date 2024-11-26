import os
import pandas as pd

filepath = "./input/"


def convert_to_csv(df, output_path):

    df.to_csv(output_path, index=False)
    print(f"File saved as CSV: {output_path}")


def convert_to_json(df, output_path):

    df.to_json(output_path, orient="records", lines=True)
    print(f"File saved as JSON: {output_path}")


def convert_to_excel(df, output_path):

    df.to_excel(output_path, index=False)
    print(f"File saved as Excel: {output_path}")


def request_conversion_type(df, filename):

    print(f"Choose the file format to convert {df}:")
    print("1. CSV")
    print("2. JSON")
    print("3. Excel")

    choice = input("Enter the number of your choice: ").strip()
    name = os.path.splitext(filename)[0]

    if choice == '1':
        convert_to_csv(df, f"{name}")
    elif choice == '2':
        convert_to_json(df, f"{name}")
    elif choice == '3':
        convert_to_excel(df, f"{name}")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


def read_file(filename):

    if filename.endswith('.csv'):
        file = pd.read_csv(filepath + filename)
    elif filename.endswith('.xlsx') or filename.endswith('.xls'):
        file = pd.read_excel(filepath + filename)
    elif filename.endswith('.json'):
        file = pd.read_json(filepath + filename)
    else:
        print("File type not supported")
    return request_conversion_type(file, filename)


if __name__ == '__main__':

    for file in os.listdir(filepath):
        print(f"Loading file: {file}")
        read_file(file)
