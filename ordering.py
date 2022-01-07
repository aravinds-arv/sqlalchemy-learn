from main import User, Session, engine
from sqlalchemy import desc

localSession = Session(bind=engine)

# ascending order
users_asc = localSession.query(User).order_by(User.username).all()

# descending order
users_desc = localSession.query(User).order_by(desc(User.username)).all()

for user in users_asc:
    print(f'User {user.username}')

for user in users_desc:
    print(f'User {user.username}')
