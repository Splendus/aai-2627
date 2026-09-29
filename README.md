# Applied AI in Python — WS 2026/27

Course material for *Applied AI in Python* (University of Salzburg).
New notebooks and problem sheets are added here before each session.

```text
notebooks/   lecture notebooks and scripts, released session by session
sheets/      problem sheets
project/     project guidelines
data/        small datasets used in the notebooks
work/        YOUR copies of notebooks (you create this directory; git ignores it)
```

## 1. Get the material

**Option A: git (recommended).** You get updates with a single command, and you don't need a GitHub account.

```sh
git clone https://github.com/Splendus/aai-2627.git
cd aai-2627
```

- **Linux:** install `git` with your package manager if it isn't already there.
- **macOS:** the first `git` command may offer to install the *Command Line Tools*. Accept, and wait for the installation to finish.
- **Windows:** install [Git for Windows](https://git-scm.com/downloads/win), or run `winget install Git.Git`.

**Option B: ZIP.** On the repository page, click *Code → Download ZIP* and unpack it. You won't get updates automatically, so download the new notebooks each week.

## 2. Set up Python

The download is about 1 GB, mostly PyTorch.

### Route 1: uv (recommended)

[uv](https://docs.astral.sh/uv/) installs the right Python version and all packages in exactly the versions we use in class, on every operating system.

Install uv, then **open a new terminal**:

```sh
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```powershell
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then, inside the course directory:

```sh
uv sync            # downloads Python 3.13 and all packages into .venv/
uv run jupyter lab # starts Jupyter in your browser
```

**VS Code:** open the course directory and choose the `.venv` environment as the kernel ("Select Kernel" at the top right of a notebook).

### Route 2: venv + pip (if uv does not work on your machine)

First install **Python 3.13** from [python.org](https://www.python.org/downloads/). On Windows, the "install for me only" option needs no admin rights. Then, inside the course directory:

```sh
# macOS / Linux
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/jupyter lab
```

```powershell
# Windows
py -3.13 -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\jupyter lab
```

You don't need to "activate" the environment. Calling the programs inside `.venv` directly also works on Windows machines that block activation scripts.

### Intel Macs (bought before 2021)

PyTorch no longer supports Intel Macs with Python 3.13. Run this **once** before `uv sync`:

```sh
uv python pin 3.12
```

This installs the last PyTorch version for Intel Macs. With Route 2, install Python **3.12** instead of 3.13.

## 3. Working with the notebooks

- **Don't edit the notebooks in `notebooks/` directly.** Copy them to `work/` first and work on the copy. Otherwise `git pull` refuses to update the files you have changed.
- **Getting updates** (Option A):

  ```sh
  git pull
  uv sync      # Route 2 instead: .venv/bin/python -m pip install -r requirements.txt
  ```

## 4. Optional: Graphviz (from the autograd sessions on)

Some notebooks draw computation graphs, which needs the Graphviz program. Without it, only the cells that draw a graph fail. Everything else works.

- **macOS:** `brew install graphviz`
- **Windows:** installer from [graphviz.org/download](https://graphviz.org/download/). Tick "add to PATH".
- **Linux:** `sudo apt install graphviz` (or your distribution's equivalent)

## Troubleshooting

| Problem | Try |
| --- | --- |
| `uv: command not found` right after installing | Open a new terminal. |
| The uv installer is blocked (Windows) | `winget install astral-sh.uv`, or use Route 2. |
| `uv sync` cannot download Python (e.g. behind a proxy) | Install Python 3.13 from python.org, then run `uv sync --no-managed-python`. |
| Jupyter doesn't list the course environment | Start Jupyter via `uv run jupyter lab`, or select `.venv` as the kernel in VS Code. |
| Anything else | Bring your laptop to the session or send me an email. |
