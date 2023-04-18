
import pandas as pd
import numpy as np
import regex as re
import time
import PyPDF2
import pyttsx3


# setup engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# voice
voice_choice = "f"
engine.setProperty('voice', voices[1].id)


#speed
engine.setProperty('rate', 150)

# absolute path
path = 'C:/Users/akasp/OneDrive/Desktop/die-melodie/test'


# select file

book_choice = 'test.pdf'


# creating a pdf file object
pdfFileObj = open(path+"\\"+book_choice, 'rb')


# initialize dataframe to hold documents
df = pd.DataFrame(columns=['page_no', 'page'])



# creating a pdf reader object 
pdfReader = PyPDF2.PdfReader(pdfFileObj, strict=False)
pages = len(pdfReader.pages)



for p in range(pages):
  pageObj = pdfReader.pages[p]
  # print(p)
  df.loc[p, 'page_no'] = p+1
  page_content = pageObj.extract_text()
  # print(page_content)
  df.loc[p, 'page'] = page_content


#closing the pdf file object 
pdfFileObj.close() 

df['page'].replace('', np.nan, inplace=True)
df.dropna(subset=['page'], inplace=True)
df.reset_index(drop=True, inplace=True)

# printing number of pages in pdf file
time.sleep(1)


df['page'] = [re.sub(r'\n+', " ", str(x)) for x in df['page']]
df['page'] = [re.sub(r"([a-z])([A-Z])", r"\1 \2", str(x)) for x in df['page']]
df['page'] = [re.sub(r"([A-Z]{2,})([a-z])", r"\1 \2", str(x)) for x in df['page']]
df['page'] = [re.sub(r"([0-9])([A-Z])", r"\1 \2", str(x)) for x in df['page']]
df['page'] = [re.sub(r"([A-Z])([0-9])", r"\1 \2", str(x)) for x in df['page']]
df['page'] = [re.sub(r"([0-9])([a-z])", r"\1 \2", str(x)) for x in df['page']]
df['page'] = [re.sub(r"(\))([A-Z])", r"\1 \2", str(x)) for x in df['page']]
df['page'] = [re.sub(r'– +', "–", str(x)) for x in df['page']]
# df['page'] = [re.sub(r'\n', " ", str(x)) for x in df['page']]
df['page'] = [re.sub(r'\s+', " ", str(x)) for x in df['page']]

content = " ".join(df['page'].tolist())

#print("\n5. Do you want to continue where you have left off?\nIf yes, please enter a page number, if no, hit enter.")
#page_choice = input("Please enter page number: ") or "0"
#page_choice = int(page_choice)
#print("\tPage", str(page_choice), "selected, flipping to the page now...")
#time.sleep(1)

page_choice = 0

# cutoff before start
df = df.iloc[page_choice: , :]

# estimate
word_counts = df["page"].apply(lambda n: len(n.split()))
minutes = word_counts.sum() / 200 #estimate
seconds = minutes* 60

def convert_to_preferred_format(sec):
   sec = sec % (24 * 3600)
   hour = sec // 3600
   sec %= 3600
   min = sec // 60
   sec %= 60
   return "%02d:%02d:%02d" % (hour, min, sec) 

#print("\nEstimated time of the audio:", convert_to_preferred_format(seconds))
time.sleep(1)

# print("\nGo!\n")
# df.head(20)

#play
for i, row in df.iterrows():
    #print("\n# PAGE NO.", str(i), "#")
    #print(row['page'])
    engine.say(row['page']) # to read immediately
    engine.runAndWait()

