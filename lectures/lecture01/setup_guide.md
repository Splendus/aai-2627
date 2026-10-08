# Python environment setup guide

This tutorial gives a brief overview of how to get the course material and set up the Python environment we will use throughout the course. Setting up this environment is your **first homework**: bring a working setup to the next session.

We use [uv](https://docs.astral.sh/uv/), a tool that installs the right Python version and exactly the package versions we use in class, on Windows, macOS and Linux alike. This setup is minimal and easy to debug in case of issues. A more thorough resource is uv's official [getting started guide](https://docs.astral.sh/uv/getting-started/).

## Prerequisites

- About **1 GB** of free disk space (mostly for PyTorch) and an internet connection.
- No Python installation is needed: uv downloads its own Python. If you have used Anaconda or conda before, you don't need to uninstall anything; uv works independently of it.

## 1 - Get the course material

All lecture material, problem sheets and the project guidelines live in the course repository. Clone it with git (no GitHub account needed):

```sh
git clone https://github.com/Splendus/aai-2627.git
cd aai-2627
```

If you don't have git yet, the repository's README explains how to install it. Alternatively, download the repository as a ZIP file (*Code → Download ZIP* on the repository page) and unpack it. The unpacked folder is called `aai-2627-main`, and Windows' *Extract All* even nests it twice (`aai-2627-main\aai-2627-main`). Take the inner folder, the one that directly contains `pyproject.toml`, and rename it to `aai-2627`, so that all commands in this guide work as written. In that case, you have to download new material again each week.

The repository is organized as follows:

```text
lectures/   lecture notebooks and scripts, released session by session
sheets/     problem sheets
project/    project guidelines
data/       small datasets used in the notebooks
work/       YOUR copies of notebooks (you create this directory; git ignores it)
```

Some of these folders only appear once their first material has been released.

## 2 - Install uv

**On the university's lab PCs, uv doesn't work** (their security software blocks it). There, follow the section [University lab PCs (Windows)](#university-lab-pcs-windows) below instead of steps 2–4. Steps 2–4 are for your own computer.

Install uv with the command for your operating system, then **open a new terminal**, so that the `uv` command is found:

```sh
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```powershell
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Check that it worked:

```sh
uv --version
```

## 3 - Create the course environment

Inside the course directory (`aai-2627`), run

```sh
uv sync
```

This reads the files `pyproject.toml` and `uv.lock` of the repository, downloads a suitable Python version if needed (currently 3.13), and installs all packages we need for the course into a folder `.venv` inside the course directory: numpy, pandas, matplotlib, scikit-learn, seaborn, Jupyter and PyTorch. Unlike conda, there is no environment to create, name or activate: the environment *is* the `.venv` folder of the project, and `uv run <command>` runs a command inside it.

**Intel Macs (bought before 2021):** PyTorch no longer supports Intel Macs with Python 3.13 or newer. Run `uv python pin 3.12` once *before* `uv sync`.

To verify your setup, run

```sh
uv run python -c "import sys, numpy, pandas, matplotlib, sklearn, torch; print('Python', sys.version.split()[0], '| torch', torch.__version__, '| setup complete')"
```

Your setup is complete if this prints a line ending with `setup complete` (the version numbers may differ slightly).

During the course, the environment will grow when we need further packages. You then only have to update the material and the environment:

```sh
git pull
uv sync
```

## 4 - Launch Jupyter

Inside the course directory, run

```sh
uv run jupyter lab
```

This starts Jupyter's web editor in your browser. If it does not open on its own, copy & paste the link shown in the terminal into your browser. If you prefer the classic interface, use `uv run jupyter notebook` instead.

Create a folder `work/` in the course directory for your own notebooks. Don't edit the notebooks in `lectures/` directly: copy them to `work/` first. Otherwise `git pull` refuses to update the files you have changed.

## University lab PCs (Windows)

On the lab PCs, the security software blocks the small launcher programs that uv creates, so we use the preinstalled Python 3.14 instead, which works with all our packages. git isn't installed there either:

1. Download the material as a ZIP (see step 1) and save the inner folder as `C:\Users\<your id>\aai-2627`, i.e. directly in your user folder, renamed without `-main`.
2. Open PowerShell and create the environment (installing takes a few minutes):

   ```powershell
   cd $env:USERPROFILE\aai-2627
   python -m venv .venv
   .venv\Scripts\python -m pip install -r requirements.txt
   ```

3. Verify the setup:

   ```powershell
   .venv\Scripts\python -c "import sys, numpy, pandas, matplotlib, sklearn, torch; print('Python', sys.version.split()[0], '| torch', torch.__version__, '| setup complete')"
   ```

4. Launch Jupyter:

   ```powershell
   .venv\Scripts\python -m jupyterlab
   ```

Always start programs this way, via `.venv\Scripts\python -m ...`. Launchers like `jupyter.exe`, `jupyter lab` (with a space) or `uv run` are blocked on these PCs ("Zugriff verweigert" / "Access denied"). The environment stays on the PC when you log out, so you only have to install it once per PC; next time, steps 2 (only the `cd` line) and 4 are enough.

## Alternative: IDE

In case you prefer an Integrated Development Environment (IDE) over the web editor, e.g. VS Code and PyCharm also support Jupyter notebooks. Open the course directory and select the `.venv` environment as the notebook kernel (in VS Code: "Select Kernel" at the top right of a notebook).

If you want to use all capabilities of PyCharm, apply for a free [educational license](https://www.jetbrains.com/community/education/). With it you have full access to all tools, like remote development, notebooks, the scientific mode, etc.

## If something does not work

The README of the course repository has a troubleshooting section, e.g. for a blocked installer on Windows, and an alternative route without uv (Python's built-in `venv` and `pip`). If you are stuck, bring your laptop to the next session or send me an email (<dominik.geng@plus.ac.at>).
