from django.shortcuts import render,get_object_or_404,redirect
from .models import Aluno,Curso,Cidade
from .forms import AlunoForm
from .filters import AlunoFilter
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login')
def aluno_editar(request,id):
    aluno = get_object_or_404(Aluno,id=id)
   
    if request.method == 'POST':
        form = AlunoForm(request.POST,instance=aluno)

        if form.is_valid():
            form.save()
            return redirect('aluno_listar')
    else:
        form = AlunoForm(instance=aluno)

    return render(request,'aluno/form.html',{'form':form})

@login_required(login_url='/accounts/login')
def aluno_remover(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    return redirect('aluno_listar') # procure um url com o nome 'lista_aluno'

@login_required(login_url='/accounts/login')
def aluno_criar(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            form = AlunoForm()
    else:
        form = AlunoForm()

    return render(request, "aluno/form.html", {'form': form})

@login_required(login_url='/accounts/login')
def aluno_listar(request):

    alunos = Aluno.objects.all().order_by('nome_aluno')

    paginator = Paginator(alunos, 2)

    pagina = request.GET.get('pagina')

    pag_obj = paginator.get_page(pagina)

    context ={

        'pag_obj':pag_obj
    }
    return render(request, "aluno/alunos.html",context)

@login_required(login_url='/accounts/login')
def index(request):
    total_alunos = Aluno.objects.count()
    total_cidades = Cidade.objects.count()
    total_curso = Curso.objects.count()
    context = {
        'total_alunos' : total_alunos,
        'total_cidades' : total_cidades,
        'total_cursos' : total_curso
    }
    return render(request, "aluno/index.html",context)


