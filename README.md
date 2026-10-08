# Applied AI in Python — WS 2026/27

Course material for *Applied AI in Python* (University of Salzburg).
New notebooks and problem sheets are added here during the semester.

Lecturer: Dominik Geng, <dominik.geng@plus.ac.at>

Organization, assessment and attendance: see the [syllabus](syllabus.pdf).

```text
syllabus.pdf  organization, assessment and attendance
lectures/     lecture notebooks and scripts, released session by session
sheets/       problem sheets
project/      project guidelines
data/         small datasets used in the notebooks
work/         YOUR copies of notebooks (you create this directory; git ignores it)
```

## 1. Get the material

**Option A: git (recommended).** You get updates with a single command, and you don't need a GitHub account.

```sh
git clone https://github.com/Splendus/aai-2627.git
cd aai-2627
```

If you do not already have `git` installed:

### **Linux:** install `git` with your package manager if it isn't already there.

If you’re on a Debian-based distribution, such as Ubuntu:

```sh
sudo apt install git-all
```

If you’re on Fedora, you can use:

```sh
sudo dnf install git-all
```


### **macOS:** 

Simply type 
```sh
git
```
in a shell and it should offer to install the *Command Line Tools*. Accept, and wait for the installation to finish.

### **Windows:** 

install [Git for Windows](https://git-scm.com/downloads/win), or run `winget install Git.Git`.

**Option B: ZIP.** On the repository page, click *Code → Download ZIP* and unpack it. The unpacked folder is called `aai-2627-main`, and Windows' *Extract All* even nests it twice (`aai-2627-main\aai-2627-main`). Take the inner folder, the one that directly contains `pyproject.toml`, and rename it to `aai-2627`, so that all commands below work as written. You won't get updates automatically, so download the new notebooks each week.

## 2. Set up Python

The download is about 1 GB, mostly PyTorch.

### uv (recommended)

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
uv sync            # downloads a suitable Python and all packages into .venv/
uv run jupyter lab # starts Jupyter in your browser
```

**VS Code:** open the course directory and choose the `.venv` environment as the kernel ("Select Kernel" at the top right of a notebook).

### Alternative: venv + pip (if uv does not work on your machine)

First install **Python 3.13 or 3.14** from [python.org](https://www.python.org/downloads/) (Intel Macs: 3.12). On Windows, the "install for me only" option needs no admin rights. Then, inside the course directory (replace `3.14` by the version you installed):

```sh
# macOS / Linux
python3.14 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m jupyterlab
```

```powershell
# Windows
py -3.14 -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m jupyterlab
```

You don't need to "activate" the environment. Calling the programs inside `.venv` directly also works on Windows machines that block activation scripts.

### University lab PCs (Windows)

On the lab PCs, uv can't be used: their security software blocks the small launcher programs that uv creates. Use the preinstalled Python 3.14 instead, which works with our packages. git isn't installed there either, so download the material as a ZIP (see option B above) to `C:\Users\<your id>\aai-2627`. Then, in PowerShell:

```powershell
cd $env:USERPROFILE\aai-2627
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m jupyterlab
```

Always start programs this way, via `.venv\Scripts\python -m ...`. Launchers like `jupyter.exe` or `uv run` are blocked on these PCs ("Zugriff verweigert" / "Access denied"). The environment stays on the PC when you log out, so you only have to install it once per PC.

### Intel Macs (bought before 2021)

PyTorch no longer supports Intel Macs with Python 3.13 or newer. Run this **once** and install Python **3.12** instead of 3.13 before `uv sync`:

```sh
uv python pin 3.12
```


## 3. Working with the notebooks

- **Don't edit the notebooks in `lectures/` directly.** Copy them to `work/` first and work on the copy. Otherwise `git pull` refuses to update the files you have changed.
- **Getting updates** (Option A):

  ```sh
  git pull
  uv sync      # or use venv+pip instead: .venv/bin/python -m pip install -r requirements.txt
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
| The uv installer is blocked (Windows) | `winget install astral-sh.uv`, or use a python venv. |
| `uv sync` cannot download Python (e.g. behind a proxy) | Install Python 3.13 from python.org, then run `uv sync --no-managed-python`. |
| Jupyter doesn't list the course environment | Start Jupyter via `uv run jupyter lab`, or select `.venv` as the kernel in VS Code. |
| "Zugriff verweigert" / "Access denied" (os error 5) when running `python.exe`, `jupyter.exe` or `uv run` | Security software blocks launcher programs on this PC. Use the steps for the university lab PCs in section 2. |
| Anything else | Bring your laptop to the session or send me an email (<dominik.geng@plus.ac.at>). |
