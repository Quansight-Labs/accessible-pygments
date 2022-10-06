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
- `git tag -a vX.X.X -m 'Release x.x.x'`
- Update `VERSION_INFO` in the `__init__.py` add `dev` and increment version
- `git add && git commit`
- `git push`
- `git push --tags`
