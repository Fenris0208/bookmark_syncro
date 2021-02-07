class bookmark: 
    num_bookmarks = 0
    def __init__(self,url,add_date, folder ):
        self.url = url
        self.add_date = add_date
        self.folder = folder
        self.hash = self.generation_hash()
        bookmark.num_bookmarks += 1

    def __del__(self): 
        bookmark.num_bookmarks-=1
        
    def generation_hash(self):
        return hash(self.url)

    def get_contet(self):        
        print("Bookmark\t:\t", self.url)
        print("add_Date\t:\t", self.add_date)
        print("in Folder\t:\t", self.folder)
        print("Hash\t\t:\t", self.hash)
    
    def get_url(self):
        return self.url

    def get_add_date(self):
        return self.add_date

    def get_folder(self):
        return self.folder

    def get_hash(self):
        return self.hash