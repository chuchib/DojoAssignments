#Find and Replace

>>> str = "If monkeys like bananas, then I must be a monkey!"
>>> print str.find("monkeys")
3
>>> print str.replace("monkeys","alligators")
If alligators like bananas, then I must be a monkey!
>>>

#Min and Max
>>> x = [2,54,-2,7,12,98]
>>> print min(x)
-2
>>> print max(x)
98
>>>

#First and last
>>> x = ["hello",2,54,-2,7,12,98,"world"]
>>> print x[0]
hello
>>> print x[7]
world
>>>

#New List

>>> x = [19,2,54,-2,7,12,98,32,10,-3,6]
>>> x.sort()
>>> print x
[-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
>>> firstHalf = x[0:5]
>>> secondHalf = x[5:]
>>>
>>> print firstHalf
[-3, -2, 2, 6, 7]
>>> print secondHalf
[10, 12, 19, 32, 54, 98]
>>>
>>> secondHalf.insert(0,firstHalf)
>>>
>>> print secondHalf
[[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]
>>>
