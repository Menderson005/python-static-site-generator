#Number 1.7 Import Typer 
import typer 
from ssg.site import Site 

#Number 1.8 Configuration options
def main(source="content", dest="dist"):
    config = {
        "source": source,
        "dest": dest
    }

#Number 1.9 Build the site
    Site(**config).build()

#Number 1.10 Run typer
typer.run(main)