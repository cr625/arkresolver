from django.shortcuts import render, get_object_or_404

from .models import ARK


def ARK_list(request):
    arks = ARK.published.all()
    return render(request, '/ark/list.html', {'ARKs': arks})


def ARK_detail(request, naan, shoulder, ark_id):
    ark = get_object_or_404(ARK, naan=naan, shoulder=shoulder, ark_id=ark_id)

    return render(request, '/ark/detail.html', {'ARK': ark})
