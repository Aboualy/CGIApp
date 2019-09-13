"""
test_handleurl.py
"""
import pytest
from unittest.mock import patch, mock_open
from handleurl import create_csv_file


data = ["URL", "Check_time",
        "Response_time", "Response_status_code",
        "Response_headers"
        ]


def test_create_csv_file():
    open_mock = mock_open()
    with patch("handleurl.open", open_mock, create=True):
        create_csv_file(data)
    open_mock.assert_called_with("output.csv", "w", newline='')
    open_mock.return_value.write.assert_called_once_with(data)

