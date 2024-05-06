
from app import db
from app.models.models import Film, Character

def seed_data():
    # Add seed data here
    if not Film.query.first():
        # Create a list of dictionaries representing film data
        film_data_list = [
            {
                'title': 'Spirited Away',
                'director': 'Hayao Miyazaki',
                'description': "Chihiro's family is moving to a new house, but when they stop on the way to explore an abandoned village, her parents undergo a mysterious transformation and Chihiro is whisked into a world of fantastic spirits ruled over by the sorceress Yubaba.",
                'imageURL': 'https://m.media-amazon.com/images/M/MV5BMjlmZmI5MDctNDE2YS00YWE0LWE5ZWItZDBhYWQ0NTcxNWRhXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_FMjpg_UX1000_.jpg'
            },
            {
                'title': "Howl's Moving Castle",
                'director': 'Hayao Miyazaki',
                'description': "When an unconfident young woman is cursed with an old body by a spiteful witch, her only chance of breaking the spell lies with a self-indulgent yet insecure young wizard and his companions in his legged, walking castle.",
                'imageURL': 'https://m.media-amazon.com/images/M/MV5BNmM4YTFmMmItMGE3Yy00MmRkLTlmZGEtMzZlOTQzYjk3MzA2XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg'
            },
            {
                'title': "My Neighbor Totoro",
                'director': "Hayao Miyazaki",
                'description': "When two girls move to the country to be near their ailing mother, they have adventures with the wondrous forest spirits who live nearby.",
                'imageURL': 'https://m.media-amazon.com/images/M/MV5BYzJjMTYyMjQtZDI0My00ZjE2LTkyNGYtOTllNGQxNDMyZjE0XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_FMjpg_UX1000_.jpg'
            },
            {
                'title': "Kiki's Delivery Service",
                'director': "Hayao Miyazaki",
                'description': "A young witch, on her mandatory year of independent life, finds fitting into a new community difficult while she supports herself by running an air courier service.",
                'imageURL': 'https://m.media-amazon.com/images/M/MV5BYTQ1ZTM1ZTgtN2Q2Ny00YjFkLTliNjEtN2I1ZmY5ZTY1OTEzXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_FMjpg_UX1000_.jpg'
            },
            {
                'title': "Castle in the Sky",
                'director': "Hayao Miyazaki",
                'description': "A young boy and a girl with a magic crystal must race against pirates and foreign agents in a search for a legendary floating castle.",
                'imageURL': 'https://m.media-amazon.com/images/M/MV5BNDFhZmY2NTgtMzljYy00MTlhLTgyMjItNTEwZWJkYThhYzkyXkEyXkFqcGdeQXVyNTgyNTA4MjM@._V1_FMjpg_UX1000_.jpg'
            },
            {
                'title': "Ponyo",
                'director': "Hayao Miyazaki",
                'description': "A five-year-old boy develops a relationship with Ponyo, a young goldfish princess who longs to become a human after falling in love with him.",
                'imageURL': 'https://m.media-amazon.com/images/M/MV5BOTc3YmM3N2QtODZkMC00ZDE5LThjMTQtYTljN2Y1YTYwYWJkXkEyXkFqcGdeQXVyODEzNjM5OTQ@._V1_FMjpg_UX1000_.jpg'
            }
        ]

        # Add films to the database
        for film_data in film_data_list:
            film = Film(**film_data)
            db.session.add(film)

        # Commit changes to the database
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
