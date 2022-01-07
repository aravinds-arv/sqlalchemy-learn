from main import User, Session, engine

localSession = Session(bind=engine)

user_to_update = localSession.query(User).filter(User.username=='thor').first()

user_to_update.email = "odinson@test.com"
localSession.commit()
