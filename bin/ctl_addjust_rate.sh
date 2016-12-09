#!/bin/bash
celery -A mutraff_router control rate_limit tasks.add 10/s
