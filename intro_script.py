# This is your first Python script!
# It shows how to use variables, functions, loops, and conditional logic.
# Don't worry if this looks confusing at first—each part is explained step by step.
# You can ask ChatGPT to explain *any* line of code to you.

# ---------- FUNCTIONS ----------

# A function is a reusable block of code.
# It takes input (called parameters), does something with it, and can return a result.
def calculate_weekly_leads(daily, days=5):
    """
    Calculates the number of leads over a work week.
    'daily' is how many leads per day.
    'days' is how many days you're working (default is 5).
    """
    return daily * days

# ---------- ENTRY POINT ----------

# This line tells Python to start by running the main function.
# It ensures this code runs only when the file is executed directly.
if __name__ == "__main__":
  
  # ---------- VARIABLES ----------
    
  # A variable stores information we can use later.
  # Here's a variable storing your name.
  name = "Tyrone"

  # Here's a variable storing your job title
  job_title = "Revenue Operations Analyst"

  # A number variable representing how many leads you generate per day
  daily_leads = 25

  # A list variable (think of it like a spreadsheet column with multiple values)
  lead_sources = ["LinkedIn", "Google Ads", "Webinar", "Referral"]

  # ---------- PRINTING VALUES ----------
  
  # This prints text to the screen. You can also include variables using f-strings.
  print(f"Hi {name}, welcome to your first Python script!")
  print(f"Your job title is: {job_title}")
  print(f"You're currently generating {daily_leads} leads per day.\n")

  # ---------- FOR LOOP ----------

  # A for loop repeats something for every item in a list.
  print("Here are your lead sources:")

  for source in lead_sources:
      print(f"- {source}")  # This line will repeat once for each lead source

  print("\n")

  # ---------- WHILE LOOP ----------

  # A while loop repeats something as long as a condition is true.
  # Let's say we want to simulate processing 3 new leads.
  leads_to_process = 3

  print("Processing new leads:")

  while leads_to_process > 0:
      print(f"Processing a lead... {leads_to_process} left.")
      leads_to_process -= 1  # This subtracts 1 from the variable each time

  print("All leads processed!\n")

  # ---------- CONDITIONAL STATEMENTS ----------

  # These let you make decisions in your code.
  # Let's say we want to give feedback based on how many leads are being generated.
  if daily_leads > 30:
      print("Great job! You're generating a lot of leads.")
  elif daily_leads >= 15:
      print("You're doing well! Keep pushing to hit 30.")
  else:
      print("Let’s explore ways to increase lead generation.")

  print("\n")

  # ---------- USING A FUNCTION ----------

  # Now we'll call the function we defined at the top of the file
  weekly_leads = calculate_weekly_leads(daily_leads)

  print(f"If you generate {daily_leads} leads per day, you'll generate {weekly_leads} leads in a 5-day week!")

  # ---------- END ----------

  print("\n🎉 Congratulations on running your first Python script!")
