from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Standard model that defines all Coin Data
class Currency(models.Model):
    name = models.CharField(max_length=20)
    symbol = models.CharField(max_length=7)
    rank = models.CharField(max_length=5)
    price_usd = models.FloatField(max_length=20)
    volume_24h_usd = models.CharField(max_length=20)
    market_cap_usd = models.CharField(max_length=20)
    available_supply = models.CharField(max_length=20)
    total_supply = models.CharField(max_length=20)
    percent_change_1h = models.CharField(max_length=10)
    percent_change_24h = models.CharField(max_length=10)
    percent_change_7d = models.CharField(max_length=10)
    last_updated = models.CharField(max_length=20)
    
    # Ticker history should be a comma separated list of values
    ticker_history = models.CharField(max_length=44,default='')
    
    # Redefine the string response to be more explicit
    def __str__(self):
        return (self.name+" "+self.symbol)

# ExtendUser will extend the user model to include some additional fields
class ExtendUser(models.Model):
    
    # Establish a 1 to 1 relationship with the User table
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    
    # Define additional fields to create
    email_contact = models.BooleanField(default=True)
    subscription_status = models.BooleanField(default=True)
    
    # The watchlist and alerts fields aren't an actual fields but rather a  
    # N to N with the Currency table
    watchlist = models.ManyToManyField(Currency,default="",related_name='user_watchlist')
    alerts = models.ManyToManyField(Currency,default="",related_name='user_alerts')
    
    # Redefine the string response to be more explicit
    def __str__(self):
        return ("User: "+self.user.username+", ID: "+str(self.id))

# Whenever a user is created, create an ExtendUser object for it 
@receiver(post_save, sender=User)
def create_user_extenduser(sender, instance, created, **kwargs):
    if created:
        ExtendUser.objects.create(user=instance)

# Append the ExtendUser data to the user that was created
@receiver(post_save, sender=User)
def save_user_extenduser(sender, instance, **kwargs):
    instance.extenduser.save()


