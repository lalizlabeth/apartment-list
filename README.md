Normalize File Path
===================

Apartment List Coding Challenge
-------------------------------

This method will *normalize* a *string* which represents a file path. Normalizing, in this case, consists of two parts.
* all single dot components of the path must be removed.  
    * For example, "foo/./bar" should be normalized to "foo/bar".
* all double dots components of the path must be removed, along with their parent directory, if any.  
    * For example, "foo/bar/../baz" should be normalized to "foo/baz".


The program is written with Python 2.7. Make sure you have Python installed on your computer before continuing. You can download it [linkref]: http://www.python.org/download/ here.