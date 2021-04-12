from consumer import GenerateDiscountCodesEventConsumer, EventBusClient
from logger import log

def main():
    client = EventBusClient()
    event_consumer = GenerateDiscountCodesEventConsumer(client=client)
    log.msg('Start Consuming events')
    event_consumer.consume()

if __name__ == '__main__':
    main()
