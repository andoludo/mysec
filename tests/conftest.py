from pathlib import Path

import pytest
from bearish.database.crud import BearishDb


@pytest.fixture(scope="session")
def bearish_db() -> BearishDb:
    database_path = Path(__file__).parent.joinpath("data", "bear_sec.db")
    return BearishDb(database_path=database_path)
