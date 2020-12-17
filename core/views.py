from django.shortcuts import render
from rest_framework import viewsets, views  # add this
from .serializers import PaymentSerializer  # add this
from rest_framework.response import Response
from .models import Payment
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import statistics


class PaymentView(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    # queryset = Payment.objects.all()[:5]
    queryset = Payment.objects.all()


# Building a custom view model for other stuff
# @parser_classes([JSONParser])
class TestView(views.APIView):
    serializer_class = PaymentSerializer
    permission_classes = []

    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, *args, **kwargs):
        # test_id = request.data("test-id")
        print("What is this request \n")
        print(type(request))
        print(type(request.data))
        print(request.data["test-one"])
        test_id = request.data["test-one"]
        if test_id == "one":

            for i, c in enumerate(Payment.objects.all()[:5]):
                print(c.amount)
                print(i, c, type(c))

            data = list(Payment.objects.all()[:5].values())  # wrap in list(), because QuerySet is not JSON serializable
            print("Activated with one value")
            return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})
            # return Response({"success": True})
            # return Payment.objects.all()[:5]
        else:
            print("Something else")
            return Response({"success": False})


# Building a custom view model for other stuff
# @parser_classes([JSONParser])
class MeanMedianView(views.APIView):
    serializer_class = PaymentSerializer
    permission_classes = []

    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, *args, **kwargs):
        rental_values = []

        for i, c in enumerate(Payment.objects.all()):
            rental_values.append(c.amount)

        mean = statistics.mean(rental_values)
        median = statistics.median(rental_values)

        return Response({"mean": mean, "median": median})
