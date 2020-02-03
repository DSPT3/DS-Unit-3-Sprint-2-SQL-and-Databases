{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "conn =sqlite3.connect('toy_data.db')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<sqlite3.Connection at 0x15e4d1c4570>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "conn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['.anaconda',\n",
       " '.atom',\n",
       " '.bash_history',\n",
       " '.bash_profile',\n",
       " '.conda',\n",
       " '.condarc',\n",
       " '.continuum',\n",
       " '.docker',\n",
       " '.eclipse',\n",
       " '.gitconfig',\n",
       " '.idlerc',\n",
       " '.ipynb_checkpoints',\n",
       " '.ipython',\n",
       " '.jupyter',\n",
       " '.matplotlib',\n",
       " '.profile',\n",
       " '.PyCharmCE2019.2',\n",
       " '.pylint.d',\n",
       " '.python_history',\n",
       " '.spyder-py3',\n",
       " '.ssh',\n",
       " '.virtualenvs',\n",
       " '.vscode',\n",
       " '3D Objects',\n",
       " 'Anaconda3',\n",
       " 'AppData',\n",
       " 'Application Data',\n",
       " \"Bruno's Lecture OOP.ipynb\",\n",
       " 'Contacts',\n",
       " 'Cookies',\n",
       " 'Desktop',\n",
       " 'Documents',\n",
       " 'Downloads',\n",
       " 'Favorites',\n",
       " 'IntelGraphicsProfiles',\n",
       " 'Links',\n",
       " 'Local Settings',\n",
       " 'MicrosoftEdgeBackups',\n",
       " 'Music',\n",
       " 'My Documents',\n",
       " 'NetHood',\n",
       " 'NTUSER.DAT',\n",
       " 'ntuser.dat.LOG1',\n",
       " 'ntuser.dat.LOG2',\n",
       " 'NTUSER.DAT{c0628bd6-fd19-11e9-8953-b7b074b89daa}.TM.blf',\n",
       " 'NTUSER.DAT{c0628bd6-fd19-11e9-8953-b7b074b89daa}.TMContainer00000000000000000001.regtrans-ms',\n",
       " 'NTUSER.DAT{c0628bd6-fd19-11e9-8953-b7b074b89daa}.TMContainer00000000000000000002.regtrans-ms',\n",
       " 'ntuser.ini',\n",
       " 'OneDrive',\n",
       " 'Pipfile',\n",
       " 'Practice OOP.ipynb',\n",
       " 'PrintHood',\n",
       " 'PycharmProjects',\n",
       " 'Recent',\n",
       " 'regsvr32',\n",
       " 'Rolling Hope Code.ipynb',\n",
       " 'rpg_db.py',\n",
       " 'rpg_db2.py',\n",
       " 'Saved Games',\n",
       " 'Searches',\n",
       " 'SendTo',\n",
       " 'Start Menu',\n",
       " 'Templates',\n",
       " 'toy_data.db',\n",
       " 'Untitled.ipynb',\n",
       " 'Videos',\n",
       " '_netrc']"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "os.listdir()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "query = 'CREATE TABLE toy(name varchar(30), size int);'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['__class__',\n",
       " '__delattr__',\n",
       " '__dir__',\n",
       " '__doc__',\n",
       " '__eq__',\n",
       " '__format__',\n",
       " '__ge__',\n",
       " '__getattribute__',\n",
       " '__gt__',\n",
       " '__hash__',\n",
       " '__init__',\n",
       " '__init_subclass__',\n",
       " '__iter__',\n",
       " '__le__',\n",
       " '__lt__',\n",
       " '__ne__',\n",
       " '__new__',\n",
       " '__next__',\n",
       " '__reduce__',\n",
       " '__reduce_ex__',\n",
       " '__repr__',\n",
       " '__setattr__',\n",
       " '__sizeof__',\n",
       " '__str__',\n",
       " '__subclasshook__',\n",
       " 'arraysize',\n",
       " 'close',\n",
       " 'connection',\n",
       " 'description',\n",
       " 'execute',\n",
       " 'executemany',\n",
       " 'executescript',\n",
       " 'fetchall',\n",
       " 'fetchmany',\n",
       " 'fetchone',\n",
       " 'lastrowid',\n",
       " 'row_factory',\n",
       " 'rowcount',\n",
       " 'setinputsizes',\n",
       " 'setoutputsize']"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "curs = conn.cursor()\n",
    "dir(curs)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x15e4d2101f0>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "curs.execute(query)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "curs.close()\n",
    "conn.commit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "curs2 = conn.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "curs2.execute('SELECT * FROM toy;').fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "insert_query = 'INSERT INTO toy (name, size) VALUES (\"awesome\", 27);'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "curs2.execute(insert_query)\n",
    "curs2.close()\n",
    "conn.commit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('awesome', 27)]"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "curs3 = conn.cursor()\n",
    "curs3.execute('SELECT * from toy;').fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "insert_query_again = 'INSERT INTO toy (name, size) VALUES (\"second row\", 30);'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x15e4d2a41f0>"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "curs3.execute(insert_query_again)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('awesome', 27), ('second row', 30)]"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "curs3.execute ('SELECT * from toy;').fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "curs3.close()\n",
    "conn.commit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
