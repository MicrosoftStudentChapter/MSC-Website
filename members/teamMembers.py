import csv


class Member:
    def __init__(self, mid, mname, mposition, mimg, mfb, mlinkedin, minsta, mgit):
        self.id = mid
        self.name = mname
        self.position = mposition
        self.img = mimg
        self.fb = mfb
        self.linkedin = mlinkedin
        self.insta = minsta
        self.github = mgit


members = []

with open("members/members.csv", 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for member in csv_reader:
        members.append(Member(int(member['id']), member['name'], member['position'], member['img'],
                              member['fb'], member['linkedin'], member['insta'], member['github']))
