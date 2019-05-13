# !/usr/bin/python
# -*- coding: utf-8 -*-

# Simple algorithm to count
# number of occurrences of (n) in (ar)

# Algorithm: Functionality
# 	each time (n) is found in (ar)
# 	(count) variable in incremented (by 1)

def count(ar, n):
    """
    This function accepts two arguments.  for an instructional video see: https://www.youtube.com/watch?v=zY0ZGwvFHJk

    :param ar: Can be an array
    :param n:  Is what you're looking for
    :return:  updates count.
    """
    count = 0

    for element in ar:
        # More complex condition could be
        # => (not element != n)
        if element == n:
            count += 1

    return count

# Testing
# add your test cases in list below
test_cases = [([1, 1, 2, 3, 5, 8, 13, 21, 1], 5), ("Captain America", "a")]
for test_case in test_cases:
    print("TestCase: {}, {}".format(test_case[0], test_case[1]))
    print("Results: {}\n".format(count(test_case[0], test_case[1])))

# You can add condition to check weather output is correct
# or not

#  Let's do some in testing
fruits = [(["apple", "banana", "cherry"],"banana")]

if "banana" in fruits:
    print("yep, banana")

for checkme in fruits:
    print("Check them fruits: {}, {}".format(checkme[0],checkme[1]))
    print("count fruit in delivery: {}\n".format(count(checkme[0], checkme[1])))

