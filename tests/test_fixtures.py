def test_fx_patch_clickhouse_client(testdir):
    testdir.makepyfile("""
import clickhouse_driver


def test_clickhouse_driver_client(fx_patch_clickhouse_client):
    client = clickhouse_driver.Client("localhost")
""")

    result = testdir.runpytest()
    result.assert_outcomes(passed=1)


def test_fx_clickhouse_client(testdir):
    testdir.makepyfile("""
import clickhouse_driver

import pytest


@pytest.mark.parametrize("result", [[1, 2, 3]])
def test_clickhouse_execute(fx_clickhouse_client, result):
    fx_clickhouse_client.execute.return_value = result

    client = clickhouse_driver.Client("localhost")

    assert result == client.execute("SELECT sum(x) FROM test")


def test_clickhouse_connection_connected(fx_clickhouse_client):
    client = clickhouse_driver.Client("localhost")

    assert client.connection.connected
    assert isinstance(client.connection.connected, bool)
""")

    result = testdir.runpytest()
    result.assert_outcomes(passed=2)
