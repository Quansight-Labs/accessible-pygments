# Making a release

Follow these instructions to make a new release of the `accessible-pygments` package.

1. Create a new branch for the release

   ```bash
    git checkout -b release-vX.X.X
   ```

2. Document the changes since the last release

   - Update the `CHANGELOG.md` with `gitchangelog` or any other tool of your choice
   - Commit the changes `git add && git commit -m "Update changelog"`

3. Check the package locally

   ```bash
   # since we use vcs to dynamically set the tag you can check with hatch
   $ hatch version

   0.0.5.dev18+g8b0f6ba.d20230403

   # build locally and check the artifacts
   $ hatch build

   [sdist]
   dist/accessible_pygments-0.0.5.dev19+g076246a.d20230403.tar.gz

   [wheel]
   dist/accessible_pygments-0.0.5.dev19+g076246a.d20230403-py3-none-any.whl

   # check the contents
   twine check dist/*

   # clean the build artifacts
   hatch clean
   ```

4. Submit the PR, and merge the release branch into main once approved.
5. After merge: check the build artifacts from the GitHub actions workflow
6. Prepare the release commit - checkout the branch for the release and make sure it is to date and the repo is clean:

   ```bash
   git checkout main
   git fetch && git pull
   git clean -xdfi
   ```

7. Tag the release with the version number and push the tag to GitHub

   ```bash
   git tag -a vX.X.X -m 'Release x.x.x'
   git push --tags
   ```

   If you need to course-correct and delete the tag:

   ```bash
    git tag -d vX.X.X
    git push --delete origin vX.X.X
   ```

8. Check that the release was published correctly
