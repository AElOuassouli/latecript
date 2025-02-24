format:
	uvx ruff format src/

lint: 
	uvx ruff check src/

lint-fix:
	uvx ruff check --fix src/ 

run: 
	uv run latecript --settings_file .settings.json