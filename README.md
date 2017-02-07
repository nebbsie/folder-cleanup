# Immaculate

[logo]:https://raw.githubusercontent.com/nebbsie/immaculate/master/logo.png "Immaculate logo"
![alt text](https://raw.githubusercontent.com/nebbsie/immaculate/master/logo.png "Logo Title Text 1")

**Immaculate** is a directory cleanup tool. Use it to move files from within directories to the base directory. **Immaculate** also allows different parameter inputs. Such as only moving _text_ files, _video_ files, _music_ files etc.

#Installation

# Code Example
## All Files
`python immaculate.py all <dir>`

This will do the same as above but to every file.

## Film
`python immaculate.py films <dir>` or with filesize parameter  `python immaculate.py films 100 <dir>`

This will search through the dir folder and look for all films in folders, they will be placed in the base folder of the directory tree. This is usefull when you have your movies in a folder, but as you add more you keep adding them into the movies folder as folder. This is a way of of automating the process of going into each folder and moving them. To the correct folder location(base of the directory tree). Using the film parameter will also mean it will check if the film is above a certain size. If no size are set with parameters it will use a default size of 400MB. To set a new size after films you need to add a paramenter of size after the films parameter this is in MB.

