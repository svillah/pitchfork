import stop
import pandas as pd
import csv

# create a dataframe from output csv of scrape.py
df = pd.read_csv('output.csv')
df.columns = ["artist","rating","album", "best_new_tag", "genre", "publish_date", "abstract"]

#album abstracts before removing stop words
x1 = df[["abstract"]]
print(x1)

# parse and remove stop words
i = 1
for index, row in df.iterrows():
    words = str(row['abstract'])
    parse = words.split()

    resultList = [word for word in parse if word.lower() not in stop.stopwords]
    result = ' '.join(resultList)
    result.replace('"','')

    #abstracts after removing stop words
    print(result)

    #replace df cell with new abstract
    df.loc[index,'abstract'] = result 
    
    i+=1

df.to_csv('refined.csv', index=False)

