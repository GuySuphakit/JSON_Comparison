import json
import logging
import sys
from typing import Any, Dict, List, Optional

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)




def compare_jsons(
    source: Dict[str, Any],
    target: Dict[str, Any],
    parent_keys: List[str] = [],
    prev_key: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """
    Recursively compare two JSON objects and generate a list of actions to transform the source into the target.

    Args:
    source (Dict[str, Any]): The source JSON object.
    target (Dict[str, Any]): The target JSON object.
    parent_keys (List[str], optional): List of parent keys for nested structures. Defaults to [].
    prev_key (Optional[str], optional): The previous key in the current level. Defaults to None.

    Returns:
    List[Dict[str, Any]]: A list of action items, each containing:
        - operation: Either 'add_new_key' or 'modify_value'
        - value: The value to be added or modified
        - parent_key: List of parent keys
        - after_key: The key after which the operation should be performed

    Raises:
    TypeError: If source or target are not dictionaries.
    """
    if not isinstance(source, dict) or not isinstance(target, dict):
        raise TypeError("Both source and target must be dictionaries")

    actions = []

    for key, target_value in target.items():
        try:
            if key not in source:
                logger.info(f"Adding new key: {key} at path: {'.'.join(parent_keys)}")
                actions.append(
                    {
                        "operation": "add_new_key",
                        "value": {key: target_value},
                        "parent_key": parent_keys,
                        "after_key": prev_key,
                    }
                )
            elif isinstance(target_value, dict) and isinstance(source[key], dict):
                actions.extend(
                    compare_jsons(source[key], target_value, parent_keys + [key], None)
                )
            elif source[key] != target_value:
                logger.info(
                    f"Modifying value for key: {key} at path: {'.'.join(parent_keys)}"
                )
                actions.append(
                    {
                        "operation": "modify_value",
                        "value": {key: target_value},
                        "parent_key": parent_keys,
                        "after_key": prev_key,
                    }
                )
            prev_key = key
        except Exception as e:
            logger.error(f"Error processing key {key}: {str(e)}")
            raise

    return actions


def read_json_file(file_path: str) -> Dict[str, Any]:
    """
    Read and parse a JSON file.

    Args:
    file_path (str): Path to the JSON file.

    Returns:
    Dict[str, Any]: Parsed JSON data.

    Raises:
    FileNotFoundError: If the file doesn't exist.
    json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in file {file_path}: {str(e)}")
        raise


def write_json_file(file_path: str, data: List[Dict[str, Any]]) -> None:
    """
    Write data to a JSON file.

    Args:
    file_path (str): Path to the output JSON file.
    data (List[Dict[str, Any]]): Data to write.

    Raises:
    IOError: If there's an error writing to the file.
    """
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        logger.info(f"Results written to {file_path}")
    except IOError as e:
        logger.error(f"Error writing to file {file_path}: {str(e)}")
        raise


def run_json_comparison(source_file: str, target_file: str, output_file: str) -> None:
    """
    Main function to read source and target JSON files, compare them, and write the results to an output file.

    Args:
    source_file (str): Path to the source JSON file.
    target_file (str): Path to the target JSON file.
    output_file (str): Path to the output JSON file where the results will be written.
    """
    try:
        source = read_json_file(source_file)
        target = read_json_file(target_file)

        logger.info("Starting JSON comparison")
        result = compare_jsons(source, target)
        logger.info(f"Comparison complete. Found {len(result)} differences")

        write_json_file(output_file, result)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    SOURCE_FILE = "configs/source.json"
    TARGET_FILE = "configs/target.json"
    OUTPUT_FILE = "configs/answer.json"
    run_json_comparison(SOURCE_FILE, TARGET_FILE, OUTPUT_FILE)
