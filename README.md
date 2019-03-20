

# Guide on how to code in Python.
*For beginners on the road to expert!*

## Table of Contents

- [Hello World](#1-hello-world)
- [Hello User](#2-hello-user)
- [Compute Gross Pay](#3-compute-gross-pay)
- [Compute Gross Pay with Conditions](#4-gross-pay-with-conditions)
- [Try Except](#try-except)
  - [Gross Pay](#5-gross-pay)
  - [Grading System](#6-grading-system)
- [Functions](#functions)
  - [Gross Pay](#7-gross-pay)
  - [Grading System](#8-grading-system)
- [Loop](#loop)
  - [Compute Input](#9-compute-input)
  - [Min & Max](#10-min-and-max)
- [Strings](#11-string)
- [File](#file)
  - [Print text from a file](#12-print-text-from-file)
  - [Compute values within file](#13-compute-values-within-file)
- [List](#14-list)
- [Dictionary](#15-dictionary)
- [Tuples](#16-tuples)
- [Expressions](#expressions)
  - [Compute values within file](#17-compute-values-within-file)
  - [Highest Emails](#18-highest-emails)

----

###  1. Hello World
**Q.  Output *'Hello World'* to the screen.**
<br>

*[Code](https://github.com/JuzerShakir/How-to-Python/blob/master/Hello%20World.py)*

![Code for Hello World](https://i.imgur.com/ABnhejs.png)
<br>

**Output.**

![Answer to 1st question](https://i.imgur.com/iWgOyd0.png)
---

###  2. Hello User
**Q. Greet *'Hello'* to the user with *it's name.***
<br>

*[Code](https://github.com/JuzerShakir/How-to-Python/blob/master/Hello%20User.py)*

![Code for Hello User](https://i.imgur.com/PVyb32d.png)

<br>

**Output.**

![Output for Hello User]()

*[Back to Top](#table-of-contents)*

---

### 3. Compute Gross Pay
**Q. Write a program to prompt user for hours and rate per hour to compute their gross pay.**
<br>

*[Code](https://github.com/JuzerShakir/How-to-Python/blob/master/Compute%20Gross%20Pay.py)*

![Code for Gross Pay](https://i.imgur.com/ozCYvYd.png)

<br>

**Output.**

![Output for Compute Gross Pay]()

---

### 4. Gross Pay with Conditions
**Q. Rewrite your pay computation *([Exercise 3](#3-compute-gross-pay))* to give the employee 1.5 times the hourly rate for hours worked above 40 hours.**
<br>

*[Code](https://github.com/JuzerShakir/How-to-Python/blob/master/Compute%20Gross%20Pay%20with%20Conditions.py)*

![Code for Conditions](https://i.imgur.com/gYQxFVb.png)

<br>

**Output.**

![Output for Gross Pay with Conditions]()

*[Back to Top](#table-of-contents)*

---

### Try Except
#### 5. Gross Pay
**Q. Rewrite your pay program *([Exercise 4](#4-gross-pay-with-conditions))* using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.**
<br>

*[Code](https://github.com/JuzerShakir/How-to-Python/blob/master/Try%20Except/Gross%20Pay.py)*

![Code for Try Except](https://i.imgur.com/5XkzjeI.png)

<br>

**Output.**

![Output for Gross Pay]()

---

#### 6. Grading System
**Q. Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message.<br>
If the score is between 0.0 and 1.0, print a grade using the following table:**

| **Score** |  **Grade** |
| --------- | ---------- |
| **>=0.9** |  A         |
| **>=0.8** |  B         |
| **>=0.7** |  C         |
| **>=0.6** |  D         |
| **< 0.6** |  F         |

<br>

*[Code](https://github.com/JuzerShakir/How-to-Python/blob/master/Try%20Except/Grading%20System.py)*

![Code for Try Except 2](https://i.imgur.com/2Gxg853.png)

<br>

**Output.**

![Output for Grading System]()

*[Back to Top](#table-of-contents)*

---

### Functions
#### 7. Gross Pay
**Q. Rewrite your pay computation *([Exercise 5](#5-gross-pay))* and create a function called *'computepay'* which takes two parameters (hours and rate).**
<br>

*[Code](https://github.com/JuzerShakir/How-to-Python/blob/master/Functions/Gross%20Pay.py)*

![Code for Functions](https://i.imgur.com/DSu9qjX.png)

<br>

**Output.**

![Output for Gross Pay]()

---

#### 8. Grading System
**Q. Rewrite grading program *([Exercise 6](#6-grading-system))* using function named *'computegrade'*.**
<br>

*[Code](https://github.com/JuzerShakir/How-to-Python/blob/master/Functions/Grading%20System.py)*

![Code for Functions 2](https://i.imgur.com/3AsehCR.png)

<br>

**Output.**

*[Back to Top](#table-of-contents)*

![Output for Grading System]()

---

### Loop
#### 9. Compute Input
**Q. Write a program which repeatedly reads numbers until the user inputs *"done"*. Once *"done"* is entered, print out the *total, count, and average* of the *input numbers*. If the user enters anything other than a number,  detect their mistake using try and except and print an error message and skip to the next number.**
<br>

*[Code](https://github.com/JuzerShakir/How-to-Python/blob/master/Loop/Compute%20Input.py)*

![Code for Loop](https://i.imgur.com/CttKiRB.png)

<br>

**Output.**

![Output for Compute Input]()


---

#### 10. Min and Max
**Q. Similar to *[Exercise 9](#9-compute-input)*, only output a minimum and a maximum number inputted by the user.**
<br>

*[Code](https://github.com/JuzerShakir/How-to-Python/blob/master/Loop/Min%20and%20Max.py)*

![Code for Loop 2](https://i.imgur.com/EckOUBw.png)

<br>

**Output.**

![Output for Min and Max]()

*[Back to Top](#table-of-contents)*

---

### 11. String
**Q. Use *'find'* and *string slicing* to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.**<br>
*str = 'X-DSPAM-Confidence: 0.8475'*
    
<br>

*[Code](https://github.com/JuzerShakir/How-to-Python/blob/master/String.py)*

![Code for String](https://i.imgur.com/HZpjZcS.png)

<br>

**Output.**

![Output for String]()

---

### File
#### 12. Print text from file
**Q. Write a program to read through a file *[mbox-short.txt](https://github.com/JuzerShakir/How-to-Python/blob/master/File/mbox-short.txt)* and print the contents of the file (line by line) all in upper case.**
<br>

*[Code](https://github.com/JuzerShakir/How-to-Python/blob/master/File/Print%20text%20from%20a%20file.py)*

![Code for File](https://i.imgur.com/MylFIIG.png)

<br>

**Output.**

*[Back to Top](#table-of-contents)*

![Output for Print text from file]()

---

#### 13. Compute values within file
**Q. Write a program to read through the file *[mbox-long.txt](https://github.com/JuzerShakir/How-to-Python/blob/master/File/mbox-long.txt)* and look for lines of the form:**<br>

*X-DSPAM-Confidence: 0.8475* <br>

**When you encounter a line that starts with *"X-DSPAM-Confidence:"* pull apart the line to extract the floating-point number from that line. Count number of occurances on the file and then compute the total of the spam confidence values from these lines. Also print out the average spam confidence values.**

<br>

*[Code](https://github.com/JuzerShakir/How-to-Python/blob/master/File/Compute%20values%20within%20file.py)*

![Code for File 2](https://i.imgur.com/OQodMYp.png)

<br>

**Output.**

![Output for Compute values within file]()

---

### 14. List
**Q.  Write a program to open the file *[romeo.txt](https://github.com/JuzerShakir/How-to-Python/blob/master/List/romeo.txt)* and read it line by line.**<br>
**For each line, split the line into a list of words using the *'split'* function. For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list. When the program completes, sort and print the resulting words in alphabetical order.**
<br>

*[Code](https://github.com/JuzerShakir/How-to-Python/blob/master/List/Splitting%20and%20Sorting.py)*

![Code for List](https://i.imgur.com/C8Wwk7H.png)

<br>

**Output.**

![Output for List]()

*[Back to Top](#table-of-contents)*

---

### 15. Dictionary
**Q. Write a program to read through a mail log from *[mbox-long.txt](https://github.com/JuzerShakir/How-to-Python/blob/master/Dictionary/mbox-long.txt)*  file, line starting with *'From'*. Build a histogram using a dictionary to count how many messages have come from each email address.** <br>

**Look through the dictionary using loop to find who has the most messages and print how many messages the person has.**
<br>

*[Code](https://github.com/JuzerShakir/How-to-Python/blob/master/Dictionary/Most_email.py)*

![Code for Dictionary](https://i.imgur.com/dduRO1m.png)

<br>

**Output.**

![Output for Dictionary]()

---

### 16. Tuples
**Q. Write a program that counts the distribution of the hour of the day for each of the messages in the *[mbox-long.txt](https://github.com/JuzerShakir/How-to-Python/blob/master/Tuples/mbox-long.txt)* file. You can pull the hour from the *'From'* line by finding the time string and then splitting that string into parts using the colon character.**<br>
**Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour.**
<br>

*[Code](https://github.com/JuzerShakir/How-to-Python/blob/master/Tuples/Most_mail_hour.py)*

![Code for Tuples](https://i.imgur.com/csRPYqd.png)

<br>

**Output.**

![Output for Tuples]()

*[Back to Top](#table-of-contents)*

---

### Expressions
#### 17. Compute values within file
**Q. Sum up all *'X-DSPAM-Confidence'* values from *[mbox.txt](https://github.com/JuzerShakir/How-to-Python/blob/master/Expressions/mbox.txt)* file.**
<br>

*[Code](https://github.com/JuzerShakir/How-to-Python/blob/master/Expressions/Compute%20values%20within%20file.py)*

![Code for Expression - Sum](https://i.imgur.com/2NrCPeU.png)
<br>

**Output.**

![Output for Compute values within file]()

---

#### 18. Highest Emails
**Q. Write a program similar to *[Exercise 15](#15-dictionary)* but regardless of whether the line starts from *'From'* on *[mbox.txt](https://github.com/JuzerShakir/How-to-Python/blob/master/Expressions/mbox.txt)* file.**
<br>

*[Code](https://github.com/JuzerShakir/How-to-Python/blob/master/Expressions/Highest%20Email.py)*

![Code for Expression - Email](https://i.imgur.com/sLw3Fca.png)

<br>

**Output.**

![Output for Highest Emails]()

*[Back to Top](#table-of-contents)*

---