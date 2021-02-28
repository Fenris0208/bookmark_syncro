class inputFile():
    def __init__(self, file):
        self.file_name = file
        self.data = open(file,'r')
        print("file input success\nContent:\n",self.data.read())

    def ToString(self):
        return self.data.read()

    # returnvalue is a list of bookmars 
    def generating_bookmarks(self):
        bookmarks = []


        return bookmarks
