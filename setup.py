from setuptools import setup, find_packages

setup(
    name="python-telegram-framework",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "python-telegram-bot",
        "packaging"
    ],
    entry_points={
        'console_scripts': [
            'python-telegram-framework=telegram_framework.management.commands.startproject:main',
        ],
    },
    author="Víctor Martínez Amador",
    author_email="vmartineza33@gmail.com",
    description="Un framework pequeño para crear bots de Telegram",
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
