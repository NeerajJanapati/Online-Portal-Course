"""
Course Models - Online Course Portal
Database models for managing courses and related data
"""

from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    """
    Course model representing an online course in the portal.
    Each course is associated with an instructor (User).
    """
    title = models.CharField(max_length=100, help_text="Course title")
    description = models.TextField(help_text="Detailed course description")
    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='taught_courses',
        help_text="Course instructor"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return f"{self.title} by {self.instructor.username}"