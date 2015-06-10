from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

DATABASES = {
    'USER': "root",
    'NAME': "pinoyskool_recto",
    'PASSWORD': "root",
    'HOST': "localhost",
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%(USER)s:%(PASSWORD)s@localhost/%(NAME)s' % DATABASES


class Studentlog(db.Model):
  __tablename__ = 'student_log'
  id = db.Column(db.Integer, primary_key = True)
  RFID = db.Column(db.String(255))
  IDnumber = db.Column(db.String(255))
  sy_id = db.Column(db.String(10))
  entry_date = db.Column(db.DateTime, nullable=False)
  inam = db.Column(db.DateTime, nullable=False)
  outam = db.Column(db.DateTime, nullable=False)
  inpm = db.Column(db.DateTime, nullable=False)
  outpm = db.Column(db.DateTime, nullable=False)
  STATUS = db.Column(db.Integer)
  late_am = db.Column(db.DateTime, nullable=False)
  late_pm = db.Column(db.DateTime, nullable=False)


@app.route('/studentlog/', methods=['GET'])
def studentlog():
  if request.method == 'GET':
    results = Studentlog.query.limit(10).offset(0).all()

    json_results = []
    for result in results:
      d = {'RFID': result.RFID,
           'IDnumber': result.IDnumber,
           'sy_id': result.sy_id}
      json_results.append(d)

    return jsonify(items=json_results)

if __name__ == '__main__':
  app.run(debug=True)
