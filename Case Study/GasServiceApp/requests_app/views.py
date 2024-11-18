from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('view_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'requests_app/submit_request.html', {'form': form})

@login_required
def view_requests(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'requests_app/view_requests.html', {'requests': requests})

@staff_member_required
def manage_requests(request):
    all_requests = ServiceRequest.objects.all()
    return render(request, 'requests_app/manage_requests.html', {'requests': all_requests})


@staff_member_required
def resolve_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    service_request.status = 'Resolved'
    service_request.resolved_at = timezone.now()
    service_request.save()
    return HttpResponseRedirect(reverse('manage_requests'))
