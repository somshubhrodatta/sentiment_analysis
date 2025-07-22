from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import analyze_sentiment
from .models import ChatMessage

class ChatAPI(APIView):
    def post(self, request):
        text = request.data.get('message')
        if not text:
            return Response({'error': 'Message required'}, status=400)
        
        # Analyze sentiment
        result = analyze_sentiment(text)
        
        # Save to database
        ChatMessage.objects.create(
            user_message=text,
            sentiment=result['label'],
            confidence=result['score'],
            bot_response=result['response']
        )
        
        return Response({
            'message': text,
            'sentiment': result['label'],
            'confidence': result['score'],
            'response': result['response']
        })
def chat_view(request):
    return render(request, 'chatbot/index.html')