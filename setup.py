import subprocess
from setuptools import setup, find_packages

framework_version = subprocess.run(['git', 'describe', '--tags', '--abbrev=0'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip().replace("v", "")
assert "." in framework_version

with open("telegram_framework/VERSION", "w", encoding="utf-8") as fh:
    fh.write(f'{framework_version}\n')

setup(
    name="python-telegram-framework",
    version=framework_version,
    packages=find_packages(),
    package_data={'telegram_framework': ['VERSION']},
    include_package_data=True,
    install_requires=[
        "packaging",
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
