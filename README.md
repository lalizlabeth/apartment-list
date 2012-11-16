Apartment List Coding Challenge
-------------------------------

This method will *normalize* a *string* which represents a file path. Normalizing, in this case, consists of two parts.
* all single dot components of the path must be removed.  
    * For example, "foo/./bar" should be normalized to "foo/bar".
* all double dots components of the path must be removed, along with their parent directory, if any.  
    * For example, "foo/bar/../baz" should be normalized to "foo/baz".


The program is written with Python 2.7. Make sure you have Python installed on your computer before continuing. You can download it [here](http://www.python.org/download/). Here are the steps to running the program. Also, pull the files from GitHub or just download the file.

1. Open up Terminal (or Command Line on PC).
2. CD into the directory where you have stored "normalize.py"
3. When you have found the correct directory, type "python normalize.py" to run the program.
4. You will be prompted to input your file path. After you input your file path, it will output the normalized path.
5. If you want to run the program again, simply type "yes" to normalize another path.
6. If you want to terminate the program, type "no" or Ctrl/Cmd-C.

