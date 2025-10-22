from django.db import models
# Create your models here.

from django.core.validators import RegexValidator

# Charging Station Model
class ChargingStation(models.Model):
    class StationAttribute(models.TextChoices):
        SHARED = 'shared', 'Shared Station'
        PERSONAL = 'personal', 'Personal Station'

    class StationType(models.TextChoices):
        TESLA = 'tesla', 'Tesla Exclusive'
        MIXED = 'mixed', 'Mixed Use'

    class StationStatus(models.TextChoices):
        AVAILABLE = 'available', 'Available'
        PENDING = 'pending', 'Application Pending'
        CREATING = 'creating', 'Under Construction'
        DEPRECATED = 'deprecated', 'Deprecated'

    name = models.CharField(max_length=100, verbose_name='Station Name')
    station_id = models.CharField(max_length=50, unique=True, verbose_name='Station ID')
    attributes = models.CharField(
        max_length=20,
        choices=StationAttribute.choices,
        verbose_name='Station Attribute'
    )
    station_type = models.CharField(
        max_length=20,
        choices=StationType.choices,
        verbose_name='Station Type'
    )
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    address = models.TextField(verbose_name='Detailed Address')
    eircode = models.CharField(
        max_length=8,
        validators=[RegexValidator(r'^[A-Z]\d{2}[A-Z]{2}\d{2}$', 'Invalid Eircode format (e.g. D01ZZ13)')],
        verbose_name='Eircode'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')
    status = models.CharField(
        max_length=20,
        choices=StationStatus.choices,
        default=StationStatus.PENDING,
        verbose_name='Status'
    )
    thumbnail = models.CharField(max_length=50, verbose_name='thumbnail ID')

    def __str__(self):
        return self.name

# Charging Pile Model
class ChargingPile(models.Model):
    class PileType(models.TextChoices):
        FAST = 'fast', 'Fast Charging'
        SLOW = 'slow', 'Slow Charging'

    class PileStatus(models.TextChoices):
        AVAILABLE = 'available', 'Available'
        IN_USE = 'in_use', 'In Use'
        MAINTENANCE = 'maintenance', 'Awaiting Maintenance'
        ABANDONED = 'abandoned', 'Abandoned'

    pile_id = models.CharField(max_length=50, unique=True, verbose_name='Pile ID')
    name = models.CharField(max_length=100, verbose_name='Pile Name')
    pile_type = models.CharField(
        max_length=20,
        choices=PileType.choices,
        verbose_name='Pile Type'
    )
    power = models.FloatField(verbose_name='Power Rating (kW)')
    remarks = models.TextField(verbose_name='Remarks', blank=True, null=True)
    station = models.ForeignKey(ChargingStation, on_delete=models.CASCADE, verbose_name='Belonging Station')
    pricing_id = models.CharField(max_length=50, verbose_name='Pricing Standard ID')
    status = models.CharField(
        max_length=20,
        choices=PileStatus.choices,
        default=PileStatus.AVAILABLE,
        verbose_name='Status'
    )

    def __str__(self):
        return self.name

# Pricing Standard Model
class PricingStandard(models.Model):
    class PricingType(models.TextChoices):
        UNIFIED = 'unified', 'Unified Pricing'
        CUSTOM = 'custom', 'Custom Pricing'

    pricing_id = models.CharField(max_length=50, unique=True, verbose_name='Pricing ID')
    pricing_type = models.CharField(
        max_length=20,
        choices=PricingType.choices,
        verbose_name='Pricing Type'
    )
    time_period = models.CharField(max_length=100, verbose_name='Time Period')
    electricity_fee = models.FloatField(verbose_name='Electricity Fee')
    service_fee = models.FloatField(verbose_name='Service Fee')
    remarks = models.TextField(verbose_name='Remarks', blank=True, null=True)

    def __str__(self):
        return self.pricing_id

# Charging Record Model
class ChargingRecord(models.Model):
    class TransactionStatus(models.TextChoices):
        COMPLETED = 'completed', 'Completed'
        REFUNDING = 'refunding', 'Refunding'
        REFUNDED = 'refunded', 'Refunded'

    order_id = models.CharField(max_length=50, unique=True, verbose_name='Order ID')
    customer_id = models.CharField(max_length=50, verbose_name='Customer ID')
    payment_method = models.CharField(max_length=50, verbose_name='Payment Method')
    amount = models.FloatField(verbose_name='Amount')
    charging_amount = models.FloatField(verbose_name='Charging Amount (kWh)')
    pile = models.ForeignKey(ChargingPile, on_delete=models.CASCADE, verbose_name='Charging Pile')
    transaction_status = models.CharField(
        max_length=20,
        choices=TransactionStatus.choices,
        default=TransactionStatus.COMPLETED,
        verbose_name='Transaction Status'
    )

    def __str__(self):
        return self.order_id

# Recharge Record Model
class RechargeRecord(models.Model):
    class RechargeStatus(models.TextChoices):
        COMPLETED = 'completed', 'Completed'
        REFUNDING = 'refunding', 'Refunding'
        REFUNDED = 'refunded', 'Refunded'

    order_id = models.CharField(max_length=50, unique=True, verbose_name='Order ID')
    customer_id = models.CharField(max_length=50, verbose_name='Customer ID')
    payment_method = models.CharField(max_length=50, verbose_name='Payment Method')
    amount = models.FloatField(verbose_name='Amount')
    status = models.CharField(
        max_length=20,
        choices=RechargeStatus.choices,
        default=RechargeStatus.COMPLETED,
        verbose_name='Status'
    )

    def __str__(self):
        return self.order_id

# User Model
class User(models.Model):
    user_id = models.CharField(max_length=50, unique=True, verbose_name='User ID')
    name = models.CharField(max_length=100, verbose_name='User Name')
    contact = models.CharField(max_length=50, verbose_name='User Contact')
    password = models.CharField(max_length=100, verbose_name='User Password')
    is_member = models.BooleanField(default=False, verbose_name='Is Member')

    def __str__(self):
        return self.name

# Member Model
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User ID')
    balance = models.FloatField(verbose_name='Balance')

    def __str__(self):
        return f"{self.user.name}'s Membership"