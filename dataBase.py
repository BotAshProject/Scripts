import flask_app

def add(id_user, id_product):
    db = flask_app.toConnect()
    cursor = db.cursor()
    sql = 'INSERT INTO UserChoose(id_user, id_product) VALUES ({}, {})'.format(id_user, id_product)
    cursor.execute(sql)
    db.commit()
    db.close()

def show(id_user):
    db = flask_app.toConnect()
    cursor = db.cursor()
    sql = 'SELECT * FROM UserChoose WHERE id_user={}'.format(id_user)
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

def delete(id_user):
    db = flask_app.toConnect()
    cursor = db.cursor()
    sql = 'DELETE FROM UserChoose WHERE id_user={}'.format(id_user)
    cursor.execute(sql)
    db.commit()
    db.close()