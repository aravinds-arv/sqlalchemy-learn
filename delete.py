from main import User, Session, engine

localSession = Session(bind=engine)

user_to_delete = localSession.query(User).filter(User.username=='wayne').first()

localSession.delete(user_to_delete)
localSession.commit()
