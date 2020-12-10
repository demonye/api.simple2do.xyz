from django.db import models


class TodoTask(models.Model):
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def delete(self):
        self.is_archived = True
        self.save()
