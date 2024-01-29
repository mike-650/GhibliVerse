from app import db
from app.models import Film, Character

def seed_data():
    # Add seed data here
    if not Film.query.first():
        # Add seed data here
        film1 = Film(title='Spirited Away', director='Hayao Miyazaki', description="Chihiro's family is moving to a new house, but when they stop on the way to explore an abandoned village, her parents undergo a mysterious transformation and Chihiro is whisked into a world of fantastic spirits ruled over by the sorceress Yubaba.")
        film2 = Film(title="Howl's Moving Castle", director='Hayao Miyazaki', description="When an unconfident young woman is cursed with an old body by a spiteful witch, her only chance of breaking the spell lies with a self-indulgent yet insecure young wizard and his companions in his legged, walking castle.")

        db.session.add_all([film1, film2])
        db.session.commit()

if __name__ == '__main__':
    seed_data()
