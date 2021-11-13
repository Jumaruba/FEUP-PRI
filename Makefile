VENV = pri_venv
PYTHON = python
PIP = pip


# RAW DATA ======================================================
# There are the files to be gathered.
gather_output_path = src/data/raw/

# CSV CLEAN FILES =============================================== 
# Path to the clean files.
clean_output_path = src/data/clean/
clean_exec_path = src/pipeline/clean/
clean_files = authors.csv books.csv genres.csv reviews.csv 

# Get complete path to clean output files. 
clean_output_filepaths = $(addprefix $(clean_output_path), $(clean_files))


# CSV COMBINED FILES ============================================
# Path to combined files.
combine_output_path = src/data/combine/
combine_exec_path = src/pipeline/combine/
# The order here matters. 
combine_files = genres_books.csv authors_books.csv reviews.csv 

# Get complete path to combined output files. 
combine_output_filepaths = $(addprefix $(combine_output_path), $(combine_files))


# MD EXPLORE FILES ==============================================
explore_output_path = src/data/explore/
explore_exec_path = src/pipeline/explore/
explore_files = reviews.md

# Get complete path to explore output files.
explore_output_filepaths = $(addprefix $(explore_output_path), $(explore_files))


# TARGETS =======================================================
.PHONY: all


all: $(VENV)/bin/activate clean combine
	@echo "Run Code"


$(VENV)/bin/activate: requirements.txt
	python -m venv $(VENV)
	$(PIP) install -r requirements.txt 


# GATHER ========================================
gather_: 
	@echo [ GATHER ] Books...
	@wget -o $(gather_output_path)books.json https://drive.google.com/uc?id=1LXpK1UfqtP89H1tYy0pBGHjYk8IhigUK
	@echo [ GATHER ] Authors...
	@wget -o $(gather_output_path)authors.json https://drive.google.com/uc?id=19cdwyXwfXx_HDIgxXaHzH0mrx8nMyLvC
	@echo [ GATHER ] Genres...
	@wget -o $(gather_output_path)genres.json https://drive.google.com/uc?id=1ah0_KpUterVi-AHxJ03iKD6O0NfbK0md
	@echo [ REVIEWS ] Reviews...
	@wget -o $(gather_output_path)reviews.json https://drive.google.com/uc?id=196W2kDoZXRPjzbTjM6uvTidn6aTpsFnS 
	

# CLEAN ==============================================
clean_: $(clean_output_filepaths)

# Creates the specific .csv if it does not exists. 
$(clean_output_filepaths): 
	@echo [ CREATING ] $@...
	@ $(PYTHON) $(patsubst $(clean_output_path)%.csv, $(clean_exec_path)%.py, $@)

# COMBINE ================================================
combine_: $(combine_output_filepaths)


$(combine_output_filepaths):
	@echo [ CREATING ] $@...
	@ $(PYTHON) $(patsubst $(combine_output_path)%.csv, $(combine_exec_path)%.py, $@)


# EXPLORE ===============================================
explore_: $(explore_output_filepaths)

$(explore_output_filepaths):
	@echo [CREATING] $@...
	@$(PYTHON) $(patsubst $(explore_output_path)%.md, $(explore_exec_path)%.py, $@)
	@mv $(patsubst $(explore_output_path)%, %, $@) $@


# CLEAN ================================================= 
clean_gather:
	@echo Removing gathered files...
	@rm ./src/data/raw/*

clean_clean:
	@echo Removing cleaned files...
	@rm ./src/data/clean/*

clean_combine:
	@echo Removing combined files...
	@rm ./src/data/combine/*

clean_explore:
	@echo Removing explored files...
	@rm -r -f ./src/data/explore/*

clean: clean_clean clean_combine clean_explore




	
