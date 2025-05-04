# sphinx-test

```
PREFIX=/opt/local/mypackage

cmake . -B _build --install-prefix=${PREFIX}

cmake --build _build

cmake --install _build

PYTHONPATH=${PREFIX}/lib python3 -c 'import mypackage; print(mypackage.add(1, 2))'
```
