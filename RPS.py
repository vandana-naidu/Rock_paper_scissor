
import random
def rock_paper_scissor(comp_pick,user_pick):
    user_score=0
    comp_score=0
    while True:
        comp_pick = random.randint(1, 3)
        if comp_pick == 1:
            comp_pick = "rock"
        if comp_pick == 2:
            comp_pick = "paper"
        if comp_pick == 3:
            comp_pick = "scissor"

        user_pick = input("enter rock/paper/scissor:  enter 'q' to quit ").lower()

        if user_pick==comp_pick:
            print("ur guess and comp guess are same.., so guess again")
        elif user_pick=="rock" and comp_pick=="scissor":
            print("you won..,your guess was:",user_pick,"and computer guess was:",comp_pick,)
            user_score+=1
        elif user_pick=="paper" and comp_pick=="rock":
            print("you won..,your guess was:",user_pick,"computer guess was:",comp_pick)
            user_score+=1
        elif user_pick=="scissor" and comp_pick=="paper":
            print("you won..,your guess was:",user_pick,"computer guess was:",comp_pick)
            user_score+=1
        elif user_pick=="q":
            print("quitting..,")
            quit()
        else:
            print("computer won ..,you guess was:",user_pick,"and computer guess was:",comp_pick)
            comp_score+=1
            print("guess again")
        print("Total score of user:", user_score)
        print("Total score of computer:", comp_score)




if __name__ == "__main__":
    instructions = """-->In this game computer will have a randomly guess either rock/paper/scissor
-->you have to guess and enter one among rock/paper/scissor
-->when your guess is rock and computer guess is scissor.., you will win
-->when your guess is paper and computer guess is rock.., you will win
-->when your guess is scissor and computer guess is paper.., you will win
-->in the other cases.., computer will win
-->and for each correct guess you will get 1 point"""
    print(instructions)
    comp_pick=""
    user_pick=""
    rock_paper_scissor(comp_pick,user_pick)

