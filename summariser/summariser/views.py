from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.template.loader import get_template
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,TextSumForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import wikipedia
import nltk
import en_core_web_sm

def landing(request):
    return render(request,'landing.html')
def registerPage(request):
    form=CreateUserForm
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'account created')
            return redirect('login')

    context={
        "form":form,
    }
    return render(request,'register.html',context)
def loginPage(request):
    if request.method=='POST':
       username=request.POST.get('username')
       password=request.POST.get('password')
       user=authenticate(request,username=username,password=password)
       if user is not None:
           login(request,user)
           return redirect('home1')
       else :
           messages.info(request,'Username or password incorrect')
    context={}
    return render(request,'login.html',context)
def textsumPage(request):
    form=TextSumForm(request.POST or None)
    context={
        "form":form
    }
    if request.method=="POST":
        if form.is_valid():
            s=form['text'].value()
            wikisearch = wikipedia.page(s)
            wikicontent = wikisearch.content
            nlp = en_core_web_sm.load()
            summarizer_lex = LexRankSummarizer()
            # nltk.download('punkt')

            doc = nlp(wikicontent)
            parser = PlaintextParser.from_string(doc,Tokenizer("english"))
            summary= summarizer_lex(parser.document, 2)
            # print(summary)
            lex_summary=""
            for sentence in summary:
                lex_summary+=str(sentence)
            print(lex_summary)
            # print(lex_summary)
            # print(doc)
            


    
    return render(request,'textsum.html',context)
def codesumPage(request):
    
    return render(request,'codesum.html')
def pysumPage(request):
    
    return render(request,'pysum.html')
