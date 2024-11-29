import unittest
import requests
from requests import Response
from typing import Dict, Any


class TestSpecifiedRecipientDisbursement(unittest.TestCase):
    print_flag = True

    def setUp(self):
        self.vendor = getattr(self, 'vendor', None)
        self.authorization_token = getattr(self, 'authorization_token', None)

        if TestSpecifiedRecipientDisbursement.print_flag:
            print()
            print()
            print(f"========== TEST SPECIFIED RECIPIENT DISBURSEMENT FEATURE WITH VENDOR {self.vendor.upper()} ==========")
            TestSpecifiedRecipientDisbursement.print_flag = False
    
    def test_specified_recipient_disbursement_success(self):
        request_payload = {
            "vendor_name": self.vendor,
            "account_number": "9835913523521",
            "amount": "1000",
            "bank_code": "ID_BCA",
            "account_holder_name": "SENDER TEST USER",
            "currency": "IDR"
        }

        expected_response_payload = {
            "data": {
                "bank_code": "ID_BCA",
                "account_number": "9835913523521",
                "amount": 1000.0,
                "user_id": 662,
                "account_holder_name": "SENDER TEST USER",
                "currency": "IDR",
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()
        
        self.assertIn('id', response_payload['data'])

        del response_payload['data']['id']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_payload, expected_response_payload)
    
    def test_specified_recipient_disbursement_failed_because_there_is_no_account_number_in_the_payload(self):
        request_payload = {
            "vendor_name": self.vendor,
            "amount": "1000",
            "bank_code": "ID_BCA",
            "account_holder_name": "SENDER TEST USER",
            "currency": "IDR"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: account_number tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)
    
    def test_specified_recipient_disbursement_failed_because_there_is_no_amount_in_the_payload(self):
        request_payload = {
            "vendor_name": self.vendor,
            "account_number": "9835913523521",
            "bank_code": "ID_BCA",
            "account_holder_name": "SENDER TEST USER",
            "currency": "IDR"
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
    
    def test_specified_recipient_disbursement_failed_because_there_is_no_bank_code_in_the_payload(self):
        request_payload = {
            "vendor_name": self.vendor,
            "account_number": "9835913523521",
            "amount": "1000",
            "account_holder_name": "SENDER TEST USER",
            "currency": "IDR"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: bank_code tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)
    
    def test_specified_recipient_disbursement_failed_because_there_is_no_currency_in_the_payload(self):
        request_payload = {
            "vendor_name": self.vendor,
            "account_number": "9835913523521",
            "amount": "1000",
            "bank_code": "ID_BCA",
            "account_holder_name": "SENDER TEST USER"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: currency tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)

    def test_specified_recipient_disbursement_failed_because_unsupported_currency_type(self):
        request_payload = {
            "vendor_name": self.vendor,
            "account_number": "9835913523521",
            "amount": "1000",
            "bank_code": "ID_BCA",
            "account_holder_name": "SENDER TEST USER",
            "currency": "USD"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: Invalid currency: USD. Supported currencies are: IDR, PHP, MYR, VND, THB",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)
    
    def test_specified_recipient_disbursement_failed_because_there_is_no_account_holder_name_in_the_payload(self):
        request_payload = {
            "vendor_name": self.vendor,
            "account_number": "9835913523521",
            "amount": "1000",
            "bank_code": "ID_BCA",
            "currency": "IDR"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: account_holder_name tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)
 
    def __fetch_api(self, payload: Dict[str, Any]) -> Response:
        from main import SPECIFIED_RECIPIENT_DISBURSEMENT_URL

        headers = {
            "Authorization": self.authorization_token,
            "Content-Type": "application/json",
        }
        
        return requests.post(
            url = SPECIFIED_RECIPIENT_DISBURSEMENT_URL,
            json = payload,
            headers = headers
        )