# General Makefile for auto. doc generation
INIT_FILE=src/__init__.py

# Build the UML graphs (packages & classes graphs)
graph:
	@echo "Building the UML graphs"
	@echo "# Init file. Keep empty" >> $(INIT_FILE)
	@pyreverse -Abo png src/ --output-directory uml/
	@rm $(INIT_FILE)