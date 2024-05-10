## Version 0.0.5 (29-04-2024)

- MAINT - Add pre-commits and update docs by @trallard in https://github.com/Quansight-Labs/accessible-pygments/pull/26
- ENH - Move to hatch for dev/build by @trallard in https://github.com/Quansight-Labs/accessible-pygments/pull/27
- MAINT - Delete docs/all_themes.pptx by @gabalafou in https://github.com/Quansight-Labs/accessible-pygments/pull/40
- [DOC] Remove conda instructions from contributing by @gabalafou in https://github.com/Quansight-Labs/accessible-pygments/pull/39
- ENH - Remove build artifacts from the repo by @gabalafou in https://github.com/Quansight-Labs/accessible-pygments/pull/41
- ENH - Automate theme READMEs by @gabalafou in https://github.com/Quansight-Labs/accessible-pygments/pull/42
- MAINT - Miscellaneous updates by @trallard in https://github.com/Quansight-Labs/accessible-pygments/pull/46
- BUG - Ensure no local version by @trallard in https://github.com/Quansight-Labs/accessible-pygments/pull/48
- ENH - Automate theme README screenshots by @gabalafou in https://github.com/Quansight-Labs/accessible-pygments/pull/43
- MAINT - Update pre-commit hooks by @trallard in https://github.com/Quansight-Labs/accessible-pygments/pull/45
- BUG - Fix contrast failures for high contrast light theme by @gabalafou in https://github.com/Quansight-Labs/accessible-pygments/pull/33
- ENH -Fix broken theme URLs in README, typo in demo html by @meli-lewis in https://github.com/Quansight-Labs/accessible-pygments/pull/53
- ENH - Update code to not get images from placeholder.com by @Carreau in https://github.com/Quansight-Labs/accessible-pygments/pull/51
- ENH -Reflect that rgb colors are in 0-1 and floats. by @Carreau in https://github.com/Quansight-Labs/accessible-pygments/pull/52
- ENH - Small refactor of color utils for readibility and type checkability by @gabalafou in https://github.com/Quansight-Labs/accessible-pygments/pull/55
- ENH - Rename hex to float function by @gabalafou in https://github.com/Quansight-Labs/accessible-pygments/pull/57
- ENH - Set a11y-light default background to #f2f2f2 (light gray) by @gabalafou in https://github.com/Quansight-Labs/accessible-pygments/pull/56

### New Contributors

- @trallard made their first contribution in https://github.com/Quansight-Labs/accessible-pygments/pull/26
- @pre-commit-ci made their first contribution in https://github.com/Quansight-Labs/accessible-pygments/pull/28
- @gabalafou made their first contribution in https://github.com/Quansight-Labs/accessible-pygments/pull/40
- @meli-lewis made their first contribution in https://github.com/Quansight-Labs/accessible-pygments/pull/53
- @Carreau made their first contribution in https://github.com/Quansight-Labs/accessible-pygments/pull/51

## Version 0.0.4 (22-03-2023)

- Merge pull request #24 from mgorny/setup-exclude. [Tania Allard]

  Exclude "test" package from being installed

- Exclude "test" package from being installed. [Michał Górny]

  Add `test` to exclude for `find_packages()`, to prevent the package
  from wrongly installing the `test` directory into site-packages, e.g.:

      /usr/lib/python3.11/site-packages/test

## Version 0.0.3 (09-02-2023)

- Merge pull request #22 from Quansight-Labs/update-readme. [Stephannie
  Jimenez Gacha]

  Document accessibility features in main readme

- Document accessibility features in main readme. [Stephannie Jimenez]
- Merge pull request #20 from Quansight-Labs/fix-highlight. [Stephannie
  Jimenez Gacha]

  Check the highlight color and add highlighted examples to the demo page

- Update themes readme with new colors. [Stephannie Jimenez]
- Check the highlight color and add highlighted examples to the demo
  page. [Stephannie Jimenez]
- Set development version to 0.0.3. [Stephannie Jimenez]
- Release v0.0.2. [Stephannie Jimenez]
- Update changelog. [Stephannie Jimenez]

# Version 0.0.2 (08-11-2022)

- Merge pull request #18 from Quansight-Labs/update-docs. [Stephannie
  Jimenez Gacha]

  Improve readme

- Add direct links to demo page and replace the gif with static image of
  all the current themes. [Stephannie Jimenez]
- Merge pull request #17 from Quansight-Labs/add-creative. [Stephannie
  Jimenez Gacha]

  Add greative theme

