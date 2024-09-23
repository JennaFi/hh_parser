from unittest.mock import patch

import pytest
import requests

from src.api.base_parser import BaseParser
from src.api.parser import HHParser


def test_base_parser():
    BaseParser.load_vacancies('test')

def test_load_vacancies(get_request, get_vacancies_upload):
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = get_request
        assert HHParser.load_vacancies("test") == get_vacancies_upload


def test_load_vacancies_exception():
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 201
        with pytest.raises(requests.RequestException):
            HHParser.load_vacancies("test")