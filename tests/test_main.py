from main import create_order, create_timestamp

# test json file
def test_create_order():
    order = create_order()
    assert isinstance(order, dict)
    assert len(order) == 6
    assert order['order_id'].isdigit()
    assert order['customer_id'].count('-') == 4
    assert order['item_name'] in ('apple', 'banana', 'orange', 'grape', 'watermelon', 'pineapple')
    assert order['order_amount'] in range(1, 1000)
    assert order['item_price'] in range(1, 1000)
    assert order['payment_provider'] in ('paypal', 'klarna', 'cc')
    