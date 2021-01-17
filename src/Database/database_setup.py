def database_initial_setup(con):
  with con:
      con.execute("""
          CREATE TABLE IF NOT EXISTS MESSAGE (
              message_id INTEGER NOT NULL PRIMARY KEY,
              message_content TEXT,
              message_datetime TIMESTAMP,
              week_number INTEGER,
              author_discriminator TEXT,
              author_name TEXT
          );
      """)

      con.execute("""
          CREATE TABLE IF NOT EXISTS REACTIONS (
              message_id INTEGER NOT NULL,
              author_discriminator TEXT NOT NULL,
              author_name TEXT,
              emoji_id INTEGER NOT NULL,
              reaction_datetime TIMESTAMP,
              week_number INTEGER,
              PRIMARY KEY (message_id, author_discriminator, author_name, emoji_id)
          );
      """)

      con.execute("""
          CREATE TABLE IF NOT EXISTS EMOJIS (
              emoji_id INTEGER NOT NULL PRIMARY KEY,
              emoji_name TEXT
          );
      """)
