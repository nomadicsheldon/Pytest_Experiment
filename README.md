# Pytest_Experiment

### get detail about test case- add `-v` at the end like this 👉
```
py.test -v
or
pytest -v
```
### run all test cases 👉 
```
py.test
```
(it will choose files which starts with test)

### command for running particular file from terminal 👉 
```
pytest filename.py
```
### command for running particular function from terminal 👉
```
pytest filename.py::fuctionname
```
### it will run the testcases which contains add keyword or string 👉
```
pytest -v -k "keyword"
```
### you can use or operator as well here like this 👉 
```
pytest -v -k "add or string"
pytest -v -k "add and string"
```
### selection marker(Example- @pytest.mark.number) to run the test cases 👉
```
pytest -v -m number
```
### Whenever first failure occure after that test execution will stop 👉
```
pytest -v -x
```
### it will not print tech brace in terminal 👉
```
pytest -v -x --tb=no
```
### whenever failure number will cross limit of maxfail 👉
```
pytest -v --maxfail=2
```
### show skip message in terminal 👉
```
pytest -v -rsx
```
### show only important info nothing else in terminal 👉
```
pytest -v -q
```
---
### for skipping particular function 👉
```
@pytest.mark.skip(reason="do not run number add test")
```

### for skip particular condition 👉
```
@pytest.mark.skipif(sys.version_info > (3, 3), reason="do not run number add test")
```
### Print log also in terminal
```
pytest -v -s
```
---
