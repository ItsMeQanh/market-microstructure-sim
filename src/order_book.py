class OrderBook:
    def __init__(self):
        self.bids = []
        self.asks = []

    def add_order(self, side, price, quantity):
        order = {'price': price, 'quantity': quantity}
        if side == 'bid':
            self.bids.append(order)
        elif side == 'ask':
            self.asks.append(order)

    def get_top_of_book(self):
        top_bid = max(self.bids, key=lambda x: x['price'], default=None)
        top_ask = min(self.asks, key=lambda x: x['price'], default=None)
        return top_bid, top_ask