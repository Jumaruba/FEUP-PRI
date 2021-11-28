VENV = pri_venv
PYTHON = python3
PIP = pip


# CSV CLEAN FILES =============================================== 
# Path to the clean files.
clean_output_path = src/data/clean/
clean_exec_path = src/prepare/clean/
clean_files = authors.csv books.csv genres.csv reviews.csv 

# Get complete path to clean output files. 
clean_output_filepaths = $(addprefix $(clean_output_path), $(clean_files))


# CSV COMBINED FILES ============================================
# Path to combined files.
combine_output_path = src/data/combine/
combine_exec_path = src/prepare/combine/
# The order here matters. 
combine_files = genres_books.csv authors_books.csv reviews.csv 

# Get complete path to combined output files. 
combine_output_filepaths = $(addprefix $(combine_output_path), $(combine_files))


# MD EXPLORE FILES ==============================================
explore_output_path = src/data/explore/
explore_exec_path = src/prepare/explore/
explore_plot_path = src/data/explore/plots/
explore_files = reviews.md genres.md authors.md books.md

# Get complete path to explore output files.
explore_output_filepaths = $(addprefix $(explore_output_path), $(explore_files))

# TARGETS =======================================================
.PHONY: all


all: pri_venv/ install clean_ combine_ explore_


install: 
	. ./$(VENV)/bin/activate && $(PIP) install -r requirements.txt

pri_venv/: 
	$(PYTHON) -m venv $(VENV)


# CLEAN ==============================================
clean_:  $(clean_output_path) $(clean_output_filepaths)

$(clean_output_path):
	@echo [ CREATING ] Clean folder...
	@mkdir -p $@ 

# Creates the specific .csv if it does not exists. 
$(clean_output_filepaths): 
	@echo [ CREATING ] $@...
	@. ./$(VENV)/bin/activate && $(PYTHON) $(patsubst $(clean_output_path)%.csv, $(clean_exec_path)%.py, $@)

# COMBINE ================================================
combine_: $(combine_output_path) $(combine_output_filepaths)

$(combine_output_path):
	@echo [ CREATING ] Combine folder...
	@mkdir -p $@ 


$(combine_output_filepaths):
	@echo [ CREATING ] $@...
	@. ./$(VENV)/bin/activate && $(PYTHON) $(patsubst $(combine_output_path)%.csv, $(combine_exec_path)%.py, $@)


# EXPLORE ===============================================
explore_:  $(explore_plot_path) $(explore_output_filepaths) 

# Create the plot folder
$(explore_plot_path): 
	@echo [ CREATING ] Plot folder...
	@mkdir -p $@ 

$(explore_output_filepaths):
	@echo [ CREATING ] $@...
	@. $(VENV)/bin/activate && $(PYTHON) $(patsubst $(explore_output_path)%.md, $(explore_exec_path)%.py, $@)


# CLEAN =================================================  
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




	