- Add greative to main readme. [Stephannie Jimenez]
- Add greative theme. [Stephannie Jimenez]
- Merge pull request #16 from Quansight-Labs/add-blinds. [Stephannie
  Jimenez Gacha]

  Add blinds themes

- Add color theme names in main readme. [Stephannie Jimenez]
- Add blinds dark theme. [Stephannie Jimenez]
- Add blinds light theme. [Stephannie Jimenez]
- Merge pull request #14 from Quansight-Labs/add-gotthard. [Stephannie
  Jimenez Gacha]
- Add gotthard light theme. [Stephannie Jimenez]
- Add gotthard dark theme. [Stephannie Jimenez]
- Center gif. [Stephannie Jimenez]
- Upload gif with themes. [Stephannie Jimenez]
- Update supported themes. [Stephannie Jimenez Gacha]
- Merge pull request #11 from Quansight-Labs/add-github-hcontrast.
  [Stephannie Jimenez Gacha]

  Add github light and dark high contrast

- Add github light high contrast theme. [Stephannie Jimenez]
- Add github dark high contrast theme. [Stephannie Jimenez]
- Update theme list. [Stephannie Jimenez Gacha]
- Fix typos. [Stephannie Jimenez]
- Merge pull request #9 from Quansight-Labs/github-light-colorblind.
  [Stephannie Jimenez Gacha]

  Add github light colorblind theme

- Add github light colorblind theme. [Stephannie Jimenez]
- Update current themes. [Stephannie Jimenez Gacha]
- Merge pull request #8 from Quansight-Labs/add-github-dark-colorblind.
  [Stephannie Jimenez Gacha]

  Add github dark colorblind theme

- Add github dark colorblind theme. [Stephannie Jimenez]
- Merge pull request #7 from Quansight-Labs/fix-github-light.
  [Stephannie Jimenez Gacha]

  Fix github light theme

- Update screenshot. [Stephannie Jimenez]
- Update readme. [Stephannie Jimenez]
- Fix github light colors. [Stephannie Jimenez]
- Merge pull request #6 from Quansight-Labs/github-dark-theme.
  [Stephannie Jimenez Gacha]

  Add `github-dark` theme

- Fix typo. [Stephannie Jimenez]
- Add readme.md. [Stephannie Jimenez]
- Add github-dark theme. [Stephannie Jimenez]
- Merge pull request #5 from Quansight-Labs/github-light-theme.
  [Stephannie Jimenez Gacha]

  Add `github light` theme

- Add github light theme. [Stephannie Jimenez]
- Merge pull request #4 from Quansight-Labs/move-images. [Stephannie
  Jimenez Gacha]

  Move theme images to corresponding folder

- Move theme images to corresponding folder. [Stephannie Jimenez]
- Add badges. [Stephannie Jimenez]
- Fix css loading in demo. [Stephannie Jimenez]
- Move demo page to docs folder. [Stephannie Jimenez]
- Update README.md installation. [Stephannie Jimenez Gacha]
- Set development version to 0.0.2. [Stephannie Jimenez]
- Release v0.0.1. [Stephannie Jimenez]
- Create changelog and release instructions. [Stephannie Jimenez]

## Version 0.0.1 ( 06-08-2022 )

- Update contributing guide. [Stephannie Jimenez]
- Add working demo. [Stephannie Jimenez]
- Fix autogenerated css and start working on static demo. [Stephannie Jimenez]
- Refactoring for automatic theme discovery. [Stephannie Jimenez]
- Add contributing.md and minor refactoring. [Stephannie Jimenez]
- Add pitaya-smoothie to main readme. [Stephannie Jimenez]
- Add image. [Stephannie Jimenez]
- Add pitaya smoothie theme. [Stephannie Jimenez]
- Fix readme in each theme. [Stephannie Jimenez]
- Refactor themes and readme. [Stephannie Jimenez]
- Add light high contrast mode. [Stephannie Jimenez]
- Fix typo. [Stephannie Jimenez]
- Add high contrast dark theme. [Stephannie Jimenez]
- Reorganize colors. [Stephannie Jimenez]
- Add example images. [Stephannie Jimenez]
- Add contrast checks for light theme. [Stephannie Jimenez]
- Make colors bigger. [Stephannie Jimenez]
- Add dark theme contrast ratio. [Stephannie Jimenez]
- Add readme and minor color fixes. [Stephannie Jimenez]
- Rename files and add scripts for multiple languages. [Stephannie Jimenez]
- Add first iteration of dark theme. [Stephannie Jimenez]
- Fix setup.py, add tests and first iteration of light theme. [Stephannie Jimenez]
- Add structure files. [Stephannie Jimenez]
- Initial commit. [Tania Allard]
