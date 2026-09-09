import mysql.connector
from datetime import datetime
class DbConnect:

    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Amrithasuku@123",
                database="gym_db"
            )
            return self.connection
        except Exception as e:
            return  None

class GymMemberManager(DbConnect):

    def get(self):
       try:
           self.connect = super().get_connection()
           self.cursor = self.connect.cursor()
           query = "select * from member"
           self.cursor.execute(query)
           records = self.cursor.fetchall()
           print(records)
       except Exception as e:
           print(e)

    def get_object(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from member where id = %s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None
    def post(self,**kwargs):
        self.connect = super().get_connection()
        self.cursor = self.connect.cursor()
        query = """insert into member(name,place,mobile,plan,fee,joined_on)
        values(%s ,%s,%s,%s,%s,%s)"""
        values= [v for v in kwargs.values()]
        self.cursor.execute(query,values)
        self.connect.commit()
        print("New member added successfully")

    def retrieve(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM member WHERE id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            if record == None:
                print("Member not found!")
            else:
                print(record)
        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            self.connect = self.get_connection()
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM member WHERE id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            if record != None:
                query = "DELETE FROM member WHERE id=%s"
                self.cursor.execute(query, values)
                self.connection.commit()
                print("member deleted Successfully...!")
            else:
                print("member not found")
        except Exception as e:
            print(e)




connection_instance = DbConnect()
print(connection_instance.get_connection())

member_instance = GymMemberManager()
# member_instance.get()
# member_instance.post(name="Ammu",place="kottayam",mobile=9876543211,plan="2 months",
#                      fee=4000,joined_on=datetime.datetime.today())
member_instance.retrieve(id=1)
member_instance.delete(id=2)