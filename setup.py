from setuptools import setup

setup(
    name = 'taskaty',
    version = '0.1.0',
    description = 'A Simple Command Line Task-app Written In Python',
    author = 'Ahmed Abdulelah',
    install_requires = ['tabulate'],
    entry_points = {
        'console_scripts': [
            'taskaty=taskaty:main'
        ]
    }
)