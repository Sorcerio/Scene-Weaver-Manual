# Scene Weaver: Running Tests

- [Scene Weaver: Running Tests](#scene-weaver-running-tests)
  - [Entering the Virtual Environment](#entering-the-virtual-environment)
  - [Preparing for Tests](#preparing-for-tests)
  - [Running the Tests](#running-the-tests)

---

Scene Weaver comes with a set of unit tests using the Python `unittest` library to ensure code functionality.

## Entering the Virtual Environment

All Scene Weaver commands should be run through an associated Python Virtual Environment that is setup following the instructions in the project's root [README file](../README.md).

The Python Virtual Environment can be activated by running the following:

1. Open a command line in the top level directory of Scene Weaver.
   * This is the directory this file is in.
2. Run `.\.venv\Scripts\activate` to activate the Scene Weaver's virtual environment.

## Preparing for Tests
1. [Enter the Virtual Environment](#entering-the-virtual-environment) if not already within it.
2. Run `pip install -r .\requirements-tests.txt` to install dependencies specific to testing Scene Weaver.

## Running the Tests
Note that when running tests directories like the `MockImageGenerator`'s `mockImages/` _will be modified_ during the process!

1. [Enter the Virtual Environment](#entering-the-virtual-environment) if not already within it.
2. Run `coverage run -m unittest discover -s .\tests\ -v -b` to trigger the testing process and generate a code coverage report.
   * Runs in Verbose mode with prints from the non-test code suppressed. 
3. Run `coverage html` to generate a human-readable HTML version of the coverage report.
4. Open the [index.html](../htmlcov/index.html) (`./htmlcov/index.html`) file to view the coverage report.
5. _(Optional)_ Run `coverage lcov -o lcov.info` to generate an LCOV version of the coverage report for use with [VSCode's Gutters Extension](https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters) or other in-IDE coverage system.
   * It works ok.
