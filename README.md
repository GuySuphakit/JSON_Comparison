# JSON Comparison Tool

This Python project provides a tool to compare two JSON files and generate a list of actions required to transform the source JSON into the target JSON. It is designed for scenarios where you need to identify differences between two JSON structures and automate the process of updating one JSON file to match another.

## Folder Structure

```
├── README.md
├── requirements.txt
├── configs
│   ├── answer.json         # Output JSON file with differences
│   ├── source.json         # Source JSON file
│   └── target.json         # Target JSON file
├── poetry.lock
├── pyproject.toml
├── src
│   ├── __init__.py
│   └── main.py             # Main script with JSON comparison functions
└── tests
    ├── __init__.py
    └── test_main.py        # Unit and integration tests for the JSON comparison tool
```

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/GuySuphakit/JSON_Comparison.git
   cd JSON_Comparison
   ```

2. **Install dependencies:**

   If you are using Poetry (recommended):

   ```sh
   poetry install
   ```

   Alternatively, if you prefer `pip`:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

To compare two JSON files and generate a list of actions to transform the source JSON into the target JSON, follow these steps:

1. Prepare Your JSON Files:

   - Place your JSON files in the `configs` directory.
   - By default, the tool expects the files to be named `source.json` and `target.json`.

2. Run the Comparison:

   Using Poetry:

   ```sh
   poetry run python -m src.main
   ```

   This command will read `source.json` and `target.json`, perform the comparison, and write the results to `answer.json` in the `configs` directory.

   Using Pip (if you prefer):

   ```sh
   python -m src.main
   ```

   Ensure that you have installed the necessary dependencies listed in `requirements.txt` before running this command.

3. Verify the Output:
   - The comparison results will be saved in `configs/answer.json`.
   - Review the `answer.json` file to see the list of actions required to transform the source JSON into the target JSON.

**Note:** If you wish to use different file paths or names, update the `SOURCE_FILE`, `TARGET_FILE`, and `OUTPUT_FILE` variables in the `src/main.py` script accordingly.

---

### Custom File Paths

If you want to specify different paths for your JSON files, you can modify the paths in the `run_json_comparison` function in `src/main.py`.

```python
if __name__ == "__main__":
    SOURCE_FILE = "your/source/file.json"
    TARGET_FILE = "your/target/file.json"
    OUTPUT_FILE = "your/output/file.json"
    run_json_comparison(SOURCE_FILE, TARGET_FILE, OUTPUT_FILE)
```

## Testing

Unit tests and an integration test are provided in the `tests` directory. To run the tests:

```sh
pytest
```

This will execute all tests in the `tests` directory, ensuring the correctness of the JSON comparison functionality.

---
