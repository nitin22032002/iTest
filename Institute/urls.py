from django.urls import path
from .views import Batch,Register_Institute,Register_User
urlpatterns=[
    path("institute/",Register_Institute.as_view()),
    path("reg/institute",Register_Institute.as_view()),
    path("user/",Register_User.as_view()),
    path("reg/user",Register_User.as_view()),
    path("batch/",Batch.as_view()),
    path("reg/batch",Batch.as_view()),
    path("fetch/allinstitute/",Register_User().getAllInstitute),
    path("fetch/allbatch/",Register_User().getAllBatch),
    path("fetch/allinstitute/user/",Register_User().getInstituteUser),
    path("fetch/allbatch/user/",Register_User().getBatchUser),
    path("requests/",Register_User().RequestUser),
    path("verify/user/",Register_User().verifyUser),
    path("delete/user/",Register_User().DeleteUser),
    path("removeinstitute/",Register_Institute().deleteInstitute),
    path("view/batchs/",Batch().viewBatch),
    path("delete/batch/",Batch().deleteBatch),
]