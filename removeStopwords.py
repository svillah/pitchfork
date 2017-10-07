import stop
import pandas as pd

# create a dataframe from output csv of scrape.py
df = pd.read_csv('output.csv')
df.columns = ["artist","rating","album", "best_new_tag", "genre", "publish_date", "abstract"]

# isolate abstract field particularly
x1 = df[["abstract"]]

#album abstracts before removing stop words
print(x1)

# parse and remove stop words
i = 1
for row in x1.values:
    words = str(row)
    parse = words.split()

    resultList = [word for word in parse if word.lower() not in stop.stopwords]
    result = ' '.join(resultList)

    #abstracts after removing stop words
    print(result)

    df.at[i,7] = result #fio how to replace current element with new result!!!!
    
    i+=1

#df.to_csv('output.csv')


        
    

