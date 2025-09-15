# Career Guidance Chatbot - CareerGuru
# A simple Python chatbot to guide students about career options after 10th, 12th, and B.Tech.

import time

def bot_print(message):
    """Print bot messages with a typing effect"""
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

def main():
    bot_print("🤖 Welcome to CareerGuru - Your Career Guidance Chatbot!")
    bot_print("You can ask me about career options after 10th, 12th, or B.Tech.")
    bot_print("Type 'exit' anytime to quit.\n")

    while True:
        user_input = input("You: ").lower()

        # --- After 10th ---
        if "10th" in user_input:
            bot_print("Bot: After 10th, you can choose from these major streams:")
            bot_print(" • MPC (Maths, Physics, Chemistry) → Engineering, Architecture, Defense, etc.")
            bot_print(" • BiPC (Biology, Physics, Chemistry) → Medicine, Pharmacy, Agriculture, etc.")
            bot_print(" • CEC (Civics, Economics, Commerce) → B.Com, CA, Law, etc.")
            bot_print(" • MEC (Maths, Economics, Commerce) → Business, Banking, Management, etc.")
            bot_print(" • Vocational Courses → Polytechnic, ITI, Skill training, etc.")
            bot_print(" • Diploma options in Engineering, Agriculture, etc.")

        # --- After 12th ---
        elif "12th" in user_input:
            bot_print("Bot: After 12th, you have many paths depending on your stream:")
            bot_print(" • Engineering (B.Tech, B.E.)")
            bot_print(" • Medicine (MBBS, BDS, B.Pharm, Nursing, etc.)")
            bot_print(" • Commerce (B.Com, CA, CS, CMA, BBA, etc.)")
            bot_print(" • Arts (BA, Journalism, Psychology, etc.)")
            bot_print(" • Law (BA LLB, BBA LLB)")
            bot_print(" • Design & Creative fields (Fashion, Interior, Animation, Multimedia)")
            bot_print(" • Defense (NDA, Navy, Airforce)")
            bot_print(" • Hotel Management, Agriculture, Veterinary Sciences")

        # --- After B.Tech ---
        elif "b.tech" in user_input or "btech" in user_input:
            bot_print("Bot: After B.Tech, you can choose:")
            bot_print(" • Higher Studies → M.Tech, MS, MBA")
            bot_print(" • Jobs → IT, Core Engineering, Public Sector, Startups")
            bot_print(" • Government Exams → UPSC, SSC, State PSC, GATE, etc.")
            bot_print(" • Research → PhD, Research Labs, Teaching")
            bot_print(" • Entrepreneurship → Start your own business")
            bot_print(" • Skill-based Courses → Data Science, AI, ML, Cloud, Cybersecurity")

        # Exit condition
        elif "exit" in user_input or "quit" in user_input:
            bot_print("Bot: Thank you for using CareerGuru! 👋 Good luck with your future.")
            break

        # Default response
        else:
            bot_print("Bot: Sorry, I can only guide for careers after 10th, 12th, or B.Tech. Please try again.")

if __name__ == "__main__":
    main()

