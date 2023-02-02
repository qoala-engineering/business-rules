init_env:
	python3 -m virtualenv venv

start_env:
	source ./venv/bin/activate

init_dep:
	pip install -r dev-requirements.txt -e .
	pip install fastapi
	pip install uvicorn

start_sample_app:
	uvicorn samples.main:app --reload

start_life_app:
	uvicorn life_insurance.main:app --reload