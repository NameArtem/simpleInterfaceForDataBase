#-*- coding:utf-8 -*-
###########################################################
####	This is specially file for connect to DB 	####
############################################################

import psycopg2

# connect to DB
global dbname, user, pssw, dbTypes, bigTableList
bigTableList = list()
dbTypes = {1:'VARCHAR',2:'INTEGER',3:'TEXT',4:'BIGINT',5:'DATE', 6:'MONEY',7:'BOOLEAN'}

class workWithDB():

    #connect to DB
    def connectTo(self):
        global dbname, user, pssw
        #data for connect
        self.connectType = int(raw_input('Choose 1 for connect to DB without host/post\nChoose 2 for connect to DB with host/port\n:'))
        #connect withou host/post
        if self.connectType == 1:
            self.dbname = raw_input('Enter database name: ')
            self.user = raw_input('Enter username: ')
            self.pssw = raw_input('Enter password: ')
            #create connect string
            self.connect_string = "dbname='{0}' user='{1}' password='{2}'".format(self.dbname, self.user, self.pssw)
            #connecting
        #connect with host/port (future when program will become networked)
        #if self.connectType == 2:
            #self.dbname = raw_input('Enter database name: ')
            #self.user = raw_input('Enter username: ')
            #self.pssw = raw_input('Enter password: ')
            #self.host =
            #self.post =
            # create connect string
        self.conn = psycopg2.connect(self.connect_string)
        self.cur = self.conn.cursor()

    #show all tables with column
    def showMe(self):
        #show all column into a table
        self.cur.execute('''SELECT table_name, column_name
                          FROM information_schema.columns
                          WHERE table_schema=\'public\'''')
        self.cols = self.cur.fetchall()

    #If user is needed in new data base type (only for current session)
    def newType(self):
        global dbTypes


    #creat New table in the DB
    def creatTable(self):
        global dbTypes
        #value for creating
        self.newTableName = raw_input("Enter new table name: ")
        self.columns = int(raw_input("Now enter, how many columns will be there: "))
        self.namesList = ()
        self.choice = ''
        self.steps = 0
        while self.choice != 'n':
            self.steps += 1
            print "Now exist next types for DB, do you need else?"
            self.dictLen = 0
            for i in dbTypes:
                self.dictLen += 1
                print dbTypes[i]
            self.choice = raw_input('Enter (Y)es or (N)o: ').strip().lower()
            if self.choice =='y' and self.steps != self.columns:   #creat new type
                self.dictValue = raw_input('Enter new type for DataBase: ').upper()
                dbTypes.update([(self.dictLen+1, self.dictValue)])  #update new type in the dict
            else:
                break
        ######Дописать создание....


    #show datas in table
    def showTable(self):
        global bigTableList
        while True:
            #start menu
            try:
                self.tableName = raw_input('''
                Enter table name, you chose one from list
                => {0}: '''.format(', '.join(bigTableList)))
                self.selects = int(raw_input('How many selects do you need from table {0}: '.format(self.tableName)))
                self.selectsNames = ''
                count = 0   #for counting steps
                #create string of selects
                for select in range(self.selects):
                    count += 1
                    select = raw_input('Enter name: ')
                    self.selectsNames = self.selectsNames + select
                    if self.selects > 1 and count != self.selects:
                        self.selectsNames = self.selectsNames+','
                #create SQL
                self.cur.execute("SELECT {0} FROM {1}".format(self.selectsNames, self.tableName))
                self.rows = self.cur.fetchall()
                # showing
                print '|---Show DB under line---|'
                for row in self.rows:
                    print row
                print '|---Stop showing DB---|'
                self.sss = raw_input()
                answer = raw_input('Show another table? (Y)es or (N)o: ').strip().lower()
                if answer == 'n':
                    break
            except ValueError:  #if value doesn't exitst
                answer = raw_input('Sorry. Your choice is wrong. Show another table? (Y)es or (N)o: ').strip().lower()
                if answer == 'n':
                    break

    #this function to INSERT something in table
    def insertValue(self):
        global bigTableList
        while True:
            try:
                self.tableName = raw_input('''
                Enter table name, where you want to INSERT. Exist tables in list
                => {0}: '''.format(', '.join(bigTableList)))
                inserts = raw_input("What insert parameter: ")
                rows = list()
                count = int(raw_input('How main rows for inserting you need: '))
                steps = 0
                while steps != count:
                    row = raw_input('Enter name of row: ')
                    rows.append(row)
                    print ('Have got it!')
                cur.execute("INSERT INTO {0}({1}) VALUES ({2})".format (self.tableName,', '.join(rows), inserts,))
                conn.commit()
                #доделать
            except:
                print ('Ops, something happens')










    #close DB
    def closeBD(self):
        self.cur.close()
        self.conn.close()


#    try:
#    except:
#        print("DataBase doesn't available")
#
#    while True:
#        try:
#            cur = conn.cursor()
#            print("1 - Insert in database \n2 - Delete \n3 - Show table \n4 - Find in database")
#            choice = input("What a choice: ")
#            if choice == 1:  # Insert to DB
#                # inserts = raw_input("What insert parameter: ")
#                # print("Your parametr: ", inserts)
#               cur.execute("INSERT INTO main_data(main_data) VALUES (%s)", (inserts,))
#                conn.commit()
#                cur.close()
#            if choice == 2:  # Delete
#                delete = raw_input("What do a delete: ")
#                cur.execute("DELETE FROM main_data WHERE main_data=%s;", (delete,))
#                conn.commit()
#                print "Delete - ", delete
#            if choice == 3:  # Show DB
#                cur.execute("SELECT id,main_data FROM main_data")
#                rows = cur.fetchall()
#                print '_____________________Show DB under line__________________________'
#                for row in rows:
#                    print row[0], '=>', row[1]
#                    print '_____________________Stop showing DB_____________________________'
#                cur.close()
#            if choice == 4:  # Find
#                find = raw_input("What a find: ")
#                cur.execute("SELECT id, main_data FROM main_data")
#                rows = cur.fetchall()
#                for row in rows:
#                    row[0], row[1]
#                if row[1] == find:
#                    print "Exist in database: id - ", row[0], ", found parametr - ", row[1]
#
#        except EOFError:
#            print "\nGood lack!"
#            break
#        print('Welcom to database...')




