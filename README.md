# Simulations Workshop 2026


| Week | Topic | Notes |
|---|---|---|
| [Week 1](week%201/) | Bouncing balls: 1D floor, 2D circular boundary | [week 1/README.md](week%201/README.md) |

## Setup

Needs [uv](https://docs.astral.sh/uv/) and Python 3.12+. `uv` handles the
Python version and the virtualenv itself, so nothing else to install.

```bash
# 1. get the code
git clone https://github.com/seds-celestia-simulations/simulations-workshop-2026.git


# 2. change directory
cd simulations-workshop-2026

# 3. create the venv and install dependencies.
uv sync
```

Don't have `uv`?

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # macOS / Linux
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"   # Windows
```

## Running a sim

```bash
uv run "week 1/bouncingball.py"
uv run "week 1/roundboundary.py"
```

A window opens; close it to quit.




