from django.shortcuts import render
from django.http import HttpResponse
import json
from .dataPro import *



# Create your views here.
def hello(request):
    return HttpResponse('hwllo world')




#解释词语
def explain(request):
    sWord = request.GET['key']
    print(sWord)
    ans = explainWord(sWord)
    


    return HttpResponse(json.dumps(ans), content_type="application/json")

# var data = null;

# var xhr = new XMLHttpRequest();
# xhr.withCredentials = true;

# xhr.addEventListener("readystatechange", function () {
#   if (this.readyState === 4) {
#     console.log(this.responseText);
#   }
# });

# xhr.open("GET", "http://127.0.0.1:8000/word/explain?key=关键字");
# xhr.setRequestHeader("cache-control", "no-cache");
# xhr.setRequestHeader("postman-token", "e0ee775a-3693-b79c-78b1-e6a48550f0bb");

# xhr.send(data);







#两个词的相似度





#计算句子主谓宾


#计算文本相似度