#######mothod for connection well. It's better way
#try:
#    cursor.execute(sql_statement)
#    result = cursor.fetchall()
#except sqlite3.DatabaseError as err:
#    print("Error: ", err)
#else:
#    conn.commit()





if __name__ == '__main__':
    s = workWithDB()
    try:
        s.connectTo()
        print "Welcome to you DB", s.dbname
        while True:
            #get all tables in DB
            # pretty showing
            s.showMe()
            print "Exist such table and columns in DB ", s.dbname
            ##############################################################
            ###Creating beautiful table###################################
            ##############################################################
            c1 = 0
            c2 = 0
            #make int from lenght of col[number]
            for col in s.cols:
                if c1 < len(col[0]):
                    c1 = len(col[0])
                    c1_midle = len(col[0])/2
                if c2 < len(col[1]):
                    c2 = len(col[1])
                    c2_midle = len(col[1]) / 2
            #create table
            main_line_start = '|---'
            main_line_mid = '---|---'
            main_line_end = '---|'
            line = '-'
            table = 'TABLE'
            columns_from = 'COLUMNS'
            count = 0
            main_line = main_line_start
            finish_line = main_line_start
            for i in range(c1 - len(table)):
                count = count + 1
                if count == (c1 - len(table))/2:
                    main_line = main_line+table
                if count == c1 - len(table):
                    main_line = main_line+main_line_mid
                else:
                    main_line = main_line+line
            count = 0
            for i in range(c2 - len(columns_from)):
                count = count + 1
                if count == (c2 - len(columns_from)) / 2:
                    main_line = main_line + columns_from
                if count == c2 - len(columns_from):
                    main_line = main_line + main_line_end
                else:
                    main_line = main_line + line
            count = 0
            for i in range(c1+c2+5):
                count = count + 1
                finish_line = finish_line+line
                if count == (c1+c2+5):
                    finish_line = finish_line + main_line_end

            #show the first line
            print main_line
            #other lines
            count_cols = len(s.cols)
            other_line = main_line_start
            for col in s.cols:
                #### Вот из-за этой штуки нет данныйх во втором столбце (+ change_message),
                # а в первой из-за auth_user_user_permissions
                if 'content_type_id' not in col:
                    if 'change_message' not in col:
                        if 'auth_user_user_permissions' not in col:
                            other_line = main_line_start
                            count = 0
                            #collect list of tables name
                            if col[0] not in bigTableList:
                                bigTableList.append(col[0])
                            #####

                            for j in range(c1 - len(col[0])):
                                count = count + 1
                                if count == (c1 - len(col[0])) / 2:
                                    other_line = other_line + col[0]
                                if count == c1 - len(col[0]):
                                    other_line = other_line + main_line_mid
                                else:
                                    other_line = other_line + line
                            count = 0
                            for j in range(c2 - len(col[1])):
                                #print type(col[1])
                                if col[1]:
                                    count = count + 1
                                    if count == (c2 - len(col[1])) / 2:
                                        other_line = other_line + col[1]
                                    if count == c2 - len(col[1]):
                                        other_line = other_line + main_line_end
                                    else:
                                        other_line = other_line + line
                #print col
                print other_line
            print finish_line
            #####################################################
            ###Done creating the beautiful table#################
            #####################################################

            print "\n\n\nUse the first letter in brackets + ENTER for control this DB_Client"
            #manu
            menuChoice = raw_input('''
            Enter what do you want to do with you DataBase {0}:
            (C)REATE new table in DataBase {0},
            (I)NSERT in DataBase {0},
            (D)ELETE somethink from DataBase {0},
            (S)HOW value from table,

            Enter your choice: '''.format(s.dbname)).strip().lower()
           #choices
            if menuChoice == 'c':
                s.creatTable()

            if menuChoice == 'i':
                s.insertValue()

            if menuChoice == 'd':
                break

            if menuChoice == 's':
                s.showTable()

        s.closeBD()








    except KeyboardInterrupt:
        'Connection is stopped'
    except psycopg2.DatabaseError as err:
        print "Such error: ",err









#########################################################################
###############################		HELP	#########################
# create DB
# cur.execute("CREATE TABLE name (id PRIMARY KEY, etc);")

# Same connection to DB without variables
# conn =psycopg2.connect(dbname='', user='', password=''


# insert
# cur.execute("INSERT INTO name (data1, etc) VALUES (%s,%s)" % (var1,var2))

# select
# cur.execute("SELECT * FROM db_mane;")
# cur.fetchall()   - if use all parameters
# or
# cur.fetchone()	  - if use one parameter

# update
# cur.execute("UPDATE db_name SET nam=new_value WHERE id=number")

# delete
# cur.execute("DELETE FROM db_name WHERE id=number;")

# make the changes
# conn.commit()

# count rows
# cur.rowcount()

# close DB
# cur.close()
# conn.close()



























