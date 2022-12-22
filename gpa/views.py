from django.views import generic

from .models import Course


class IndexView(generic.ListView):
    context_object_name = 'course_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Course.objects.all()
