# import pytest
# import rpyc

# from mt5linux_updated import MetaTrader5


# class MockMetaTrader5Service(rpyc.Service):
#     def exposed_terminal_info(self):
#         # Return some mock terminal info
#         return {"mock_info": "Mock terminal info"}

#     def exposed_initialize(self):
#         # Mock initialization
#         pass

#     def exposed_shutdown(self):
#         # Mock shutdown
#         pass


# def start_mock_server():
# /*************  ✨ Codeium Command ⭐  *************/
#     """
#     Starts a mock MetaTrader 5 service using rpyc.
#     This service provides a mock implementation of the MetaTrader 5 API.
#     """
# /******  27cce0b3-9ca6-478c-9bd8-f486ef9858a5  *******/
#     server = rpyc.ThreadedServer(MockMetaTrader5Service, port=1235)
#     server.start()


# @pytest.fixture(scope="session", autouse=True)
# def start_server():
#     start_mock_server()


# @pytest.fixture
# def mt5():
#     mt5 = MetaTrader5(port=1235)
#     mt5.initialize()
#     yield mt5
#     mt5.shutdown()


# def test_terminal_info(mt5):
#     info = mt5.terminal_info()
#     assert info == {"mock_info": "Mock terminal info"}


def add(x, y):
    return x + y


def test_add():
    assert add(2, 3) == 5
