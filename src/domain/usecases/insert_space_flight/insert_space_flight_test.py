import pytest
from .insert_space_flight import InsertSpaceFlightUseCase
from src.infra.test import SpaceFlightNewRepositorySpy
from src.utils.errors import MissingParamError


def make_sut():
    respository = SpaceFlightNewRepositorySpy()
    sut = InsertSpaceFlightUseCase(respository)
    return sut, respository


def make_sut_with_success_false():
    class SpaceFlightNewRepositorySpy:
        def insert(self, data: dict):
            return None

    respository = SpaceFlightNewRepositorySpy()
    sut = InsertSpaceFlightUseCase(respository)
    return sut, respository


def test_should_raise_if_no_limit_page_is_provided():
    sut, _ = make_sut()
    with pytest.raises(Exception) as err_info:
        sut.insert_one()

    assert str(err_info.value) == str(MissingParamError("data"))


def test_should_call_insert_with_correct_params_if_data_is_provided():
    sut, repository = make_sut()
    data = {"id": 1}
    sut.insert_one(data=data)

    assert data["id"] == repository.param_inserted_data["id"]


def test_should_return_success_is_true_if_data_is_inserted():
    sut, _ = make_sut()
    data = {"id": 1}
    response = sut.insert_one(data)

    assert response["success"] is True


def test_should_return_success_is_false_if_no_data_is_inserted():
    sut, _ = make_sut_with_success_false()
    data = {"id": 1}
    response = sut.insert_one(data)

    assert response["success"] is False
