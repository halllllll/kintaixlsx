from openpyxl.styles import Font
from openpyxl.styles import Alignment
A1 = Font(
    name="MS UI Gothic",
    size=19.0,
    extend=None,
    underline=None,
    vertAlign=None,
    scheme=None,
    charset=128,
    family=3.0,
    bold=False,
    italic=False,
    strike=None,
    outline=None,
    shadow=None,
    condense=None,
)

A2 = Font(
    name="MS PGothic" ,
    size=10.0,
    extend=None,
    underline=None,
    vertAlign=None,
    scheme=None,
    charset=128,
    family=3.0,
    bold=True,
    italic=False,
    strike=None,
    outline=None,
    shadow=None,
    condense=None,
)
G2 = Font(
    name="MS PGothic",
    size=14.0,
    extend=None,
    underline=None,
    vertAlign=None,
    scheme=None,
    charset=128,
    family=3.0,
    bold=False,
    italic=False,
    strike=None,
    outline=None,
    shadow=None,
    condense=None,
)

G2_Align = Alignment(
    horizontal='right',
    vertical='center',
    textRotation=0, 
    wrapText=None, 
    shrinkToFit=None, 
    indent=0.0, 
    relativeIndent=0.0, 
    justifyLastLine=None, 
    readingOrder=0.0
)