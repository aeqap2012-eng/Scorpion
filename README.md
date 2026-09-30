🦂 Scorpion

Scorpion is a simple, lightweight, and beginner-friendly programming language built from scratch with Python.

The goal of Scorpion is to provide a clean and readable syntax that is easier to understand for beginners while having its own programming style instead of simply copying Python syntax.

✨ Features

- 🟢 Simple and readable syntax
- ⚡ Lightweight interpreter
- 💻 Interactive REPL
- 📁 ".sc" source files
- 🔤 Variables
- 💬 User input
- 🔁 Repetition
- 🔀 Conditions
- 🎲 Random numbers
- ⏱️ Delays
- 🆘 Built-in "help" command
- 🚪 Simple program control

🚀 Getting Started

Requirements

You need:

- Python 3
- Git (optional, for contributing or publishing)

Run Scorpion

Clone the repository:

git clone https://github.com/YOUR_USERNAME/Scorpion.git
cd Scorpion

Start the Scorpion interpreter:

python scorpion.py

You should see:

🦂 Scorpion Programming Language
Version 0.1.0
اكتب "exit" للخروج

>>

📖 Your First Program

Create a file named:

hello.sc

Add:

show "Welcome to Scorpion!"

set name = "Hassan"

show "Hello " + name

repeat 3
    show "Scorpion!"
end

Run it with:

python scorpion.py hello.sc

🧰 Commands

Command| Description
"show"| Display text or a value
"set"| Create or change a variable
"ask"| Ask the user for input
"wait"| Wait for a number of seconds
"random"| Generate a random number
"repeat"| Repeat a block of code
"when"| Create a condition
"otherwise"| Alternative condition branch
"end"| End a code block
"help"| Display Scorpion help
"exit"| Exit the interpreter

💡 Example

set name = "Hassan"

show "Hello " + name

when name == "Hassan"
    show "Welcome to Scorpion!"
otherwise
    show "Unknown user"
end

🛠️ Project Structure

Scorpion/
├── scorpion.py
├── examples/
│   └── hello.sc
└── tests/

🎯 Project Goals

Scorpion is currently an early-stage project.

Future versions are planned to include:

- Functions
- Lists
- More operators
- Better error messages
- File operations
- More built-in commands
- A proper lexer and parser
- Modules and libraries
- A package system
- Improved performance
- More testing

📌 Status

Version: 0.1.0
Status: Early Development

Scorpion is currently experimental and is being developed from scratch.

🤝 Contributing

Contributions, ideas, bug reports, and improvements are welcome.

If you find a bug or have an idea for a new Scorpion feature, open an Issue or submit a Pull Request.

📄 License

This project is currently under development. A license will be added in a future release.

---

🦂 Scorpion — Simple syntax. Different language.
