
class Member:
    def __init__(self, mname, mposition, mimg, mfb, mlinkedin, minsta, mgit):
        self.name = mname
        self.position = mposition
        self.img = mimg
        self.fb = mfb
        self.linkedin = mlinkedin
        self.insta = minsta
        self.github = mgit

# secNames = ['Pranjal', 'Arpit']


def Secretaries():
    Pranjal = Member("Pranjal", "General Secretary", "../../static/members/Secretaries/Pranjal.jpg", "#", "https://www.linkedin.com/in/pranjalgupta29",
                     "https://www.instagram.com/_pranj.al/", "https://github.com/pranjalgupta29")
    Arpit = Member("Arpit", "Finance Secretary", "../../static/members/Secretaries/Arpit.jpg", "#", "https://www.linkedin.com/in/arpit-arora-2b7847192/",
                   "https://www.instagram.com/arpit.arora18/", "https://github.com/arpit1709")

    return Pranjal, Arpit


def JointSecretaries():
    Paras = Member("Paras", "Joint Secretary", "../../static/members/Secretaries/Paras.jpg",
                   "#", "https://www.linkedin.com/in/paras-dhanwal/", "#", "#")
    Paritosh = Member("Paritosh", "Joint Secretary", "../../static/members/Secretaries/Paritosh.jpg", "https://www.facebook.com/paritosh.arora.507",
                      "https://www.linkedin.com/in/arora-paritosh", "https://www.instagram.com/paritosh.exe/", "https://github.com/CLASHERBROs")
    Anushri = Member("Anushri", "Joint Secretary", "../../static/members/Secretaries/Anushri.jpeg", "#",
                     "https://www.linkedin.com/in/anushri-jain23/", "https://www.instagram.com/anushri._.jain/", "https://github.com/anushri2325")
    Saurav = Member("Saurav", "Joint Secretary", "../../static/members/Secretaries/Saurav.jpeg", "https://www.facebook.com/saurav.srivastav.391",
                    "https://www.linkedin.com/in/saurav-shrivastav-635996184", "https://www.instagram.com/_saurav_shrivastav_/", "https://github.com/Saurav-Shrivastav")

    return Paras, Paritosh, Anushri, Saurav


def Heads():
    Ritik = Member("Ritik", "Technical Head", "../../static/members/Heads/Ritik1.jpg", "https://www.facebook.com/ritik.rajdev",
                   "https://www.linkedin.com/in/ritikrajdev/", "https://www.instagram.com/ritik_rajdev/", "https://github.com/ritikrajdev")
    Shourya = Member("Shouraya", "Marketing Head", "../../static/members/Heads/Shouraya.jpg", "#",
                     "https://www.linkedin.com/in/shouraya-goyal-aa471b1a2", "https://www.instagram.com/shouraya.7/", "https://github.com/Shouraya/")
    Divyanshu = Member("Divyanshu", "Finance Head", "../../static/members/Heads/Divyanshu.jpg", "https://www.facebook.com/divyanshu.jindal.359",
                       "https://www.linkedin.com/in/divyanshu-jindal-5b675b197/", "https://www.instagram.com/jindal_dv/?r=nametag", "https://github.com/Dv2204")
    Akshat = Member("Akshat", "Event Management", "../../static/members/Heads/Akshat.jpg", "#", "https://www.linkedin.com/in/akshat-sharma-8a412a193/",
                    "https://www.instagram.com/akshat_sharma_2001/", "https://github.com/SharmaAkshat007")

    return Ritik, Shourya, Divyanshu, Akshat
