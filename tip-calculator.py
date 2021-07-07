welcome = "Welcome to the tip calculator."
stars = len(welcome) * ("*")
print(stars, "\n", welcome,"\n", stars)

def questions():
  while True:
    try:
      total = float(input("What's the total bill?\n$"))
      tip = int(input("What percentage tip would you all like to give? 10, 12, 15, or 20\n"))
      people = int(input("How many people to split the bill?\n"))
      calculate_total_tip = ((total * tip) / 100)
      tip_and_bill = float(total / people) + (calculate_total_tip/ people)
      final_amount = round(tip_and_bill, 2)
      print(f'Each person should pay ${final_amount}.')
      break
    except ValueError:
      print("Oops! Something went wrong. Try using numbers only.\n")
      continue

questions()