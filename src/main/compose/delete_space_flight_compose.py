from src.infra.repo import SpaceFlightNewRepository
from src.domain.usecases.delete_space_flight import DeleteSpaceFlightUseCase
from src.presenters.controllers.delete_space_flight import DeleteSpaceFlightController


def delete_space_flight_compose():

    repo = SpaceFlightNewRepository()
    use_case = DeleteSpaceFlightUseCase(repo)
    controller = DeleteSpaceFlightController(use_case)

    return controller
