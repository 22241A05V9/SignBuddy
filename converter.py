import os


def rename_files_in_directory(directory):
    # Get all the files in the directory
    for filename in os.listdir(directory):
        # Check if the file has spaces in its name
        if ' ' in filename:
            # Define the new filename with spaces replaced by underscores
            new_filename = filename.replace(' ', '_')

            # Get the full path to the file
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")
        else:
            print(f"No space in: {filename}")


# Example usage
directory = r"C:\Users\ruthv\Desktop\MPS 2\MPS_2\static\ISL_Gif"  # Replace this with your actual directory path
rename_files_in_directory(directory)
