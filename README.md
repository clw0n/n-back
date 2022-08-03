# N-Back
N-Back is a cognitive enhancment game that was proven to increase your fluid intelligence, which is the 'intelligence' responsible for problem solving skills, analogies, reasoning skills, which was previously thought to be fixed after a certain period.

To install the game, simply clone the repository in the terminal
with :

``````````
git clone https://github.com/clw0n/n-back 

sudo python3 stats.py

python3 n-back.py

``````````
You need root access in order to create a folder and write files in (you can check the code in stats.py to be sure)

Note : project not finished, Implementing soon (by order):
  - __Fixing all bugs__ (game never stops), making a function for a better visual expression on the terminal, making so that you don't have to press a +       ENTER to match with the correct position
  - The __non-visual timer__
  - __Dual__ (adding sound), __Tri__ (adding colors), __Quad__ (adding figures) 
  - The __log function__ in n-back.py with the __date, time spent, games played with their respective accuracy, level increased, end date__ (making sure       not to create unnecessary logs, possibly with a dictionnary) (database)
  - The stats.py script, scraping the data from the log system with a __graphical user interface for the statistics graph__ (disregarding pre-existing         scraped data to not loop through the entire log folder)
  - __The graphical user interface__ for the n-back app, using the pre-existing algorithm which will consist of a welcome screen with "PLAY" -> Single,         Dual,Tri, Quad, Penta. "SETTINGS" to change visual parameters, sound parameters, etc. "STATS" which already exists and "USER" to change and create new
    users. (only need for a well designed front-end and creating parameters for the front-end.)
  
