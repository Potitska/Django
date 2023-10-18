from django.db.models import Manager


class CarManager(Manager):
    # a method that will show cars for more than such and such a price
    def price_gt(self, price):
        return self.filter(price__gt=price)

    # a method that will show only AUDI
    def cars_audi(self):
        return self.filter(brand='audi')
