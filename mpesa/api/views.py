from datetime import datetime
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from mpesa.api.serializers import LNMonlineSerializer
from mpesa.models import LNMonline




class LNMCallbackAPIView(CreateAPIView):
    queryset = LNMonline.objects.all()
    serializer_class = LNMonlineSerializer
    permission_classes = [AllowAny]
    def create(self, request):
        merchant_request_id = request.data["Body"]["stkCallback"]["MerchantRequestID"]
        checkout_request_id = request.data["Body"]["stkCallback"]["CheckoutRequestID"]
        result_code = request.data["Body"]["stkCallback"]["ResultCode"]
        result_description = request.data["Body"]["stkCallback"]["ResultDesc"]
        amount = request.data["Body"]["stkCallback"]["CallbackMetadata"]['Item'][0]['Value']
        mpesa_reciept_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]['Item'][1]['Value']
        # balance = request.data["Body"]["stkCallback"]["CallbackMetadata"]['Item'][2]['Value']
        transaction_date = request.data["Body"]["stkCallback"]["CallbackMetadata"]['Item'][3]['Value']
        phone_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]['Item'][4]['Value']

        str_transaction_date = str(transaction_date)

        transaction_datetime = datetime.strptime(str_transaction_date, "%Y%m%d%H%M%S")

        x = LNMonline.objects.create(
        Merchant_Request_ID = merchant_request_id,
        Checkout_Request_ID = checkout_request_id,
        Result_Code = result_code,
        Result_Description = result_description,
        Amount = amount,
        Mpesa_Receipt_Number = mpesa_reciept_number,
        Transaction_Date = transaction_datetime,
        Phone_Number = phone_number
        )
        x.save()
        return Response({"Description":"It worked"})
        