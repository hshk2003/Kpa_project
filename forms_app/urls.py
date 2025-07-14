# forms_app/urls.py

from django.urls import path
from .views import BogieChecksheetCreateView, WheelSpecsView

urlpatterns = [
    # POST /api/forms/bogie-checksheet
    path('bogie-checksheet', BogieChecksheetCreateView.as_view(), name='bogie-checksheet'),

    # GET and POST /api/forms/wheel-specifications
    path('wheel-specifications', WheelSpecsView.as_view(), name='wheel-specifications'),
]
