from django.shortcuts import render
from .models import User, UserProfile
from django.db import connection
from django.db.models import Q




# DATABASE ORM , SQL CODING !!!!!!!!!!!!!!!!
# ACCESS SQLITE EXPLORER .. right click dqsqlite3 .. click open database .. sqlite explorer will aviable for viewing 
# remove the _ at the end of a method to use it


# OVERVIEW 1 ... basic orm sql with django/python


# user sql view basic 
# def users_list(request):
def users_list_(request):    # added _ to halt this method 
    users = User.objects.all()   # variable users bound to all users with there fields 
    # users = User.objects.raw("SELECT * FROM members_user")     # sql way of getting all users with feilds 

    print(users)            # print users variable data into terminal
    print(users.query)      # print the users querys into terminal 
    print(connection.queries)    # sql connections query displayes time as well to load data 
    return render(request, 'registration/users_list.html', {'users': users})    # return html file with data 

# go to http://localhost:7000/members/users_list/ ..SQL info dispayed in template and SQL will be displayed in terminal 








# OVERVIEW 2 ... Simple object relational queries, simple OR query, Q objects - OR query, view query SQL, query performance 


# created another function .. # filtering user by first name ... doing two filter searches at once 
def users_list_(request):
    users = User.objects.filter(first_name__startswith='chetram') | User.objects.filter(first_name__startswith='john')
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})   

# go to http://localhost:7000/members/users_list/   ... will display user information based on first_name .. on template and terminal 





# implemented Q for more advacbed search ... same as previous coding with less code ...  filtering user by first name ... doing two filter searches at once 
def users_list_(request):
    # users = User.objects.filter(Q(first_name__startswith='chetram') | Q(first_name__startswith='john'))
    users = User.objects.filter(~Q(first_name__startswith='chetram') | Q(first_name__startswith='john'))            # addded ~ to Q will halt that specfic Q search
    # users = User.objects.filter(Q(first_name__startswith='john'))                                                 # searching just for john first_name
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})   

# go to http://localhost:7000/members/users_list/   ... will display user information based on first_name .. on template and terminal .. 
# we can keep adding new Q searches

# ...............................................................................................................






#OVERVIEW 3 ... Simple AND queries .. exclude ... simple AND query, Q objects-AND query, view query sql, query performance



# preform an AND query on database
def users_list_(request):
    users = User.objects.filter(city_id=1) & User.objects.filter(state_id=1)                                               
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})   

# go to http://localhost:7000/members/users_list/   ... will display users information based on city_id and state_id .. both feilds must be TRUE
# used & to search two different feilds and once 


# preform an AND query WITH Q on database
def users_list_(request):
    users = User.objects.filter(Q(first_name__startswith='chetram') & Q(last_name__startswith='bassit'))                                              
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})   

# go to http://localhost:7000/members/users_list/   ... will display users information based on specfic fields 
# used & to search two different feilds and once 



# using exclude with & and Q
def users_list_(request):
    users = User.objects.exclude(Q(first_name__startswith='chetram') & Q(last_name__startswith='bassit'))                                              
    # users = User.objects.exclude(city_id=1) & User.objects.filter(first_name__startswith='chetram')                                               
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})   

# go to http://localhost:7000/members/users_list/   ...returns all user but exclude users with the following fields .. 
# used exclude 

# ...........................................................................................








#OVERVIEW 4 ... Simple UNION queries ... Simple UNION query, view query sql, query performance
# usng the User model and the UserProfile model ... using UNION to acces data from both models 

# values_list and using UNION 
def users_list_(request):
    users = User.objects.all().values_list("first_name").union(UserProfile.objects.all().values_list("first_name"))                                                                                      
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})

# gets first name for both User model and UserProfile model ... if firstname is in both models it will only be displayed once
# so it also doesnt display duplicate fistnames 



# values and using UNION     .......   different from values_list .... return in dictionary form "value":"key"
def users_list_(request):
    users = User.objects.all().values("first_name").union(UserProfile.objects.all().values("first_name"))                                                                                      
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users}) 


