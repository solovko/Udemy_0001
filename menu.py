##
from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        self.user = input("Enter your authors name:")
        self.user_blog = None
        if self._user_has_account():
            # undersore convention means that
            # it is private method to be used withing
            # the class
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            # self.user_blog = blog Instead we create object Blog
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Do you want to red (R) or  write (W) blogs?")
        if read_or_write == 'R':
            self.list_blogs()
            self.view_blog()
            # allow user to pick one
            # display posts
            pass
        elif read_or_write == 'W':
            # self._prompt_write_post()
            # Not necessery method instead:
            self.user_blog.new_post()
            pass
        else:
            print("Thank you for blogging!")

    # def _prompt_write_post(self):#<<Not necessary method
    #     self.user_blog.new_post()
    def list_blogs(self):
        blogs = Database.find(collection='blogs',
                              query={})
        for blog in blogs:
            print("ID; {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))
    def view_blog(self):
        blog_to_see = input("Enter the ID of blog you'd like to read:")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, title: {}\n\n{}".format(post['created_date'], post['title'], post['content']))
