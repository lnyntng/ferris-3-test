from google.appengine.ext import ndb, db
from ferris3 import Model, Service, hvild, auto_service
import ferris3 as f3
from pprint import pprint


class Post(Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty()


PostMessage = f3.model_message(Post)


@auto_service
class PostsService(Service):
    list = hvild.list(Post)
    paginated_list = hvild.paginated_list(Post, limit=3)
    get = hvild.get(Post)
    delete = hvild.delete(Post)
    insert = hvild.insert(Post)
    update = hvild.update(Post)

    @f3.auto_method(returns=PostMessage, name="get_by_title")
    def get_by_title(self, request, title=(str,)):
        query = Post.query(Post.title == title)
        post = query.get()
        pprint(post.key.kind())
        if not post:
            raise f3.NotFoundException()
        if not post.key.kind() == 'Post':
            raise f3.InvalidRequestException()
        message = f3.messages.serialize(PostMessage, post)
        pprint(4)
        return message
