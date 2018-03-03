# a program for counting and recording employees.
class Employee(object):

    def __init__(self, record, name, age, salary, email, department, place_of_department):
        """Class initiation."""
        self.record = record
        self.name = name
        self.age = age
        self.salary = salary
        self.email = email
        self.departement = department
        self.place_of_department = place_of_department

    def write_info(self):
        writer = open("employee.txt", "a")
        writer.write("\n\n*****************************************")
        writer.write("\n")
        writer.write("Record     :  {0}".format(self.record))
        writer.write("\n")
        writer.write("Name       :  {0}".format(self.name))
        writer.write("\n")
        writer.write("Age        :  {0}".format(self.age))
        writer.write("\n")
        writer.write("Salary     :  {0}".format(self.salary))
        writer.write("\n")
        writer.write("Email      :  {0}".format(self.email))
        writer.write("\n")
        writer.write("Department :  {0}".format(self.departement))
        writer.write("\n")
        writer.write("work place :  {0}".format(self.place_of_department))
        writer.write("\n\n*****************************************\n\n\n")
