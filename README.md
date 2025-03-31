# typewriter_function
Short function to accomplish a typewriter effect.

```python
import sys
from time import sleep

def typewriter(string)
  for char in string:
    sleep(uniform(0.1,0.25))
    sys.stdout.write(char)
    sys.stdout.flush()
```
