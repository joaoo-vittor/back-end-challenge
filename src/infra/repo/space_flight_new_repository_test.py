import pytest
from src.infra.test import mock_one_space_flight, mock_list_space_flight
from .space_flight_new_repository import SpaceFlightNewRepository
from src.infra.config import DBConnectionHandler
from src.utils.errors import MissingParamError


def test_should_insert_if_data_is_provided():
    respository = SpaceFlightNewRepository()
    response = respository.insert(mock_one_space_flight)

    assert response["inserted_id"] is not None


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


def test_should_find_one_space_flight():
    respository = SpaceFlightNewRepository()
    data = respository.find_one(2)

    assert list(data.values())[1] == 2
    assert data is not None


def test_should_update_one_space_flight():
    respository = SpaceFlightNewRepository()
    data = respository.update(2, {"title": "Updated Title"})

    assert data["modified_count"] == 1
    assert data is not None


def test_should_delete_one_space_flight():
    respository = SpaceFlightNewRepository()
    data = respository.delete(3)

    assert data["deleted_count"] == 1
    assert data is not None


@pytest.fixture(scope="module", autouse=True)
def delete_many_space_flight():
    with DBConnectionHandler() as connection:
        connection.get_collection("spaceFlight").insert_many(mock_list_space_flight)
    yield
    with DBConnectionHandler() as connection:
        connection.get_collection("spaceFlight").delete_many({})
