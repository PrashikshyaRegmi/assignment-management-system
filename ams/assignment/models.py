from django.db import models


class Teacher(models.Model):
    teachername = models.CharField(max_length=100)
    teacheremail = models.EmailField(max_length=100)
    teachersubject = models.CharField(max_length=100)
    assignments= models.FileField(upload_to='teachers/assignments/')
    duedate = models.CharField(max_length=100)

    def __str__(self):
        return self.teachername

    def delete(self, *args, **kwargs):
        self.assignments.delete()
        super().delete(*args, **kwargs)

STATUS_CHOICES = (
('Competed', 'Completed'),
('Uncompleted', 'Uncompleted'),
)
class Student(models.Model):
    studentname = models.CharField(max_length=100)
    studentemail = models.EmailField(max_length=100)
    subject= models.CharField(max_length=100)
    completiondate=models.CharField(max_length=100,null=True)
    studassignments= models.FileField(upload_to='students/studassignment/')
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,)


    """def completion(self):
        if(self.completiondate >=self.studduedate):
            self.status=default='Completed'
        else:
            self.status=default='Uncompleted'"""

    def __str__(self):
        return self.studentname

    def delete(self, *args, **kwargs):
        self.studassignments.delete()
        super().delete(*args, **kwargs)

