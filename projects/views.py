import json, requests
from django.shortcuts import render


def fetch_data():
    """
    Fetch data periodically using Github API and store in a json file
    """
    repos = []
    response = requests.get(
        "https://api.github.com/orgs/MicrosoftStudentChapter/repos?sort=created"
    )
    if response.status_code == 200:
        with open("projects/api.json", mode="w") as file:
            data = response.json()
            for i in range(len(data)):

                # to append data based on name
                description = data[i]["description"]
                if description is not None and "project" in description.lower():
                    repos.append(data[i])
            json.dump(repos, file)
    else:
        print("Error fetching data")


def projects(request):
    """
    Read data from a json file and pass it to projects.html
    """
    final = []
    # fetch_data()
    with open("projects/api.json") as json_data:
        data = json.load(json_data)
        for i in range(len(data)):
            projects = {}
            projects["name"] = data[i]["name"]
            projects["url"] = data[i]["html_url"]
            projects["description"] = data[i]["description"]
            projects["image"] = "/static/projects/images/" + data[i]["name"] + ".png"
            final.append(projects)

    return render(request, "projects/projects.html", {"projects": final})
