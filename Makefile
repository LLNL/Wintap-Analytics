fmt:
	pipenv run black ./
	pipenv run isort ./

requirements:
	pipenv requirements > requirements.txt

venv:
	pip3 install pipenv
	pipenv install --dev
