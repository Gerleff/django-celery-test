"""API методы"""
import json
from uuid import uuid4

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views import View

from .models import Account
from .schemas import (ApiOutputSchema, ApiAddInputSchema,
                      ApiSubstractInputSchema)


class ApiView(View):
    def __init__(self, *args, **kwargs):
        super(ApiView, self).__init__(*args, **kwargs)
        self.output_schema = ApiOutputSchema
        self.input_schema = None


class PingView(ApiView):
    """обработчик GET /ping"""
    def get(self, request: WSGIRequest) -> JsonResponse:
        result = {
            'status': 200,
            'description': {
                'message': 'pong'
            }
        }
        response = self.output_schema(**result)
        return JsonResponse(response.dict())


class StatusView(ApiView):
    """обработчик GET /status"""
    def get(self, request: WSGIRequest, account_id: uuid4) -> JsonResponse:
        account = Account.objects.get(pk=account_id)
        result = {
            'status': 200,
            'addition': account.to_dict(),
            'description': {
                'message': 'Accepted' if account.status else 'Denied'
            }
        }
        response = self.output_schema(**result)
        return JsonResponse(response.dict())


class SubstractView(ApiView):
    """обработчик PATCH /substract"""
    @staticmethod
    def calculate(account: Account, request_body: dict) -> int:
        """Вычислить возможность списания"""
        calc = account.balance - account.hold - request_body.get('substraction')
        if calc >= 0:
            account.hold += request_body.get('substraction')
            account.save()
        return calc

    def patch(self, request: WSGIRequest, account_id: uuid4) -> JsonResponse:
        self.input_schema = ApiSubstractInputSchema
        account = Account.objects.get(pk=account_id)
        try:
            request_body = self.input_schema(
                **json.loads(request.body.decode('utf-8'))).dict()
            assert account.status, 'Card is blocked'
            calc = self.calculate(account, request_body)
            result = {
                'status': 200,
                'result': False if calc < 0 else True
            }
        except Exception as e:
            result = {
                'status': 400,
                'description': {
                    'message': str(e)
                }
            }
        result['addition'] = account.to_dict()
        response = self.output_schema(**result)
        return JsonResponse(response.dict())


class AddView(ApiView):
    """обработчик PATCH /add"""
    def patch(self, request: WSGIRequest, account_id: uuid4) -> JsonResponse:
        self.input_schema = ApiAddInputSchema
        account = Account.objects.get(pk=account_id)
        try:
            request_body = self.input_schema(
                **json.loads(request.body.decode('utf-8'))).dict()
            assert account.status, 'Card is blocked'
            account.balance += request_body.get('addition')
            account.save()
            result = {
                'status': 200,
                'result': True
            }
        except Exception as e:
            result = {
                'status': 400,
                'description': {
                    'message': str(e)
                }
            }
        result['addition'] = account.to_dict()
        response = self.output_schema(**result)
        return JsonResponse(response.dict())
