from app import db
from app.models.models import Film, Character

def seed_data():
    # Add seed data here
    if not Film.query.first():
        # Add seed data here
        film1 = Film(title='Spirited Away', director='Hayao Miyazaki', description="Chihiro's family is moving to a new house, but when they stop on the way to explore an abandoned village, her parents undergo a mysterious transformation and Chihiro is whisked into a world of fantastic spirits ruled over by the sorceress Yubaba.")
        film2 = Film(title="Howl's Moving Castle", director='Hayao Miyazaki', description="When an unconfident young woman is cursed with an old body by a spiteful witch, her only chance of breaking the spell lies with a self-indulgent yet insecure young wizard and his companions in his legged, walking castle.")

        db.session.add_all([film1, film2])
        db.session.commit()
        print("Successfully seeded Films!")

    if not Character.query.first():
        # Add seed data here
        char1 = Character(name='Chihiro Ogino', description="A gangly, ten-year-old human girl, heroine of the movie. At first Chihiro is sullen, whiny, and afraid, with an annoying voice and sulky face. After her name is changed to Sen, she becomes brave and self-sufficient enough to free herself and her parents from the spirit world.", film_id=1)
        char2 = Character(name='Howl Jenkins', description="Howl Jenkins was born to an ordinary family in modern-day Wales. However, he himself was anything but ordinary. Gifted with a natural talent for magic, he began studying it. Even in college, he wrote his thesis on magical spells and charms, and joined a group of other gifted magicians on Earth.", film_id=2)

        db.session.add_all([char1, char2])
        db.session.commit()
        print("Successfully seeded Characters!")

if __name__ == '__main__':
    seed_data()
