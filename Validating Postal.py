Here's the extracted text from the image:

---

A valid postal code **P** has to fulfill both below requirements:
1. **P** must be a number in the range from 100000 to 999999 inclusive.
2. **P** must not contain more than one alternating repetitive digit pair.

Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

For example:

- **121426** # Here, 1 is an alternating repetitive digit.
- **523563** # Here, NO digit is an alternating repetitive digit.
- **552523** # Here, both 2 and 5 are alternating repetitive digits.

Your task is to provide two regular expressions **regex_integer_in_range** and **regex_alternating_repetitive_digit_pair**. Where:

- **regex_integer_in_range** should match only integers in the range from 100000 to 999999 inclusive.
- **regex_alternating_repetitive_digit_pair** should find alternating repetitive digit pairs in a given string.

Both these regular expressions will be used by the provided code template to check if the input string **P** is a valid postal code using the following expression:

```python
(bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
```

---


code:

regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


