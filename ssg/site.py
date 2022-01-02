#Number 1.1 Import pathlib
from pathlib import Path 

#Number 1.2 Create a Class
class Site: 
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)
   
   #Number 1.3 Find root directory
    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
    
        #Number 1.4 Make a directory
        directory.mkdir(parents=True, exist_ok=True)
       
   #Number 1.5 Make a destination directory & Number 1.6 Recreate all Paths
    def build(self):
       self.dest.mkdir(parents=True, exist_ok=True)
       for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            else:
                print("Not a Directory")
    