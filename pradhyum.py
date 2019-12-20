import sqlite3 as lite


# functionality goes here

class DatabaseManager(object):

    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS course(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT, DESCRIPTION TEXT, PRICE TEXT, is_PRIVATE BOOLEAN NOT NULL DEFAULT 1)"
                    )
        except Exception:
            print("Unable to connect DB !..")

    # TODO: insert data     
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO course(NAME, DESCRIPTION, PRICE, is_PRIVATE) VALUES (?,?,?,?)",data)
                return True
        except Exception:
            return False

    # TODO: fetch data    
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT *FROM course")
                return cur.fetchall()
        except Exception:
            False

    # TODO: delete data
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.exexute(sql,[id])
            return True
        except Exception:
            False


# TODO:interface here

def main():
    print("*"*40)
    print("\n :: Course Management ::\n")
    print("*"*40)

    db = DatabaseManager()

    print("#" *40)
    print("\n ::  User Manua  :: \n")
    print("#" * 40)

    print("\nPress 1. Insert a new course\n")
    print("Press 2. Fetch a course\n")
    print("Press 3. delete a course (ID Required)\n")
    print("#" * 40)
    print("\n" )

    choice  = input("Enter your choice")

    if choice == "1":
        name = input("\nEnter a name of the course:")
        description = input("\nEnter their description:")
        price = input("\n Enter their price:")
        private = input("\n is this private or not : (0/1)")

        if db.insert_data([name, description, price, private]):
            print("Course was inserted successfulle")
        else:
            print("opps !... is something missing")

    elif choice == "2":
        print("\n:: Course List ::\n")

        for index , item in enumerate(db.fetch_data()):
            print("\n S.No : " + str(index+1))
            print("\n Course Id : " + str(item[0]))
            print("\n Course Name : " + str(item[1]))
            print("\n Course Description : " + str(item[2]))
            print("\n Course price : " + str(item[3]))

            private ='yes' if item[4] else 'no'
            print("\n Is private : " + private)
            print("\n")
             
    elif choice == "3":
        record_id = input("Enter the course ID")

        if db.delete_data(record_id):
            print("Course was deleted")
        else:
            print("Ooppss something wrong")

    else:
        print("Please select the right choice")


if __name__ == '__main__':
    b=1
    while(b==1):
        main()
        b=int(input())
