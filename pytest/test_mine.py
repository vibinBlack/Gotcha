def isSubstring(name , para):
    if name in para:
        return True
    else:
        return False

def test_what():
    name = "VinayMuthangi"
    para = "Hi, My name is Vinay Muthangi. I am from Hyderabad. I am currently pursuing my B.Tech final year in GRIET in IT field. My goal is to become a great software engineer. Thank You. Yours sincerely -VinayMuthangi"
    assert isSubstring(name, para)
