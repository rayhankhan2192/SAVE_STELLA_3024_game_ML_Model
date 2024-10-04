from django.urls import path
from .views import PredictAquaticEnvironmentView

urlpatterns = [
    path('hydrosphere/predict/', PredictAquaticEnvironmentView.as_view(), name='predict_aquatic_environment'),
]
