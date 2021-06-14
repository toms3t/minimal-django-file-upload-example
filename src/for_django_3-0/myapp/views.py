from django.shortcuts import redirect, render
from .models import Document, Airplane
from .forms import DocumentForm
import csv


def my_view(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            with open('/Users/tomset/Documents/python/minimal-django-file-upload-example/src/for_django_3-0/media/documents/planes.csv', newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')  
                for row in spamreader:
                    newplane = Airplane()
                    row_data = row[0].split(',')
                    newplane.airplane_id = row_data[0]
                    newplane.airplane_name = row_data[1]
                    newplane.airplane_model = row_data[2]
                    newplane.save()

            # Redirect to the document list after POST
            with open('/Users/tomset/Documents/python/minimal-django-file-upload-example/src/for_django_3-0/media/documents/planes.csv', newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')  
                for row in spamreader:
                    row_data = row[0].split(',')
                    print(row_data)
                    newdoc.airplane_id = row_data[0]
                    newdoc.airplane_name = row_data[1]
                    newdoc.airplane_model = row_data[2]
                    newdoc.save()
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'list.html', context)
