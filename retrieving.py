from main import User, Session, engine

local_session = Session(bind=engine)

# to fetch all entries
users = local_session.query(User).all()

for user in users:
    print(user.username)

# limiting results to 3
users = local_session.query(User).all()[:3]

for user in users:
    print(user.username)

# fetching the first result
user = local_session.query(User).first()
print(user)

# filtering and fetching the first matching result
hawkeye = local_session.query(User).filter(User.username=='clint').first()
print(hawkeye)
