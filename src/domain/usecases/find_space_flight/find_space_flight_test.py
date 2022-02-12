import pytest
from .find_space_flight import FindSpaceFlightUseCase
from src.infra.test import SpaceFlightNewRepositorySpy
from src.utils.errors import MissingParamError


def make_sut():
    respository = SpaceFlightNewRepositorySpy()
    sut = FindSpaceFlightUseCase(respository)
    return sut, respository


def make_sut_with_success_false():
    class SpaceFlightNewRepositorySpy:
        def find(self, limit_page: int, skip_page: int):
            return None

    respository = SpaceFlightNewRepositorySpy()
    sut = FindSpaceFlightUseCase(respository)
    return sut, respository


def test_should_raise_if_no_limit_page_is_provided():
    sut, _ = make_sut()
    limit_page = 3
    with pytest.raises(Exception) as err_info:
        sut.find_by(limit_page=limit_page)

    assert str(err_info.value) == str(MissingParamError("skip_page"))


def test_should_raise_if_no_skip_page_is_provided():
    sut, _ = make_sut()
    skip_page = 1
    with pytest.raises(Exception) as err_info:
        sut.find_by(skip_page=skip_page)

    assert str(err_info.value) == str(MissingParamError("limit_page"))


def test_should_call_find_one_by_with_correct_params_if_limit_page_skip_page_is_provided():
    sut, repository = make_sut()
    limit_page = 3
    skip_page = 1
    sut.find_by(limit_page=limit_page, skip_page=skip_page)

    assert limit_page == repository.param_find_limit_page
    assert skip_page == repository.param_find_skip_page


def test_should_return_success_is_true_if_data_is_delected():
    sut, _ = make_sut()
    limit_page = 3
    skip_page = 1
    response = sut.find_by(limit_page, skip_page)

    assert response["success"] is True


def test_should_return_success_is_false_if_no_data_is_delected():
    sut, _ = make_sut_with_success_false()
    limit_page = 3
    skip_page = 1
    response = sut.find_by(limit_page, skip_page)

    assert response["success"] is False
