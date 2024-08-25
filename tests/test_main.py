import json

import pytest

from src.main import compare_jsons, read_json_file, write_json_file

# Test data
source_data = {
    "event": {
        "name": "Global Music Festival",
        "location": {"city": "Tokyo", "country": "Hokkaido"},
    }
}

target_data = {
    "event": {
        "name": "Global Music Festival",
        "date": "2024-08-10",
        "location": {"city": "Tokyo", "country": "Japan"},
    }
}

expected_result = [
    {
        "operation": "add_new_key",
        "value": {"date": "2024-08-10"},
        "parent_key": ["event"],
        "after_key": "name",
    },
    {
        "operation": "modify_value",
        "value": {"country": "Japan"},
        "parent_key": ["event", "location"],
        "after_key": "city",
    },
]


def test_compare_jsons():
    result = compare_jsons(source_data, target_data)
    assert result == expected_result


def test_compare_jsons_empty():
    assert compare_jsons({}, {}) == []


def test_compare_jsons_identical():
    assert compare_jsons(source_data, source_data) == []


def test_compare_jsons_nested():
    source = {"a": {"b": {"c": 1}}}
    target = {"a": {"b": {"c": 2, "d": 3}}}
    expected = [
        {
            "operation": "modify_value",
            "value": {"c": 2},
            "parent_key": ["a", "b"],
            "after_key": None,
        },
        {
            "operation": "add_new_key",
            "value": {"d": 3},
            "parent_key": ["a", "b"],
            "after_key": "c",
        },
    ]
    assert compare_jsons(source, target) == expected


def test_compare_jsons_invalid_input():
    with pytest.raises(TypeError):
        compare_jsons([], {})
    with pytest.raises(TypeError):
        compare_jsons({}, [])


def test_read_json_file(tmp_path):
    file_path = tmp_path / "test.json"
    with open(file_path, "w") as f:
        json.dump(source_data, f)

    assert read_json_file(str(file_path)) == source_data


def test_read_json_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_json_file("nonexistent.json")


def test_read_json_file_invalid_json(tmp_path):
    file_path = tmp_path / "invalid.json"
    with open(file_path, "w") as f:
        f.write("This is not valid JSON")

    with pytest.raises(json.JSONDecodeError):
        read_json_file(str(file_path))


def test_write_json_file(tmp_path):
    file_path = tmp_path / "output.json"
    write_json_file(str(file_path), expected_result)

    with open(file_path, "r") as f:
        assert json.load(f) == expected_result


# Integration test
def test_end_to_end(tmp_path):
    source_path = tmp_path / "source.json"
    target_path = tmp_path / "target.json"
    output_path = tmp_path / "output.json"

    with open(source_path, "w") as f:
        json.dump(source_data, f)
    with open(target_path, "w") as f:
        json.dump(target_data, f)

    # Mock the main function
    import sys

    from src.main import run_json_comparison

    sys.argv = ["main.py"]  # Reset sys.argv

    # Monkey-patch the file paths
    import src.main

    src.main.SOURCE_FILE = str(source_path)
    src.main.TARGET_FILE = str(target_path)
    src.main.OUTPUT_FILE = str(output_path)

    run_json_comparison()

    with open(output_path, "r") as f:
        assert json.load(f) == expected_result


if __name__ == "__main__":
    pytest.main()
