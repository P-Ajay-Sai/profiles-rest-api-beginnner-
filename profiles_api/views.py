from rest_framework.views import APIView
from rest_framework.views import Response


class HelloApiView(APIView):
    """test API View """

    def get(self,request,format=None):
        """return a list of API features"""
        an_apiview=[
        'Usees HTTP methods as functions (get,post,patch,put,delete) ',
        'Is simlar to a tradtional django View ',
        'Gives you the most control over you applaication logic',
        'Is Mapped manually to URLs ',
        ]
        return Response({"message":"Hello","an_apiview":an_apiview})
