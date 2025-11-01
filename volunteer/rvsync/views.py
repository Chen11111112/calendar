from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Event
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def delete_event_api(request, pk):
    if request.method == "POST":
        event = get_object_or_404(Event, pk=pk)
        event.delete()
        return JsonResponse({"status": "deleted"})
    return JsonResponse({"error": "Invalid request"}, status=400)


def calendar_view(request):
    return render(request, 'calendar.html')

import json

# views.py

@csrf_exempt
def add_event_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title", "未命名事件")
        start = data.get("start")
        end = data.get("end", start)
        identity = data.get("identity", "t") 

        event = Event.objects.create(
            title=title,
            start_time=start,
            end_time=end,
            identity=identity
        )

        return JsonResponse({
            "id": event.id,
            "title": event.title,
            "start": event.start_time.isoformat(),
            "end": event.end_time.isoformat(),
            "identity": event.identity
        })
    return JsonResponse({"error": "Invalid request"}, status=400)


def events_api(request):
    events = Event.objects.all() # Get
    data = []
    for event in events:
        data.append({
            "id": event.id,
            "title": event.title,
            "start": event.start_time.isoformat(),
            "end": event.end_time.isoformat(),
            "identity": event.identity,
        })
    return JsonResponse(data, safe=False)
