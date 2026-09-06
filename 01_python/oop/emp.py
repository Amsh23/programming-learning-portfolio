class employee:
    def __init__(self,fn,ln,job,salary):
        self.firstname=fn
        self.lastname=ln
        self.job=job
        self.salary=salary
    def func1(self,percent):
        return self.salary*percent