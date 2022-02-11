import pytest
from src.infra.test import mock_one_space_flight, mock_list_space_flight
from .space_flight_new_repository import SpaceFlightNewRepository
from src.infra.config import DBConnectionHandler
from src.utils.errors import MissingParamError


def test_should_insert_if_data_is_provided():
    respository = SpaceFlightNewRepository()
    response = respository.insert(mock_one_space_flight)

    assert response.inserted_id is not None


def test_should_raise_if_no_data_is_privided():
    """Should raise if no data is provided"""
    with pytest.raises(Exception) as exe_info:
        sut = SpaceFlightNewRepository()
        sut.insert()

    assert str(exe_info.value) == str(MissingParamError("data"))


def test_should_find_space_flight_pagination():
    respository = SpaceFlightNewRepository()
    data = respository.find(3, 1)

    assert len(data) == 3


@pytest.fixture(scope="module", autouse=True)
def delete_many_space_flight():
    with DBConnectionHandler() as connection:
        connection.get_collection("spaceFlight").insert_many(mock_list_space_flight)
    yield
    with DBConnectionHandler() as connection:
        connection.get_collection("spaceFlight").delete_many({})
