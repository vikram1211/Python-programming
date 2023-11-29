def Get_string():
    word1=input("Player 1: ")
    word2=input("Player 2: ")
    return word1,word2

def Compute_score(word):
    POINTS={
        'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,
        'r':1,'s':1,'t':1,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10
    }
    word=word.lower()
    score=0
    n=len(word)
    for i in range(n):
        if word[i] in POINTS.keys():
            score+=POINTS[word[i]]
    return score

def main():
    a,b=Get_string()
    p1_score=Compute_score(a)
    p2_score=Compute_score(b)
    if p1_score>p2_score:
        print("Player 1 wins!")
    elif p1_score<p2_score:
        print("Player 2 wins!")
    elif p1_score==p2_score:
        print("Tie!")

main()

