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
# The order here matters. 
combine_files = genres_books authors_books reviews 

# Get complete path to combined output files. 
combine_csv_files = $(addsuffix .csv, $(combine_files)) 
combine_output_filepaths = $(addprefix $(combine_output_path), $(combine_csv_files))


# MD EXPLORE FILES ==============================================
explore_output_path = src/data/explore/
explore_exec_path = src/pipeline/explore/
explore_files = reviews

# Get complete path to explore output files.
explore_md_files = $(addsuffix .md, $(explore_files))
explore_output_filepaths = $(addprefix $(explore_output_path), $(explore_md_files))

# TARGETS =======================================================
.PHONY: all


all: $(VENV)/bin/activate cleaning combine
	@echo "Run Code"


$(VENV)/bin/activate: requirements.txt
	python -m venv $(VENV)
	$(PIP) install -r requirements.txt
	
# CLEANING ==============================================
cleaning: $(clean_output_filepaths)


# Creates the specific .csv if it does not exists. 
$(clean_output_filepaths): 
	@echo [ CREATING ] $@...
	@ $(PYTHON) $(patsubst $(clean_output_path)%.csv, $(clean_exec_path)%.py, $@)

# COMBINE ================================================
combine: $(combine_output_filepaths)


$(combine_output_filepaths):
	@echo [ CREATING ] $@...
	@ $(PYTHON) $(patsubst $(combine_output_path)%.csv, $(combine_exec_path)%.py, $@)


# EXPLORE ===============================================
explore: $(explore_output_filepaths)

$(explore_output_filepaths):
	@echo [CREATING] $@...
	@ $(PYTHON) $(patsubst $(explore_output_path)%.md, $(explore_exec_path)%.py, $@)
	mv $(patsubst $(explore_output_path)%, %, $@) $@


# CLEAN =================================================
clean_combine:
	@echo Removing combined files...
	@rm ./src/data/processed/*

clean_clean:
	@echo Removing cleaned files...
	@rm ./src/data/clean/*

clean:
	rmdir /q /s $(VENV)
	@rm ./src/data/combine/*
	@rm ./src/data/clean/*




	
