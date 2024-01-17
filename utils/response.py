from rest_framework import status
from rest_framework.response import Response


class CustomResponse:

    def __init__(self, message={}, general_message=[], response={}):
        if not isinstance(general_message, list):
            general_message = [general_message]

        self.message = {'general': general_message}
        self.message.update(message)
        self.response = response

    def get_success_response(self):
        return Response(
            data={
                "hasError": False,
                "statusCode": 200,
                "message": self.message,
                "response": self.response,
            },
            status=status.HTTP_200_OK
        )

    def get_failure_response(self):
        return Response(
            data={
                "hasError": True,
                "statusCode": 400,
                "message": self.message,
                "response": self.response,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

