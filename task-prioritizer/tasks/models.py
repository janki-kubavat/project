from django.db import models

class Task(models.Model):
    id_text = models.CharField(max_length=128, unique=True)  # store original id
    title = models.CharField(max_length=300)
    due_date = models.DateField(null=True, blank=True)
    estimated_hours = models.FloatField(null=True, blank=True, default=1.0)
    importance = models.IntegerField(default=5)
    dependencies = models.JSONField(default=list, blank=True)  # store list of ids
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_dict(self):
        return {
            "id": self.id_text,
            "title": self.title,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "estimated_hours": self.estimated_hours,
            "importance": self.importance,
            "dependencies": self.dependencies,
        }

    def __str__(self):
        return f"{self.id_text} - {self.title}"
