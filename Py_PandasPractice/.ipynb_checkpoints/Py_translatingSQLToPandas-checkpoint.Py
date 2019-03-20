import pandas as pd
from numpy import nan
from random import randint
from random import choice



# A toy dataframe with some random data

d2 = {'D':list(range(10)),'E':[randint(1,10) for i in range(10)], 'F':[choice(['x','y','z']) for i in range(10)]}
df2 = pd.DataFrame(d2)
df2


# And one more exciting toy dataframe with null values (gasp!)
dnone = {'D':list(range(10)),'E':[randint(1,10) for i in range(10)], 'F':[choice(['x','y','z',nan]) for i in range(10)]}
dfnone = pd.DataFrame(dnone)
dfnone



# SELECT * FROM df2:
df2

# SELECT E from df2:
df2['E']
df2.E


# SELECT E, F FROM df:
df[['A','B']]

# SELECT TOP 2 * FROM df2:
df2.head(2)

# SELECT DISTINCT * FROM df2:
df2.drop_duplicates()


# SELECT DISTINCT E FROM df2:
df2['E'].drop_duplicates()

# SELECT DISTINCT * FROM dfnone - in SQL NULL counts as a distinct value in this context
dfnone['F'].drop_duplicates()   # And NaN shows up here as well, so the behavior w/ DISTINCT is similar to SQL


# SELECT DISTINCT E,F FROM df2:
df2[['E','F']].drop_duplicates()


# SELECT * FROM df2 WHERE F='x':
df2[df2['F']=='x'] 
df2.loc[df2['F']=='x']  # equivalently  (When is .loc necessary?)


# Breaking this down a bit:
df2['F']=='x'           # returns a pd series of booleans
type(df2['F']=='x')  
df2[[True]*5+[False]*5] # Selecting the first 10 rows by booleans


# SELECT * FROM dfnone WHERE F='x' - in SQL NULL is left out
dfnone.loc[dfnone['F']=='x']


# SELECT * FROM dfnone WHERE F != 'x' - in SQL NULL is left out here as well, because NULL yields an Unknown truth value when compared
dfnone.loc[dfnone['F'] != 'x'] # notice the NaN is *not* left out here; one way Pandas != SQL




# SELECT * FROM df2 WHERE F='x' AND E > 5
df2[(df2['F']=='x') & (df2['E']>5)]
df2.loc[(df2['F']=='x') & (df2['E']>5)]  # equivalently (again, when is .loc necessary?)

# Break this down: selection using series of booleans
(df2['F']=='x')
(df2['E']>5)           # both series of booleans
(df2['F']=='x') & (df2['E']>5)  #  A series of booleans, True where both arguments are true and false otherwise



# SELECT * FROM df2 WHERE F IN ('x','y')
df2
df2[df2['F'].isin(['x','y'])]

# Breaking this down somewhat
df2['F'].isin(['x','y'])      # series of booleans 





# SELECT * FROM df2 ORDER BY E DESC
df2.sort_values(by='E',axis=0,ascending=False)  # 'axis' determines whether we sort rows or columns.  Here's sorting by rows according to column E

df2[['D','E']].sort_values(by=3,axis=1,ascending=False)  # sorted by columns according to the value in row 3. (not very useful)

df2.sort_values(by='E',axis=0,ascending=False)   # Notice that there's now no neatly ordered index - the existing index is out of order
df2.sort_values(by='E',axis=0,ascending=False).reset_index()  # Now there's a new ordered index, as well as a new 'index' column preserving the old index 


# SELECT SUM(D) FROM df2 GROUP BY F
df2.groupby('F').sum()
df2  # Notice that F has been turned from a column to an index, and the 
df2.groupby('F').sum().reset_index()  # Now there's a new index so F can be a column again


# SELECT SUM(D) FROM df2 WHERE F IN ('x','y') GROUP BY F
df2[df2['F'].isin(['x','y'])].groupby('F').sum()


# SELECT SUM(D) FROM df2 GROUP BY F,E
df2
df2.groupby(['F','E']).sum()
df2.groupby(['F','E']).sum().reset_index()




# Dealing with null values: note that there are two to watch out for, None and np.nan ('NaN')
# A simple dataframe from a dictionary with a None value
d = {'A':[1,2,3],'B':[20,nan,60],'c':['x','y',None]}
d
df = pd.DataFrame(d)
df

# One thing to note: in SQL NULL = NULL has Unknown truth value.  Python behaves differently:
None == None  # True
nan==nan      # False

df.isna() 
df.isnull()    # This seem equivalent, but there may be a difference between isna and isnull

# SELECT ISNULL(B,0) FROM df








