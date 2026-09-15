# JermeinBot-v2

JermeinBot-v2 is a rule-based chatbot built with Python. It uses keyword matching to provide responses about programming, IT support, software architecture, and basic technical concepts.

The project was created to practice Python fundamentals while building a simple and organized conversational application.

## Features

* Keyword-based response system
* Interactive command-line chatbot
* User input handling
* Case-insensitive question matching
* Basic input cleanup with `strip()` and `lower()`
* Reusable functions
* Dictionary-based response storage
* Unknown-question fallback response
* Exit command to close the chatbot

## Topics Covered

The chatbot includes responses related to:

* Python
* JavaScript
* Variables
* `if` statements
* ChatGPT
* Software architecture
* IT support
* Internet troubleshooting
* Tier 1 support
* Basic technical concepts

## Tech Stack

* Python 3.10+
* Python standard library

## Project Structure

```text
JermeinBot-v2/
└── bot.py
```

The main file contains the chatbot logic, including the response dictionary, question matching, message display, and application loop.

## How It Works

The chatbot follows a simple rule-based process:

1. The user enters a question.
2. The input is cleaned and converted to lowercase.
3. The chatbot searches for matching keywords.
4. If a keyword is found, the corresponding response is displayed.
5. If no keyword matches, the chatbot returns a fallback message.
6. The user can type `exit` to close the application.

## Installation

Make sure Python 3.10 or later is installed.

Clone the repository:

```bash
git clone https://github.com/jermeinthomas/JermeinBot-v2
```

Enter the project directory:

```bash
cd JermeinBot-v2
```

## How to Run

Run the chatbot with:

```bash
python bot.py
```

## Why This Project Matters

This project was built to practice fundamental Python concepts through a practical application.

It demonstrates:

* Functions
* Dictionaries
* Loops
* Conditional statements
* String methods
* User input
* Keyword matching
* Basic code organization
* Separation of responsibilities

Although JermeinBot-v2 is a simple rule-based chatbot, it provides a foundation for future improvements such as more advanced matching, additional responses, and integration with external services.

## License

This project is released under the MIT License.
