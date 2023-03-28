from windowsget_pdm import download
import pytest
from pathlib import Path
from requests.exceptions import HTTPError
import os

correct_urls = [
    "https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data"
] 

bad_urls = [
    "https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing",
    "https://raw.githubusercontent.com/c17hawke/raw_data/main/xyz"
]

@pytest.mark.parametrize("url", correct_urls)
def test_correct_urls_only(url):
    filepath = Path(url).name
    response = download(url=url, filepath=Path(filepath))
    assert isinstance(response, int)
    os.remove(Path(filepath))

@pytest.mark.parametrize("url", bad_urls)
def test_bad_urls_only(url):
    filepath = Path(url).name
    with pytest.raises(HTTPError):
        response = download(url=url, filepath=Path(filepath))
