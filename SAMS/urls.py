from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, AccountViewSet, ProfessorViewSet, MaterialsViewSet

router = DefaultRouter()
router.register('student', StudentViewSet, basename='student')
router.register('account', AccountViewSet, basename='account')
router.register('professor', ProfessorViewSet, basename='professor')
router.register('materials', MaterialsViewSet, basename='materials')


urlpatterns = [
    path('', include(router.urls)),

]

















#
# from django.contrib import admin
# from django.urls import path
# from rest_framework.routers import DefaultRouter
# from .views import Student, AccountCreate,  StudentCreation, StudentDetail
# from .views import  StudentList, ProfessorCreate, ProfessorList
# from .views import Alldata




# router = DefaultRouter()
# router.register('Student', StudentViewSet, basename='Student')
# urlpatterns = [
#     path('accountcreate/', AccountCreate.as_view()),
#     # path('studentdetails/<int:Student_ID>', StudentDetail.as_view()),
#     # path('update/<str:email>/', AccountUpdateDelete.as_view()),
#     path('studentcreate/', StudentCreation.as_view()),
#     # path('studentupdtedelete/<int:Student_ID>/', StudentRetrieveUpdateDelete.as_view()),
#     path('all_students/', StudentList.as_view()),
#     path('professorcreate/', ProfessorCreate.as_view()),
#     # path('professordeleteupdate/<str:Name>/', ProfessorUpdate.as_view()),
#     path('all_professors/',ProfessorList.as_view()),
#     # path('student_materials/<int:Student_ID>', Alldata)
#     # path('PrepYearMaterials/', Materiallist.as_view()),
#     # path('PrepYearMaterialsadd/', MaterialCreate.as_view()),
#     # path('PrepYearMaterialsupdatedelete/', MaterialsUpdateDelete.as_view()),
# ]

# urlpatterns = urlpatterns + router.urls
