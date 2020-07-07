from django.db import models


class vendor(models.Model):
    Name = models.CharField(max_length=100)
    cust_id = models.IntegerField()

# for vendor createsuperuser name is puja password is 0123456

class customer(models.Model):
    Name = models.CharField(max_length=100)
    customer_id = models.IntegerField()


class administration(models.Model):
    Name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)

class Proudct(models.Model):
    name = models.CharField(max_length=100)
    agriculture = models.CharField(max_length=100)
    beauty_zone = models.CharField(max_length=100)
    travels = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    on_demand_service = models.CharField(max_length=100)

    # bus_tickets
    # e_commerce
    # functional_hall
    # courier
    # automobile
    # events
    # dance_music_classes
    # rechargers
    # books
    # shoppings
    # flights
    # insurance_zone
    # transport_services
    # flowers
    # sport_shops
    # interior_design
    # shopping
    # internet_shop
    # workshops
    # real_estate
    # play_shcool
    # domastic_help
    # celebration_services
    # apply_for_loans
    # doctors
    # general_bazar
    # petcare
    # catering_services
    # jewellery
    # home_decor
    # book_banker

    def __str__(self):
        return self.name

class Products(models.Model):
    CHOICE_FIELD = (
        ('book_banker1', 'book_banker'),
        ('home_decor1', 'home_decor'),
        ('agriculture', 'AGRICULTURE'),
        ('beauty_zone', 'beauty_zone'),
        ('travels', 'travels'),
        ('hospital', 'hospital'),
        ('travels', 'travels'),
        ('on_demand_service', 'on_demand_service'),
        ('bus_tickets', 'bus_tickets'),
        ('e_commerce', 'e_commerce'),
        ('functional_hall', 'functional_hall'),
        ('courier', 'courier'),
        ('automobile', 'automobile'),
        ('events', 'events'),
        ('dance_music_classes', 'dance_music_classes'),
        ('rechargers', 'rechargers'),
        ('books', 'books'),
        ('shoppings', 'shoppings'),
        ('flights', 'flights'),
        ('automobile', 'automobile'),
        ('insurance_zone', 'insurance_zone'),
        ('transport_services', 'transport_services'),
        ('automobile', 'automobile'),
        ('transport_services', 'transport_services'),
        ('sport_shops', 'sport_shops'),
        ('interior_design', 'interior_design'),
        ('sport_shops', 'sport_shops'),
        ('shopping', 'shopping'),
        ('sport_shops', 'sport_shops'),
        ('internet_shop', 'internet_shop'),
        ('workshops', 'workshops'),
        ('real_estate', 'real_estate'),
        ('play_shcool', 'play_shcool'),
        ('real_estate', 'real_estate'),
        ('domastic_help', 'domastic_help'),
        ('celebration_services', 'celebration_services'),
        ('apply_for_loans', 'apply_for_loans'),
        ('real_estate', 'real_estate'),
        ('doctors', 'doctors'),
        ('general_bazar', 'general_bazar'),
        ('petcare', 'petcare'),
        ('catering_services', 'catering_services'),
        ('jewellery', 'jewellery'),
        ('home_decor', 'home_decor'),
        ('book_banker', 'book_banker'),
        ('others', 'others'),
    )

    # link = models.ForeignKey(Proudct, on_delete=models.CASCADE)
    product = models.CharField(max_length=100, choices=CHOICE_FIELD)

    def __str__(self):
        return self.product

    # Create your models here.

