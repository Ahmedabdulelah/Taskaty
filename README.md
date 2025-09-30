# Taskaty 📝

A simple **Command Line Task Manager** written in Python.  
Taskaty helps you add, list, check, and remove tasks easily using the terminal.

## Features 🚀
- Add tasks with title, description, start and end date.
- List unfinished tasks or all tasks.
- Mark tasks as done.
- Remove a specific task or all tasks.
- Show due dates automatically.
- Lightweight and file-based (stores tasks in a `.txt` file).

## Installation ⚙️

Clone the repository:
```bash
git clone https://github.com/yourusername/taskaty.git
cd taskaty

Create a virtual environment (optional but recommended):
python -m venv env
source env/bin/activate   # On Linux/Mac
env\Scripts\activate      # On Windows

Install Taskaty locally:

pip install -e .


## **Usage 💡**
Add a task
taskaty add "Study Python" -d "Finish Project" -e 2025-10-05

List unfinished tasks
taskaty list

List all tasks
taskaty list -a

Mark a task as done
taskaty check -t 1

Remove a task
taskaty remove -t 2

Reset (delete all tasks)
taskaty reset

Example Output 📋
No  Title         Description              Start Date   End Date   Due Date     Done
1   Study Python  Finish argparse section  2025-09-29  2025-10-05  6 days left  False
