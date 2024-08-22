from setuptools import setup, find_packages

setup(
    name="python-telegram-framework",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pipenv",
        "packaging"
        "python-telegram-bot[all]",
        "pyngrok",
    ],
    entry_points={
        'console_scripts': [
            'python-telegram-framework=telegram_framework.management:execute_from_command_line',
        ],
    },
    author="Víctor Martínez Amador",
    author_email="vmartineza33@gmail.com",
    description="Small framework to create bots with python-telegram-bot",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/vmartinez33/python-telegram-framework",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
