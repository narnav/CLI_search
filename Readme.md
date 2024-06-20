Classes and Methods
TextFileSearcher
__init__(self, file_name, search_string, case_sensitive=False)
Initializes the TextFileSearcher instance.

file_name (str): The name of the file to search.
search_string (str): The string to search for.
case_sensitive (bool): Optional; defaults to False. Determines if the search should be case-sensitive.
search(self)
Performs the search on the specified file.

Returns: A list of tuples containing the line number and the line content for each match, or None if the file is not found.
CommandLineInterface
__init__(self)
Initializes the CommandLineInterface instance.

parse_arguments(self)
Parses command-line arguments to set the file name, search string, and options for case sensitivity and report generation.

print_usage(self)
Prints usage information for the application.

print_results(self, results)
Prints the search results.

results (list): The list of search results, where each result is a tuple of (line number, line content).
print_report(self, results)
Prints a summary report of the search results.

results (list): The list of search results, where each result is a tuple of (line number, line content).
run(self)
Executes the application: parses arguments, performs the search, and prints the results or report.

Error Handling
If the specified file is not found, the application prints an error message: File '<file_name>' not found.
Example Output
Search Results
shell
Copy code
Line 2: This is an example line containing the search term.
Line 4: Another line with the search term here.
Report
shell
Copy code
Search Report for 'search term' in 'example.txt':
Total occurrences: 2
Notes
Ensure the file path is correct and the file is accessible.
The script reads the entire file into memory; for very large files, this might not be efficient. Consider optimizing for larger files if necessary.