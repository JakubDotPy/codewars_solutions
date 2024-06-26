"""Kata - Coding Meetup #7 - Higher-Order Functions Series - Find the most senior developer

completed at: 2023-06-01 20:29:20
by: Jakub Červinka

You will be given a sequence of objects representing data about developers who have signed up to attend the next coding meetup that you are organising.

Your task is to return a sequence which includes the developer who is the oldest. In case of a tie, include all same-age senior developers listed in the same order as they appeared in the original input array.

For example, given the following input array:

```javascript
var list1 = [
  { firstName: 'Gabriel', lastName: 'X.', country: 'Monaco', continent: 'Europe', age: 49, language: 'PHP' },
  { firstName: 'Odval', lastName: 'F.', country: 'Mongolia', continent: 'Asia', age: 38, language: 'Python' },
  { firstName: 'Emilija', lastName: 'S.', country: 'Lithuania', continent: 'Europe', age: 19, language: 'Python' },
  { firstName: 'Sou', lastName: 'B.', country: 'Japan', continent: 'Asia', age: 49, language: 'PHP' },
];
```

```python
list1 = [
  { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
  { 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
  { 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
  { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
]
```
```cobol
       01  List.
          03  ListLength      pic 9(2) value 4.
          03  dev1.
              05 FirstName    pic a(9)  value 'Gabriel'.
              05 LastName     pic x(2)  value 'X.'.
              05 Country      pic a(24) value 'Monaco'.
              05 Continent    pic a(8)  value 'Europe'.
              05 Age          pic 9(3)  value 49.
              05 Language     pic a(10) value 'PHP'.
          03  dev2.
              05 FirstName    pic a(9)  value 'Odval'.
              05 LastName     pic x(2)  value 'F.'.
              05 Country      pic a(24) value 'Mongolia'.
              05 Continent    pic a(8)  value 'Asia'.
              05 Age          pic 9(3)  value 38.
              05 Language     pic a(10) value 'Python'.
          03  dev3.
              05 FirstName    pic a(9)  value 'Emilija'.
              05 LastName     pic x(2)  value 'S.'.
              05 Country      pic a(24) value 'Lithuania'.
              05 Continent    pic a(8)  value 'Europe'.
              05 Age          pic 9(3)  value 19.
              05 Language     pic a(10) value 'Python'.
          03  dev4.
              05 FirstName    pic a(9)  value 'Sou'.
              05 LastName     pic x(2)  value 'B.'.
              05 Country      pic a(24) value 'Japan'.
              05 Continent    pic a(8)  value 'Asia'.
              05 Age          pic 9(3)  value 49.
              05 Language     pic a(10) value 'PHP'.
```

your function should return the following array:

```javascript
[
  { firstName: 'Gabriel', lastName: 'X.', country: 'Monaco', continent: 'Europe', age: 49, language: 'PHP' },
  { firstName: 'Sou', lastName: 'B.', country: 'Japan', continent: 'Asia', age: 49, language: 'PHP' },
]
```

```python
[
  { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
  { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
]
```
```cobol
       01  result.
          03  res-length      pic 9(2) value 2.
          03  .
              05 FirstName    pic a(9)  value 'Gabriel'.
              05 LastName     pic x(2)  value 'X.'.
              05 Country      pic a(24) value 'Monaco'.
              05 Continent    pic a(8)  value 'Europe'.
              05 Age          pic 9(3)  value 49.
              05 Language     pic a(10) value 'PHP'.
          03  .
              05 FirstName    pic a(9)  value 'Sou'.
              05 LastName     pic x(2)  value 'B.'.
              05 Country      pic a(24) value 'Japan'.
              05 Continent    pic a(8)  value 'Asia'.
              05 Age          pic 9(3)  value 49.
              05 Language     pic a(10) value 'PHP'.
```

Notes:


 - The input array will always be valid and formatted as in the example above and will never be empty.
<br>
<br>
<br>
<br>
<br>

This kata is part of the **Coding Meetup** series which includes a number of short and easy to follow katas which have been designed to allow mastering the use of higher-order functions. In JavaScript this includes methods like: `forEach, filter, map, reduce, some, every, find, findIndex`. Other approaches to solving the katas are of course possible.

Here is the full list of the katas in the **Coding Meetup** series:

<a href="http://www.codewars.com/kata/coding-meetup-number-1-higher-order-functions-series-count-the-number-of-javascript-developers-coming-from-europe">Coding Meetup #1 - Higher-Order Functions Series - Count the number of JavaScript developers coming from Europe</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-2-higher-order-functions-series-greet-developers">Coding Meetup #2 - Higher-Order Functions Series - Greet developers</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-3-higher-order-functions-series-is-ruby-coming">Coding Meetup #3 - Higher-Order Functions Series - Is Ruby coming?</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-4-higher-order-functions-series-find-the-first-python-developer">Coding Meetup #4 - Higher-Order Functions Series - Find the first Python developer</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-5-higher-order-functions-series-prepare-the-count-of-languages">Coding Meetup #5 - Higher-Order Functions Series - Prepare the count of languages</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-6-higher-order-functions-series-can-they-code-in-the-same-language">Coding Meetup #6 - Higher-Order Functions Series - Can they code in the same language?</a>

<a href="http://www.codewars.com/kata/coding-meetup-number-7-higher-order-functions-series-find-the-most-senior-developer">Coding Meetup #7 - Higher-Order Functions Series - Find the most senior developer</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-8-higher-order-functions-series-will-all-continents-be-represented">Coding Meetup #8 - Higher-Order Functions Series - Will all continents be represented?</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-9-higher-order-functions-series-is-the-meetup-age-diverse">Coding Meetup #9 - Higher-Order Functions Series - Is the meetup age-diverse?</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-10-higher-order-functions-series-create-usernames">Coding Meetup #10 - Higher-Order Functions Series - Create usernames</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-11-higher-order-functions-series-find-the-average-age">Coding Meetup #11 - Higher-Order Functions Series - Find the average age</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-12-higher-order-functions-series-find-github-admins">Coding Meetup #12 - Higher-Order Functions Series - Find GitHub admins</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-13-higher-order-functions-series-is-the-meetup-language-diverse">Coding Meetup #13 - Higher-Order Functions Series - Is the meetup language-diverse?</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-14-higher-order-functions-series-order-the-food">Coding Meetup #14 - Higher-Order Functions Series - Order the food</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-15-higher-order-functions-series-find-the-odd-names">Coding Meetup #15 - Higher-Order Functions Series - Find the odd names</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-16-higher-order-functions-series-ask-for-missing-details">Coding Meetup #16 - Higher-Order Functions Series - Ask for missing details</a>
"""

def find_senior(lst): 
    max_age = max(d['age'] for d in lst)
    return list(filter(lambda d: d['age'] == max_age, lst))
    
    
