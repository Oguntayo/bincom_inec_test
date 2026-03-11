from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone
from .models import PollingUnit, AnnouncedPUResult, LGA, Party

def pollingUnitResults(request):
    polling_units = PollingUnit.objects.only("uniqueid", "polling_unit_name")
    parties = Party.objects.all()
    pu_id = request.GET.get("polling_unit")

    # Create a dictionary of all parties with 0 as default score
    party_results = {p.partyid: 0 for p in parties}

    if pu_id:
        results = AnnouncedPUResult.objects.filter(
            polling_unit__uniqueid=pu_id
        )
        for r in results:
            if r.party_abbreviation in party_results:
                party_results[r.party_abbreviation] = r.party_score

    # Convert to list for template
    normalized_results = [{"party": p, "score": s} for p, s in party_results.items()]

    return render(
        request,
        "election_results/polling_unit_results.html",
        {
            "polling_units": polling_units,
            "results": normalized_results,
            "selected_pu": pu_id
        }
    )


def lgaResults(request):
    lgas = LGA.objects.all()
    parties = Party.objects.all()
    lga_id = request.GET.get("lga")

    # Create a dictionary of all parties with 0 as default score
    party_results = {p.partyid: 0 for p in parties}

    if lga_id:
        results = (
            AnnouncedPUResult.objects
            .filter(polling_unit__lga__uniqueid=lga_id)
            .values("party_abbreviation")
            .annotate(total_votes=Sum("party_score"))
        )
        for r in results:
            if r["party_abbreviation"] in party_results:
                party_results[r["party_abbreviation"]] = r["total_votes"]

    # Convert to list for template
    normalized_results = [{"party": p, "score": s} for p, s in party_results.items()]

    return render(
        request,
        "election_results/lga_results.html",
        {
            "lgas": lgas,
            "results": normalized_results,
            "selected_lga": lga_id
        }
    )


def addResults(request):
    polling_units = PollingUnit.objects.only("uniqueid", "polling_unit_name")
    parties = Party.objects.all()
    if request.method == "POST":
        pu = request.POST.get("polling_unit")
        polling_unit = PollingUnit.objects.get(uniqueid=pu)
        print(request.POST)

        for party in parties:
            score = request.POST.get(party.partyid)
            if score:
                AnnouncedPUResult.objects.create(
                    polling_unit=polling_unit,
                    party_abbreviation=party.partyid,
                    party_score=score,
                    entered_by_user="admin",
                    date_entered=timezone.now(),
                    user_ip_address=request.META.get("REMOTE_ADDR")
                )

    return render(
        request,
        "election_results/add_results.html",
        {
            "polling_units": polling_units,
            "parties": parties
        }
    )