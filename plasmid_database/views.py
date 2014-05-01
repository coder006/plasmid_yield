from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import biosop
from sklearn import linear_model

def calculate_yield(coeffs, inputs):
    print len(coeffs), " : ", len(inputs) 
    plasmid_yield = 0
    for i in range(len(coeffs)):
        plasmid_yield += coeffs[i]*inputs[i]
    return plasmid_yield

def calculate_coeffs():
    rows = list(biosop.objects.all())
    dim1 = []
    dim2 = []
    for row in rows:
        temp = [row.culture_volume, row.form, row.volume_buffer1, row.volume_buffer2, row.volume_buffer3, row.volume_resuspension, row.const]
        dim1.append(temp)
        dim2.append(row.pl_yield)
    clf = linear_model.Ridge(alpha = 0.0003)
    clf.fit(dim1,dim2)
    coeffs = clf.coef_
    return coeffs

@csrf_exempt
def index(request):
    voc = float(request.POST.get('culture'))
    moi = request.POST.get('moi')
    toi = int(request.POST.get('toi'))
    od = float(request.POST.get('od'))
    conc = float(request.POST.get('conc')) * 10
    buffer1 = float(request.POST.get('buffer1'))
    buffer2 = float(request.POST.get('buffer2'))
    buffer3 = float(request.POST.get('buffer3'))
    inputs = [voc, 1, buffer1, buffer2, buffer3, conc, 0]
    coeffs = calculate_coeffs().tolist()
    plasmid_yield = calculate_yield(coeffs, inputs)
    plasmid_yield = plasmid_yield/1000.0
    plasmid_yield = "{0:.2f}".format(plasmid_yield).encode('utf8')
    if plasmid_yield[0] == '-':
        plasmid_yield = plasmid_yield[1:]
    #plasmid_yield = int(plasmid_yield)
    res = "<h1>The final yield = " + `plasmid_yield` + "micro grams </h1>"
    return HttpResponse(res)
