init_env:
	python3 -m virtualenv venv

start_env:
	source ./venv/bin/activate

init_dep:
	pip install -r dev-requirements.txt -e .
	pip install fastapi
	pip install uvicorn

start_app:
	uvicorn main:app --reload