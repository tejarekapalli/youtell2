from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User, Calculation, Number, Operation
from .forms import CalculationForm

@login_required
def home(request):
    if request.user.is_staff:
        return redirect('admin:index')
    else:
        return redirect('student_dashboard')

@login_required
def master_dashboard(request):
    calculations = Calculation.objects.filter(master=request.user)
    return render(request, 'master_dashboard.html', {'calculations': calculations})

@login_required
def student_dashboard(request):
    calculations = Calculation.objects.all()
    return render(request, 'student_dashboard.html', {'calculations': calculations})

@login_required
def create_calculation(request):
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            calculation = form.save(commit=False)
            calculation.master = request.user
            calculation.result = calculate(calculation.left_operand.value, calculation.operation.function_name, calculation.right_operand.value)
            calculation.save()
            return redirect('master_dashboard')
    else:
        form = CalculationForm()
    return render(request, 'create_calculation.html', {'form': form})

def calculate(left_operand, operation, right_operand):
    return eval(f"{left_operand} {operation} {right_operand}")

@login_required
def activity_log(request):
    calculations = Calculation.objects.filter(master=request.user)
    return render(request, 'activity_log.html', {'calculations': calculations})
