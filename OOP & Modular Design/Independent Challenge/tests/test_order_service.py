import pytest

from repositories.mock_order_repository import MockOrderRepository
from services.order_service import OrderService


def create_service():
    repository = MockOrderRepository()
    return OrderService(repository)


def test_create_order():
    service = create_service()

    order = service.create_order(
        "ORD001",
        "Vyshnavi",
        "Laptop",
        2,
        50000
    )

    assert order.order_id == "ORD001"
    assert order.customer_name == "Vyshnavi"
    assert order.calculate_total() == 100000


def test_find_order():
    service = create_service()

    service.create_order(
        "ORD002",
        "Charan",
        "Phone",
        1,
        30000
    )

    order = service.find_order("ORD002")

    assert order is not None
    assert order.product_name == "Phone"


def test_invalid_quantity():
    service = create_service()

    with pytest.raises(ValueError):
        service.create_order(
            "ORD003",
            "Vyshnavi",
            "Laptop",
            0,
            50000
        )


def test_invalid_price():
    service = create_service()

    with pytest.raises(ValueError):
        service.create_order(
            "ORD004",
            "Vyshnavi",
            "Laptop",
            1,
            -500
        )


def test_missing_customer_name():
    service = create_service()

    with pytest.raises(ValueError):
        service.create_order(
            "ORD005",
            "",
            "Laptop",
            1,
            50000
        )