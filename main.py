nominee_1 = input('enter the nominee 1 name : ')
nominee_2 = input('enter the nominee 2 name : ')

nom_1_votes = 0
nom_2_votes = 0

votes_id = [1,2,3,4,5,6,7,8,9,10]

num_of_voter = len(votes_id)

while True:

    if votes_id == []:
        if nom_1_votes > nom_2_votes:
            percent = nom_1_votes / num_of_voter * 100
            print(f'{nominee_1} has won by {percent:.2f} percent')
            break
        else:
          
            percent = nom_2_votes / num_of_voter * 100
            print(f'{nominee_2} has won by {percent:.2f} percent') 
            break
    
    else:
        voter = int(input('enter your voter id no: '))
        if voter in votes_id:
            print('you are a voter')
            votes_id.remove(voter)

            vote = int(input('enter your vote 1 or 2 : '))

            if vote == 1:
                nom_1_votes += 1 
                print('thank you for casting your vote')

            elif vote == 2:
                nom_2_votes += 1
                print('thank you for voting')
            
        else:
            print('your are not a voter or your have already voted')
            