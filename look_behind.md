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

In this example, the findall function searches for jumps\s (i.e. jumps with a space at the end) and then will capture all the alphanumeric characters that come after. It will return `over` as the match.


### Negative lookbehind

When the pattern is found it makes sure the parser is not directly infornt of the matched pattern.

It makes sure that the parser does not exist directly in fornt of the pattern that it is lookng for.

`(?<!Charlook)X`
 
if there is no `Charlook` in fornt of `X` it will then match with `X`.

```python
import re

text = ".2 The dog is big.43 people"
ans = re.findall(r'(?<!\.)\d+', text)

print(ans) #['3']
```

In this example, it is searching for a digit without a `.` (period) in fornt of it. As `4` is the character before the `3`, therefor the only digit without a period before it is `3`,

