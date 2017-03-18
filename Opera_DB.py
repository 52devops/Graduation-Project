import pymysql
import os
import pickle
class My_DB(object):
    def __init__(self):
        f = open('config.ini','rb')
        data = pickle.load(f)
        f.close()
        mail = data['mail']
        db_user = data['db_user']
        db_add = data['db_add']
        db_pass = data['db_pass']
        self.db = pymysql.connect(db_add,db_user,db_pass,'Gra')
        self.cursor = self.db.cursor()

    def push(self,name,file):
        f = open(file,'rb')
        self.data = f.read()
        f.close()
        command = 'INSERT INTO Pic(name,data) VALUES(%s,%s)'
        args = (name,self.data)
        self.cursor.execute(command,args)
        self.db.commit()
        self.db.close()
    def check(self,command):
        self.cursor.execute(command)
        self.db.close()
        return self.cursor.fetchone()
    def pull(self):
        name = []
        data = []
        command = 'select data from Pic'
        self.cursor.execute(command)
        p_data = self.cursor.fetchall()
        self.cursor.execute('select name from Pic')
        p_name = self.cursor.fetchall()
        for i in p_data:
            data.append(i[0])
        for i in p_name:
            name.append(i[0])
        name_data = dict(zip(name,data))
        path = os.getcwd()
        for i in name_data.keys():
            print(i)
            filname = path + "\\" + "Pic" + "\\" + i
            f = open(filname,'wb')
            f.write(name_data[i])
            print(name_data[i])
            f.close()
        self.db.close()
if __name__ == '__main__':
    test = My_DB()
    # test.push('welcome','welcome.jpg')
    test.pull()

# if __name__ == '__main__':
#     db = pymysql.connect('db_host','db_user','db_pass','db_name')
#     print(db)
#     cursor = db.cursor()
#     cursor.execute("show tables;")
#     data = cursor.fetchall()
#     print(data)
#     db.close()