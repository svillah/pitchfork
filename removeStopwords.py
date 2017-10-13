import stop
import pandas as pd
import csv

# create a dataframe from output csv of scrape.py
df = pd.read_csv('output.csv')
df.columns = ["artist","rating","album", "best_new_tag", "genre", "publish_date", "abstract", "fullDesc"]

#album abstracts before removing stop words
x1 = df[["abstract"]]
print(x1)

# parse and remove stop words
i = 1
for index, row in df.iterrows():
    #remove stopwords from abstract
    abstract = str(row['abstract'])
    parse = abstract.split()

    resultList = [word for word in parse if word.lower() not in stop.stopwords]
    result = ' '.join(resultList)
    result.replace('"','')

    #replace df cell with new abstract
    df.loc[index,'abstract'] = result

    #remove stopwords from whole review
    review = str(row['fullDesc'])
    again = review.split()
    siftList = [word for word in again if word.lower() not in stop.stopwords]
    sift = ' '.join(siftList)
    sift.replace('"','')

    #replace df cell with new whole review
    df.loc[index, 'fullDesc'] = sift
    
    i+=1

df.to_csv('refined.csv', index=False)

