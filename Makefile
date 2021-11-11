VENV = pri_venv
PYTHON = python
PIP = pip


# CSV CLEAN FILES =============================================== 
# Path to the clean files.
clean_output_path = src/data/clean/
clean_exec_path = src/pipeline/cleaning/
clean_files = authors books genres reviews


# Get complete path to clean output files. 
clean_csv_files = $(addsuffix .csv, $(clean_files)) 
clean_output_filepaths = $(addprefix $(clean_output_path), $(clean_csv_files))


# CSV COMBINED FILES ============================================
# Path to combined files.
combine_output_path = src/data/processed/
combine_exec_path = src/pipeline/combine/
combine_files = authors_books genres_books reviews

# Get complete path to combined output files. 
combine_csv_files = $(addsuffix .csv, $(combine_files)) 
combine_output_filepaths = $(addprefix $(combine_output_path), $(combine_csv_files))

# TARGETS =======================================================
.PHONY: all


all: $(VENV)/bin/activate cleaning combine
	@echo "Run Code"


$(VENV)/bin/activate: requirements.txt
	python -m venv $(VENV)
	$(PIP) install -r requirements.txt
	
	
cleaning: $(clean_output_filepaths)


# Creates the specific .csv if it does not exists. 
$(clean_output_filepaths): 
	@echo [ CREATING ] $@...
	@ $(PYTHON) $(patsubst $(clean_output_path)%.csv, $(clean_exec_path)%.py, $@)


combine: $(combine_output_filepaths)


$(combine_output_filepaths):
	@echo [ CREATING ] $@...
	@ $(PYTHON) $(patsubst $(combine_output_path)%.csv, $(combine_exec_path)%.py, $@)


clean:
	rmdir /s /q $(VENV)




	
