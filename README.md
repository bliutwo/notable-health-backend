# Notable Health Backend Application

This repo will contain whatever Notable Health asks me to implement.

> For the take-home, we ask you to implement a transcription text parser that transforms text based on certain phrases. It’s based on an actual problem we solved here and is meant to be representative of the kind of work we’d do together day to day week to week. You’re free to use whatever languages, frameworks, etc that you’d like. It’s a good idea to have a hello-world type project set up before you start the problem so you don’t spend time getting things set up.

## Preparation Prompt

I came up with these potential (but kind of failed lol) potentially useful prompts.

### Find and replace, no regex

Python has a built-in function called `.replace()`: https://www.geeksforgeeks.org/python-string-replace/

~~Write a function `find_and_replace()` that takes three arguments:~~

- ~~a string text *t*, which is the text used to search and replace~~
- ~~a string variable *query*, which is the query to find~~
- ~~a string variable *replace*, which is what you should replace every instance of *query* with~~

~~Output: modified *t* with all instances of *query* replaced with *replace*~~

### Find and replace with regex

Write a function `find_and_replace_regex()` that takes two arguments:

- a string text *t*
- a regular expression string *r*

For every instance of text that matches the regular expression *r*, put two asterisks on each side of it.

Output: *t* with modifications as specified
