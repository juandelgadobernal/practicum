# practicum

This repository contains the 'Practicum' code exercise.

## [reverse_list] Write a function that takes an array as input and returns the array in reverse order.
Conditions:
* Do not use built-in functions
* Any programming language

## [differents_locators] Locators
  * Open https://about.google/ and write at least 5 different locators for a headline logo (on the top left part of the page). Use different approaches: xpath, css, and others

## [code_challengue] Write a basic test in any programming language and framework, which will:
  * Open https://www.google.com/search?q=1
  * Locate the logo (on the top left side) and check its visibility
  * Locate the search textarea and check its visibility
  * Enter any new search query
  * Check that the entered search query is present and no placeholder is present.

## To run [reverse_list] from ~/Practicum
    python reverse_list.py

## To run [differents_locators] from ~/Practicum
    python differents_locators.py

## To run [code_challengue] from ~/Practicum
    * Create python virtual environment
      python3 -m venv venv
    * Activate environment
      source venv/bin/activate
    * Install dependencies
      pip install -r requirements.txt
    * Run from ~/Practicum/test_cases
    pytest -s code_challenge.py




      
