from .models import BlogPost

class BlogPostDBRouter:
    def db_for_read(self,model,**hints):
        if(model==BlogPost):
            return 'posts'
        return None

    def db_for_write(self,model,**hints):
        if(model==BlogPost):
            return 'posts'
        return None