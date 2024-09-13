import ddtrace.tracer
from celery import shared_task
from common.djangoapps.util.json_request import JsonResponse


@shared_task
def sample_task():
    print("📋📋📋 Task is running in this process.")


def run_celery_task(request):
    print(f"ℹ️ Current root span: {ddtrace.tracer.current_root_span()._pprint()}")
    sample_task.apply_async()
    return JsonResponse({}, status=200)
