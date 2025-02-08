# Make commands for development
# 
# `make setup` install required Python modules.

PIP=pip
PYTHON=python

all: sample1.analysis

requirements.txt: requirements.in
	$(PIP) install -r requirements.in
	@echo "# GENERATED FROM requirements.in.  DO NOT EDIT DIRECTLY." > requirements.txt
	$(PIP) freeze >> requirements.txt

requirements.flag: requirements.txt
	$(PIP) install -r requirements.txt
	touch requirements.flag

sample1.png: sample1.pdf requirements.flag
	@echo Converting pdf to png...
	$(PYTHON) pdf-to-image.py sample1.pdf

sample1.png.flag: sample1.png
	@echo Uploading png to S3...
	./upload-to-s3.sh sample1.png
	touch sample1.png.flag

sample1.analysis: sample1.png.flag
	@echo Running analysis...
	(source .env; $(PYTHON) analyze-image.py `./echo-s3-url.sh sample1.png`)
