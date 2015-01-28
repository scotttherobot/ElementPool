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

### Data structure

Why does the question data structure look like, might you ask? Here's a sample
of what is returned from `pool.sortedQuestions()`. I've broken up each question
tuple some for readability.

```python
[
('T1A01', {
   'choices': [
      ('A', 'Providing personal radio communications for as many citizens as possible'), 
      ('B', 'Providing communications for international non-profit organizations'), 
      ('C', 'Advancing skills in the technical and communication phases of the radio art'), 
      ('D', 'All of these choices are correct ')
   ], 
   'prompt': 'Which of the following is a purpose of the Amateur Radio Service as stated in the FCC rules and regulations?', 
   'id': 'T1A01', 
   'figure': '', 
   'correct': 'C'
}), 
('T6C08', {
   'choices': [
      ('A', 'Variable capacitor'), 
      ('B', 'Variable inductor'), 
      ('C', 'Variable resistor'), 
      ('D', 'Variable transformer')], 
   'prompt': 'What is component 9 in figure T2?', 
   'id': 'T6C08', 
   'figure': 'T2', 
   'correct': 'C'
})
]
```
