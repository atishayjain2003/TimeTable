from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Timetable
from .serializers import TimetableSerializer

class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer

    def create(self, request, *args, **kwargs):
        # Get data from the request
        if request.method == 'POST':
            data = request.data  # Fixed: No parentheses needed here

        # Validate if the required fields are present in the request
        if not all(key in data for key in ("day_of_week", "class_name", "subject", "teacher", "timeslot")):
            return Response({"error": "Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the timetable entry directly using the foreign key IDs
        try:
            timetable = Timetable.objects.create(
                day_of_week=data["day_of_week"],
                class_name=data["class_name"],  
                subject=data["subject"],        
                teacher=data["teacher"],        
                timeslot=data["timeslot"]       
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Serialize and return the created timetable
        serializer = self.get_serializer(timetable)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
