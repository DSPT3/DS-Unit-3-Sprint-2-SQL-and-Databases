#%%
import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')

# %%
curs = conn.cursor()
query = '''
SELECT COUNT(name) 
FROM charactercreator_character;
'''
results = curs.execute(query).fetchall()
print('\n------------RPG-QUERIES------------')
print('How many total characters are there?')
print(results[0][0])
# %%
curs2 = conn.cursor()
query = '''
SELECT COUNT(*)
FROM charactercreator_mage; 
'''
results = curs2.execute(query).fetchall()
print('How many total mages are there?')
print(results[0][0])

# %%
