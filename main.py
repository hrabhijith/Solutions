# !/usr/bin/env python3
# !/usr/bin/python -3.5.2
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import re
import math

app = Flask(__name__)


# List which holds initial data
userList = []
userList = ['John', 'Bob', 'Rob', 'Mike', 'Jason']

xList = []
sortedList = []
resultList = []


# Method to convert decimal to binary
def integer_to_string(n, base):
    resultStr = ""
    while (n > 0):
        digit = n % base
        n = int(n / base)
        resultStr = chr(digit + ord('0')) + resultStr
    return resultStr


# function to check for palindrome
def isPalindrome(i, k):
    temp = i
    # m stores reverse of a number
    m = 0
    while (temp > 0):
        m = (temp % 10) + (m * 10)
        temp = int(temp / 10)

    # if reverse is equal to number
    if (m == i):
        # converting to base k
        str1 = integer_to_string(m, k)
        str2 = str1
        # reversing number in base k
        # str=str[::-1];
        # checking palindrome
        # in base k
        if (str1[::-1] == str2):
            return i

    return 0


# function to find sum of palindromes
def sumPalindrome():
    sum = 0
    for i in range(1000000):
        sum += isPalindrome(i, 2)
    return sum


# Function to find the Egyptian fraction
def egyptianFraction(nume, deno):
    denominators = []
    resultList.clear()

    while nume != 0:
        # taking ceiling
        x = math.ceil(deno / nume)

        # storing value in denominator list
        denominators.append(x)

        # updating new nr and dr
        nume = x * nume - deno
        deno = deno * x

    # Loading the values
    for i in range(len(denominators)):
        if i != len(denominators) - 1:
            resultList.append(" 1/{0} +" .
                              format(denominators[i]))
        else:
            resultList.append(" 1/{0}" .
                              format(denominators[i]))

    return resultList


# Solution homepag route method
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


# Problem 1 - write a small library of ordered hash tables;
# you should provide lookup, insert and delete functions, at least
@app.route('/library', methods=['GET', 'POST'])
def library():
    global userList
    if request.method == 'POST':
        # Filtering the list based on search term
        r = re.compile(".*" + request.form['term'].lower())
        userList2 = list(filter(r.match, (x.lower() for x in userList)))
        userList1 = list(x.title() for x in userList2)

        i = 1
        userList1 = userList1
        for k in userList1:
            xDict = {'id': '', 'name': ''}
            xDict['id'] = i
            xDict['name'] = userList1[i-1]
            i = i + 1
            xList.append(xDict)

        # Reversing the list contents based on id
        sortedList = sorted(xList, key=lambda i: i['id'])
        xList.clear()

        return render_template('library.html', list=sortedList)

    i = 1
    for k in userList:
        xDict = {'id': '', 'name': ''}
        xDict['id'] = i
        xDict['name'] = userList[i-1]
        i = i + 1
        xList.append(xDict)

    sortedList = sorted(xList, key=lambda i: i['id'])
    xList.clear()

    return render_template('library.html', list=sortedList)


# Add item route
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        userList.append(request.form['name'].title())
        return redirect('/library')


# Delete item route
@app.route('/delete/<string:name>', methods=['GET', 'POST'])
def delete(name):
    global userList

    for i in userList:
        if i == name:
            userList.remove(name)

    return redirect('/library')


# Problem 2 - write a program that calculates the ratio of
# two numbers as an Egyptian fraction
@app.route('/fraction', methods=['GET', 'POST'])
def fraction():
    if request.method == 'POST':
        # calling the Egyptian fraction calculator function
        resultList = egyptianFraction(int(request.form['numerator']),
                                      int(request.form['denominator']))

        return render_template('fraction.html', list=resultList)

    return render_template('fraction.html')


# Problem 3 - Find the sum of all numbers, less than
#  one million, which are palindromic in base 10 and base 2.
@app.route('/palindrome', methods=['GET'])
def palindrome():
    sum = sumPalindrome()
    return render_template('palindrome.html', sum=sum)


# Server host listening starts
if __name__ == "__main__":
    app.run(debug=True, port=1111)
