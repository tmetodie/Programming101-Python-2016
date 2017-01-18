class Log:
    def __init__(self, filename):
        self.filename = filename
        self.file_handler = None

    def logging(self, text):
        self.file_handler.write(text + '\n')

    def __enter__(self):
        print("__enter__")
        self.file_handler = open(self.filename, "r+")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self.file_handler.close()
        return True

with Log("log_file.txt") as logfile:
    print("Main")
    logfile.logging("Test1")
    logfile.logging("Test2")


with Log("log_file1.txt") as l1:
    l1.logging("In file 1")
    var = 5
    with Log("log_file2.txt") as l2:
        l2.logging("Logginf in file 2: {0}".format(var))
