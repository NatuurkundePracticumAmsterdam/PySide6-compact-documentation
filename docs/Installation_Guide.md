Installation guide
===

To ensure a clean install, first create a new conda environment.

```
(base) conda create -n my_env
(base) conda activate my_env
```

On the fresh environment the following command will install PySide6 and its dependencies

```
(my_env) conda install pyside6
```

To add PySide6 to a poetry project

```
poetry add pyside6
```