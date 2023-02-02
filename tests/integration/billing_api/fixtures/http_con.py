from typing import Generator

import requests  # type: ignore
from pytest import fixture


@fixture(scope="function")
def http_con() -> Generator:
    """Http клиент.

    Yields:
        con(Generator): http сессия
    """
    con = requests.Session()
    yield con
    con.close()
