install-dependencies:
	pip install --upgrade pip; \
	pip install pytest

test:
	pytest -v
