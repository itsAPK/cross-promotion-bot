from bot.database.models.channel_db import channel


def chunck():
    l=[r.channel_id for r in session.query(Channel).distinct()]
    for i in range(0,len(l),):
        yield l[i:i+Config.CHUNK_SIZE]