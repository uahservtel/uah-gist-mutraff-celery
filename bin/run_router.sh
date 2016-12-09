#!/bin/bash

AMQP_BROKER="amqp:://localhost"
export PYTHONPATH=../app
celery -A mutraff_router worker --loglevel=info
