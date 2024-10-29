"""
mt5linux Unit Testing
"""

import pytest

from mt5linux_updated import MetaTrader5


@pytest.fixture
def mt5():
    mt5 = MetaTrader5(port=1235)
    mt5.initialize()
    yield mt5
    mt5.shutdown()


def test_terminal_info(mt5):
    info = mt5.terminal_info()
    assert info is not None
