# lookbehind in regex assignment

### lookbehind

It searches for the pattern to the right of the parsers current position and dertermins wheather if its a match or not.

`(?<=Charlook)X`

It will searches for `Charlook` and if the pattern `X` follows after it - then it will be a match.

e.g:
```python
import re

text = "The quick brown fox jumps over the lazy dog"
ans = re.findall(r'(?<=jumps\s)\w+', text)

print(ans) # ['over']
```

In this example, the findall function searches for jumps\s (i.e. jumps with a space at the end) and then will captures all the alphanumeric characters that come after. It will return `over` as the match in a list.


### Negativelook behind

It will make sure that thee parser does not exist before the pattern that is found

`(?<!Charlook)X`

It will look for X if there is no `Charlook` before the matched characters.

```python
import re

text = ".2 The dog is big.23 people"
ans = re.findall(r'(?<!\.)\d+', text)

print(ans) #['3']
```

In this example, it is looking for a digit without a `.` (period) before it. The only digit without a period before it is `3` as `2` is the char before the three.

