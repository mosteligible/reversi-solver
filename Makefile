install-dependencies:
	pip install --upgrade pip; \
	pip install pytest

test:
	pytest -v; \
	echo ""; \
	echo "Running go tests.." ; \
	cd solver-go && go test ./...

solve:
	python3 main.py

solve-go:
	cd solver-go && go build && ./reversi_solver
