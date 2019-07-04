from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView,UpdateView, CreateView
from .models import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from ams.forms import MarkAttendanceForm
from django.urls import reverse_lazy

# Create your views here.
#Index
class Index(TemplateView):
    template_name = 'ams/index.html'

class Home( LoginRequiredMixin, ListView):
    model=SubjectByFaculty

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(facultyId=self.request.user.faculty.facultyId)

    context_object_name = 'sbf'
    template_name='ams/home.html'


# @login_required
# def home(request, pk):
#     SBF = get_object_or_404(SubjectByFaculty, pk=User.Faculty.facultyId)
#     return redirect('ams/home.html', pk=SBF.pk)

#class Home(TemplateView):
#    template_name = 'ams/home.html'

class MarkAttendance(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('ams.is_faculty',)
    # permission_required=['Faculty.is_faculty']
    login = '/login/'
    model = SubjectByFaculty

    def get_queryset(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # pk = self.request.POST.get('pk')
        subId = SubjectByFaculty.objects.filter(pk=self.kwargs['pk'])
        # print(self.kwargs['pk'])
        # SBId = Subject.objects.filter(pk=subId('subjectId'))
        for subI in subId:

            sub = Subject.objects.filter(subjectName=subI.subjectId)
            for sb in sub:
                # branch = sb.branchId
                # semester = sb.semesterId
                student = Students.objects.filter(branchId=sb.branchId, semesterId=sb.semesterId)
                # context['studetbyclass'] = StudentByClass.objects.filter(branchId=sb.branchId, semesterId=sb.semesterId)
        return student
        # qs = self.model.objects.all()
        # return get_object_or_404(SubjectByFaculty)
    context_object_name = 'students'
    template_name = "ams/markattendance.html"

# def get_queryset(self, **kwargs):
#     pk = self.kwargs.get('pk')
#     # qs = self.model.objects.all()
#     # return get_object_or_404(SubjectByFaculty)
#     return SubjectByFaculty.objects.filter(pk=self.kwargs.get('pk'))

    # form_class = MarkAttendanceForm
    # success_url = reverse_lazy('home')

    # def get_queryset(self):
    #     pk=self.kwargs['pk']
    #     queryset = super().get_queryset()
    #     return queryset.filter(Students=self.Students.pk)
    # permissin_req

# def markAttendance(request, pk):
#     # permission_required=['Faculty.is_faculty']
#     subject = get_object_or_404(Subject, pk=pk)
#     return redirect('ams/markattendance.html', pk=pk)
#     # model = Students
#     # context_object_name = 'students'

# class StudentProfile(PermissionRequiredMixin, LoginRequiredMixin,ListView):
#     permission_required=('ams.is_student')
#     # permission_required=['Faculty.is_faculty']
#     login = '/login/'
#     template_name = "ams/student_profile.html"
#     # permissin_req
