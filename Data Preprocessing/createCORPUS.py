import sqlite3
import pandas as pd

timeframes = ['2011-08']

for timeframe in timeframes:
    connection = sqlite3.connect('{}.db'.format(timeframe))
    c = connection.cursor()
    limit = 5000
    last_unix = 0
    cur_length = limit
    counter = 0
    test_done = False

    while cur_length == limit:

        df = pd.read_sql(
            "SELECT * FROM parent_reply WHERE unix > {} and parent NOT NULL and score > 0 ORDER BY unix ASC LIMIT {}".format(last_unix, limit), connection)
        last_unix = df.tail(1)['unix'].values[0]
        cur_length = len(df)

        if not test_done:
            with open('data1', 'a', encoding='utf8') as f:
                for i in df.index:
                    f.write(df.loc[i, 'parent']+'\t'+df.loc[i, 'comment']+'\n')

            test_done = True

        else:

            with open('data1.txt', 'a', encoding='utf8') as f:
                for i in df.index:
                    f.write(df.loc[i, 'parent']+'\t'+df.loc[i, 'comment']+'\n')

        counter += 1
        if counter % 20 == 0:
            print(counter*limit, 'rows completed so far')
