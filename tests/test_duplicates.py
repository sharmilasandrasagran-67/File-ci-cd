import pandas as pd
from scripts.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic(tmp_path):
    # Create a sample CSV with duplicates
    test_file = tmp_path / "test.csv"
    test_file.write_text("a,b\n1,2\n1,2\n3,4\n")

    output_file = tmp_path / "out.csv"
    df = remove_duplicates(test_file, output_file)

    # Check duplicates removed
    assert len(df) == 2

    # Verify saved file contents
    saved_df = pd.read_csv(output_file)
    assert len(saved_df) == 2


def test_remove_duplicates_empty(tmp_path):
    # Create an empty CSV
    test_file = tmp_path / "empty.csv"
    test_file.write_text("a,b\n")

    output_file = tmp_path / "out.csv"
    df = remove_duplicates(test_file, output_file)

    # Should remain empty
    assert df.empty
    saved_df = pd.read_csv(output_file)
    assert saved_df.empty


def test_remove_duplicates_all_unique(tmp_path):
    # All rows unique
    test_file = tmp_path / "unique.csv"
    test_file.write_text("a,b\n1,2\n3,4\n5,6\n")

    output_file = tmp_path / "out.csv"
    df = remove_duplicates(test_file, output_file)

    # Should keep all rows
    assert len(df) == 3
    saved_df = pd.read_csv(output_file)
    assert len(saved_df) == 3


def test_remove_duplicates_all_duplicates(tmp_path):
    # All rows identical
    test_file = tmp_path / "dupes.csv"
    test_file.write_text("a,b\n5,5\n5,5\n5,5\n")

    output_file = tmp_path / "out.csv"
    df = remove_duplicates(test_file, output_file)

    # Should keep only one row
    assert len(df) == 1
    saved_df = pd.read_csv(output_file)
    assert len(saved_df) == 1
