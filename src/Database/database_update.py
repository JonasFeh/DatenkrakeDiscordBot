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
  current_datetime = datetime.datetime.now()
  week_number = current_datetime.isocalendar()[1]
  if reaction.custom_emoji:
    emoji_id = reaction.emoji.id
    data = (message_id, author_discriminator, author_name, emoji_id, current_datetime, week_number)
    print('Inserting new reaction.\n')
    #print(data)
    query = """INSERT INTO REACTION_CUSTOM (message_id, author_discriminator, author_name, emoji_id, reaction_datetime, week_number) VALUES(?, ?, ?, ?, ?, ?)"""
  else:
    emoji_name = reaction.emoji
    data = (message_id, author_discriminator, author_name, emoji_name, current_datetime, week_number)
    print('Inserting new reaction.\n')
    #print(data)
    query = """INSERT INTO REACTION_LEGACY (message_id, author_discriminator, author_name, emoji_name, reaction_datetime, week_number) VALUES(?, ?, ?, ?, ?, ?)"""
  update_emojis(con, reaction.emoji, reaction.custom_emoji)
  cursor.execute(query, data)
  con.commit()

def update_emojis(con, emoji, is_custom):
  cursor = con.cursor()
  if is_custom:
    emoji_id = str(emoji.id)
    emoji_name = emoji.name
    data = (emoji_id, emoji_name)
    query = """INSERT INTO EMOJIS (emoji_id, emoji_name) VALUES(?, ?)"""
    cursor.execute(query, data)
  else:
    print(type(emoji))
    print(str(emoji))
    emoji_id = emoji
    query = """INSERT INTO EMOJIS (emoji_id) VALUES(?)"""
    cursor.execute(query, emoji_id)