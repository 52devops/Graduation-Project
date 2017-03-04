import pymysql

class My_DB(object):
    def __init__(self,db_address,db_user,db_passwd,db_name,parent=None):
        self.db = pymysql.connect(db_address,db_user,db_passwd,db_name)
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
    def pull(self):
        pass

if __name__ == '__main__':
    test = My_DB('wangyaohua.cn','wangyaohua','WanG68313157','Gra')
    test.push('welcome','welcome.jpg')


# if __name__ == '__main__':
#     db = pymysql.connect('db_host','db_user','db_pass','db_name')
#     print(db)
#     cursor = db.cursor()
#     cursor.execute("show tables;")
#     data = cursor.fetchall()
#     print(data)
#     db.close()