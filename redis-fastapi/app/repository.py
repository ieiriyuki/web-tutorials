import redis


class CreditRepository:
    def __init__(self, reader: redis.Redis, writer: redis.Redis):
        self.reader = reader
        self.writer = writer

    def get_credit(self, id: int):
        amount = self.reader.get(id)
        if amount is not None:
            return int(amount)
        else:
            return None

    def set_credit(self, id: int, amount: int):
        self.writer.set(id, amount)

    def add_credit(self, id: int, amount: int):
        self.reader.incrby(id, amount)

    def swap_db(self):
        self.reader.swapdb(
            self.reader.client().connection.db,
            self.writer.client().connection.db,
        )

    def initialize_credit(self):
        for id in range(0, 10):
            self.writer.set(id, 1000)

        self.swap_db()
        self.writer.flushdb()
