#!/usr/bin/python3
import logging
import os
import sys
from flask import Flask, request
from jaeger_logger_reporter import LoggerTraceConfig, LoggerTracerReporter

from flask import Flask, request
app = Flask(__name__)

config = LoggerTraceConfig(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'local_agent': {
                'reporting_host': os.environ.get('JAEGER_AGENT_HOST', 'jaeger'),
                'reporting_port': os.environ.get('JAEGER_AGENT_PORT', '5775'),
            },
            'logging': True,
            'max_tag_value_length': sys.maxsize
        },
        service_name='test',
        validate=True,
    )

    # setup my logger (optional)
tracer_logger = logging.getLogger('my.logger')
tracer_logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '[%(levelname)s][%(date)s] %(name)s %(span)s %(event)s %(message)s')
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
tracer_logger.addHandler(handler)
# define the logger to use, by default LoggerTracerReporter but can be changed.
tracer = config.initialize_tracer(
    logger_reporter=LoggerTracerReporter(logger=tracer_logger))
    

@app.route('/')
def hello_world():
    with tracer.start_span('TestSpan') as span:
        span.log_kv({'event': 'test message', 'life': 42})

        with tracer.start_span('ChildSpan', child_of=span) as child_span:
            child_span.log_kv({'event': 'down below'})
    return 'Ynov Hello World'

app.run(debug=True, host='0.0.0.0')

time.sleep(2)
tracer.close()