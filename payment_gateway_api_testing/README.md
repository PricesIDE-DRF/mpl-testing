# Automated API Testing Payment Gateway

This project contains API testing using the Python programming language for the Payment Gateway product.

## Project Structure
```plaintext
MPL-TESTING
├── amanah_functional_testing
|   ├── ...
└── payment_gateway_api_testing
    ├── tests                                        # API unit tests for all features in the Payment Gateway product
    |   ├── disbursement                             # API unit tests for disbursement feature
    |   |   ├── __init__.py                          # A marker for a package in Python
    |   |   ├── test_agent_disbursement.py           # Agent disbursement API unit tests
    |   |   ├── test_disbursement.py                 # Disbursement API unit tests
    |   |   ├── test_international_disbursement.py   # International disbursement API unit tests
    |   |   └── test_special_disbursement.py         # Special disbursement API unit tests
    |   └── __init__.py                              # A marker for a package in Python
    └── main.py                                      # The main class. TO run automated API testing, simply focus on this file
```

## Getting Started

### Prerequisites
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation: Clone the Repository
```bash
git clone <repository-url>
cd mpl-testing
```

### Running Tests
1. Adjust the following constant variables according to your product:
    - `BASE_URL`: The your API base URL
    - Disbursement URLs (If you don't have disbursement feature in your product, you can skip this step)
        - `DISBURSEMENT_URL`: The your disbursement feature (core) base URL
        - `AGENT_DISBURSEMENT_URL`: The your agent disbursement feature base URL
        - `INTERNATIONAL_DISBURSEMENT_URL`: The your international disbursement feature base URL
        - `SPECIAL_DISBURSEMENT_URL`: The your special disbursement feature base URL
    - `TEST_ACCOUNT_EMAIL`: Email of the account that will be used for testing
    - `TEST_ACCOUNT_PASSWORD`: Password of the account that will be used for testing
    - `TEST_DISBURSEMENT_AGENT_ID`: ID of the agent account that will be used for testing. Specifically for the agent disbursement feature, if your product doesn't have this feature, you can skip this step.
    - `SELECTED_FEATURE_VARIATION`: Features and vendors used in your product. Please read the `FEATURE_VARIATION_CATALOG` and `VENDOR_CATALOG` first.
        - **Pattern**: [[feature_variation, payment_vendor], ...]
        - **Example**: [[FEATURE_VARIATION_CATALOG.DISBURSEMENT, VENDOR_CATALOG.FLIP]]

2. Run the following command:
    ```bash
    cd payment_gateway_api_testing
    python main.py
    ```

3. The API testing will run, and the results will be available in the terminal.