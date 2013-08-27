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

