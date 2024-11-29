import unittest
import requests
from requests import Response
from typing import Dict, Any


class TestVirtualAccount(unittest.TestCase):
    print_flag = True

    def setUp(self):
        self.vendor = getattr(self, 'vendor', None)
        self.authorization_token = getattr(self, 'authorization_token', None)

        if TestVirtualAccount.print_flag:
            print()
            print()
            print(f"========== TEST VirtualAccount FEATURE WITH VENDOR {self.vendor.upper()} ==========")
            TestVirtualAccount.print_flag = False

    def test_virtual_account_success(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "bank": "bca",
            "title": "Bayar Gojek",
            "amount": "100000",
            "name": "Rifqi Farel Muhammad",
            "email": "rifqifarel222@gmail.com",
            "phone": "085892025984"
        }

        expected_response_payload = {
            "data": {
                "vendorName": self.vendor,
                "bankCode": "bca",
                "amount": 100000,
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()
        
        self.assertIn('id', response_payload['data'])
        self.assertIn('vaAccountNumber', response_payload['data'])

        del response_payload['data']['id']
        del response_payload['data']['vaAccountNumber']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_payload, expected_response_payload)
    

    def test_virtual_account_failed_because_there_is_no_amount_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "bank": "bca",
            "title": "Bayar Gojek",
            "name": "Rifqi Farel Muhammad",
            "email": "rifqifarel222@gmail.com",
            "phone": "085892025984"
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

    def test_virtual_account_failed_because_there_is_no_bank_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "title": "Bayar Gojek",
            "amount": "100000",
            "name": "Rifqi Farel Muhammad",
            "email": "rifqifarel222@gmail.com",
            "phone": "085892025984"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: bank tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)


    def __fetch_api(self, payload: Dict[str, Any]) -> Response:
        from main import VIRTUAL_ACCOUNT_PAYMENT_URL

        headers = {
            "Authorization": self.authorization_token,
            "Content-Type": "application/json",
        }
        
        return requests.post(
            url = VIRTUAL_ACCOUNT_PAYMENT_URL,
            json = payload,
            headers = headers
        )