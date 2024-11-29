import unittest
import requests
from requests import Response
from typing import Dict, Any


class TestPaymentLink(unittest.TestCase):
    print_flag = True

    def setUp(self):
        self.vendor = getattr(self, 'vendor', None)
        self.authorization_token = getattr(self, 'authorization_token', None)

        if TestPaymentLink.print_flag:
            print()
            print()
            print(f"========== TEST PaymentLink FEATURE WITH VENDOR {self.vendor.upper()} ==========")
            TestPaymentLink.print_flag = False

    def test_payment_link_success(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "amount":"230000",
            "sender_name":"rila123",
            "title": "bayar",
            "email": "rila@gmail.com",
        }

        expected_response_payload = {
            "data": {
                "amount": 230000,
                "vendorName": self.vendor,
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()
        
        self.assertIn('id', response_payload['data'])
        self.assertIn('paymentLink', response_payload['data'])

        del response_payload['data']['id']
        del response_payload['data']['paymentLink']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_payload, expected_response_payload)
    

    def test_payment_link_failed_because_there_is_no_amount_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "sender_name":"rila123",
            "title": "bayar",
            "email": "rila@gmail.com",
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


    def __fetch_api(self, payload: Dict[str, Any]) -> Response:
        from main import PAYMENT_LINK_PAYMENT_URL

        headers = {
            "Authorization": self.authorization_token,
            "Content-Type": "application/json",
        }
        
        return requests.post(
            url = PAYMENT_LINK_PAYMENT_URL,
            json = payload,
            headers = headers
        )