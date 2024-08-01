# views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_data = {
            "success": True,
            "data": serializer.data,
            "message": "Payment created successfully"
        }
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['post'])
    def confirm(self, request, pk=None):
        payment = self.get_object()
        if payment.status == 'Pending':
            payment.status = 'Confirmed'
            payment.save()
            response_data = {
                "success": True,
                "data": PaymentSerializer(payment).data,
                "message": "Payment confirmed successfully"
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data = {
                "success": False,
                "message": "Payment is not in pending status"
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)



