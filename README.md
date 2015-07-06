# py-Goldsberry
Python Package for facilitating analysis of NBA Data

[package building guide](http://www.scotttorborg.com/python-packaging/minimal.html)

###Status
**5-6-15**
* Updated Shotchart.py
* Added Miscellaneous.py
* Fixed error in database table

**3-16-15**
* Posted old packages to Github
* Need To update `__init__.py` to import each separate file when the package is loaded
* Need to finish identifying all of the data tables
* Need to organize possible data tables into unifying framework
* Create a branch for each sub-module and assign each for completion

**3-15-15**

* Copied and broke apart the existing code for `NBAStats`
* 80% finished with going through [stats.nba.com](http://stats.nba.com) and identifying all of the available data tables
* Need to create organizing framework for the package with two goals **Ease of Use** & **Minimal Web Calls**
* Need to start documentation website. One key part of the website should include NBA Explanations of each statistics. These are easily copyable from the website. Need to be sure to provide attribution.
* For some of the aggregated stats, may need to think about pulling them on the regular to figure out how they change on a game-by-game basis. If we can compute some of the stats from others that are available, we can minimize the number of calls to the website and use the new metrics as examples in the lessons. Additionally, we can build the functionality in the package to automatically compute the statistics on a given set of data.
* Need to either use Cardinal or Github as a task manager and progress report to keep each other updated on the progress of the package.
* Need to read up on Python3 to get a better idea of how it handles certain things. Long-term plan needs to be improving computational efficiency of the package.
