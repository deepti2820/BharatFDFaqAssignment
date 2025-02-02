from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer  # ✅ Import the serializer

class FAQListView(APIView):
    def get(self, request):
        lang = request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        faqs = cache.get(cache_key)

        if not faqs:
            faqs = FAQ.objects.all()
            serializer = FAQSerializer(faqs, many=True)  # ✅ Use the serializer
            faqs = serializer.data
            cache.set(cache_key, faqs, timeout=3600)  # Cache for 1 hour

        return Response(faqs)
