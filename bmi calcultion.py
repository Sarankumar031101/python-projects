import datetime
import random
import time
import sys
now = datetime.datetime.now()


  # Creating arrays for different muscle groups
chest_exercises = ["Push-ups", "Chest press", "Incline push-ups", "Decline push-ups", "Wide grip push-ups",
                   "Diamond push-ups", "Pike push-ups", "Chest fly", "Dips", "Chest squeeze",
                   "Cross-body mountain climbers", "Chest tap push-ups", "Plyometric push-ups", "Incline chest press",
                   "Clap push-ups", "Isometric chest squeeze", "Side-to-side push-ups", "Wall push-ups", "Box push-ups",
                   "One-arm push-ups"]

shoulder_exercises = ["Shoulder press", "Front raise", "Lateral raise", "Reverse fly", "Shrugs",
                      "Upright row", "Shoulder circles", "Scaption", "Rotator cuff exercises", "Arm circles",
                      "Shoulder taps", "Plank to push-up", "Pike walk", "Shoulder squeeze", "External rotations",
                      "Internal rotations", "Standing shoulder abduction", "Face pulls", "YTWL exercises",
                      "Shoulder stretches"]

biceps_exercises = ["Bicep curls", "Hammer curls", "Concentration curls", "Zottman curls", "Reverse curls",
                    "Drag curls", "Incline curls", "Preacher curls", "21s", "Isometric bicep squeeze",
                    "Spider curls", "Alternating curls", "Curl and press", "Bicep blaster", "Cross-body hammer curls",
                    "Wrist curls", "Plank curls", "Bodyweight bicep exercises", "Chin-ups", "Bar hangs"]

triceps_exercises = ["Tricep dips", "Tricep kickbacks", "Close grip push-ups", "Skull crushers", "Tricep extensions",
                     "Diamond push-ups", "Tricep press", "Overhead tricep extension", "Tricep squeeze", "Lying tricep extension",
                     "Tricep pushdowns", "Bench dips", "Dumbbell tricep dips", "Tricep rope pushdowns", "Kickbacks",
                     "Reverse grip pushdowns", "Bodyweight tricep exercises", "Tricep stretches", "Scorpion push-ups",
                     "Plank tricep dips"]

back_exercises = ["Pull-ups", "Chin-ups", "Lat pulldowns", "Dumbbell rows", "Bent-over rows",
                  "T-bar rows", "Single-arm rows", "Face pulls", "Deadlifts", "Good mornings",
                  "Hyperextensions", "Reverse fly", "Lat pushdowns", "Scapular retraction", "Supermans",
                  "Inverted rows", "Bodyweight back exercises", "Chest-supported rows", "Seated cable rows",
                  "Renegade rows"]

abs_exercises = ["Crunches", "Leg raises", "Russian twists", "Planks", "Mountain climbers",
                 "Bicycle crunches", "V-ups", "Hollow body hold", "Flutter kicks", "Side plank",
                 "Windshield wipers", "Reverse crunches", "Oblique crunches", "Dragon flags", "Toe touches",
                 "Lying leg raises", "Scissor kicks", "Sit-ups", "Twisting plank", "Roll-ups"]

leg_exercises = ["Squats", "Lunges", "Step-ups", "Calf raises", "Leg press",
                 "Deadlifts", "Leg curls", "Leg extensions", "Wall sit", "Box jumps",
                 "Sumo squats", "Jump squats", "Bulgarian split squats", "Hamstring curls", "Glute bridges",
                 "Side lunges", "Inner thigh lifts", "Outer thigh lifts", "Cossack squats", "Chair pose"]





