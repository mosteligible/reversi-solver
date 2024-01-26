install-dependencies:
	pip install --upgrade pip; \
	pip install pytest

test:
	pytest -v

solve:
	python3 main.py
