## Natural Language Processing

- Overview
- Motivation
- Technical Aspect
- Run
- Directory Tree
- Credits

### Overview
It is a simple flask application to demonstrate working of fuzzywuzzy library in Python.
The library is efficient in detecting spelling mistakes in text.
Generally in NLP chatbots, which involve communicating with a human, mistakes are common.
"To Err is Human"
To deal with that we are blessed to have this library that is bsed completely on fuzzy logic, which doesn't say YES or NO straightaway but rather gives the percentage of probability of something.
So, let's say we can say YES by a probability of 95% and No with a probability of 5%, then we'll most likely choose YES as the outcome.
Fuzzywuzzy is a part of soundex algorithm which aids in resolving phonetics, fixing typos etc. which are bound to come when dealing with texts like comments in twitter/ YouTube/ Facebook or chatbots interacting with humans.

### Motivation
I have a lot of interest in NLP and I admire how it is continuously evolving over time.
So, an idea struck me some time back to explore good python libraries that might prove to be great in Natural language preprocessing.

### Technical Aspect
Tech stack includes: -
- Flask = 2.0.1
- fuzzywuzzy = 0.18.0
- Python = 3.8.11

### Run
- Download the code.
- Run app.py (entry point of flask application)
- It'll show a url, open that url in browser, you'll see a placeholder to write in the city (misspelt city) textbox provided.
- Click `Show Results` button
- It'll show 3 most matching city names with similarity percentage.

### Directory Tree
![directory tree flask app]()

### Credits
Code Idea: https://www.youtube.com/watch?v=6i5bHQZ-c5U
