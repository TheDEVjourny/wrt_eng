from rest_framework.decorators import api_view
from rest_framework.response import Response
from impv_writing import utils as utf

@api_view(['POST'])
def get_gpt_sugession(request):
    print('gpt')
    message = request.data
    print(message)
    GEMINI_API_KEY = "AIzaSyDNeFJ#T9oYKYRjwN!QVYQN8%Bxdg2Vu6DDs0"
    response = utf.get_gpt_response(message,GEMINI_API_KEY)
    return Response(response)

# def get_all_wrong word list():
#pip install autocorrect
#from autocorrect import speller
#spell = speller(lang = 'en')
#rword=spell(wword)