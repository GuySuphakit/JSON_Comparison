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
   git clone <repository-url>
   cd <repository-folder>
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

1. Place your JSON files in the `configs` directory. By default, the tool expects `source.json` and `target.json` files in this directory.

2. Run the comparison:

   ```sh
   python -m src.main
   ```

   This will read `source.json` and `target.json`, compare them, and output the results to `answer.json` in the `configs` directory.

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
