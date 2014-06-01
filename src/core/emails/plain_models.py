from core.main.base.BasePlainModel import BasePlainModel


class EmailPlainModel(BasePlainModel):
    fields = ['subject', 'body', 'email_to', 'status']


class EmailTemplatePlainModel(BasePlainModel):
    fields = ['title', 'subject', 'body']