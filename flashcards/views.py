from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from .models import Pattern

# Create your views here.
def fetch_static(response):
  data = [
    {
      "title": "Sliding Window",

      "desc": "The Sliding Window pattern is used to perform a required operation on a specific window size of a given array or linked list, such as finding the longest subarray containing all 1s. Sliding Windows start from the 1st element and keep shifting right by one element and adjust the length of the window according to the problem that you are solving. In some cases, the window size remains constant and in other cases the sizes grows or shrinks. Following are some ways you can identify that the given problem might require a sliding window: The problem input is a linear data structure such as a linked list, array, or string; You’re asked to find the longest/shortest substring, subarray, or a desired value.",
      
      "example": {
        "algoName": "Maximum Sum Subarray of Size K",

        "question": "Given an array of positive numbers and a positive number k, find the maximum sum of any contiguous subarray of size k.",
        
        "solution": "To calculate the sum of a contiguous subarray, we can utilize the sum of the previous subarray. Consider each subarray as a sliding window of size k. To calculat the sum of the next subarray, slide the window ahead by one element. Slide the window forward and claculate the sum of the new position of the sliding window. Subtract the element going out of the sliding window, ie subtract the first element of the window. Add the new element getting included in the sliding window, ie the element coing right after the end of the window. This approach will save us from re-calculating the sum of the overlapping part of the sliding window."
      }
    },
    
    {
      "title": "Two Pointers or Iterators",

      "desc": "Two Pointers is a pattern where two pointers iterate through the data structure in tandem until one or both of the pointers hit a certain condition.Two Pointers is often useful when searching pairs in a sorted array or linked list; for example, when you have to compare each element of an array to its other elements. Two pointers are needed because with just pointer, you would have to continually loop back through the array to find the answer. This back and forth with a single iterator is inefficient for time and space complexity — a concept referred to as asymptotic analysis. While the brute force or naive solution with 1 pointer would work, it will produce something along the lines of O(n²). In many cases, two pointers can help you find a solution with better space or runtime complexity.",

      "example": {
        "algoName": "Pair with Target Sum",

        "question": "Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target. Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.",

        "solution": "We can follow the Two Pointers approach. We will start with one pointer pointing to the beginning of the array and another pointing at the end. At every step, we will see if the numbers pointed by the two pointers add up to the target sum. If they do, we have found our pair. Otherwise, we will do one of two things. otherwise, we will do one of two things: 1. If the sum of the two numbers pointed by the two pointers is greater than the target sum, this means that we need a pair with a smaller sum. So, to try more pairs, we can decrement the end-pointer. 2. If the sum of the two numbers pointed by the two pointers is smaller than the target sum, this means that we need a pair with a larger sum. So, to try more pairs, we can increment the start-pointer."
      }
    },

    {
      "title": "Fast and Slow pointers",

      "desc": "The Fast and Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two pointers which move through the array (or sequence/linked list) at different speeds. This approach is quite useful when dealing with cyclic linked lists or arrays. By moving at different speeds (say, in a cyclic linked list), the algorithm proves that the two pointers are bound to meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.",

      "example": {
        "algoName": "",

        "question": "",

        "solution": ""
      }
    },

    {
      "title": "Merge Intervals",

      "desc": "The Merge Intervals pattern is an efficient technique to deal with overlapping intervals. In a lot of problems involving intervals, you either need to find overlapping intervals or merge intervals if they overlap. The pattern works like this: Given two intervals (a and b), there will be six different ways the two intervals can relate to each other: Understanding and recognizing these six cases will help you help you solve a wide range of problems from inserting intervals to optimizing interval merges. How do you identify when to use the Merge Intervals pattern? If you are asked to produce a list with only mutually exclusive intervals; If you hear the term overlapping intervals.",

      "example": {
        "algoName": "Merge Intervals",

        "question": "Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.",

        "solution": "Take the example of two intervals (a and b) such that a.start <= b.start. Scenario 1: a and b do not overlap. Scenario 2: some part of b overlaps with a. Scenario 3: a fully overlaps b. Scenario 4: b fully overlaps a but both have the same start time. Our goal is to merge the intervals whenever they overlap. Sort the intervals on the start time to ensure a.start <= b.start. If a overlaps b (i.e. b.start <= a.end), we need to merge them into a new interval c. We will keep repeating the above two steps to merge c with the next interval if it overlaps with c."
      }
    },

    {
      "title": "Cyclic sort",

      "desc": "This pattern describes an interesting approach to deal with problems involving arrays containing numbers in a given range. The Cyclic Sort pattern iterates over the array one number at a time, and if the current number you are iterating is not at the correct index, you swap it with the number at its correct index. You could try placing the number in its correct index, but this will produce a complexity of O(n^2) which is not optimal, hence the Cyclic Sort pattern.",

      "example": {
        "algoName": "Missing Number",

        "question": "Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.",

        "solution": "If nums were in order, it would be easy to see which number is missing. irst, we sort nums. Then, we check the two special cases that can be handled in constant time - ensuring that 0 is at the beginning and that nn is at the end. Given that those assumptions hold, the missing number must somewhere between (but not including) 0 and nn. To find it, we ensure that the number we expect to be at each index is indeed there. Because we handled the edge cases, this is simply the previous number plus 1. Thus, as soon as we find an unexpected number, we can simply return the expected number."
      }
    },

    {
      "title": "In-place reversal of linked list",

      "desc": "In a lot of problems, you may be asked to reverse the links between a set of nodes of a linked list. Often, the constraint is that you need to do this in-place, i.e., using the existing node objects and without using extra memory. This is where the above mentioned pattern is useful.This pattern reverses one node at a time starting with one variable (current) pointing to the head of the linked list, and one variable (previous) will point to the previous node that you have processed. In a lock-step manner, you will reverse the current node by pointing it to the previous before moving on to the next node. Also, you will update the variable “previous” to always point to the previous node that you have processed.",

      "example": {
        "algoName": "Reverse a linked list",

        "question": "Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.",

        "solution": "To reverse a LinkedList, we need to reverse one node at a time. We will start with a variable current which will initially point to the head of the LinkedList and a variable previous which will point to the previous node that we have processed; initially previous will point to null. In a stepwise manner, we will reverse the current node by pointing it to the previous before moving on to the next node. Also, we will update the previous to always point to the previous node that we have processed. "
      }
    },

    {
      "title": "Tree BFS",

      "desc": "This pattern is based on the Breadth First Search (BFS) technique to traverse a tree and uses a queue to keep track of all the nodes of a level before jumping onto the next level. Any problem involving the traversal of a tree in a level-by-level order can be efficiently solved using this approach. The Tree BFS pattern works by pushing the root node to the queue and then continually iterating until the queue is empty. For each iteration, we remove the node at the head of the queue and “visit” that node. After removing each node from the queue, we also insert all of its children into the queue.",

      "example": {
        "algoName": "Binary Tree Level Order Traversal",

        "question": "Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.",

        "solution": "We scan through the tree level by level, following the order of height, from top to bottom. The nodes on higher level would be visited before the ones with lower levels. The simplest way to solve the problem is to use a recursion. Let's first ensure that the tree is not empty, and then call recursively the function helper(node, level), which does the following: (1) The output list here is called levels, and hence the current level is just a length of this list len(levels). Compare the number of a current level len(levels) with a node level level. If you're still on the previous level - add the new one by adding a new list into levels. (2) Append the node value to the last list in levels. (3) Process recursively child nodes if they are not None : helper(node.left / node.right, level + 1)"
      }
    },

    {
      "title": "Tree DFS",
      "desc": "",
      "example": {
        "algoName": "",
        "question": "",
        "solution": ""
      }
    },

    {
      "title": "Two heaps",

      "desc": "",

      "example": {
        "algoName": "",

        "question": "",

        "solution": ""
      }
    },

    {
      "title": "Subsets",

      "desc": "",

      "example": {
        "algoName": "",

        "question": "",

        "solution": ""
      }
    },
            
    {
      "title": "Modified binary search",

      "desc": "",

      "example": {
        "algoName": "",

        "question": "",

        "solution": ""
      }
    },

    {
      "title": "Top K elements",

      "desc": "",

      "example": {
        "algoName": "",

        "question": "",

        "solution": ""
      }
    },
    
    {
      "title": "K-way Merge",

      "desc": "",

      "example": {
        "algoName": "",

        "question": "",

        "solution": ""
      }
    },
    
    {
      "title": "Topological sort",
      
      "desc": "",

      "example": {
        "algoName": "",

        "question": "",
        
        "solution": ""
      }
    },
  ]

  return JsonResponse(data, safe=False)

def fetch_db(response):
  pattern = Pattern.objects.all()
  return HttpResponse(pattern)