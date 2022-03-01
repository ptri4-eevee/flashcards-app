from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from .models import Pattern, PatternTable

# Create your views here.
def fetch_static(response):
  data = [
    {"key": 0, "name": "Sliding Window", "question": "a", "solution": "a"}, 
    {"key": 1, "name": "Two Pointers", "question": "b", "solution": "b"}, 
    {"key": 2, "name": "", "question": "c", "solution": "c"}, 
    {"key": 3, "name": "d", "question": "d", "solution": "d"}, 
    {"key": 4, "name": "e", "question": "e", "solution": "e"}, 
    {"key": 5, "name": "f", "question": "f", "solution": "f"}, 
    {"key": 6, "name": "g", "question": "g", "solution": "g"}, 
    {"key": 7, "name": "h", "question": "h", "solution": "h"}, 
    {"key": 8, "name": "i", "question": "i", "solution": "i"}, 
    {"key": 9, "name": "j", "question": "j", "solution": "j"}, 
    {"key": 10, "name": "k", "question": "k", "solution": "k"}, 
    {"key": 11, "name": "l", "question": "l", "solution": "l"}, 
    {"key": 12, "name": "m", "question": "m", "solution": "m"}, 
    {"key": 13, "name": "n", "question": "n", "solution": "n"}
    ]  
  return JsonResponse(data, safe=False)

def fetch_db(response):
  pattern = Pattern.objects
  return HttpResponse('<h2>%s</h2><br></br><p>%s</p>', % () )
