This is a [cut-up technique](https://en.wikipedia.org/wiki/Cut-up_technique) simulator in which you enter a poem, the program intelligently applies the cut-up technique to it and writes another poem based on it.

# How to run
* ``python3 digital_cutup.py <originalPoemFile>``
  - This is create the new poem file ("cut_up_poem.txt") in the current directory
* ``python3 digital_cutup.py <originalPoemFile> <newPoemOutputDirectory>``
  - This is create the new poem file ("cut_up_poem.txt") in the output directory specified in <newPoemOutputDirectory>

###Libs used:
* Python3 libs like random and sys
* [language-check](https://pypi.org/project/language-check/)
  - Used for text correction and grammar checks (so that things make (a bit of) sense)
* [numpy](https://pypi.org/project/numpy/) (Copyright © 2005-2019, NumPy Developers.)
  - Used for generating gaussian distributions in order to generate a random number of words for each line
