import unittest
import requests
from requests import Response
from typing import Dict, Any


class TestInvoice(unittest.TestCase):
    print_flag = True

    def setUp(self):
        self.vendor = getattr(self, 'vendor', None)
        self.authorization_token = getattr(self, 'authorization_token', None)

        if TestInvoice.print_flag:
            print()
            print()
            print(f"========== TEST Invoice FEATURE WITH VENDOR {self.vendor.upper()} ==========")
            TestInvoice.print_flag = False

    def test_invoice_success(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "amount": "150000",
            "quantity": "3",
            "price_per_item": "50000"
        }

        expected_response_payload = {
            "data": {
                "amount": 150000,
                "vendorName": self.vendor,
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()
        
        self.assertIn('id', response_payload['data'])
        self.assertIn('transactionUrl', response_payload['data'])

        del response_payload['data']['id']
        del response_payload['data']['transactionUrl']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_payload, expected_response_payload)
    

    def test_invoice_failed_because_there_is_no_amount_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "quantity": "3",
            "price_per_item": "50000"
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

    def test_invoice_failed_because_there_is_no_quantity_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "amount": "150000",
            "price_per_item": "50000"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: quantity tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)

    def test_invoice_failed_because_there_is_no_price_per_item_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "amount": "150000",
            "quantity": "3"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: price_per_item tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)

    def test_invoice_failed_because_sum_amount_not_match(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "amount": "150000",
            "quantity": "2",
            "price_per_item": "50000",
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: Jumlah quantity dan price_per_item tidak sesuai dengan amount.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)


    def __fetch_api(self, payload: Dict[str, Any]) -> Response:
        from main import INVOICE_PAYMENT_URL

        headers = {
            "Authorization": self.authorization_token,
            "Content-Type": "application/json",
        }
        
        return requests.post(
            url = INVOICE_PAYMENT_URL,
            json = payload,
            headers = headers
        )