# ......................................................








#OVERVIEW 5 ... Simple NOT queries ... Simple NOT query, view query sql, query performance

# NOT Eexample in SQL lanuage 
# SELECT * FROM Users WHERE NOT first_name = chetram

# NOT Eexample in ORM lanuage 
# exclude()
# filter(~Q)


# using exclude 
def users_list_(request):
    users = User.objects.exclude(first_name__startswith='chetram')                                                                                      
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users}) 



# using exclude with & .. excluding based on 2 parameters
def users_list_(request):
    users = User.objects.exclude(first_name__startswith='chetram') & User.objects.exclude(last_name__startswith='doe')                                                                              
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users}) 



# using parameters inside exclude ... WE DO NOT HAVE AN AGE FEILD USING AS AN EXMPLE CODING CANNOT EXECUTE UNTIL ADDING AGE FIELD TO MODELS
def users_list_(request):
    users = User.objects.exclude(age__gt=19)                                                                              
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users}) 

    # gt       GREATER THAN
    # gte      GREATER THAN OR EQUAL TO 
    # lt       LESS NOT 
    # lte      LESS THEN OR EQUAL TO 
# this func will return all user queryes excluding those greater than age 19



# using exclude wth Q and parameters
def users_list_(request):
    users = User.objects.exclude(~Q(age__gt=19))                                                                              
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users}) 
# this func will return all user queryes excluding those greater than age 19



# using exclude wth Q and parameters and & 
def users_list_(request):
    users = User.objects.exclude(~Q(age__gt=19)&~Q(first_name__Startswith='chetram'))                                                                              
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users}) 
# exclusing queries based on two feilds 

# .....................................................................









# OVERVIEW 6 ... Simple field selection and output ... selecting indiviusal database fields .. outputting to template


# using ONLY
def users_list_(request):
    users = User.objects.filter(city_id=1).only('first_name')                                                                  
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})
    
# get user based on city and return users firstname 

# ......................................................................................








# OVERVIEW 7 .. performing RAW queries with SQL
# raw method takes a raw SQL query and executes them 



def users_list_(request):
    sql = "SELECT * FROM members_user"
    users = User.objects.raw(sql)            # select everything from members app, user model                                                       
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})
# will display all queries from that table members_user 



# elect everything from members app, user model, where the last name is doe 
def users_list_(request):
    users = User.objects.raw("SELECT * FROM members_user WHERE last_name='doe'")                                                          
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})
# displays all data if last name is doe 



# returning a for loop with RAW ..  on demand  
def users_list_(request):
    users = User.objects.all()
    for u in User.objects.raw("SELECT * FROM members_user"):
        print(u)

    # print(users)            
    # print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})
# .................................................








# OVERVIEW 8 ... Performing CUSTOM SQL directly .. 

# using connection with cursor anf fetch one allows us to access the database and use SQL to get data 
def users_list_(request):
    cursor = connection.cursor()
    cursor.execute("SELECT count(*) FROM members_user")
    users = cursor.fetchone()
    print(users)
    print(connection.queries)

    return render(request, 'registration/users_list.html', {'users': users})

# this functions returns the number .. count .. of total users



# using connection with cursor and fetch all allows us to access the database and use SQL to get data 
def users_list_(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM members_user")
    users = cursor.fetchall()
    print(users)
    print(connection.queries)

    return render(request, 'registration/users_list.html', {'users': users})
# data returned differently then fatchone 





# creating a function to return queries as a dictionary 
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def users_list(request):
    cursor = connection.cursor()
    # cursor.execute("SELECT * FROM members_user")
    cursor.execute("SELECT * FROM members_user WHERE last_name='doe'")
    users = dictfetchall(cursor)
    print(users)
    print(connection.queries)

    return render(request, 'registration/users_list.html', {'users': users})
# change cursor.execute() to which ever querying we want to do 
# ..............................................................
