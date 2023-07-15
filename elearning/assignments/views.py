from django.shortcuts import render, redirect
from .models import Assignment

def create_assignment(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        assignment = Assignment.objects.create(
            title=title,
            description=description,
            created_by=request.user
        )
        # Additional logic for saving assignment details
        return redirect('assignment_list')
    return render(request, 'create_assignment.html')

def assignment_list(request):
    assignments = Assignment.objects.filter(created_by=request.user)
    return render(request, 'assignment_list.html', {'assignments': assignments})

def complete_assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    return render(request, 'complete_assignment.html', {'assignment': assignment})

def submit_assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    if request.method == 'POST':
        answer = request.POST['answer']
        # Process the submitted answer, calculate score, and save the submission
        # You can create a Submission object here and save it to the database
        
        return redirect('assignment_list')  # Redirect to the assignment list page
    return render(request, 'submit_assignment.html', {'assignment': assignment})
