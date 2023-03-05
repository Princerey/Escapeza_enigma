from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import threading
import time

def check_triangle(request):
    if request.method == 'POST':
        side1 = int(request.POST['side1'])
        side2 = int(request.POST['side2'])
        side3 = int(request.POST['side3'])

        if (side1**2 + side2**2 == side3**2) or (side1**2 + side3**2 == side2**2) or (side2**2 + side3**2 == side1**2):
            return render(request, 'home.html', {'message': 'TEAM AVAILABLE!'})
        else:
            # Define a timer function to be run in a separate thread
            def timer():
                time.sleep(30)
                penalty_message = "The team formation is wrong. You have been penalized for 30 seconds."
                template = loader.get_template('home.html')
                context = {'penalty_message': penalty_message, 'time_left': 0}
                return HttpResponse(template.render(context, request))

            # Start the timer in a separate thread
            t = threading.Thread(target=timer)
            t.start()

            # Return a response with the penalty message
            penalty_message = "The team formation is wrong. You have been penalized for 30 seconds"
            template = loader.get_template('home.html')
            context = {'penalty_message': penalty_message, 'time_left': 30}
            return HttpResponse(template.render(context, request))
    else:
        return render(request, 'home.html')
