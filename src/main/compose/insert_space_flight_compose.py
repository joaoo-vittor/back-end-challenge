from src.infra.repo import SpaceFlightNewRepository
from src.domain.usecases.insert_space_flight import InsertSpaceFlightUseCase
from src.presenters.controllers.insert_space_flight import InsertSpaceFlightController


def insert_space_flight_compose():

    repo = SpaceFlightNewRepository()
    use_case = InsertSpaceFlightUseCase(repo)
    controller = InsertSpaceFlightController(use_case)

    return controller
