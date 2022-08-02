# N-Back
N-Back is a cognitive enhancment game that was proven to increase your fluid intelligence. To install the game, simply clone the repository in the terminal
with : git clone https://github.com/clw0n/n-back and run 'python3 n-back.py'

To create the log folder, thus enabling statistics, simply run the log.py script in your terminal with : python3 log.py, this will create a "__log__" folder in the previously cloned directory.

In order to view your progress, run the 'stats' script in the terminal with python3 stats.py.

Note : project not finished, Implementing soon (by order):
  - Fixing all bugs (game never stops), making a function for a better visual expression on the terminal, making so that you don't have to press a + ENTER     to match with the correct position
  - The non-visual timer
  - Dual (adding sound), Tri (adding colors), Quad (adding figures) 
  - The log function in n-back.py with the date, time spent, games played with their respective accuracy, level increased, end date (making sure not to         create unnecessary logs, possibly with a dictionnary)
  - The stats.py script, scraping the data from the log system with a graphical user interface for the graph (disregarding pre-existing scraped data to not     loop through the entire log folder)
  - The graphical user interface for the n-back app, using the pre-existing algorithm which will consist of a welcome screen with "PLAY" -> Single, Dual,       Tri, Quad, Penta. "SETTINGS" to change visual parameters, sound parameters, etc. "STATS" which already exists and "USER" to change and create new           users. (only need for a well designed front-end and creating parameters for the front-end.)
  
