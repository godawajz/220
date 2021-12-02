"""
Name: Joanna Godawa
sales_force.py

sales force class

Certificate of authenticity:
I certify that this assignment is my own work."""
from hw10.sales_person import SalesPerson


class SalesForce:
    """
    Allows for the creation of a list of sales people from a file, whose
    information can be accessed and compared.
    """
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        with open(file_name) as f_in:
            for line in f_in:
                line = line.strip("\n")
                temp = line.split(", ")
                person = SalesPerson(int(temp[0]), temp[1])
                sales = temp[2].split(" ")
                for sale in sales:
                    person.enter_sale(float(sale))
                self.sales_people.append(person)

    def quota_report(self, quota):
        out_list = []
        for person in self.sales_people:
            out_list.append([person.get_id(), person.get_name(),
                             person.total_sales(), person.met_quota(quota)])
        return out_list

    def top_seller(self):
        out_list = []
        ties = []
        top_seller = self.sales_people[0]
        for i in range(1, len(self.sales_people)):
            if self.sales_people[i].total_sales() == top_seller.total_sales():
                ties.append(self.sales_people[i])
            if self.sales_people[i].total_sales() > top_seller.total_sales():
                top_seller = self.sales_people[i]
                ties.clear()
        out_list.append(top_seller)
        for person in ties:
            out_list.append(person)
        return out_list

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if person.get_id() == employee_id:
                return person
        return None
