venv:
	pip3 install pipenv
	pipenv install --dev

requirements:
	pipenv requirements > requirements.txt
