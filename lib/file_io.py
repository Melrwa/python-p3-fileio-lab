from pathlib import Path  # Import Path for handling file paths in an object-oriented way

def write_file(file_name, file_content):
    """
    Creates a new text file (or overwrites an existing one) and writes the given content to it.
    
    Args:
        file_name (str or Path): The name or path of the file (without extension).
        file_content (str): The content to write to the file.
    """
    file_name = Path(file_name).with_suffix(".txt")  # Ensure the file has a .txt extension
    with open(file_name, "w") as file:  # Open the file in write mode
        file.write(file_content)  # Write the content to the file

def append_file(file_name, append_content):
    """
    Appends content to an existing text file. If the file doesn't exist, it creates one.
    
    Args:
        file_name (str or Path): The name or path of the file (without extension).
        append_content (str): The content to append to the file.
    """
    file_name = Path(file_name).with_suffix(".txt")  # Ensure the file has a .txt extension
    with open(file_name, "a") as file:  # Open the file in append mode
        file.write(append_content)  # Append the new content to the file

def read_file(file_name):
    """
    Reads and returns the content of a text file.
    
    Args:
        file_name (str or Path): The name or path of the file (without extension).
    
    Returns:
        str: The content of the file.
    """
    file_name = Path(file_name).with_suffix(".txt")  # Ensure the file has a .txt extension
    with open(file_name, "r") as file:  # Open the file in read mode
        return file.read()  # Read and return the content of the file
