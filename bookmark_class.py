class bookmark: 
    num_bookmarks = 0
    def __init__(self,folder, url, add_date, name):
        self.folder = folder
        self.url = url
        self.add_date = add_date
        self.name = name
        self.hash = self.generation_hash()
        bookmark.num_bookmarks += 1

    def __del__(self): 
        bookmark.num_bookmarks-=1
    
    # to check later in the database
    # Hash change every start of the programm!!!
    # -> useless
    def generation_hash(self):
       # return hash(self.url+self.add_date+self.folder)
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

    def get_name(self):
        return self.name

    def get_folder(self):
        return self.folder

    def get_hash(self):
        return self.hash

    def generate_string(self):
        return "<DT><A HREF= \""+self.url+"\" ADD_DATE=\""+self.add_date+"\">"+self.name+"</A>"

#<DT><A HREF="https://www.trash-mail.com/posteingang/" ADD_DATE="1609963768">Wegwerf-Email von TRASH-MAIL - Emails anonym empfangen</A>