import unittest
import requests
from enum import Enum

from tests.disbursement.test_disbursement import TestDisbursement
from tests.disbursement.test_agent_disbursement import TestAgentDisbursement
from tests.disbursement.test_international_disbursement import TestInternationalDisbursement
from tests.disbursement.test_special_disbursement import TestSpecialDisbursement


########### CATALOG ###########
class FEATURE_VARIATION_CATALOG(Enum):
    DISBURSEMENT = TestDisbursement
    AGENT_DISBURSEMENT = TestAgentDisbursement
    INTERNATIONAL_DISBURSEMENT = TestInternationalDisbursement
    SPECIAL_DISBURSEMENT = TestSpecialDisbursement


class VENDOR_CATALOG(Enum):
    FLIP = "Flip"
    MIDTRANS = "Midtrans"
    OY = "Oy"



########### CONSTANT VARIABLES, ADJUST WITH YOUR REQUIREMENTS ###########
BASE_URL = "http://localhost:443"

# Disbursement URLs
DISBURSEMENT_URL = f"{BASE_URL}/call/disbursement"
AGENT_DISBURSEMENT_URL = f"{BASE_URL}/call/disbursement/agent"
INTERNATIONAL_DISBURSEMENT_URL = f"{BASE_URL}/call/disbursement/international"
SPECIAL_DISBURSEMENT_URL = f"{BASE_URL}/call/disbursement/special"

TEST_ACCOUNT_EMAIL = ""
TEST_ACCOUNT_PASSWORD = ""
TEST_DISBURSEMENT_AGENT_ID = 17

# Check CATALOG section
# Pattern: [[feature_variation, payment_vendor], ...]. Example: [[FEATURE_VARIATION_CATALOG.DISBURSEMENT, VENDOR_CATALOG.FLIP]]
SELECTED_FEATURE_VARIATION = [
    
]



########### DON'T EDIT THE CODE BELOW! ###########
def validate_selected_features():
    valid_features = list(FEATURE_VARIATION_CATALOG)
    for feature in SELECTED_FEATURE_VARIATION:
        if feature[0] not in valid_features:
            raise ValueError(f"{feature[0]} is not a valid feature variation.")

def login() -> str:
    print("========== LOGIN ==========")
    headers = {
        "Content-Type": "application/json",
    }
    request_payload = {
        'email': TEST_ACCOUNT_EMAIL,
        'password': TEST_ACCOUNT_PASSWORD
    }

    response = requests.post(
        url = f"{BASE_URL}/auth/login/pwd", 
        json = request_payload,
        headers=headers
    )
        
    if response.status_code != 200:
        raise ValueError(f"Failed {response.status_code} {response.text}")

    response_payload = response.json()
    print(f"Login successful, welcome back {response_payload['data']['name']}! Starting testing ...")

    return f"Basic {response_payload['data']['token']}"

def suite(authorization_token: str):
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    for feature in SELECTED_FEATURE_VARIATION:
        feature_variation = feature[0]
        vendor = feature[1].value
        test_case = loader.loadTestsFromTestCase(feature_variation.value)
        
        for test in test_case:
            test.vendor = vendor
            test.authorization_token = authorization_token
        
        suite.addTests(test_case)

    return suite

if __name__ == '__main__':
    validate_selected_features()
    authorization_token = login()

    runner = unittest.TextTestRunner()
    runner.run(suite(authorization_token))