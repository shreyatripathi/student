import web
import MySQLdb as db

urls = (
    '/', 'Index',
    '/add', 'add'
    )

render = web.template.render('templates/')
db = web.database(dbn='mysql', db='db', user='root', pw='root') 

class Index:

    def GET(self):
        students = db.select('student')
        return render.indexstudent(students)

class add:
    def POST(self):
        i = web.input()
        n = db.insert('student', name=i.name)
        raise web.seeother('/')

if __name__ == '__main__':
  app = web.application(urls, globals())
  app.run()
