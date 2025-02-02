from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question_en = models.TextField()
    answer_en = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def get_question(self, lang='en'):
        return getattr(self, f'question_{lang}', self.question_en)

    def get_answer(self, lang='en'):
        return getattr(self, f'answer_{lang}', self.answer_en)