def loading_animation(iterations, prefix='', suffix='', length=30, fill='█', print_end='\r'):  
    for i in range(iterations + 1):
        percent = int((i / iterations) * 100)
        bar = fill * int(length * i // iterations)
        spaces = ' ' * (length - len(bar))
        sys.stdout.write(f'\r{prefix}[{bar}{spaces}] {percent}% {suffix}')
        sys.stdout.flush()
        time.sleep(0.1)  # Adjust the sleep time for the desired speed
    print(print_end)

# Example usage





def person():
    name=input("name : ")
    age=int(input("age : "))
    w=int(input('enter your weight in kg : '))
    h1=float(input('ebter your height in cm : '))
    h=h1/100
    
    print('hello '+name+' please wait we are calculating...')
    print('\n')
    
    loading_animation(50, prefix='Progress:', suffix='Complete', length=50)
    print('\n')
    
    bmicalc(age,w,h)

def bmicalc(age,w,h):
    BMI=w/(h*h)
    print('yor bmi is: ',BMI)
    if(BMI>0):
        if(BMI<=16):
            print("You are very underweight")
            bw = "underweight"
        elif(BMI<=18.5):
            print("You are underweight")
            bw =  "underweight"
        elif(BMI<=25):
            print("Congrats! You are Healthy")
            bw = "Healthy"
        elif(BMI<=30):
            print("You are overweight")
            bw = "overwight"
        else: 
            print("You are very overweight")
            bw = "overweight"
    else:
        print("enter valid details")
    print('\n')
       
    excersice_diet(bw)
    
    
    
def excersice_diet(bw):
    v =(input('if you want excersice  and diet sugestion \n or \n Dont want sugestion (Y/N) :'))
    print('\n')
    if (bw == "underweight"):
        if(v=='y'or v=='Y'):
                print("""Eating nutritious foods that are high in calories is a good way to gain weight""")

                def select_elements(array):
                    return random.sample(array, 2)

                selected_elements_array1 = select_elements(chest_exercises)
                selected_elements_array2 = select_elements(shoulder_exercises)
                selected_elements_array3 = select_elements(biceps_exercises)
                selected_elements_array4 = select_elements(triceps_exercises)
                selected_elements_array5 = select_elements(back_exercises)
                selected_elements_array6 = select_elements(abs_exercises)
                selected_elements_array7 = select_elements(leg_exercises)


                print(now.strftime("Start your"+" "+"%A"+" "+"Excersise"))
                print('\n') 
                print("chest    excersise each excersise 15x3 reps :", selected_elements_array1)
                print('\n') 
                print("Shoulder excersise each excersise 15x3 reps :", selected_elements_array2)
                print('\n') 
                print("biceps   excersise each excersise 15x3 reps :", selected_elements_array3)
                print('\n') 
                print("triceps  excersise each excersise 15x3 reps :", selected_elements_array4)
                print('\n') 
                print("back     excersise each excersise 15x3 reps :", selected_elements_array5)
                print('\n') 
                print("abs      excersise each excersise 15x3 reps :", selected_elements_array6)
                print('\n') 
                print("leg      excersise each excersise 15x3 reps :", selected_elements_array7)
                print('\n') 


                     
               


    if (bw == "Healthy"):
        if(v=='y'or v=='Y'):
                print("""Eating nutritious foods that are high in calories is a good way to gain weight""")
                
                def select_elements(array):
                    return random.sample(array, 3)
    
                selected_elements_array1 = select_elements(chest_exercises)
                selected_elements_array2 = select_elements(shoulder_exercises)
                selected_elements_array3 = select_elements(biceps_exercises)
                selected_elements_array4 = select_elements(triceps_exercises)
                selected_elements_array5 = select_elements(back_exercises)
                selected_elements_array6 = select_elements(abs_exercises)
                selected_elements_array7 = select_elements(leg_exercises)
    
    
                print(now.strftime("Start your"+" "+"%A"+" "+"Excersise"))
                print('\n') 
                print("chest    excersise each excersise 15x3 reps :", selected_elements_array1)
                print('\n') 
                print("Shoulder excersise each excersise 15x3 reps :", selected_elements_array2)
                print('\n') 
                print("biceps   excersise each excersise 15x3 reps :", selected_elements_array3)
                print('\n') 
                print("triceps  excersise each excersise 15x3 reps :", selected_elements_array4)
                print('\n') 
                print("back     excersise each excersise 15x3 reps :", selected_elements_array5)
                print('\n') 
                print("abs      excersise each excersise 15x3 reps :", selected_elements_array6)
                print('\n') 
                print("leg      excersise each excersise 15x3 reps :", selected_elements_array7)
                print('\n') 
                
    
                
                     
        
                
    if (bw == "overweight"):
        if(v=='y'or v=='Y'):
                print("""Eating nutritious foods and concentrate on fat less (carbless food) is a good way to loss weight""")
                
                def select_elements(array):
                    return random.sample(array, 4)
    
                selected_elements_array1 = select_elements(chest_exercises)
                selected_elements_array2 = select_elements(shoulder_exercises)
                selected_elements_array3 = select_elements(biceps_exercises)
                selected_elements_array4 = select_elements(triceps_exercises)
                selected_elements_array5 = select_elements(back_exercises)
                selected_elements_array6 = select_elements(abs_exercises)
                selected_elements_array7 = select_elements(leg_exercises)
    
    
                print(now.strftime("Start your"+" "+"%A"+" "+"Excersise"))
                print('\n') 
                print("chest    excersise each excersise 15x3 reps :", selected_elements_array1)
                print('\n') 
                print("Shoulder excersise each excersise 15x3 reps :", selected_elements_array2)
                print('\n') 
                print("biceps   excersise each excersise 15x3 reps :", selected_elements_array3)
                print('\n') 
                print("triceps  excersise each excersise 15x3 reps :", selected_elements_array4)
                print('\n') 
                print("back     excersise each excersise 15x3 reps :", selected_elements_array5)
                print('\n') 
                print("abs      excersise each excersise 15x3 reps :", selected_elements_array6)
                print('\n') 
                print("leg      excersise each excersise 15x3 reps :", selected_elements_array7)
                print('\n') 
    
                
                     
person()
            
