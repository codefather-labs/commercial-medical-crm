from django.db import models
from django.db.models import QuerySet


class Research(models.Model):
    organization = models.ForeignKey(
        "core.Organization",
        on_delete=models.deletion.SET_NULL,
        related_name='organization_researches',
        db_index=True,
        null=True,
        blank=False
    )

    @property
    def statement_history(self):
        return self.research_statement_history.all()


class Customer(models.Model):
    first_name = models.CharField(
        max_length=255, null=False, blank=True
    )
    last_name = models.CharField(
        max_length=255, null=False, blank=True
    )
    email = models.EmailField(
        max_length=255, null=False, blank=True
    )
    organization = models.ForeignKey(
        "core.Organization",
        on_delete=models.deletion.SET_NULL,
        related_name='organization_customers',
        null=True,
        blank=False
    )

    @property
    def orders(self):
        return self.customers_orders.all()


# Payment

class Order(models.Model):
    organization = models.ForeignKey(
        "core.Organization",
        on_delete=models.deletion.SET_NULL,
        related_name='organization_orders',
        null=True,
        blank=False
    )

    customer = models.ForeignKey(
        "core.Customer",
        on_delete=models.deletion.SET_NULL,
        related_name='customers_orders',
        null=True,
        blank=False
    )

    @property
    def statement_history(self):
        return self.order_statement_history.all()


class Organization(models.Model):
    # ONE TO MANY Order
    # ONE TO ONE head of organization -> UserModel
    # ONE TO MANY employees -> UserModel

    name = models.CharField(
        max_length=255, null=False, blank=True
    )

    email = models.EmailField(
        max_length=255, null=False, blank=True
    )

    @property
    def researches(self) -> QuerySet[Research]:
        return self.organization_researches.all()

    @property
    def customers(self) -> QuerySet[Customer]:
        return self.organization_customers.all()

    @property
    def orders(self) -> QuerySet[Order]:
        return self.organization_orders.all()


class Statement(models.Model):
    research = models.ForeignKey(
        "core.Research",
        on_delete=models.deletion.SET_NULL,
        related_name='research_statement_history',
        null=True,
        blank=False
    )

    order = models.ForeignKey(
        "core.Order",
        on_delete=models.deletion.SET_NULL,
        related_name='order_statement_history',
        null=True,
        blank=False
    )
