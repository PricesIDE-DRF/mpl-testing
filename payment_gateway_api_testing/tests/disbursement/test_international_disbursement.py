import unittest
import requests
from requests import Response
from typing import Dict, Any


class TestInternationalDisbursement(unittest.TestCase):
    print_flag = True

    def setUp(self):
        self.vendor = getattr(self, 'vendor', None)
        self.authorization_token = getattr(self, 'authorization_token', None)

        if TestInternationalDisbursement.print_flag:
            print()
            print()
            print(f"========== TEST INTERNATIONAL DISBURSEMENT FEATURE WITH VENDOR {self.vendor.upper()} ==========")
            TestInternationalDisbursement.print_flag = False
    
    def test_international_disbursement_with_transaction_type_c2b_success(self):
        request_payload = {
            "vendor_name": self.vendor,
            "destination_country": "GBR",
            "source_country": "IDN",
            "transaction_type": "C2B",
            "amount": "200",
            "beneficiary_account_number": "12435236235",
            "beneficiary_bank_id": "123",
            "beneficiary_full_name": "Beneficiary Test User",
            "beneficiary_bank_name": "Master Card",
            "beneficiary_nationality": "UK",
            "beneficiary_province": "Manchester",
            "beneficiary_city": "Manchester",
            "beneficiary_address": "Manchester",
            "beneficiary_relationship": "FRIEND",
            "beneficiary_source_of_funds": "BUSINESS",
            "beneficiary_remittance_purposes": "TRAVEL",
            "sender_name": "SENDER TEST USER",
            "sender_country": "100252",
            "sender_place_of_birth": "100252",
            "sender_date_of_birth": "1989-03-17",
            "sender_address": "A Address",
            "sender_identity_type": "nat_id",
            "sender_identity_number": "124252634634634",
            "sender_job": "private_employee",
            "sender_email": "sendertestuser@gmail.com",
            "sender_city": "Jakarta",
            "sender_phone_number": "08123456789",
            "beneficiary_sort_code": "506967"
        }

        expected_response_payload = {
            "data": {
                "bank_code": "Master Card",
                "account_number": "12435236235",
                "amount": 200.0,
                "destination_country": "IDN",
                "user_id": 9307076,
                "source_country": "GBR",
                "beneficiary_currency_code": "GBP"
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertIn('id', response_payload['data'])
        self.assertIn('exchange_rate', response_payload['data'])
        self.assertIn('fee', response_payload['data'])
        self.assertIn('amount_in_sender_currency', response_payload['data'])

        del response_payload['data']['id']
        del response_payload['data']['exchange_rate']
        del response_payload['data']['fee']
        del response_payload['data']['amount_in_sender_currency']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_payload, expected_response_payload)
    
    def test_international_disbursement_with_transaction_type_c2c_success(self):
        request_payload = {
            "vendor_name": self.vendor,
            "destination_country": "GBR",
            "source_country": "IDN",
            "transaction_type": "C2C",
            "amount": "200",
            "beneficiary_account_number": "12435236235",
            "beneficiary_bank_id": "123",
            "beneficiary_full_name": "Beneficiary Test User",
            "beneficiary_bank_name": "Master Card",
            "beneficiary_nationality": "UK",
            "beneficiary_province": "Manchester",
            "beneficiary_city": "Manchester",
            "beneficiary_address": "Manchester",
            "beneficiary_relationship": "FRIEND",
            "beneficiary_source_of_funds": "BUSINESS",
            "beneficiary_remittance_purposes": "TRAVEL",
            "sender_name": "SENDER TEST USER",
            "sender_country": "100252",
            "sender_place_of_birth": "100252",
            "sender_date_of_birth": "1989-03-17",
            "sender_address": "A Address",
            "sender_identity_type": "nat_id",
            "sender_identity_number": "124252634634634",
            "sender_job": "private_employee",
            "sender_email": "sendertestuser@gmail.com",
            "sender_city": "Jakarta",
            "sender_phone_number": "08123456789",
            "beneficiary_sort_code": "506967"
        }

        expected_response_payload = {
            "data": {
                "bank_code": "Master Card",
                "account_number": "12435236235",
                "amount": 200.0,
                "destination_country": "IDN",
                "user_id": 9307076,
                "source_country": "GBR",
                "beneficiary_currency_code": "GBP"
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertIn('id', response_payload['data'])
        self.assertIn('exchange_rate', response_payload['data'])
        self.assertIn('fee', response_payload['data'])
        self.assertIn('amount_in_sender_currency', response_payload['data'])

        del response_payload['data']['id']
        del response_payload['data']['exchange_rate']
        del response_payload['data']['fee']
        del response_payload['data']['amount_in_sender_currency']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_payload, expected_response_payload)
    
    def test_international_disbursement_failed_because_there_is_no_beneficiary_account_number_in_the_payload(self):
        request_payload = {
            "vendor_name": self.vendor,
            "destination_country": "GBR",
            "source_country": "IDN",
            "transaction_type": "C2B",
            "amount": "200",
            "beneficiary_bank_id": "123",
            "beneficiary_full_name": "Beneficiary Test User",
            "beneficiary_bank_name": "Master Card",
            "beneficiary_nationality": "UK",
            "beneficiary_province": "Manchester",
            "beneficiary_city": "Manchester",
            "beneficiary_address": "Manchester",
            "beneficiary_relationship": "FRIEND",
            "beneficiary_source_of_funds": "BUSINESS",
            "beneficiary_remittance_purposes": "TRAVEL",
            "sender_name": "SENDER TEST USER",
            "sender_country": "100252",
            "sender_place_of_birth": "100252",
            "sender_date_of_birth": "1989-03-17",
            "sender_address": "A Address",
            "sender_identity_type": "nat_id",
            "sender_identity_number": "124252634634634",
            "sender_job": "private_employee",
            "sender_email": "sendertestuser@gmail.com",
            "sender_city": "Jakarta",
            "sender_phone_number": "08123456789",
            "beneficiary_sort_code": "506967"
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
    
    def test_international_disbursement_failed_because_there_is_no_amount_in_the_payload(self):
        request_payload = {
            "vendor_name": self.vendor,
            "destination_country": "GBR",
            "source_country": "IDN",
            "transaction_type": "C2B",
            "beneficiary_account_number": "12435236235",
            "beneficiary_bank_id": "123",
            "beneficiary_full_name": "Beneficiary Test User",
            "beneficiary_bank_name": "Master Card",
            "beneficiary_nationality": "UK",
            "beneficiary_province": "Manchester",
            "beneficiary_city": "Manchester",
            "beneficiary_address": "Manchester",
            "beneficiary_relationship": "FRIEND",
            "beneficiary_source_of_funds": "BUSINESS",
            "beneficiary_remittance_purposes": "TRAVEL",
            "sender_name": "SENDER TEST USER",
            "sender_country": "100252",
            "sender_place_of_birth": "100252",
            "sender_date_of_birth": "1989-03-17",
            "sender_address": "A Address",
            "sender_identity_type": "nat_id",
            "sender_identity_number": "124252634634634",
            "sender_job": "private_employee",
            "sender_email": "sendertestuser@gmail.com",
            "sender_city": "Jakarta",
            "sender_phone_number": "08123456789",
            "beneficiary_sort_code": "506967"
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
    
    def test_international_disbursement_failed_because_there_is_no_beneficiary_bank_name_in_the_payload(self): 
        request_payload = {
            "vendor_name": self.vendor,
            "destination_country": "GBR",
            "source_country": "IDN",
            "transaction_type": "C2B",
            "amount": "200",
            "beneficiary_account_number": "12435236235",
            "beneficiary_bank_id": "123",
            "beneficiary_full_name": "Beneficiary Test User",
            "beneficiary_nationality": "UK",
            "beneficiary_province": "Manchester",
            "beneficiary_city": "Manchester",
            "beneficiary_address": "Manchester",
            "beneficiary_relationship": "FRIEND",
            "beneficiary_source_of_funds": "BUSINESS",
            "beneficiary_remittance_purposes": "TRAVEL",
            "sender_name": "SENDER TEST USER",
            "sender_country": "100252",
            "sender_place_of_birth": "100252",
            "sender_date_of_birth": "1989-03-17",
            "sender_address": "A Address",
            "sender_identity_type": "nat_id",
            "sender_identity_number": "124252634634634",
            "sender_job": "private_employee",
            "sender_email": "sendertestuser@gmail.com",
            "sender_city": "Jakarta",
            "sender_phone_number": "08123456789",
            "beneficiary_sort_code": "506967"
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
    
    def test_international_disbursement_failed_because_there_is_no_sender_country_in_the_payload(self):
        request_payload = {
            "vendor_name": self.vendor,
            "destination_country": "GBR",
            "source_country": "IDN",
            "transaction_type": "C2B",
            "amount": "200",
            "beneficiary_account_number": "12435236235",
            "beneficiary_bank_id": "123",
            "beneficiary_full_name": "Beneficiary Test User",
            "beneficiary_bank_name": "Master Card",
            "beneficiary_nationality": "UK",
            "beneficiary_province": "Manchester",
            "beneficiary_city": "Manchester",
            "beneficiary_address": "Manchester",
            "beneficiary_relationship": "FRIEND",
            "beneficiary_source_of_funds": "BUSINESS",
            "beneficiary_remittance_purposes": "TRAVEL",
            "sender_name": "SENDER TEST USER",
            "sender_place_of_birth": "100252",
            "sender_date_of_birth": "1989-03-17",
            "sender_address": "A Address",
            "sender_identity_type": "nat_id",
            "sender_identity_number": "124252634634634",
            "sender_job": "private_employee",
            "sender_email": "sendertestuser@gmail.com",
            "sender_city": "Jakarta",
            "sender_phone_number": "08123456789",
            "beneficiary_sort_code": "506967"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: sender_country tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)
    
    def test_international_disbursement_failed_because_there_is_no_sender_name_in_the_payload(self):
        request_payload = {
            "vendor_name": self.vendor,
            "destination_country": "GBR",
            "source_country": "IDN",
            "transaction_type": "C2B",
            "amount": "200",
            "beneficiary_account_number": "12435236235",
            "beneficiary_bank_id": "123",
            "beneficiary_full_name": "Beneficiary Test User",
            "beneficiary_bank_name": "Master Card",
            "beneficiary_nationality": "UK",
            "beneficiary_province": "Manchester",
            "beneficiary_city": "Manchester",
            "beneficiary_address": "Manchester",
            "beneficiary_relationship": "FRIEND",
            "beneficiary_source_of_funds": "BUSINESS",
            "beneficiary_remittance_purposes": "TRAVEL",
            "sender_country": "100252",
            "sender_place_of_birth": "100252",
            "sender_date_of_birth": "1989-03-17",
            "sender_address": "A Address",
            "sender_identity_type": "nat_id",
            "sender_identity_number": "124252634634634",
            "sender_job": "private_employee",
            "sender_email": "sendertestuser@gmail.com",
            "sender_city": "Jakarta",
            "sender_phone_number": "08123456789",
            "beneficiary_sort_code": "506967"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: sender_name tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)
    
    def test_international_disbursement_failed_because_there_is_no_sender_address_in_the_payload(self):
        request_payload = {
            "vendor_name": self.vendor,
            "destination_country": "GBR",
            "source_country": "IDN",
            "transaction_type": "C2B",
            "amount": "200",
            "beneficiary_account_number": "12435236235",
            "beneficiary_bank_id": "123",
            "beneficiary_full_name": "Beneficiary Test User",
            "beneficiary_bank_name": "Master Card",
            "beneficiary_nationality": "UK",
            "beneficiary_province": "Manchester",
            "beneficiary_city": "Manchester",
            "beneficiary_address": "Manchester",
            "beneficiary_relationship": "FRIEND",
            "beneficiary_source_of_funds": "BUSINESS",
            "beneficiary_remittance_purposes": "TRAVEL",
            "sender_name": "SENDER TEST USER",
            "sender_country": "100252",
            "sender_place_of_birth": "100252",
            "sender_date_of_birth": "1989-03-17",
            "sender_identity_type": "nat_id",
            "sender_identity_number": "124252634634634",
            "sender_job": "private_employee",
            "sender_email": "sendertestuser@gmail.com",
            "sender_city": "Jakarta",
            "sender_phone_number": "08123456789",
            "beneficiary_sort_code": "506967"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: sender_address tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)
    
    def test_international_disbursement_failed_because_there_is_no_sender_job_in_the_payload(self):
        request_payload = {
            "vendor_name": self.vendor,
            "destination_country": "GBR",
            "source_country": "IDN",
            "transaction_type": "C2B",
            "amount": "200",
            "beneficiary_account_number": "12435236235",
            "beneficiary_bank_id": "123",
            "beneficiary_full_name": "Beneficiary Test User",
            "beneficiary_bank_name": "Master Card",
            "beneficiary_nationality": "UK",
            "beneficiary_province": "Manchester",
            "beneficiary_city": "Manchester",
            "beneficiary_address": "Manchester",
            "beneficiary_relationship": "FRIEND",
            "beneficiary_source_of_funds": "BUSINESS",
            "beneficiary_remittance_purposes": "TRAVEL",
            "sender_name": "SENDER TEST USER",
            "sender_country": "100252",
            "sender_place_of_birth": "100252",
            "sender_date_of_birth": "1989-03-17",
            "sender_address": "A Address",
            "sender_identity_type": "nat_id",
            "sender_identity_number": "124252634634634",
            "sender_email": "sendertestuser@gmail.com",
            "sender_city": "Jakarta",
            "sender_phone_number": "08123456789",
            "beneficiary_sort_code": "506967"
        }

        expected_response_payload = {
            "data": {
                "message": "Bad Request: sender_job tidak ditemukan pada payload.",
                "vmjErrorCode": 4000
            }
        }

        response = self.__fetch_api(request_payload)
        response_payload = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_payload, expected_response_payload)
    
    def __fetch_api(self, payload: Dict[str, Any]) -> Response:
        from main import INTERNATIONAL_DISBURSEMENT_URL

        headers = {
            "Authorization": self.authorization_token,
            "Content-Type": "application/json",
        }
        
        return requests.post(
            url = INTERNATIONAL_DISBURSEMENT_URL,
            json = payload,
            headers = headers
        )