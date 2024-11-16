from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from results.models.results import Results
from results.serializers.results import ResultsSerializer

class ResultsView(APIView):
    
    def get(self, request, *args, **kwargs):

        user_id = request.query_params.get('user_id', None)

        if user_id is not None:
            results = Results.objects.filter(user_id=user_id)
        else:
            results = Results.objects.all()

        if not results:
            return Response({"detail": "No results found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ResultsSerializer(results, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):

        result_id = request.query_params.get('result_id', None)
        
        if result_id is None:
            return Response({"detail": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            result = Results.objects.get(id=result_id)
        except Results.DoesNotExist:
            return Response({"detail": "Result not found"}, status=status.HTTP_404_NOT_FOUND)

        result.delete()

        return Response({"detail": "Result deleted successfully"}, status=status.HTTP_204_NO_CONTENT)