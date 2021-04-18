from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import ARK, Capture
from .forms import CaptureForm


class ARKListView(ListView):
    model = ARK
    context_object_name = "arks"
    template_name = "ark/list.html"


# def ARK_list(request):
#    arks = ARK.published.all()
#    return render(request, "resolver/ark/list.html", {"arks": arks})


def ARK_detail(request, ark_id):
    ark = get_object_or_404(ARK, ark_id=ark_id)
    # list of captures for this ARK
    captures = ark.captures.all()
    parent_uri = ark.target_uri
    new_capture = None
    if request.method == "POST":
        #  a capture was posted
        capture_form = CaptureForm(date=request.POST)
        if capture_form.is_valid():
            # create capture object but don't save it yet
            new_capture = capture_form.save(commit=False)
            # assign the current ark to the capture
            new_capture.ark = ark
            # save the capture record to the db
            new_capture.save()
    else:
        capture_form = CaptureForm()

    return render(
        request,
        "ark/detail.html",
        {
            "ark": ark,
            "captures": captures,
            "new_capture": new_capture,
            "capture_form": capture_form,
            "parent_uri": parent_uri,
        },
    )
