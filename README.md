# 1. How to create module in python :snake:

Hello, in this lesson we will learn how to use markdown to create an engaging readme.

# 2. What we will learn in this lesson :book:

    - How to create a markdownfile
    - How to write markdown syntax
    - How to format code in markdown
    - How to embed images in markdown

# Extension we need are

1. *github* markdown preview by SOTH Pisey
2. Markdown emoji by SOTH Pisey

# Emoji link

You can find all emoji's here:
<https://www.webfx.com/tools/emoji-cheat-sheet/>

# Other Markdown Editors you can use

1. MAC: **MacDown**
2. Windows: **ghostwriter** or **MarkdownEditor**

# Our Program

To load an image use an exclamation mark in square brackets **![Alternate text]** e.g ![Image of a cat]
![Test Image](/screenshots/02.png)

*picture1: useful markdown extensions*

To show our code using markdown you can use backtick `` for single code
`print('Hello World')`
*to show multiple lines of code use three backticks*
Here I have my SQL code

```python
import mysql.connector
import os

try:
    cnx = mysql.connector.connect(
        host=os.environ.get('DB_HOST'), 
        user=os.environ.get('DB_USER'),
        passwd=os.environ.get('DB_PASS'),
        database='college'
        )
    print(cnx)
    cnx.close()
except:
    print()
```
