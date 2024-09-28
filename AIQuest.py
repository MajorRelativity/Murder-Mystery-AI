import random

def choose_random_name():
    name_list = ["Gavin", "Alyssa", "Mary", "Ebenezer", "Bridgette", "Tobias", "Leona", "Franklin", "Annie", "Blake", "Beth", "Barnaby", "Brie", "Elijah", "Aubrey"]
    return(random.choice(name_list))
    
def choose_random_job():
    job_list = ["Librarian", "Farmer", "Fisherman", "Banker", "Artist", "Mayor", "Doctor", "Maid", "Miner", "Hunter", "Barber", "Carpenter", "Mailman", "Baker", "Trader"]
    return(random.choice(job_list))

def choose_random_traits():
    trait_list = ["Kind", "Arrogant", "Friendly", "Smart", "Confident", "Loyal", "Strong", "Mad", "Sad", "Decisive"]
    return(random.choice(trait_list))

def choose_motive(victim):
    motive_list = [f"I loved {victim} but they didn't love me back", "I wanted their land", f"{victim} was blackmailing me", f"{victim} saw me stealing bread", f"{victim} dated the person I love", "I got paid to do it", f"{victim} creeped me out", f"{victim} wouldn't stop bothering me for the debt I owed", "I wanted to be noticed", f"I discovered {victim} caused the accident that killed my father"]
    return(random.choice(motive_list))

def choose_relation():
    relation_list = ["Lover", "Friend", "Sibling", "Neighbor", "Renter", "Employee"]
    return(random.choice(relation_list))

def get_murder_status(i, mrdrordr, murder_method):
    if i == mrdrordr:#i will be the i in the for loop that controls the number of people talked to
        return f"the murderer and you're trying to hide that fact and you murdered the victim with {murder_method}."
    return "not the murderer"

def construct_gpt_prompt(name, job, traits, motive, relation, murder_status):
    return(f"You are {name} who works as a {job} and is {traits}. You are the victim's {relation}. You are {murder_status}. Your motive was {motive}.")
    
def construct_user_prompt(name, job, relation):
    return(f"My name is {name} and I work as a {job}. I was the victim's {relation}.")

def get_user_guess():
    print("Enter the name of who you think the murderer is: ")
    user_guess = input()
    return user_guess

def check_user_guess(user_guess, character_list, mrdrorder):
    if user_guess == character_list[mrdrorder - 1]:
        #return "Congrats! You found the murderer!"
        return True
    #return "Sorry you accused an innocent person."
    return False

def print_outro(result, user_guess, victim, motive):
    if result == True:
        print(f"You methodically pieced together all the information. By focusing on the answer you were given you were able to correctly deduce who was the murderer. {user_guess} confesses that they killed {victim} because {motive}. With the truth unveiled and justice served Pebblebrook can begin to heal again though it will never be the same.")
    print(f"You wrongly accused {user_guess} of being a murderer. Though they had a strong motive, they refused to go that far. {victim}'s murderer will run free and Pebblebrook will have to try to heal without closure.")

def main():
    character_list = []
    for i in range(5):
        name = choose_random_name()
        victim = choose_random_name()
        character_list.append(name)#need a list of who user has talked to to check user guess
        job = choose_random_job()
        traits = choose_random_traits()
        motive = choose_motive(victim)
        relation = choose_relation()
        murder_status = get_murder_status(i, 3, "poison")#need murder order from Emma
        construct_gpt_prompt(name, job, traits, motive, relation, murder_status)#need murder_method from Emma
        construct_user_prompt(name, job, relation)
    user_guess = get_user_guess()
    result = check_user_guess(user_guess, character_list, 3)#need murder order from Emma
    print_outro(result, user_guess, victim, motive)
main()