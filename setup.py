import requests
import subprocess
from setuptools import setup, find_packages

def get_latest_github_release(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    response = requests.get(url)
    if response.status_code == 200:
        release_data = response.json()
        return release_data['tag_name']
    else:
        raise Exception(f"Error fetching release data: {response.status_code}")

owner = "vmartinez33"
repo = "python-telegram-framework"
framework_version = get_latest_github_release(owner, repo).replace("v", "")
assert "." in framework_version

with open("telegram_framework/VERSION", "w", encoding="utf-8") as fh:
    fh.write(f'{framework_version}\n')

setup(
    name=repo,
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
            f"{repo}=telegram_framework.management:execute_from_command_line",
        ],
    },
    author="Víctor Martínez Amador",
    author_email="vmartineza33@gmail.com",
    description="Small framework to create bots with python-telegram-bot",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url=f"https://github.com/vmartinez33/{repo}",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
