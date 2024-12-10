c_ans=0
w_ans=0
q=["1.what is the national animal?","2.what is the national game?"]
ans=["tiger","hockey"]
for x in q:
    print(x)
    user=input("enter answer").lower()
    if user in ans:
        c_ans+=1
        print("correct answer")
        
    else:
            w_ans+=1
            print("wrong answer")
print("percentage",(c_ans/(w_ans+c_ans))*100)
