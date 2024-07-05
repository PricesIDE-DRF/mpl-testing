# Automated Functional Testing Amanah x PaymentGateway

This project contain functional testing using selenium of Amanah x PaymentGateway Product. 

## Project Structure

```plaintext
SELENIUM_SCRIPT/
├── .pytest_cache/          # Cache files for pytest
├── drivers/                # WebDriver binaries (e.g., ChromeDriver, GeckoDriver)
├── reports/                # Test reports generated after execution
├── selenium-ide/           # Selenium IDE project files
├── test/                   # Test scripts and test cases
├── utils/                  # Utility scripts and helper functions
└── requirements.txt        # Python dependencies
```

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd selenium_script
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download WebDriver binaries**:

   - For ChromeDriver: [Download here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
   - For GeckoDriver (Firefox): [Download here](https://github.com/mozilla/geckodriver/releases)

   Place the downloaded WebDriver binaries in the `drivers/` directory.

### Running Tests (Python)

To run the tests, use the following command:

```bash
pytest .\test
```

If you want to run a test for specific product, use this:

```bash
pytest .\test\productname
```

If you want to save the test result use this:

```bash
pytest .\test\productname --html=reports\report.html
```

The result will be saved on `report.html`


This will execute all the test cases located in the `test/` directory and generate reports in the `reports/` directory.

## Running Test (SeleniumIDE)

### Prerequisites

1. **Install Selenium IDE**:
   - Selenium IDE is available as a browser extension. Install it from the following links:
     - [Selenium IDE for Chrome](https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd)
     - [Selenium IDE for Firefox](https://addons.mozilla.org/en-US/firefox/addon/selenium-ide/)

### Running Selenium IDE Scripts

1. **Open Selenium IDE**:
   - After installing the extension, open Selenium IDE from your browser's extension menu.

2. **Load a Project**:
   - Click on the "Open an existing project" option.
   - Navigate to the `selenium-ide/` directory and select the project file (e.g., `project.side`).

3. **Execute Tests**:
   - Once the project is loaded, you will see a list of test cases.
   - Select the test case you want to run or run all test cases.
   - Click the "Run" button to start the execution. The results will be displayed in the Selenium IDE window.

## Directory Details

- **drivers/**: Contains the WebDriver binaries needed to run the tests. Ensure the correct version of WebDriver is placed here.

- **tests/**: Contains all the test suites and individual test cases.

- **utils/**: Contains utility scripts and helper functions used across the test cases. This includes:
  - `assert_attribute.py`: Functions for asserting attributes in web elements.
  - `assert_redirect.py`: Functions for asserting URL redirects.
  - `auth_actions.py`: Functions for handling authentication actions like login and logout.
  - `webdriver_setup.py`: Functions for setting up and configuring WebDriver instances.

- **reports/**: Stores the test reports generated after running the tests. These can be in various formats (HTML, XML, etc.) depending on the pytest plugins used.

- **selenium-ide/**: The test format to run using seleniumIDE.


