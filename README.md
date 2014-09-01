qudt-for-domain-tools
=====================

Establishing consistent unit identities in a world of whirling chaos.

It turns out that many of the software tools used in the world of engineering 
use their own unit naming conventions. This makes translation of data between 
tools difficult. Symbols and operator conventions can vary, but ultimately even
the symbol isn't enough to uniquely identify a unit -- duplicates exist.

The NASA-developed QUDT system is a fairly comprehensive listing of units, and
includes not just unit identities but conversion factors between units. If the
unit systems of various engineering tools could be mapped to corresponding units
in the QUDT database, then we could have precise identities for units across
tools, in addition to the data needed to transform values from one unit into
another.

The mission of this project is to:
- Establish unit ontologies for common engineering tools
- Map individual units in these ontologies to corresponding units in QUDT
- Provide software libraries, in a variety of languages, for retrieving mappings
  and performing transformations



GETTING STARTED
---------------
This project is still pretty new, so there are a few different parts you will have to pull together to begin working.

There are two main things you might be interested in doing:
1. Use the database to convert quantities between units, and discover equivalent units across domain tools.
2. Re-generate the database, add new units, or add whole domains to the system.

Most people will only need #1.

### DEPENDENCIES
To do #1 above:
- Python 2.7.x
- Java Development Kit, Version 6 or above (https://java.com/en/download/index.jsp)
- Gradle (http://www.gradle.org)

To do #2 above:
- See #1, plus
- OpenModelica 1.9.x (to work with Modelica database)
- An ontology editor like:
	- Protege 4.x (for visualizing ontology databases)
	- TopBraid Composer (free)

### RUNNING STUFF
Run `gradle fetchDependencies` to download the database server, raw data, and more.

- For #1:
	- run `python build_ontologies.py` to load the raw data into the database. You only gotta do this once.
	- use the qudt4dt or C# libraries to do conversions, queries, etc.
		- run `start.sh` to get the server started first. It will be located at http://localhost:3030
		- You may need to modify the constructors to point the correct server location
- For #2:
	- UNDOCUMENTED WILD WEST. GOOD LUCK.
