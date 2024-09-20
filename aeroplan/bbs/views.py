from django.shortcuts import render
from .forms import ConversionForm
from .models import convertRate

# Create your views here.

def save_conversion(departure, arrival, base_fare, date, points, cash):
    if points is not None and cash is not None:
        conversion_rate = calculate_conversion_rate(base_fare, points, cash)
        convertRate.objects.create(
            departure = departure,
            arrival = arrival,
            base_fare = base_fare,
            date = date,
            points = points,
            cash = cash,
            convertRate=conversion_rate
        )


def calculate_conversion_rate(base_fare, points, cash):
    return round(((base_fare - cash) / points) * 100, 2)


def aeroplan_view(request):
    results = []
    if request.method == 'POST':        # 当用户输入数据
        form = ConversionForm(request.POST)
        if form.is_valid():
            # 如果数据正常，开拿
            departure = form.cleaned_data['departure']
            arrival = form.cleaned_data['arrival']
            base_fare = form.cleaned_data['base_fare']
            date = form.cleaned_data['date'] # Optional

            # 保存和计算每组的结果
            for i in range(1, 5):
                points = form.cleaned_data.get(f'points{i}')
                cash = form.cleaned_data.get(f'cash{i}')
                if points is not None and cash is not None:
                    # 保存到数据库
                    save_conversion(departure, arrival, base_fare, date, points, cash)
                    # 计算转换率
                    result = calculate_conversion_rate(base_fare, points, cash)
                    # 保存每组方案的计算结果
                    results.append({
                        'scheme': f"方案 {i}",
                        'points': points,
                        'cash': cash,
                        'rate': result,
                    })
            form.initial = form.cleaned_data

            # save_conversion(departure, arrival, date, form.cleaned_data['points1'], form.cleaned_data['cash1'])
            # save_conversion(departure, arrival, date, form.cleaned_data['points2'], form.cleaned_data['cash2'])
            # save_conversion(departure, arrival, date, form.cleaned_data['points3'], form.cleaned_data['cash3'])
            # save_conversion(departure, arrival, date, form.cleaned_data['points4'], form.cleaned_data['cash4'])

    else:
        form = ConversionForm()

    
    return render(request, 'aeroplan.html', {'form': form, 'results': results})


        


