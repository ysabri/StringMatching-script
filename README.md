# StringMatching-script
Gets two strings from a CSV file then computes and outputs their scores into a new CSV file.
#Implementation Details:
* Input and output files are CSV formatted and are interpreted using python’s csv library, [the library]( http://docs.python.org/2/library/csv.html ). 
* If faced with any encoding errors, just re-save the CSV file with another encoding (Sublime works for this). The python encode method is “useless”, [why]( http://stackoverflow.com/questions/21129020/how-to-fix-unicodedecodeerror-ascii-codec-cant-decode-byte). 
* The script is implemented using Levenshtein algorithm as an example, other algorithms can be found at [py-stringmatching website]( http://pypi.python.org/pypi/py_stringmatching).
