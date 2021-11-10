VENV = pri_venv
PYTHON = python
PIP = pip

run: $(VENV)/bin/activate cleaning combine
	@echo "Run Code"

$(VENV)/bin/activate: requirements.txt
	python -m venv $(VENV)
	$(PIP) install -r requirements.txt

cleaning:
	$(PYTHON) ./src/pipeline/cleaning/clean_authors.py
	$(PYTHON) ./src/pipeline/cleaning/clean_books.py
	$(PYTHON) ./src/pipeline/cleaning/clean_genres.py
	$(PYTHON) ./src/pipeline/cleaning/clean_reviews.py
	$(PYTHON) ./src/pipeline/cleaning/clean_series.py

combine:
	$(PYTHON) ./src/pipeline/cleaning/clean_authors.py
	$(PYTHON) ./src/pipeline/cleaning/clean_books.py
	$(PYTHON) ./src/pipeline/cleaning/clean_genres.py
	$(PYTHON) ./src/pipeline/cleaning/clean_reviews.py
	$(PYTHON) ./src/pipeline/cleaning/clean_series.py

clean:
	rmdir /s /q $(VENV)