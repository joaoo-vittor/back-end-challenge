import pytest
from .find_one_space_flight import FindOneSpaceFlightUseCase
from src.infra.test import SpaceFlightNewRepositorySpy
from src.utils.errors import MissingParamError


def make_sut():
    respository = SpaceFlightNewRepositorySpy()
    sut = FindOneSpaceFlightUseCase(respository)
    return sut, respository


def make_sut_with_success_false():
    class SpaceFlightNewRepositorySpy:
        def find_one(self, id: int):
            return None

    respository = SpaceFlightNewRepositorySpy()
    sut = FindOneSpaceFlightUseCase(respository)
    return sut, respository


def test_should_raise_if_no_id_is_provided():
    sut, _ = make_sut()
    with pytest.raises(Exception) as err_info:
        sut.find_one_by()

    assert str(err_info.value) == str(MissingParamError("id"))


def test_should_call_find_one_by_with_correct_params_if_id_is_provided():
    sut, repository = make_sut()
    id = 1
    sut.find_one_by(id)

    assert id == repository.param_find_one_id


def test_should_return_success_is_true_if_data_is_delected():
    sut, _ = make_sut()
    id = 1
    response = sut.find_one_by(id)

    assert response["success"] is True


def test_should_return_success_is_false_if_no_data_is_delected():
    sut, _ = make_sut_with_success_false()
    id = 1
    response = sut.find_one_by(id)

    assert response["success"] is False
