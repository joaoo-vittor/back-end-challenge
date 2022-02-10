import pytest
from .space_flight_new_repository import SpaceFlightNewRepository
from src.utils.errors import MissingParamError


def test_should_raise_if_no_data_is_privided():
    """Should raise if no data is provided"""
    with pytest.raises(Exception) as exe_info:
        sut = SpaceFlightNewRepository()
        sut.insert()

    assert str(exe_info.value) == str(MissingParamError("data"))
