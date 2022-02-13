from src.domain.test.update_space_flight_spy import UpdateSpaceFlightUseCaseSpy
from src.infra.test import SpaceFlightNewRepositorySpy
from .update_space_flight import UpdateSpaceFlightController
from src.presenters.helpers import HttpRequest
from src.infra.test import mock_one_space_flight


def make_sut():
    use_case = UpdateSpaceFlightUseCaseSpy(SpaceFlightNewRepositorySpy())
    sut = UpdateSpaceFlightController(use_case)
    return sut, use_case


def test_route():
    sut, use_case = make_sut()

    attributes = {"id": 1, "data": mock_one_space_flight}
    http_request = HttpRequest(body=attributes)

    http_response = sut.route(http_request=http_request)

    assert attributes["id"] == use_case.param_update_by_id
    assert attributes["data"] == use_case.param_update_by_data

    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_error_no_body():
    sut, use_case = make_sut()

    http_request = HttpRequest()
    http_response = sut.route(http_request=http_request)

    assert use_case.param_update_by_data is None
    assert use_case.param_update_by_id is None

    assert http_response.status_code == 400
    assert "error" in http_response.body
