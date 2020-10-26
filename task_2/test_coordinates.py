import pytest

from coordinates_converter import convert_latitude, convert_longitude
from testdata import TEST_DATA_LONGITUDE, TEST_DATA_LATITUDE


@pytest.mark.parametrize("given_dd, expected_ddm", TEST_DATA_LONGITUDE)
def test_converted_longitude(given_dd, expected_ddm):
    assert convert_longitude(given_dd) == expected_ddm


@pytest.mark.parametrize("given_dd, expected_ddm", TEST_DATA_LATITUDE)
def test_converted_latitude(given_dd, expected_ddm):
    assert convert_latitude(given_dd) == expected_ddm
