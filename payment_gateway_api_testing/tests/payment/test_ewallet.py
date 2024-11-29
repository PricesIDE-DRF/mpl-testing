import unittest
import requests
from requests import Response
from typing import Dict, Any


class TestEwallet(unittest.TestCase):
    print_flag = True

    def setUp(self):
        self.vendor = getattr(self, 'vendor', None)
        self.authorization_token = getattr(self, 'authorization_token', None)

        if TestEwallet.print_flag:
            print()
            print()
            print(f"========== TEST EWALLET FEATURE WITH VENDOR {self.vendor.upper()} ==========")
            TestEwallet.print_flag = False

    def test_ewallet_success(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "ewallet_type": "Gopay",
            "title": "Bayar Gojek",
            "amount": "100000",
            "name": "Rifqi Farel Muhammad",
            "email": "rifqifarel222@gmail.com",
            "phone": "085892025984"
        }

        expected_response_payload = {
            "data": {
                "amount": 100000,
                "phoneNumber": "085892025984",
                "eWalletType": "Gopay",
                "vendorName": self.vendor,
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()
        
        self.assertIn('id', response_payload['data'])

        del response_payload['data']['id']
        del response_payload['data']['eWalletUrl']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_payload, expected_response_payload)
    
    def test_ewallet_failed_because_there_is_no_phone_number_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "ewallet_type": "Gopay",
            "title": "Bayar Gojek",
            "amount": "100000",
            "name": "Rifqi Farel Muhammad",
            "email": "rifqifarel222@gmail.com"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: phone tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)

    def test_ewallet_failed_because_there_is_no_amount_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "ewallet_type": "Gopay",
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

    def test_ewallet_failed_because_there_is_no_ewallet_type_in_the_payload(self):
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
                "message": "Bad Request: ewallet_type tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)


    def __fetch_api(self, payload: Dict[str, Any]) -> Response:
        from main import EWALLET_PAYMENT_URL

        headers = {
            "Authorization": self.authorization_token,
            "Content-Type": "application/json",
        }
        
        return requests.post(
            url = EWALLET_PAYMENT_URL,
            json = payload,
            headers = headers
        )