from ast import Param
from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView
from election.forms import VoteForm
from .models import Candidate, Vote


#バックエンドを指定

def select(request):
    data = Candidate.objects.all()
    params = {
        'data': data,
    }
    return render(request,'election/select.html',params)

def Choose(request,pk):   
    Candidate_data = get_object_or_404(Candidate,pk=pk)
    params = {
        'Candidate_data': Candidate_data,
    }
    return render(request,'election/Choose.html',params)

def judge(request,pk):
    judge_data = get_object_or_404(Candidate,pk=pk)
    params = {
        'judge_data':judge_data,
    }
    return render(request,'election/judge.html',params)
       
def vote(request,pk):
    if request.method == 'POST':
        #データーベース処理
        data = Vote.objects.values_list('vote_id',flat=True)
        vote_id = request.POST.get('vote_id') #フォーム取得
        #投票番号でForeach
        for d in data:
            #投票番号が一致した時
            if(d == vote_id):
                person_number = Candidate.objects.get(pk = pk)
                person_number.vote = person_number.vote + 1
                person_number.save()
                return render(request,'election/thanks.html')
        
        #投票番号がなかった時
        form = VoteForm()
        msg = '投票番号が番号がありません'
        form += msg
        #投票番号登録番号に遷移
        return render(request,'election/vote.html',{'form':form})
    else:
        #投票番号入力フォームを返す
        form = VoteForm()
        return render(request,'election/vote.html',{'form':form})
    
#投票情報
def present(request):
    present = Candidate.objects.all()
    params = {
        'present': present
    }
    return render(request,'election/base.html',params)
    
        


# Create your views here.
