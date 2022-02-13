from src.domain.test.find_space_flight_spy import FindSpaceFlightUseCaseSpy
from src.infra.test import SpaceFlightNewRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_space_flight import FindSpaceFlightController


def make_sut():
    use_case = FindSpaceFlightUseCaseSpy(SpaceFlightNewRepositorySpy())
    sut = FindSpaceFlightController(use_case)
    return sut, use_case


def test_route():
    sut, use_case = make_sut()

    attributes = {"limit_page": 10, "skip_page": 5}

    http_request = HttpRequest(query=attributes)

    http_response = sut.route(http_request=http_request)

    assert attributes["limit_page"] == use_case.params_find_by_limit_page
    assert attributes["skip_page"] == use_case.params_find_by_skip_page

    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_error_no_body():
    sut, use_case = make_sut()

    http_request = HttpRequest()
    http_response = sut.route(http_request=http_request)

    assert use_case.params_find_by_skip_page is None
    assert use_case.params_find_by_limit_page is None

    assert http_response.status_code == 400
    assert "error" in http_response.body
