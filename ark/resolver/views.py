from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import ARK


class ARKListView(ListView):
    model = ARK
    # queryset = ARK.published.all()
    context_object_name = "arks"
    # paginate_by = 3
    template_name = "resolver/ark/list.html"


def ARK_list(request):
    arks = ARK.published.all()
    return render(request, "resolver/ark/list.html", {"arks": arks})


def ARK_detail(request, ark_id):
    ark = get_object_or_404(ARK, ark_id=ark_id)
    return render(request, "resolver/ark/detail.html", {"ark": ark})
