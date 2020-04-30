import uuid
import datetime

from database import Database
from models.post import Post


class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date = input("Enter post date, or leave blank for today: (In format DD MM YY)")
        # we specify format in order to be able to parse
        if date=="":
            date=datetime.datetime.utcnow()
        #     we need 'else' statement since date variable will try to pars user input
        #     strirng, when utc.now is not a string
        else:
            date=datetime.datetime.strptime(date, "%d%m%Y") # this string was moved from date variable 4 lines below
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=date)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self) -> object:
        Database.insert(collection='blogs',
                        data=self.jason())

    def jason(self):
        return {'author': self.author,
                'title': self.title,
                'description': self.description,
                'id': self.id
                }


    #@staticmethod
    # to simplify  substentially we can use @classmethod
    #in front of id argugment  we add cls, and we replace Blog by cls
    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection="blogs",
                                      query={'id': id}
                                      )
        # do not use self.id since we do not have access
        # instead we use static method
        return cls(author=blog_data['author'], #<< was Blog changed to cls
                    title=blog_data['title'],
                    description=blog_data['description'],
                    id=blog_data['id'])
