from django.shortcuts import render, get_object_or_404
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course_detail.html', {'course': course})

def rate_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        new_rating = float(request.POST['rating'])
        course.update_rating(new_rating)
        return render(request, 'course_detail.html', {'course': course})
    return render(request, 'rate_course.html', {'course': course})
