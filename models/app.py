from database import Database
from menu import Menu
from models.blog import Blog

# Need to initialize DB in order to map URL and database
Database.initialize()
##################### Lesson 49 Running aplication
menu = Menu()
menu.run_menu()

##################### Up to the lesson 48
# blog=Blog(author="Olek",
#           title="Sample title",
#           description="Sample description")
# blog.new_post()
#
# blog.save_to_mongo()
#
# from_database = Blog.from_mongo(blog.id)
#
# print(blog.get_posts())
#
#####################
# posts=Post.from_blog("123")
# for post in posts:
#     print(post)
#####################
# post = Post.from_mongo('76d69b025b3541cf8b80dc2118b1cf67')
# print(post)
#####################
# post = Post(blog_id="123",
#             title="Another great post",
#             content="This is some simple content",
#             author="Jose")
# post.save_to_mongo()
# __author__ = "oleksandr"
#
# # This is the part of Code for lec36 MONGO D
# import pymongo
# import sys
#
# uri = "mongodb://127.0.0.1:27017"
# client = pymongo.MongoClient(uri)
# database = client['fullstack']
# collection = database['students']
# collection.remove({"name": "Julio"})
# ###########################################
# # students =collection.find({})
# # for student in students:
# #    print(student)
# ###########################################
# # LIST COMPREHENSION
# students = collection.find({}) #<<< cursor object
# student_list= []              #<<< list object
# for student in students :
#     student_list.append(student)
# Elegant  way:
#
# students = [student['mark'] for student in collection.find({}) if student['mark'] == 99]
#
# print(students)

# post = Post()
# post2 = Post()
# print(post.content)
# print(post2.content)
# # The output
# # This is some content
# # This is some content
# post2.content = "Some different content"
# print(post2.content)
#
# # The output
# # This is some content
# # This is some content
# # Some different content
# post = Post("post1 title", "post1 author", "post1 content")
# post2 = Post("post2 title", "post2 author", "post2 content")
# print(post2.content)
