from django.http import JsonResponse
from django.shortcuts import render

# Function to initialize the application
def init(request):
    if request.method == "GET":
        return render(request, "index.html", {})

def index(request):
    return JsonResponse({"message": "Welcome to the AWS Account Portal app!"}, status=200)