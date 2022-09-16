import sys

import pytest

from imaginairy import api
from imaginairy.suppress_logs import suppress_annoying_logs_and_warnings

if "pytest" in str(sys.argv):
    suppress_annoying_logs_and_warnings()


@pytest.fixture(scope="session", autouse=True)
def pre_setup():
    api.IMAGINAIRY_SAFETY_MODE = "disabled"
