.PHONY: reset test

spec:
	@echo === Generating the spec ===
	@./scripts/generate_spec.sh

sdk:
	@echo === Generating the SDK ===
	@./scripts/generate_sdk.sh

test:
	@echo === Testing the SDK ===
	@python -m pytest tests

format:
	@echo
	@echo === Formatting the Generator ===
	@isort gotham tests --profile black --multi-line NOQA -sl --project gotham
	@python -m black gotham tests

lint:
	@echo === Linting the SDK ===
	@python -m pyright gotham

reset:
	@echo === Resetting the git state ===
	git checkout HEAD -- .
