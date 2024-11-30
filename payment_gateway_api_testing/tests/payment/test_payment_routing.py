import unittest
import requests
from requests import Response
from typing import Dict, Any


class TestPaymentRouting(unittest.TestCase):
    print_flag = True

    def setUp(self):
        self.vendor = getattr(self, 'vendor', None)
        self.authorization_token = getattr(self, 'authorization_token', None)

        if TestPaymentRouting.print_flag:
            print()
            print()
            print(f"========== TEST PaymentRouting FEATURE WITH VENDOR {self.vendor.upper()} ==========")
            TestPaymentRouting.print_flag = False

    def test_payment_routing_success(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "amount" : "100000",
            "recipient_account": "123",
            "recipient_bank": "e14",
            "recipient_amount": "100000",
            "recipient_email" : "budi.arti@gmail.com",
            "recipient_note" : "donasi"
        }

        expected_response_payload = {
            "data": {
                "amount": 100000,
                "vendorName": self.vendor,
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()
        
        self.assertIn('id', response_payload['data'])
        self.assertIn('paymentCheckoutUrl', response_payload['data'])

        del response_payload['data']['id']
        del response_payload['data']['paymentCheckoutUrl']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_payload, expected_response_payload)
    

    def test_payment_routing_failed_because_there_is_no_amount_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "recipient_account": "123",
            "recipient_bank": "e14",
            "recipient_amount": "100000",
            "recipient_email" : "budi.arti@gmail.com",
            "recipient_note" : "donasi"
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

    def test_payment_routing_failed_because_there_is_no_recipient_account_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "amount" : "100000",
            "recipient_bank": "e14",
            "recipient_amount": "100000",
            "recipient_email" : "budi.arti@gmail.com",
            "recipient_note" : "donasi"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: recipient_account tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)

    def test_payment_routing_failed_because_there_is_no_recipient_bank_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "amount" : "100000",
            "recipient_account": "123",
            "recipient_amount": "100000",
            "recipient_email" : "budi.arti@gmail.com",
            "recipient_note" : "donasi"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: recipient_bank tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)

    def test_payment_routing_failed_because_there_is_no_recipient_amount_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "amount" : "100000",
            "recipient_account": "123",
            "recipient_bank": "e14",
            "recipient_email" : "budi.arti@gmail.com",
            "recipient_note" : "donasi"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: recipient_amount tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)

    def test_payment_routing_failed_because_there_is_no_recipient_email_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "amount" : "100000",
            "recipient_account": "123",
            "recipient_amount": "100000",
            "recipient_bank": "e14",
            "recipient_note" : "donasi"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: recipient_email tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)

    def test_payment_routing_failed_because_there_is_no_recipient_note_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "amount" : "100000",
            "recipient_account": "123",
            "recipient_amount": "100000",
            "recipient_bank": "e14",
            "recipient_email" : "budi.arti@gmail.com"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: recipient_note tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)


    def __fetch_api(self, payload: Dict[str, Any]) -> Response:
        from main import PAYMENT_ROUTING_PAYMENT_URL

        headers = {
            "Authorization": self.authorization_token,
            "Content-Type": "application/json",
        }
        
        return requests.post(
            url = PAYMENT_ROUTING_PAYMENT_URL,
            json = payload,
            headers = headers
        )