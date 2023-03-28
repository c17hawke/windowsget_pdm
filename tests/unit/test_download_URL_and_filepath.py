from windowsget_pdm import download
import pytest
from pathlib import Path
import shutil




correct_filepaths = [
    ("https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data", "x/y/test.csv"),
    ("https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data", "example.csv"),
] 

bad_filepaths = [
    ("https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data", "x/y/test"),
    ("https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data", "example"),
]


@pytest.mark.parametrize("url, filepath", correct_filepaths)
def test_correct_url_and_filepath(url, filepath):
    TEST_DIR = "test_dir"
    test_filepath = f"{TEST_DIR}/{filepath}"
    response = download(url=url, filepath=Path(test_filepath))
    assert isinstance(response, int)
    assert Path(test_filepath).exists()
    shutil.rmtree(TEST_DIR)


@pytest.mark.parametrize("url, filepath", bad_filepaths)
def test_bad_url_and_filepath(url, filepath):
    TEST_DIR = "test_dir"
    test_filepath = f"{TEST_DIR}/{filepath}"
    with pytest.raises(ValueError):
        response = download(url=url, filepath=Path(test_filepath))
    shutil.rmtree(TEST_DIR)

