import unittest
import requests
from requests import Response
from typing import Dict, Any


class TestCreditCard(unittest.TestCase):
    print_flag = True

    def setUp(self):
        self.vendor = getattr(self, 'vendor', None)
        self.authorization_token = getattr(self, 'authorization_token', None)

        if TestCreditCard.print_flag:
            print()
            print()
            print(f"========== TEST CreditCard FEATURE WITH VENDOR {self.vendor.upper()} ==========")
            TestCreditCard.print_flag = False

    def test_credit_card_success(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "card_number": "4011111111111112",
            "card_exp_month": "12",
            "card_exp_year": "25",
            "card_cvv": "123",
            "amount" : "16650",
        }

        expected_response_payload = {
            "data": {
                "amount": 16650,
                "statusCreditPayment": "BERHASIL",
                "vendorName": self.vendor,
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()
        
        self.assertIn('id', response_payload['data'])

        del response_payload['data']['id']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_payload, expected_response_payload)
    

    def test_credit_card_failed_because_there_is_no_amount_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "card_number": "4011111111111112",
            "card_exp_month": "12",
            "card_exp_year": "25",
            "card_cvv": "123"
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

    def test_credit_card_failed_because_there_is_no_card_number_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "card_exp_month": "12",
            "card_exp_year": "25",
            "card_cvv": "123",
            "amount" : "16650",
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: card_number tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)

    def test_credit_card_failed_because_there_is_no_card_exp_month_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "card_number": "4011111111111112",
            "card_exp_year": "25",
            "card_cvv": "123",
            "amount" : "16650",
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: card_exp_month tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)

    def test_credit_card_failed_because_there_is_no_card_exp_year_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "card_number": "4011111111111112",
            "card_exp_month": "12",
            "card_cvv": "123",
            "amount" : "16650",
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: card_exp_year tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)

    def test_credit_card_failed_because_there_is_no_card_cvv_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "card_number": "4011111111111112",
            "card_exp_month": "12",
            "card_exp_year": "25",
            "amount" : "16650",
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: card_cvv tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)

    def __fetch_api(self, payload: Dict[str, Any]) -> Response:
        from main import CREDIT_CARD_PAYMENT_URL

        headers = {
            "Authorization": self.authorization_token,
            "Content-Type": "application/json",
        }
        
        return requests.post(
            url = CREDIT_CARD_PAYMENT_URL,
            json = payload,
            headers = headers
        )