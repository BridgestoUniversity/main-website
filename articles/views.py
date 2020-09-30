from django.shortcuts import render, HttpResponse
from django.db.models import Q
from .models import Articles


def articles_page(request):
    # return HttpResponse("This is the Bridges Article Page")
    # by default, issues will be organized in descending order in terms of date

    issues = Articles.objects
    newestIssuesOrder = issues.order_by('-date')
    latestIssue = newestIssuesOrder.first()

    reqMethod = request.method

    if reqMethod == 'GET':
        orderType = request.GET.get('orderType', '')
        searchInput = request.GET.get('searchInput', '')

        # make conditions based on resetValue == 'reset'
        submitValue = request.GET.get('search', '')
        resetValue = request.GET.get('reset', '')
        debugStr = "SubmitVal: " + submitValue + ". Reset Value: " + \
            resetValue + ". OrderType: " + orderType + \
            ". Search String:" + searchInput + "."

        if (resetValue == 'reset'):
            filteredIssues = issues.order_by('-date')
            # filteredIssues.order_by('date')
        elif (submitValue == 'search'):
            filteredIssues = issues.filter(
                Q(title__icontains=searchInput) | Q(authors__icontains=searchInput) | Q(topics__icontains=searchInput) | Q(tags__icontains=searchInput) | Q(articleType__icontains=searchInput))

            if (orderType == '0'):
                filteredIssues = filteredIssues.order_by('-date')
                # print('hello')
            else:
                # bob = "name"
                filteredIssues = filteredIssues.order_by('date')

                # filteredIssues.order_by('date')
        else:
            issues = issues.order_by('-date')
            filteredIssues = issues

        return render(request, 'articles/index.html', {"issues": filteredIssues, "latestIssue": latestIssue,  "debugString": debugStr})
    # else:
    #     issues = issues.order_by('-date')
    #     latestIssue = issues.first()
    #     return render(request, 'articles/index.html', {"issues": issues, "latestIssue": latestIssue, "reqMethod": reqMethod, "debugString": "nothing"})


def articles_testing(request, id):
    test = Articles.objects.get(id=id)
    return HttpResponse("<h1>Article Title: %s</h1><p>Date: %s</p><p>Topics: %s</p><p>Tags: %s</p><p>ArticleType: %s</p><p>Summary: %s</p><p>Authors: %s</p><p>Link: %s</p>" % (test.title, test.date, test.topics, test.tags, test.articleType, test.summary, test.authors, test.link))
