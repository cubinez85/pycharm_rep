from app import app, db
from app.models import User, Post
import sqlalchemy as sa

app.app_context().push()

u = User(username='cubinez85', email='cubinez85@mail.ru')
u.set_password('123')
db.session.add(u)
db.session.commit()

# u = User(username='susan', email='susan@example.com')
# db.session.add(u)
# db.session.commit()

# query = sa.select(User)
# users = db.session.scalars(query).all()
# print(users)

# query = sa.select(User)
# users = db.session.scalars(query)
# for u in users:
#     print(u.id, u.username)


# u = db.session.get(User, 1)
# print(u)

# u = db.session.get(User, 1)
# p = Post(body='my second post!', author=u)
# db.session.add(p)
# db.session.commit()

# u = db.session.get(User, 1)
# query = u.posts.select()
# posts = db.session.scalars(query).all()
# print(posts)

# u = db.session.get(User, 2)
# query = u.posts.select()
# posts = db.session.scalars(query).all()
# print(posts)

# query = sa.select(Post)
# posts = db.session.scalars(query)
# for p in posts:
#     print(p.id, p.author.username, p.body)

# query = sa.select(User).order_by(User.username.desc())
# print(db.session.scalars(query).all())

# query = sa.select(User).where(User.username.like('c%'))
# print(db.session.scalars(query).all())



