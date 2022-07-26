from django.shortcuts import render

# Create your views here.

def chat( request ):
    if "roomid" in request.GET:
        chat_id = request.GET["roomid"]
    return render( request, 'main/chatmain.html' )