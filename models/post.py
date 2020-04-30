import uuid
from database import Database
import datetime

__author__ = "oleksandr"


class Post(object):
    # def __init__(self):
    #     self.title = "This is my title"
    #     self.content = "This is some content"
    #     self.author = "Oleksandr"

    # def __init__(self, title, author, content):
    #     self.title = title
    #     self.author = author
    #     self.created_date = date
    #     self.content = content

    def __init__(self, blog_id, title, author, content, date=datetime.datetime.utcnow(), id=None):
        # we initiate ID to default parameters
        # default parameters have to be at the end otherwise error
        self.blog_id = blog_id
        self.title = title
        self.author = author
        self.content = content
        self.created_date = date
        # self.id = id
        # module that create unic ID
        self.id = uuid.uuid4().hex if id is None else id
        # uuid - is the modul creating ID
        # uuid4  - is method

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())
        pass

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    ### Allow to get specific post from mono DB
    #### When we using oject 'cls' allows to access easily without doing multiple queries
    @classmethod                                                            #@staticmethod >> replaced by @classmethod
    def from_mongo(cls, id):                                                  # added 'cls' to arguments
        # data = Database.find_one(collection = 'posts',query = {'id' : id})
        post_data = Database.find_one(collection='posts', query={'id': id}) #changed 'return' to 'post_data'
        return cls(blog_id = post_data['blog_id'],                          #added return
                   title=post_data['title'],
                   author = post_data['author'],
                   content = post_data['content'],
                   date = post_data['created_date'],
                   id = post_data['id'])

    ### Alow to retrive all posts from specific blog
    @staticmethod
    def from_blog(id):  # for loop used since cursor is returned  by Database.find
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]
