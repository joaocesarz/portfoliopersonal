from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.


def main(request: HttpRequest) -> HttpResponse:
    
    match request.method:

        case "GET":

            return render(request, "main.html")