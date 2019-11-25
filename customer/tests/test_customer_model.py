from model_bakery import baker
from customer.models import Customer


def test_customer_model_str(db):
    """Test"""
    customer = baker.make(Customer)
    assert str(customer) == customer.email
