from rest_framework.response import Response
from rest_framework.decorators import api_view
import os
import pathlib


# Create your views here.
@api_view(['GET', 'POST'])
def handle_files(request):
    data: dict = {}

    if request.method == 'POST':
        data['param'] = request.data['param']

        if request.FILES is not None and request.FILES.__sizeof__() > 1:
            for key, file_obj in request.FILES.items():
                data[key] = file_obj.name        
                chunks = file_obj.chunks(1000000)

                pathlib.Path("./filehandler/temp/").mkdir(parents=True, exist_ok=True)
                with open(os.path.join("./filehandler/temp/", file_obj.name), "wb") as f:
                    for chunk in chunks:
                        f.write(chunk)

    return Response(data=data)