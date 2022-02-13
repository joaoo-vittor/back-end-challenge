from src.domain.test.delete_space_flight_spy import DeleteSpaceFlightUseCaseSpy
from src.infra.test import SpaceFlightNewRepositorySpy
from src.presenters.helpers import HttpRequest
from .delete_space_flight import DeleteSpaceFlightController


def make_sut():
    use_case = DeleteSpaceFlightUseCaseSpy(SpaceFlightNewRepositorySpy())
    sut = DeleteSpaceFlightController(use_case)
    return sut, use_case


def test_route():
    sut, use_case = make_sut()

    attributes = {"id": 1}

    http_request = HttpRequest(body=attributes)

    http_response = sut.route(http_request=http_request)

    assert attributes["id"] == use_case.param_delete_by_id

    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_error_no_body():
    sut, use_case = make_sut()

    http_request = HttpRequest()
    http_response = sut.route(http_request=http_request)

    assert use_case.param_delete_by_id is None

    assert http_response.status_code == 400
    assert "error" in http_response.body
