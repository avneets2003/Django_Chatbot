from django.shortcuts import render, redirect
from django.contrib import messages
import cohere
from .models import Past
from django.core.paginator import Paginator

def home(request):
	if request.method == "POST":
		question = request.POST['question']
		past_responses = request.POST['past_responses']

		# Use your API key here
		co = cohere.Client('YOUR_API_KEY')

		try:
			response = co.chat(message=question, model='command').text

			if "shamballa" in past_responses:
				past_responses = response
			else:
				past_responses = f"{past_responses}<br/><br/>{response}"

			record = Past(question=question, answer=response)
			record.save()

			return render(request, 'home.html', {"question": question, "response": response, "past_responses": past_responses})
		except Exception as e:
			return render(request, 'home.html', {"question":question, "response":e, "past_responses":past_responses})

	return render(request, 'home.html', {})

def past(request):
	p = Paginator(Past.objects.all(), 5)
	page = request.GET.get('page')
	pages = p.get_page(page)
	past = Past.objects.all()
	nums = "a" * pages.paginator.num_pages
	return render(request, 'past.html', {"past": past, "pages": pages, "nums": nums})

def delete_past(request, Past_id):
	past = Past.objects.get(pk=Past_id)
	past.delete()
	messages.success(request, ("Selected conversation has been deleted."))
	return redirect('past')
