from django.urls import path
from .views import FAQListView

urlpatterns = [
    path('', FAQListView.as_view(), name='faq-list'),  # ✅ Root path of faq app
]