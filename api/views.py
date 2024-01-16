from rest_framework_simplejwt.views import TokenObtainPairView



class CustomTokenObtainView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if 'access' in response.data:
            access_token = response.data['access']
            response.set_cookie('access_token', access_token, httponly=True)

        return response