import json

from django.test import TestCase
from django.test.client import Client


class AccountTestCase(TestCase):
    fixtures = ['test_accounts.json']

    def _test_get_response(self, response_endpoint: str):
        c = Client()
        print(f'RUNNING GET {response_endpoint}')
        response = c.get(response_endpoint)
        body = json.loads(response.content.decode('utf8'))
        self.assertEquals(response.status_code, 200)
        print(json.dumps(body, indent=4, sort_keys=True))
        print('----------------------------------------------------------------------')

    def _test_patch_response(self, response_endpoint: str, data: dict):
        c = Client()
        print(f'RUNNING PATCH {response_endpoint}')
        print(f'PATCHING DATA: {data}')
        response = c.patch(response_endpoint, f'{data}'.replace('\'', '"'))
        body = json.loads(response.content.decode('utf8'))
        self.assertEquals(response.status_code, 200)
        print(json.dumps(body, indent=4, sort_keys=True))
        print('----------------------------------------------------------------------')

    def test_ping(self):
        self._test_get_response('/api/ping')

    def test_status(self):
        bad_status = '867f0924-a917-4711-9399-0b179a96392b'
        good_status = '7badc8f8-65bc-449a-8cde-855234ac63e1'

        self._test_get_response(f'/api/status/{bad_status}')
        self._test_get_response(f'/api/status/{good_status}')

    def test_add(self):
        bad_status = '867f0924-a917-4711-9399-0b179a96392b'
        good_status = '7badc8f8-65bc-449a-8cde-855234ac63e1'
        patch_data = {'addition': 77777}
        error_data = {'addition': -77777}

        self._test_patch_response(f'/api/add/{bad_status}', patch_data)
        self._test_patch_response(f'/api/add/{good_status}', patch_data)
        self._test_patch_response(f'/api/add/{good_status}', error_data)

    def test_substract(self):
        bad_status = '867f0924-a917-4711-9399-0b179a96392b'
        good_status = '26c940a1-7228-4ea2-a3bc-e6460b172040'
        bad_substraction = '7badc8f8-65bc-449a-8cde-855234ac63e1'
        extra_bad_substraction = '5597cc3d-c948-48a0-b711-393edf20d9c0'
        patch_data = {'substraction': 111}
        error_data = {'substraction': -111}

        self._test_patch_response(f'/api/substract/{bad_status}', patch_data)
        self._test_patch_response(f'/api/substract/{good_status}', patch_data)
        self._test_patch_response(f'/api/substract/{bad_substraction}', patch_data)
        self._test_patch_response(f'/api/substract/{extra_bad_substraction}', patch_data)
        self._test_patch_response(f'/api/substract/{good_status}', error_data)

