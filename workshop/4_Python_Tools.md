# Python Environment Setup

First, clone and navigate to the wintap-analytics repo:

1. Clone github Repo: `git clone https://github.com/LLNL/Wintap-Analytics.git`
1. Navigate to the Wintap-Analtyics directory (e.g. `cd Wintap-Analytics`)
1. Follow steps until option 1 for a conda setup and option 2 to use your system python 

Second, follow option 1 or option 2 to complete the python environment setup.

## Option 1: Using Conda

**Windows/Mac/Linux**
1. Download miniconda (much lighter than full anaconda)
    1. https://docs.anaconda.com/free/miniconda/miniconda-install/
1. Create a new conda environment for wintap analytics: `conda create -n wintap-analytics python=3.10 make`
1. Activate the conda environment: `conda activate wintap-analytics​`
1. Install the requirements `make venv`

## Option 2: Using System Python 3.10

**Mac/Linux:**
1. Use make to build the venv: `make venv`
1. Activate the pipenv shell: `pipenv shell`

**Windows:**
1. Install python (www.python.org/downloads)
    1. Run custom installation
        1. ensure pip gets installed
        1. select "Add python to environment variables"
        1. optionally install for all users
    1. Open cmd prompt
        1. Validate python installed and in path by running python --version 
        1. Install pipenv: `python -m pip install pipenv`
        1. Setup pipenv, run: `python -m pipenv install`
        1. Activate the pipenv shell: `python -m pipenv shell`
