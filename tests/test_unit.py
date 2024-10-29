"""
mt5linux Unit Testing
"""

from mt5linux_updated import MetaTrader5

mt5 = MetaTrader5(port=1235)
mt5.initialize()
print(mt5.terminal_info())
mt5.shutdown()
assert True

