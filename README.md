# pytest-clickhouse-mock

Pytest plugin with session- and function-scoped fixtures that replace `clickhouse_driver.Client` with a `unittest.mock` double. Use it to test code that talks to ClickHouse without running a server.

**Python:** 3.10+

## Install

From PyPI:

```bash
uv add pytest-clickhouse-mock
```

Or with pip:

```bash
pip install pytest-clickhouse-mock
```

The plugin registers automatically when pytest loads (entry point `clickhouse_mock`).

## Fixtures

| Fixture | Scope | Purpose |
|---------|-------|---------|
| `fx_patch_clickhouse_client` | session, autouse | Patches `clickhouse_driver.Client` for the whole test run |
| `fx_clickhouse_client` | function | Returns the mock instance for the current test; resets call state after each test |

`fx_patch_clickhouse_client` is autouse: any `clickhouse_driver.Client(...)` in your tests gets the same mock class. Use `fx_clickhouse_client` when you need to configure `execute`, `connection.connected`, and other attributes.

## Usage

```python
import clickhouse_driver


def test_query(fx_clickhouse_client):
    fx_clickhouse_client.execute.return_value = [(1, 2, 3)]

    client = clickhouse_driver.Client("localhost")
    rows = client.execute("SELECT 1")

    assert rows == [(1, 2, 3)]
    fx_clickhouse_client.execute.assert_called_once_with("SELECT 1")


def test_connection(fx_clickhouse_client):
    client = clickhouse_driver.Client("localhost")

    assert client.connection.connected is True
```

After each test, `fx_clickhouse_client` resets return values and side effects so tests stay isolated.

## Development

Repository: [github.com/adalekin/pytest-clickhouse-mock](https://github.com/adalekin/pytest-clickhouse-mock)

```bash
uv sync --group dev
uv run ruff check .
uv run ruff format --check .
uv run mypy pytest_clickhouse_mock
uv run pytest
```

## License

MIT — see [LICENSE](LICENSE).
