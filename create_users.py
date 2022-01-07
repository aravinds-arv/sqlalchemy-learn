from main import User, Session, engine

localSession = Session(bind=engine)

users = [
    {
        'username':'rogers',
        'email':'rogers@test.com'
    },
    {
        'username':'stark',
        'email':'stark@test.com'
    },
    {
        'username':'banner',
        'email':'banner@test.com'
    },
    {
        'username':'thor',
        'email':'thor@test.com'
    },
    {
        'username':'romanoff',
        'email':'romanoff@test.com'
    },
    {
        'username':'clint',
        'email':'clint@test.com'
    },
    {
        'username':'wayne',
        'email':'vengeance@test.com'
    }
]

for user in users:
    new_user = User(username=user['username'], email=user['email'])
    localSession.add(new_user)
    localSession.commit()
