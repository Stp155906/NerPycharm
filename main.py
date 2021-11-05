
import spacy
from spacy import displacy
import pandas as pd
from spacy.pipeline import EntityRecognizer
import xlsxwriter

from spacy.lang.en.examples import sentences
###########################################################
print(spacy.__version__)

# FOR EACH STRING IN CELL, SPLIT STRING AT SYMBOL FUNCTION " : "

txt = "Starbucks is the best:I also like Peets : Apple "
x = txt.split(":")
print(x)

###########################################################

outWorkbook = xlsxwriter.Workbook("out.xlsx")
outSheet = outWorkbook.add_worksheet()
names = x

## WRITING HEADERS  TO INDIVIDUAL CELLS
outSheet.write("A1", "Names")  # writes to cell
outSheet.write("B1", "Entity Type")  # writes to cell
## WRITE DATA TO CELLS
# EXAMPLE NAMES HEADER
outSheet.write("A2", names[0])
outSheet.write("A3", names[1])
outSheet.write("A4", names[2])






# for every name index in collumn A, write outsheet
nlp = spacy.load("en_core_web_sm")
doc = nlp()
for token in names:
    print(doc.ents)
displacy.serve(doc, style="ent")


# EXAMPLE ENTITY_TYPES

outSheet.write("B2", names[0])
outSheet.write("B3", names[1])
outSheet.write("B4", names[2])
# outSheet.write("C2", new_code)

###########################################################
outWorkbook.close()
###########################################################
# TOKENIZE STRING ENTITY
dataframe = pd.read_excel('out.xlsx')
print(dataframe)














# print(names[0].encode('utf-8').strip())

# code = names[0].encode('utf-8').strip()
# print(code)


# to tokenize/splittext

# nlp = spacy.load("en_core_web_sm")
# doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
# for token in doc:
# print(token.text)

# doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
# for token in doc:
# print(token.text)


# to read in file and tokenize

# nlp = spacy.load('en_core_web_sm')
# nlp = nlp.to_bytes()
# file_name = nlp('out.xlsx')


# Extract tokens for the given doc
# print([token.text for token in introduction_file_doc])
# nlp = spacy.load("en_core_web_sm")
# doc = nlp(code)
# for token in doc:
# print(token.text)


########################################################

# VISUALIZE ENTITY RECOGNITION

# nlp = spacy.load("en_core_web_sm")
# doc = nlp(text)
# for token in doc:
# print(token.text)

# displacy.serve(doc, style="ent")


###########################################################

# GROUPBY FUNCTION IN (PANDAS)

###########################################################
