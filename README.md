# Discount codes Generator Job

This micro-service will listen to the `generate_discount_codes` event when published
in the event bus and it will create X number of discount codes on behave of the user.

The service is intended to run as a long running job, and it can have multiple instances running simultaneously.
