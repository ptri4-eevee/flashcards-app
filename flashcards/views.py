from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from .models import Pattern

# Create your views here.
def fetch_static(response):
  data = [
    {
      "id": 0,
      "question": "Given an array of positive numbers and a positive number k, find the maximum sum of any contiguous subarray of size k.",
      "answer": "To calculate the sum of a contiguous subarray, we can utilize the sum of the previous subarray. Consider each subarray as a sliding window of size k. To calculat the sum of the next subarray, slide the window ahead by one element. Slide the window forward and claculate the sum of the new position of the sliding window. Subtract the element going out of the sliding window, ie subtract the first element of the window. Add the new element getting included in the sliding window, ie the element coing right after the end of the window. This approach will save us from re-calculating the sum of the overlapping part of the sliding window."
    }, 
    {
      "id": 1,
      "question": "Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target. Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.",
      "answer": "We can follow the Two Pointers approach. We will start with one pointer pointing to the beginning of the array and another pointing at the end. At every step, we will see if the numbers pointed by the two pointers add up to the target sum. If they do, we have found our pair. Otherwise, we will do one of two things. otherwise, we will do one of two things: 1. If the sum of the two numbers pointed by the two pointers is greater than the target sum, this means that we need a pair with a smaller sum. So, to try more pairs, we can decrement the end-pointer. 2. If the sum of the two numbers pointed by the two pointers is smaller than the target sum, this means that we need a pair with a larger sum. So, to try more pairs, we can increment the start-pointer."
    }, 
    {
      "id": 2,
      "question": "Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.",
      "answer": "Take the example of two intervals (a and b) such that a.start <= b.start. Scenario 1: a and b do not overlap. Scenario 2: some part of b overlaps with a. Scenario 3: a fully overlaps b. Scenario 4: b fully overlaps a but both have the same start time. Our goal is to merge the intervals whenever they overlap. Sort the intervals on the start time to ensure a.start <= b.start. If a overlaps b (i.e. b.start <= a.end), we need to merge them into a new interval c. We will keep repeating the above two steps to merge c with the next interval if it overlaps with c."
    }
  ]
  return JsonResponse(data, safe=False)

def fetch_db(response):
  pattern = Pattern.objects.all()
  return HttpResponse(pattern)

  # data = [
  #   {"key": 0, "name": "Sliding Window", "question": "a", "solution": "a"}, 
  #   {"key": 1, "name": "Two Pointers", "question": "b", "solution": "b"}, 
  #   {"key": 2, "name": "", "question": "c", "solution": "c"}, 
  #   {"key": 3, "name": "d", "question": "d", "solution": "d"}, 
  #   {"key": 4, "name": "e", "question": "e", "solution": "e"}, 
  #   {"key": 5, "name": "f", "question": "f", "solution": "f"}, 
  #   {"key": 6, "name": "g", "question": "g", "solution": "g"}, 
  #   {"key": 7, "name": "h", "question": "h", "solution": "h"}, 
  #   {"key": 8, "name": "i", "question": "i", "solution": "i"}, 
  #   {"key": 9, "name": "j", "question": "j", "solution": "j"}, 
  #   {"key": 10, "name": "k", "question": "k", "solution": "k"}, 
  #   {"key": 11, "name": "l", "question": "l", "solution": "l"}, 
  #   {"key": 12, "name": "m", "question": "m", "solution": "m"}, 
  #   {"key": 13, "name": "n", "question": "n", "solution": "n"}
  #   ]  