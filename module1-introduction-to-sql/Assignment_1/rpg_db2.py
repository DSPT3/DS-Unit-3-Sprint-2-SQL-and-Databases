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
print('Total characters:',results[0][0])
# %%
query = '''
SELECT COUNT(*)
FROM charactercreator_cleric; 
'''
results = curs.execute(query).fetchall()
print('Clerics:', results[0][0])

# %%
query = '''
SELECT COUNT(*)
FROM charactercreator_fighter; 
'''
results = curs.execute(query).fetchall()
print('Fighters:', results[0][0])

# %%
query = '''
SELECT COUNT(*)
FROM charactercreator_mage; 
'''
results = curs.execute(query).fetchall()
print('Mages:', results[0][0])

# %%
query = '''
SELECT COUNT(*)
FROM charactercreator_necromancer; 
'''
results = curs.execute(query).fetchall()
print('Necromancers:', results[0][0])

# %%
query = '''
SELECT COUNT(*)
FROM charactercreator_thief; 
'''
results = curs.execute(query).fetchall()
print('Thieves:', results[0][0])

# %%
query = '''
SELECT COUNT(name)
FROM armory_item;
'''
results = curs.execute(query).fetchall()
print('Items:', results[0][0])
# %%
query = '''
SELECT count(item_id)
FROM armory_item
WHERE item_id NOT  IN
(
SELECT item_ptr_id FROM armory_weapon
)
'''
curs.execute(query)
results = curs.fetchall()
print('Non-weapons:', results[0][0])
# %%
query = '''
SELECT COUNT(cc.name)
FROM charactercreator_character AS cc,
armory_item AS ai,
charactercreator_character_inventory AS cci
WHERE cc.character_id = cci.character_id
AND ai.item_id = cci.item_id
GROUP BY cc.character_id
LIMIT 20
'''
curs.execute(query)
results = curs.fetchall()
print('The amt of items for the first 20 players', results)

# %%
