import datetime

from prometheus_client import CollectorRegistry, Gauge, push_to_gateway


if __name__ == '__main__':
    registry = CollectorRegistry()
    g = Gauge(
        'job_last_success_unixtime',
        'Last time a batch job successfully finished',
        registry=registry,
    )
    g.set_to_current_time()
    push_to_gateway(
        'localhost:9091',
        job='pigimaru',
        grouping_key={
            'weekday': datetime.datetime.now().weekday(),
            'hour': datetime.datetime.now().hour,
        },
        registry=registry,
    )

