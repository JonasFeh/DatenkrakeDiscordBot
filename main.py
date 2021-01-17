import discord
import pandas as pd
import csv

from datetime import date
import sqlite3 as sl
from src.Database.database_setup import database_initial_setup
from src.Database.database_update import insert_message, insert_reaction
from replit import db

#from .src.server_events import *
client = discord.Client()
guild = discord.Guild
# "detect_typees" Detektiert das korrekte Timestampformat
con = sl.connect('data/Database.db', detect_types=sl.PARSE_DECLTYPES)

@client.event
async def on_message(message):
  print(message)
  insert_message(con, message)
  print("Added Message to Database")

@client.event
async def on_reaction_add(reaction, user):
  insert_reaction(con, reaction, user)
  
if __name__ == "__main__":
  
  database_initial_setup(con)
  print('Database is ready')
  print("Bot is ready")
  client.run('')
