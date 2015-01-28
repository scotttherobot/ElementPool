### ElementPool

This is a Python parser for Amateur Radio Exam element question pools. This was
tested and built against the 2014 Element 1 (Technician Class) question pool.

#### Usage

All you need is a filename.

```python
import ElementPool

# Instantiate an object using the file path
pool = ElementPool.ElementPool('pools/2014-2018 Tech Pool.txt')

# To get at the raw data structures, you can call sortedQuestions()
sortedQs = pool.sortedQuestions()

# If you don't care if they're sorted
unsorted = pool.questions

# You can even treat it like a string.
print pool
```
