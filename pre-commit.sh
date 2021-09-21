set -e

echo "Running setup check"
if [ -d pre-commit-venv ]; then rm -rf pre-commit-venv; fi
python -m venv pre-commit-venv
pre-commit-venv/scripts/python.exe -m pip install --upgrade pip

echo "Running formatting, linting, tests"
pre-commit-venv/scripts/pip install -r requirements.txt -r requirements-dev.txt
pre-commit-venv/scripts/python.exe -m black repomint_mint tests
pre-commit-venv/scripts/python.exe -m flake8 repomint_mint tests
pre-commit-venv/scripts/python.exe -m pytest

echo "Removing pre-commit venv"
rm -rf pre-commit-venv

echo "Updating docs"
if ! [ -d docs ]; then mkdir docs; fi

# TODO: does not work using venv directly
echo "pydoc-markdown not working in .sh"
echo "Run -> pydoc-markdown -I repomint_mint --render-toc > docs/README.md"
pydoc-markdown -I repomint_mint --render-toc > docs/README.md