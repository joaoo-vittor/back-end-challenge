from src.infra.repo import SpaceFlightNewRepository
from src.domain.usecases.update_space_flight import UpdateSpaceFlightUseCase
from src.presenters.controllers.update_space_flight import UpdateSpaceFlightController


def update_space_flight_compose():

    repo = SpaceFlightNewRepository()
    use_case = UpdateSpaceFlightUseCase(repo)
    controller = UpdateSpaceFlightController(use_case)

    return controller
