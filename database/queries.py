from .models import SessionLocal, Song, Phrase

def get_songs():
    db = SessionLocal()
    songs = db.query(Song).all()
    db.close()
    return songs

def add_song(url, name, band):
    db = SessionLocal()
    song = Song(url=url, name=name, band=band)
    db.add(song)
    db.commit()
    db.close()

def get_phrases():
    db = SessionLocal()
    phrases = db.query(Phrase).all()
    db.close()
    return phrases

def add_phrase(text):
    db = SessionLocal()
    phrase = Phrase(text=text)
    db.add(phrase)
    db.commit()
    db.close()
