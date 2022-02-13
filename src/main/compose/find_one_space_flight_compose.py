from src.infra.repo import SpaceFlightNewRepository
from src.domain.usecases.find_one_space_flight import FindOneSpaceFlightUseCase
from src.presenters.controllers.find_one_space_flight import (
    FindOneSpaceFlightController,
)


def find_one_space_flight_compose():

    repo = SpaceFlightNewRepository()
    use_case = FindOneSpaceFlightUseCase(repo)
    controller = FindOneSpaceFlightController(use_case)

    return controller
