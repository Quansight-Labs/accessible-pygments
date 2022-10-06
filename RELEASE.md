# Release

Please follow the instructions to make a new release of the accessibility pygments package.

- `git fetch && git pull`
- `git clean -xdfi`
- Update `CHANGELOG.md` with `gitchangelog`
- `git add && git commit -m "Update changelog"`
- Update `VERSION_INFO` in the `__init__.py` removing `dev`
- `git add && git commit -m "Release vX.X.X"`
- `python setup.py bdist_wheel --universal`
- `python setup.py sdist`
- `twine check dist/*`

