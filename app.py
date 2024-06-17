import sys

class TextFileSearcher:
    def __init__(self, file_name, search_string, case_sensitive=False):
        self.file_name = file_name
        self.search_string = search_string
        self.case_sensitive = case_sensitive
        

    def search(self):
        try:
            with open(self.file_name, 'r') as file:
                lines = file.readlines()
                results = []
                for line_number, line in enumerate(lines, start=1):
                    if self.case_sensitive:
                        if self.search_string in line:
                            results.append((line_number, line.strip()))
                    else:
                        if self.search_string.lower() in line.lower():
                            results.append((line_number, line.strip()))
                return results
        except FileNotFoundError:
            print(f"File '{self.file_name}' not found.")
            return None

class CommandLineInterface:
    def __init__(self):
        self.file_name = None
        self.search_string = None
        self.case_sensitive = False
        self.report = False

    def parse_arguments(self):
        args = sys.argv[1:]

        if '--help' in args:
            self.print_usage()
            sys.exit(0)

        if '--case' in args:
            self.case_sensitive = True
            args.remove('--case')

        # if len(args) != 2:
        #     self.print_usage()
        #     sys.exit(1)
        
        # if len(args) == 3 and args[2] == :
        if '--report' in args:
            self.report = True

        self.file_name = args[0]
        self.search_string = args[1]

    @staticmethod
    def print_usage():
        print("Usage: python search.py [options] <file_name> <search_string>")
        print("Options:")
        print("  --help        Show this help message and exit")
        print("  --case        Perform a case-sensitive search")

    def print_results(self, results):
        if results:
            for line_number, line in results:
                print(f"Line {line_number}: {line}")
        elif results is not None:
            print(f"'{self.search_string}' not found in '{self.file_name}'.")

    def print_report(self, results):
        if results:
            print(f"Search Report for '{self.search_string}' in '{self.file_name}':")
            print(f"Total occurrences: {len(results)}\n")
            # for line_number, line in results:
            #     print(f"Line {line_number}: {line}")
        else:
            print(f"No occurrences of '{self.search_string}' found in '{self.file_name}'.")

    def run(self):
        self.parse_arguments()
        searcher = TextFileSearcher(self.file_name, self.search_string, self.case_sensitive)
        results = searcher.search()
        if results:
            for line_number, line in results:
                print(f"Line {line_number}: {line}")
        elif results is not None:
            print(f"'{self.search_string}' not found in '{self.file_name}'.")

        if self.report:
            self.print_report(results)
        else:
            self.print_results(results)
            
if __name__ == "__main__":
    cli = CommandLineInterface()
    cli.run()
