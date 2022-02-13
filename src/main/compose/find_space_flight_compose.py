from src.infra.repo import SpaceFlightNewRepository
from src.domain.usecases.find_space_flight import FindSpaceFlightUseCase
from src.presenters.controllers.find_space_flight import FindSpaceFlightController


def find_space_flight_compose():

    repo = SpaceFlightNewRepository()
    use_case = FindSpaceFlightUseCase(repo)
    controller = FindSpaceFlightController(use_case)

    return controller
