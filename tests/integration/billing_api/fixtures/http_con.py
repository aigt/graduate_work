from typing import Generator

import requests as requests # type: ignore
from pytest import fixture


@fixture(scope="function")
def http_con() -> Generator:
    """http клиент"""

    con = requests.Session()
    yield con
    con.close()
