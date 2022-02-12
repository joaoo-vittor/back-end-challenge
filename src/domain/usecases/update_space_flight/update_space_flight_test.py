import pytest
from .update_space_flight import UpdateSpaceFlightUseCase
from src.infra.test import SpaceFlightNewRepositorySpy
from src.utils.errors import MissingParamError


def make_sut():
    respository = SpaceFlightNewRepositorySpy()
    sut = UpdateSpaceFlightUseCase(respository)
    return sut, respository


def make_sut_with_success_false():
    class SpaceFlightNewRepositorySpy:
        def update(self, id: int, data: dict):
            return None

    respository = SpaceFlightNewRepositorySpy()
    sut = UpdateSpaceFlightUseCase(respository)
    return sut, respository


def test_should_raise_if_no_data_is_provided():
    sut, _ = make_sut()
    id = 1
    with pytest.raises(Exception) as err_info:
        sut.update_by(id=id)

    assert str(err_info.value) == str(MissingParamError("data"))


def test_should_raise_if_no_id_is_provided():
    sut, _ = make_sut()
    data = {"id": 1}
    with pytest.raises(Exception) as err_info:
        sut.update_by(data=data)

    assert str(err_info.value) == str(MissingParamError("id"))


def test_should_call_insert_with_correct_params_if_is_provided():
    sut, repository = make_sut()
    data = {"id": 1}
    id = 1
    sut.update_by(id=id, data=data)

    assert data["id"] == repository.param_update_data["id"]
    assert id == repository.param_update_id


def test_should_return_success_is_true_if_data_is_updated():
    sut, _ = make_sut()
    data = {"id": 1}
    id = 1
    response = sut.update_by(id=id, data=data)

    assert response["success"] is True


def test_should_return_success_is_false_if_no_data_is_updated():
    sut, _ = make_sut_with_success_false()
    data = {"id": 1}
    id = 1
    response = sut.update_by(id=id, data=data)

    assert response["success"] is False
