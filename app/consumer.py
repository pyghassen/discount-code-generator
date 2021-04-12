from utils import generate_codes
from db import create_code


MOCKED_TOPIC_DATA = {
    'generate_discount_codes_event': [
        {
            'user_id': 1,
            'number_of_codes': 100,
            'code_length': 8
        },
        {
            'user_id': 2,
            'number_of_codes': 50,
            'code_length': 6
        }
    ]
}


class EventBusClient:
    events = MOCKED_TOPIC_DATA
    @classmethod
    def get_events(cls, topic_name):
        return cls.events['generate_discount_codes_event']


class GenerateDiscountCodesEvent:
    topic_name = 'generate_discount_codes_event'
    def __init__(self, user_id: int, number_of_codes: int, code_length: int):
        self.user_id = user_id
        self.number_of_codes = number_of_codes
        self.code_length = code_length

    def handle(self):
        codes = generate_codes(
            number_of_codes=self.number_of_codes,
            code_length=self.code_length
        )
        for code in codes:
            create_code(self.user_id, code)

class GenerateDiscountCodesEventConsumer:
    event_class = GenerateDiscountCodesEvent
    def __init__(self, client):
        self._client = client

    def consume(self):
        events_data = self._client.get_events(self.event_class.topic_name)
        for event_data in events_data:
            event = self.event_class(**event_data)
            event.handle()
