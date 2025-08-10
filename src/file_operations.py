"""
File operations and I/O utilities.
"""

import os
import json
import csv
from typing import List, Dict, Any, Optional
from pathlib import Path


def read_text_file(file_path: str, encoding: str = 'utf-8') -> str:
    """
    Read contents of a text file.
    
    Args:
        file_path (str): Path to the file
        encoding (str): File encoding (default: utf-8)
        
    Returns:
        str: File contents
        
    Example:
        >>> content = read_text_file('example.txt')
    """
    with open(file_path, 'r', encoding=encoding) as file:
        return file.read()


def write_text_file(file_path: str, content: str, encoding: str = 'utf-8') -> None:
    """
    Write content to a text file.
    
    Args:
        file_path (str): Path to the file
        content (str): Content to write
        encoding (str): File encoding (default: utf-8)
        
    Example:
        >>> write_text_file('output.txt', 'Hello, World!')
    """
    with open(file_path, 'w', encoding=encoding) as file:
        file.write(content)


def append_to_file(file_path: str, content: str, encoding: str = 'utf-8') -> None:
    """
    Append content to a text file.
    
    Args:
        file_path (str): Path to the file
        content (str): Content to append
        encoding (str): File encoding (default: utf-8)
        
    Example:
        >>> append_to_file('log.txt', 'New log entry\\n')
    """
    with open(file_path, 'a', encoding=encoding) as file:
        file.write(content)


def read_json_file(file_path: str) -> Any:
    """
    Read and parse a JSON file.
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        Any: Parsed JSON data
        
    Example:
        >>> data = read_json_file('config.json')
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json_file(file_path: str, data: Any, indent: Optional[int] = 2) -> None:
    """
    Write data to a JSON file.
    
    Args:
        file_path (str): Path to the JSON file
        data (Any): Data to write
        indent (Optional[int]): JSON indentation (default: 2)
        
    Example:
        >>> write_json_file('output.json', {'key': 'value'})
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=indent, ensure_ascii=False)


def read_csv_file(file_path: str, delimiter: str = ',') -> List[Dict[str, str]]:
    """
    Read CSV file and return list of dictionaries.
    
    Args:
        file_path (str): Path to the CSV file
        delimiter (str): CSV delimiter (default: ',')
        
    Returns:
        List[Dict[str, str]]: List of rows as dictionaries
        
    Example:
        >>> data = read_csv_file('data.csv')
    """
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        return list(reader)


def write_csv_file(file_path: str, data: List[Dict[str, Any]], delimiter: str = ',') -> None:
    """
    Write data to a CSV file.
    
    Args:
        file_path (str): Path to the CSV file
        data (List[Dict[str, Any]]): Data to write
        delimiter (str): CSV delimiter (default: ',')
        
    Example:
        >>> data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        >>> write_csv_file('people.csv', data)
    """
    if not data:
        return
    
    fieldnames = data[0].keys()
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=delimiter)
        writer.writeheader()
        writer.writerows(data)


def file_exists(file_path: str) -> bool:
    """
    Check if a file exists.
    
    Args:
        file_path (str): Path to check
        
    Returns:
        bool: True if file exists, False otherwise
        
    Example:
        >>> file_exists('config.json')
        True
    """
    return os.path.isfile(file_path)


def create_directory(dir_path: str) -> None:
    """
    Create directory if it doesn't exist.
    
    Args:
        dir_path (str): Directory path to create
        
    Example:
        >>> create_directory('new_folder/subfolder')
    """
    os.makedirs(dir_path, exist_ok=True)


def list_files(directory: str, extension: Optional[str] = None) -> List[str]:
    """
    List files in a directory, optionally filtered by extension.
    
    Args:
        directory (str): Directory to list
        extension (Optional[str]): File extension filter (e.g., '.txt')
        
    Returns:
        List[str]: List of file paths
        
    Example:
        >>> list_files('data', '.csv')
        ['data/file1.csv', 'data/file2.csv']
    """
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if extension is None or filename.endswith(extension):
                files.append(os.path.join(root, filename))
    return files


def get_file_size(file_path: str) -> int:
    """
    Get file size in bytes.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        int: File size in bytes
        
    Example:
        >>> get_file_size('document.pdf')
        1024000
    """
    return os.path.getsize(file_path)


def copy_file(source: str, destination: str) -> None:
    """
    Copy a file from source to destination.
    
    Args:
        source (str): Source file path
        destination (str): Destination file path
        
    Example:
        >>> copy_file('original.txt', 'backup.txt')
    """
    import shutil
    shutil.copy2(source, destination)


def get_file_extension(file_path: str) -> str:
    """
    Get file extension from path.
    
    Args:
        file_path (str): File path
        
    Returns:
        str: File extension (including dot)
        
    Example:
        >>> get_file_extension('document.pdf')
        '.pdf'
    """
    return Path(file_path).suffix
