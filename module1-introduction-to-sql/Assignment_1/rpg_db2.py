#%%
import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')

# %%
'''How many total characters are there?'''

curs = conn.cursor()
query = '''
SELECT COUNT(name) 
FROM charactercreator_character; '''
curs.execute(query)
curs.execute(query).fetchall()


# %%
