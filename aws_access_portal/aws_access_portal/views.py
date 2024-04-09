from django.shortcuts import render

# Function to initialize the application
def init(request):
    if request.method == "GET":
        return render(request, "index.html", {})