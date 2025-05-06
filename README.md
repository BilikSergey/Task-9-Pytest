## Summary of repo
# Task 9 Pytest
Repo is dedicated for testing Website automationexercise using pytest, playwright, allure.
## Requirements
Among requirements are installing project, pytest, faker, any code editor, python and allure.

## Setup

- Install any code editor (VS Code) or IDE

- Install python

  ```bash
  https://www.python.org/downloads/
  ```

- Clone the project:

```bash
git clone https://github.com/BilikSergey/Task-9-Pytest.git
```

- Install dependencies:

```bash
pipenv install --dev
```

- Install python package:

```bash
py -m ensurepip --upgrade
```

- Install package manager:

```bash
pip install pipenv
```

- Create an isolated environment:

```bash
pipenv shell
```

- Install pytest-playwright

```bash
pipenv install pytest-playwright
```

- Install browsers:

```bash
playwright install
```

- Install next pytest packages for running parallel tests:

```bash
pip install pytest pytest-xdist
```

- Install allure and commandline for it

```bash
pip install allure-pytest

https://github.com/allure-framework/allure2/releases
```

- Install faker.

```bash
pip install faker
```

## Run tests
Run all tests:
```bash
pytest
```
Run tests of particular file
```bash
pytest tests/register_test.py
```
Run certain test:
```bash
pytest -v tests/basic_pages_test.py::test_verify_scroll_up_using_arrow_button_and_scroll_down_functionality
```
Run tests with Firefox:
```bash
pytest --browser=firefox
```
Run tests with WebKit:
```bash
pytest --browser webkit
```
Run tests parallelly
```bash
pytest -n 3
```
## Create a report
Run to build an allure_result
```bash
pytest --alluredir=allure-results
```
Run to build a reporter
```bash
allure serve allure-results
```
