from django.urls import path
from .views import PredictLandTypeView

urlpatterns = [
    path('atmosphere/predict/', PredictLandTypeView.as_view(), name='predict_land_type'),
]
