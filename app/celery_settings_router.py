# broker_url = 'pyamqp://guest@localhost//'
broker_url = 'amqp://localhost//'
result_backend = 'rpc://'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Madrid'
enable_utc = True
# -- JUST FOR RABBIT-MQ --
task_annotations = {
  'tasks.route_calculate': {'rate_limit': '100/s'}
}
