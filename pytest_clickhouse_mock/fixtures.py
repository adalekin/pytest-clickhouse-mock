import mock

import pytest


@pytest.fixture(scope="session", autouse=True)
def fx_patch_clickhouse_client():
    with mock.patch("clickhouse_driver.Client") as mock_client:
        yield mock_client


@pytest.fixture(scope="function")
def fx_clickhouse_client(fx_patch_clickhouse_client):
    mock_client = fx_patch_clickhouse_client.return_value
    mock_client.connection.connected = True

    yield mock_client

    mock_client.reset_mock(return_value=True, side_effect=True)
