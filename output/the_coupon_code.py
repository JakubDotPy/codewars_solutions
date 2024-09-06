"""Kata - The Coupon Code

completed at: 2024-09-05 15:32:13
by: Jakub Červinka

# Story

Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.

# Task

Your mission:  
Write a function called `checkCoupon` which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day **AFTER** the expiration date.  All dates will be passed as strings in this format: `"MONTH DATE, YEAR"`.

## Examples:

```javascript
checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  ===  true
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  ===  false
```
```typescript
checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  ===  true
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  ===  false
```
```csharp
CheckCoupon("123", "123", "July 9, 2015", "July 9, 2015")  ==  true
CheckCoupon("123", "123", "July 9, 2015", "July 2, 2015")  ==  false
```
```python
checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False
```
"""

from datetime import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    # check code match
    code_match = entered_code is correct_code
    
    # check date validity
    current_date = datetime.strptime(current_date, '%B %d, %Y')
    expiration_date = datetime.strptime(expiration_date, '%B %d, %Y')
    is_fresh = current_date <= expiration_date
    
    return code_match and is_fresh
