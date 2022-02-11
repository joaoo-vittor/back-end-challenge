import pytest
from .delete_space_flight import DeleteSpaceFlightUseCase
from src.infra.test import SpaceFlightNewRepositorySpy
from src.utils.errors import MissingParamError


def make_sut():
    respository = SpaceFlightNewRepositorySpy()
    sut = DeleteSpaceFlightUseCase(respository)
    return sut, respository


def make_sut_with_success_false():
    class SpaceFlightNewRepositorySpy:
        def delete(self, id: int):
            return None

    respository = SpaceFlightNewRepositorySpy()
    sut = DeleteSpaceFlightUseCase(respository)
    return sut, respository


def test_should_raise_if_no_id_is_provided():
    sut, _ = make_sut()
    with pytest.raises(Exception) as err_info:
        sut.delete_by()

    assert str(err_info.value) == str(MissingParamError("id"))


def test_should_call_delete_by_with_correct_params_if_id_is_provided():
    sut, repository = make_sut()
    id = 1
    sut.delete_by(id)

    assert id == repository.param_delete_id


def test_should_return_success_is_true_if_data_is_delected():
    sut, _ = make_sut()
    id = 1
    response = sut.delete_by(id)

    assert response["success"] is True


def test_should_return_success_is_false_if_no_data_is_delected():
    sut, _ = make_sut_with_success_false()
    id = 1
    response = sut.delete_by(id)

    assert response["success"] is False
