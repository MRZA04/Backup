import os
import time
import sys

def UserInputs():
  global AGE, HEIGHT, WEIGHT, CALORIES, GENDER, GOAL, EXERCISE, BMIHEIGHT, BMI
  print("INPUT AGE: ")
  AGE = int(input())
  time.sleep(2)

  print("1. MALE | 2. FEMALE: ")
  GENDER = int(input())
  time.sleep(2)

  print("ENTER HEIGHT: (CM)")
  HEIGHT = float(input())
  time.sleep(2)

  print("ENTER WEIGHT: (KG)")
  WEIGHT = float(input())
  time.sleep(2)

  print("WHAT IS YOUR DAILY CALORIE INTAKE: ")
  CALORIES = int(input())
  time.sleep(2)

  print("WHAT IS YOUR FITNESS GOAL | 1. MAINTIN | 2. CUT | 3. BULK |: ")
  GOAL = int(input())
  time.sleep(2)

  print("HOW PHYSICALLY ACTIVE ARE YOU: 1. Sedentary(0) | 2. lightly active (30 min) | 3. Moderately Active (1 hour) | 4. Very Active (2 hour) | 5. Extra Active (2+ Hours)")
  EXERCISE = int(input())
  time.sleep(2)

  BMIHEIGHT = HEIGHT / 100
  BMI = WEIGHT / (BMIHEIGHT * BMIHEIGHT)
  
  BMRcalc()
  os.system('cls')
  Output()



def BMRcalc():
  global BMR, xBMR
  if GENDER == 1:  # Male
    BMR = 66 + (13.7 * WEIGHT) + (5 * HEIGHT) - (6.8 * AGE)
    if EXERCISE == 1:
      xBMR = BMR * 1.2
    elif EXERCISE == 2:
      xBMR = BMR * 1.375
    elif EXERCISE == 3:
      xBMR = BMR * 1.55
    elif EXERCISE == 4:
      xBMR = BMR * 1.725
    elif EXERCISE == 5:
      xBMR = BMR * 1.9

  elif GENDER == 2:  # Female
    BMR = 655 + (9.6 * WEIGHT) + (1.8 * HEIGHT) - (4.7 * AGE)
    if EXERCISE == 1:
      xBMR = BMR * 1.2
    elif EXERCISE == 2:
      xBMR = BMR * 1.375
    elif EXERCISE == 3:
      xBMR = BMR * 1.55
    elif EXERCISE == 4:
      xBMR = BMR * 1.725
    elif EXERCISE == 5:
      xBMR = BMR * 1.9


def Output():
  global CUTBMR, BULKBMR, RETURN
  if BMI < 20.6:
    print("BMI: ",BMI, "UNDERWEIGHT")
  elif BMI < 25:
    print("BMI: ",BMI, "HEALTHY WEIGHT")
  elif BMI < 32:
    print("BMI: ",BMI, "OVERWEIGHT")
  elif BMI < 40.4:
    print("BMI: ",BMI, "OBESE")
  elif BMI >= 40.5:
    print("BMI: ",BMI, "MORBIDLY OBESE")

  print("BMR: ",BMR,)
  print ("Recommended Daily Calorie intake for how often you exercise: ",xBMR)
  if GOAL == 1:
    print(CALORIES, "For maintaining, you should aim for", BMR,
          "calories per day")
  elif GOAL == 2:
    CUTBMR = xBMR - 500
    print("Your Daily Calorie Intake:", CALORIES)
    print("For cutting, you should aim for", CUTBMR, "calories per day")
  elif GOAL == 3:
    BULKBMR = xBMR + 500
    print("Your Daily Calorie Intake:", CALORIES)
    print("For Bulking, you should aim for", BULKBMR, "calrories per day")

  if AGE < 5 and AGE >= 3:
    print("Aim for Consistent Physical Exercise Throughout the Day")
  elif AGE < 17 and AGE >= 6:
    print("Aim for at least an HOUR or more of exercise a day")
  elif AGE >= 18:
    print("Aim for at least 2.5 hours of exercise a week")
    
  print("\n\n\nENTER 0 TO RETURN TO MAIN MENU: ")
  RETURN = int(input())
  if RETURN == 0:
    MainMenu()
  else:
    MainMenu()
  
    
def Info():
  global Home
  print ("BASIC INFORMATION:\n\n")
  print ("BMI:\n")
  print ("The body mass index, BMI, is a system used to estimate an individual's health and fitness.\nIt is able to do this by using an equation which takes divides an individual's weight by their height.")
  print ("BMI = WEIGHT / HEIGHT^2\n\n")
  print ("BMR:\n")
  print ("BMR, Basal Metabolic Rate, is a series of calculations that estimate the number of calories an individual burns in a day")
  print ("MEN: BMR = 66 + (13.7 x weight in kg) + (5 x height in cm) - (6.8 x age in years)")
  print ("WOMEN = BMR = 655 + (9.6 x weight in kg) + (1.8 x height in cm) - (4.7 x age in years)\n\n")
  print ("MAINTAINING BODY WEIGHT:\n")
  print ("Maintiaining body weight refers to the idea of staying at the same weight over a period of time.\nIn order to maintain body weight, you need to ensure the number of calories you intake is the same as the amount you burn.\n\n")
  print ("CUTTING:\n")
  print ("Cutting is the concept of lowering your body fat by sticking in a calorie deficit.\nThis means ensuring that your calorie intake is lower than the amount of calories you burn, roughly 500 to be safe\n\n")
  print ("BULKING:\n")
  print ("Bulking is almost the opposite of cutting, the aim is to get increase muscle mass by increasing calorie intake.\n")
  print ("PRESS ENTER TO RETURN TO MENU")
  Home = (input())
  if Home == "":
    MainMenu()
  else:
    MainMenu()
    
    
def MainMenu():
  global Option
  os.system('cls')
  print ("FITNESS CALCULATOR")
  print ("1) BASIC INFORMATION")
  print ("2) CALCULAOR")
  print ("0) EXIT")
  print ("ENTER MENU OPTION: ")
  Option = (input())
  if Option == "1":
    os.system('cls')
    Info()
  elif Option == "2":
    os.system('cls')
    UserInputs()
  elif Option == "0":
    sys.exit()
  else:
    os.system('cls')
    print("INVALID OPTION, TRY AGAIN")
    MainMenu()
    

MainMenu()