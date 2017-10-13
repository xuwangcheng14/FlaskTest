from hello import db
from hello import User, Role


# admin_role = Role(name='Admin')
# mod_role = Role(name='ModTom')
user_role = Role.query.filter_by(name='User').first()
# user_jerry = User(username='Jerry', role=admin_role)
# user_lili = User(username='Lili', role=user_role)
# user_lilei = User(username='LiLei', role=user_role)
#
#
# db.session.add_all([admin_role, mod_role, user_role, user_jerry, user_lili, user_lilei])
# db.session.commit()
# print user_lilei.id


print Role.query.all()
print User.query.all()
print User.query.filter_by(role=user_role).all()


print str(Role.query)


print user_role.users.order_by(User.username).all()
print user_role.users.count()