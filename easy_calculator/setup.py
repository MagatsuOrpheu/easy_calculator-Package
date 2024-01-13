from setuptools import setup, find_packages

with open('README.md', 'r') as f:
  page_description = f.read()

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(
    name='easy_calculator',
    version='0.0.1',
    author='Jonathan Melo',
    author_email='jonathan.gabrielfm@gmail.com',
    description='An easy calculator for tests.',
    long_description=page_description,
    url='My_github_repository_project_link',
    packages=find_packages(),
    install_requirements=requirements,
    python_requires='>=3.8',
)