from django.shortcuts import render
from .serializers import BogieChecksheetSerializer, WheelSpecificationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WheelSpecificationForm

# Create your views here.


class BogieChecksheetCreateView(APIView):
    def post(self, request):
        serializer = BogieChecksheetSerializer(data=request.data)
        if serializer.is_valid():
            form = serializer.save()
            # Prepare custom response data
            data = {
                "formNumber": form.formNumber,
                "inspectionBy": form.inspectionBy,
                "inspectionDate": form.inspectionDate.isoformat(),
                "status": form.status
            }
            return Response({"success": True, "message": "Bogie checksheet submitted successfully.", "data": data},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"success": False, "message": "Validation error", "errors": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

class WheelSpecsView(APIView):
    def get(self, request):
        queryset = WheelSpecificationForm.objects.all()
        # apply optional filters
        for param in ('formNumber', 'submittedBy', 'submittedDate'):
            value = request.query_params.get(param)
            if value:
                queryset = queryset.filter(**{param: value})
        serializer = WheelSpecificationSerializer(queryset, many=True)
        return Response({
            "success": True,
            "message": "Wheel specifications fetched successfully.",
            "data": serializer.data
        })

    def post(self, request):
        serializer = WheelSpecificationSerializer(data=request.data)
        if serializer.is_valid():
            form = serializer.save()
            data = {
                "formNumber": form.formNumber,
                "status": "Saved",
                "submittedBy": form.submittedBy,
                "submittedDate": form.submittedDate.isoformat()
            }
            return Response({
                "success": True,
                "message": "Wheel specification submitted successfully.",
                "data": data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "success": False,
            "message": "Validation error",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

