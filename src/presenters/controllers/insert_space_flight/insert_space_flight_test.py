from src.domain.test.insert_space_flight_spy import InsertSpaceFlightUseCaseSpy
from src.infra.test import SpaceFlightNewRepositorySpy, mock_one_space_flight
from src.presenters.helpers import HttpRequest
from .insert_space_flight import InsertSpaceFlightController


def make_sut():
    use_case = InsertSpaceFlightUseCaseSpy(SpaceFlightNewRepositorySpy())
    sut = InsertSpaceFlightController(use_case)
    return sut, use_case


def test_route():
    sut, use_case = make_sut()

    http_request = HttpRequest(body=mock_one_space_flight)

    http_response = sut.route(http_request=http_request)

    assert mock_one_space_flight == use_case.param_insert_one_data

    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_error_no_body():
    sut, use_case = make_sut()

    http_request = HttpRequest()
    http_response = sut.route(http_request=http_request)

    assert use_case.param_insert_one_data is None

    assert http_response.status_code == 400
    assert "error" in http_response.body
