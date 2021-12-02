"""
Name: Joanna Godawa
sales_person.py

sales person class

Certificate of authenticity:
I certify that this assignment is my own work."""


class SalesPerson:
    """
    Creates a profile for a salesperson with an id number, name, and a
    list of sales they made.
    """
    def __init__(self, employee_id, name):
        self.sales = []
        self.employee_id = employee_id
        self.name = name

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0.0
        for sale in self.sales:
            total += sale
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        if self.total_sales() > other.total_sales():
            return 1
        if self.total_sales() < other.total_sales():
            return -1
        return 0

    def __str__(self):
        return "{id}-{name}: {total_sales}"\
            .format(id=self.employee_id, name=self.name, total_sales=self.total_sales())
