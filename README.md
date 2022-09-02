# Measurement Workbox

### Installation
```
pip install measurement-workbox
```

### Get started
How to use measurement-workbox

```Python
import measurement_workbox as mw
```

## Development Information
[Github Repository](https://github.com/MattWill660/measurement-workbox)  
[Packaging Information](https://packaging.python.org/en/latest/tutorials/packaging-projects/)  
[Unit Testing](https://docs.python.org/3/library/unittest.html)

### TODO:
-Write classes/code
-[Write unititests](https://realpython.com/python-testing/)  
-[Set up auto documentation](https://towardsdatascience.com/easily-automate-and-never-touch-your-documentation-again-a98c91ce1b95)  
-[Set up documentation hosting](https://realpython.com/python-project-documentation-with-mkdocs/)  
-[Upload to pip](https://packaging.python.org/en/latest/tutorials/packaging-projects/)  

### Build Distribution
Increment version number in setup.py and pyproject.toml
```
py -m pip install --upgrade build  
py -m build
```

### Upload Test Distribution
```
py -m pip install --upgrade twine  
py -m twine upload --repository testpypi dist/* 
```

### Install Test Distribution
```
py -m pip install --index-url https://test.pypi.org/simple/ --no-deps measurement-workbox  
```

### Upload and Install Real Distribution
```
py -m pip install --upgrade twine  
py -m twine upload dist/* 
python3 -m pip install measurement-workbox
```

