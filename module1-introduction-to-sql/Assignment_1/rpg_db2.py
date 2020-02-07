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
query = '''
SELECT COUNT(*)
FROM charactercreator_cleric; 
'''
results = curs.execute(query).fetchall()
print('How many clerics are there?')
print(results[0][0])

# %%
query = '''
SELECT COUNT(*)
FROM charactercreator_fighter; 
'''
results = curs.execute(query).fetchall()
print('How many fighters are there?')
print(results[0][0])

# %%
query = '''
SELECT COUNT(*)
FROM charactercreator_mage; 
'''
results = curs.execute(query).fetchall()
print('How many mages are there?')
print(results[0][0])

# %%
query = '''
SELECT COUNT(*)
FROM charactercreator_necromancer; 
'''
results = curs.execute(query).fetchall()
print('How many necromancers are there?')
print(results[0][0])

# %%
query = '''
SELECT COUNT(*)
FROM charactercreator_thief; 
'''
results = curs.execute(query).fetchall()
print('How many thieves are there?')
print(results[0][0])

# %%
query = '''
SELECT COUNT(name)
FROM armory_item;
'''
results = curs.execute(query).fetchall()
print('How many items are there?')
print(results[0][0])

# %%
query = '''SELECT count(item_id)
FROM armory_item
WHERE item_id NOT  IN
(
SELECT item_ptr_id FROM armory_weapon
)'''
curs.execute(query)
results = curs.fetchall()
print('Non-weapons:', results[0][0])
# %%
