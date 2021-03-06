# tk-talus
Random number generator in Python3

This project also uses the python module `tkinter` to display a graphical user interface (GUI)

![Bone Die](docs/images/Die_Bone.png)

Image Author: [Kolby Kirk](https://commons.wikimedia.org/wiki/File:Die_bone.jpg). [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). Image cropped from original dimensions.

## Getting Started

### 1. Clone this repository
Clone this repository using the following git command:
```bash
git clone https://github.com/mes32/tk-talus
```

### 2. Run the program
After cloning the repository, navigate into your project directory. In the code example below the path to your directory is indicated using the placeholder `<repo_directory>`. Then run the script `run.py` with python3.
```bash
# Navigate to the project directory
cd <repo_directory>

# Launch the program run.py
python3 run.py
```

### 3. About tagged versions
This project has several different versions. You can navigate between these versions using git. The command `git tag` will list all the available versions. The command `git checkout <version>` will checkout the specified version. Make sure to substitute the name of the version for the placeholder `<version>`. Checking out a version will temporarily re-write the contents of `run.py` to that version of the file.
```bash
# List all versions
git tag

# The following switches the project to version v0.0
git checkout v0.0

# To checkout another version, substitute the version name for <version>
git checkout <version>

# To checkout the latest version
git checkout master
```

## Tkinter References

- [https://python-course.eu/python_tkinter.php](https://python-course.eu/python_tkinter.php)
- [http://effbot.org/tkinterbook/tkinter-index.htm](http://effbot.org/tkinterbook/tkinter-index.htm)