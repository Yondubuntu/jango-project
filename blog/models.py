from typing import ContextManager
from django.db import models
from django.db.models.fields.json import ContainedBy

class Post (models.Model): 
    title = models.CharField(max_length=30)
    content = models.TextField

    created_at = models.DateField()
    updated_at = models.DateField(auto_now = True)
    
def __str__(self): 
    return f'[{self.pk}]{self.title}'

# author = 정두용 
