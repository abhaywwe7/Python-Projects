candidate1 = input("Enter the name of candidate1 :")
candidate2 = input("Enter the name of candidate2 :")

count1, count2 = 0,0
voter_id = [1,2,3,4,5,6,7,8,9,10]
total_voters = len(voter_id)
while True:
    if voter_id == []:
        print("Voting session is over!!!")
        if count1>count2:
            percentage = (count1/total_voters)*100
            print(candidate1," has won the election with ",percentage,"%")
            break
        elif count2>count1:
            percentage = (count2/total_voters)*100
            print(candidate2," has won the election with ",percentage,"%")
            break
        else:
            print("Both the candidates have equal number of votes..!")

    voter = int(input("Enter your voter id: "))
    if voter in voter_id:
        print("You can vote...")
        voter_id.remove(voter) #no repetition of voter so removing
        print("------------------------------------")
        print("press 1 to give vote to ",candidate1)
        print("press 2 to give vote to ",candidate2)
        print("------------------------------------")
        vote = int(input("Enter your vote here: "))
        if vote == 1:
            count1+=1
            print("Thank you for your response :)")

        elif vote == 2:
            count2+=1
            print("Thank you for your response :)")

        else:
            print("Wrong input key")


