---
hide:
  - footer
  - navigation
---

The only prerequisite for installing PySide6 is having Python installed on your system. PySide6 can be installed using the Python package manager `conda`, `pip`, or `poetry`.

## Conda

If you use `conda`, you can install PySide6 from the `conda-forge` channel. Best practice is to use an environment for your PySide6 project, and not to install it in your base environment:

1. Create and activate an environment:
```bash
conda create -n myenv
conda activate myenv
```
2. Download PySide6 from the `conda-forge` channel in the environment:
```bash
conda install -c conda-forge pyside6
```

## Pip

If you use `pip`, you can install PySide6 using the commands below. Also with `pip`, it is best practice to use a virtual environment. It is customary to use [`venv`](https://docs.python.org/3/library/venv.html#module-venv) for this purpose. `venv` is built into Python and does not require any additional installation:

1. Create and activate an environment:
```bash
python -m venv myenv
```
2. Activate the environment: <br> </br>
  Windows :material-microsoft-windows::
```
myenv\Scripts\activate
```
Unix:material-linux: / macOS:material-apple::
```bash
source myenv/bin/activate
```
3. Install PySide6 in the environment:
```bash
pip install pyside6
```

## Poetry

If you use [`poetry`](https://python-poetry.org/), you can install PySide6 using the commands below. Also with `poetry` it is best practice to use a virtual environment. This virtual environment can be either a `venv` or `conda` environment. 

1. Create and activate an environment. See sections [`pip`](#pip) and [`conda`](#conda) above on how to create and activate a `venv` or `conda` environment, respectively.
2. Create a Poetry project, if you haven't already, and navigate to it:
```bash
poetry new myproject
cd myproject
```
3. Add PySide6 to the project's `pyproject.toml` file and install to the virtual environment:
``` bash
poetry add pyside6
poetry install
```

<br>
<br>