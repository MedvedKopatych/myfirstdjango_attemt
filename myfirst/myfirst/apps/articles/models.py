from django.db import models
from django.utils import timezone
import datetime


class Article(models.Model):
    article_title = models.CharField('article title', max_length=200)
    article_text = models.TextField('article text')
    pub_date = models.DateTimeField('date of publication')

# THIS MUST BE IN EVERY MODEL!!!
    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'ARTICLE'
        verbose_name_plural = 'ARTICLES'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('author', max_length=50)
    comment_text = models.CharField('comment text', max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'COMMENT'
        verbose_name_plural = 'COMMENTS'