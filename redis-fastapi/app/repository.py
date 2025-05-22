import redis


class CreditRepository:
    def __init__(self, reader: redis.Redis, writer: redis.Redis):
        self.reader = reader
        self.writer = writer

    def key(self, id: int):
        return f"{id}"

    def get_credit(self, id: int):
        value = self.reader.hgetall(self.key(id))
        amount = value.get("amount")
        if amount is not None:
            return int(amount)
        else:
            return None

    def set_credit(self, id: int, amount: int):
        self.writer.hset(self.key(id), mapping=self.mapping(amount))

    def add_credit(self, id: int, amount: int):
        value = self.reader.hgetall(self.key(id))
        current_amount = value.get("amount")
        if current_amount is not None:
            new_amount = int(current_amount) + amount
        else:
            new_amount = amount
        self.reader.hset(self.key(id), mapping=self.mapping(new_amount))

    def swap_db(self):
        self.reader.swapdb(
            self.reader.client().connection.db,
            self.writer.client().connection.db,
        )

    def initialize_credit(self):
        for id in range(0, 5):
            self.set_credit(id, 1000)

        self.swap_db()
        self.writer.flushdb()

    def mapping(self, amount: int):
        return {"amount": amount}
