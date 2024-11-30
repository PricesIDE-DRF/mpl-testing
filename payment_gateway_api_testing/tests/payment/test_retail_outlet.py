import unittest
import requests
from requests import Response
from typing import Dict, Any


class TestRetailOutlet(unittest.TestCase):
    print_flag = True

    def setUp(self):
        self.vendor = getattr(self, 'vendor', None)
        self.authorization_token = getattr(self, 'authorization_token', None)

        if TestRetailOutlet.print_flag:
            print()
            print()
            print(f"========== TEST RetailOutlet FEATURE WITH VENDOR {self.vendor.upper()} ==========")
            TestRetailOutlet.print_flag = False

    def test_retail_outlet_success(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "amount" : "145000",
            "retail_outlet": "indomaret",
        }

        expected_response_payload = {
            "data": {
                "vendorName": self.vendor,
                "amount": 145000.0,
                "retailOutlet": "indomaret",
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()
        
        self.assertIn('id', response_payload['data'])
        self.assertIn('retailPaymentCode', response_payload['data'])

        del response_payload['data']['id']
        del response_payload['data']['retailPaymentCode']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_payload, expected_response_payload)
    

    def test_retail_outlet_failed_because_there_is_no_amount_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "retail_outlet":"indomaret",
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

    def test_retail_outlet_failed_because_there_is_no_retailOutlet_in_the_payload(self):
        request_payload = {
            f"vendor_name": self.vendor,
            "amount" : "145000",
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: retail_outlet tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)


    def __fetch_api(self, payload: Dict[str, Any]) -> Response:
        from main import RETAIL_OUTLET_PAYMENT_URL

        headers = {
            "Authorization": self.authorization_token,
            "Content-Type": "application/json",
        }
        
        return requests.post(
            url = RETAIL_OUTLET_PAYMENT_URL,
            json = payload,
            headers = headers
        )