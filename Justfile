[private]
_default:
  @just -g --list --unsorted

# Run the tests
@test:
  uv run --with . pytest

# Type check
@ty:
  uv run ty check src

# Run linting and fix errors
@ruff:
  ruff check . --fix || true
  ruff format .
  ruff check .
