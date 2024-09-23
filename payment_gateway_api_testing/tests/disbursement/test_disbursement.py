import unittest
import requests
from requests import Response
from typing import Dict, Any


class TestDisbursement(unittest.TestCase):
    print_flag = True

    def setUp(self):
        self.vendor = getattr(self, 'vendor', None)
        self.authorization_token = getattr(self, 'authorization_token', None)

        if TestDisbursement.print_flag:
            print()
            print()
            print(f"========== TEST DISBURSEMENT FEATURE WITH VENDOR {self.vendor.upper()} ==========")
            TestDisbursement.print_flag = False

    def test_disbursement_success(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "account_number": "98359135235",
            "amount": "10000",
            "bank_code": "bca"
        }

        expected_response_payload = {
            "data": {
                "bank_code": "bca",
                "account_number": "98359135235",
                "amount": 10000.0,
                "user_id": 9307076
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()
        
        self.assertIn('id', response_payload['data'])

        del response_payload['data']['id']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_payload, expected_response_payload)
    
    def test_disbursement_failed_because_there_is_no_account_number_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "amount": "10000",
            "bank_code": "bca"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: account_number, beneficiary_account_number tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)

    def test_disbursement_failed_because_there_is_no_amount_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "account_number": "98359135235",
            "bank_code": "bca"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: amount tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)
    
    def test_disbursement_failed_because_there_is_no_bank_code_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "account_number": "98359135235",
            "amount": "10000"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: bank_code, beneficiary_bank_name tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)

    def __fetch_api(self, payload: Dict[str, Any]) -> Response:
        from main import DISBURSEMENT_URL

        headers = {
            "Authorization": self.authorization_token,
            "Content-Type": "application/json",
        }
        
        return requests.post(
            url = DISBURSEMENT_URL,
            json = payload,
            headers = headers
        )