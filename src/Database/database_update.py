import datetime

def insert_message(con, message):
  cursor = con.cursor()
  message_id = message.id
  content = message.content
  current_datetime = datetime.datetime.now()
  week_number = current_datetime.isocalendar()[1]
  author_discriminator = message.author.discriminator
  author_name = message.author.name
  data = (message_id, content, current_datetime, week_number, author_discriminator, author_name)
  query = """INSERT INTO MESSAGE (message_id, message_content, message_datetime, week_number, author_discriminator, author_name) VALUES(?, ?, ?, ?, ?, ?);"""
  ls = [type(item) for item in data]
  print(ls)
  print(data)
  cursor.execute(query, data)
  con.commit()


def insert_reaction(con, reaction, user):
  cursor = con.cursor()
  message_id = reaction.message.id
  author_discriminator = user.discriminator
  author_name = user.name
  emoji_id = reaction.emoji[0].id
  current_datetime = datetime.datetime.now()
  week_number = current_datetime.isocalendar()[1]
  data = (message_id, author_discriminator, author_name, emoji_id, current_datetime, week_number)
  print('Inserting new reaction.\n')
  print(data)
  query = """INSERT INTO REACTION (message_id, author_discriminator, author_name, emoji_id, reaction_datetime, week_number) VALUES(?, ?, ?, ?, ?, ?)"""
  cursor.execute(query, data)
  update_emojis(con, reaction.emoji[0])
  con.commit()

def update_emojis(con, emoji):
  cursor = con.cursor()
  emoji_id = emoji.id
  emoji_name = emoji.name
  data = (emoji_id, emoji_name)
  query = """INSERT INTO EMOJIS (emoji_id, emoji_name) VALUES(?, ?)"""
  cursor.execute(query, data)