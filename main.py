import jellyfish

returntorun=False
alterg=['30 --> 40 minutes at 70-85% bodyweight','30-->60 minutes at 70-->85% bodyweight', '40-60 minutes at 75-90% bodyweight', '60-75 minutes at 75-90% bodyweight', '60-90 minutes at 75-90% bodyweight','60-90 minutes at 75-90% bodyweight','60-90 minutes at 75-90% bodyweight at a tempo pace every other day','60-90 minutes at 75-90% bodyweight at a tempo pace every other day']
print('Welcome to the return to run program originally created by Dr. Amol Saxena and coded by Kyan Agdassi')
injury_list=['foot stress fracture', 'plantar fasciitis', 'ankle sprain','high ankle  sprain', 'ankle surgery']
injury_return_times=['4-6 weeks', '1-3 weeks', '4-8 weeks', '6-10 weeks', '2-14 days']
return_to_run_parameters=['Walk on flat ground, up stairs, down stairs','Air Squats x10','Alternating lunge x10','Double Leg Heel Raise x20','Single Leg Heel Raise x10','Run on spot 10 seconds (knee to hip height)', 'Double Leg Hop (X20 up and down, X20 swivel, X20 side to side)','Single Leg Hop (X10 up and down, X10 swivel, X10 side to side)','Run drills (Ankling x20m x2, A Skip x20m x2, B Skip x20m x2, Straight Leg x20m, Stride 40m x3)']
injury=''
yesorno=''
yesnolst=['yes','no']
while injury_list.count(injury)==0:
  injury_similarity_list=[]
  injury=input('Please enter your foot injury\n(ex: foot stress fracture, plantar fasciitis,\nankle sprain, high ankle sprain, ankle surgery): ')
  if injury_list.count(injury)==0:
    for i in range(len(injury_list)):
      injury_similarity_list.append(jellyfish.jaro_distance(injury, injury_list[i]))
    max_index=injury_similarity_list.index(max(injury_similarity_list))
    yesorno=input('Did you mean to type %s? '%(injury_list[max_index]))
    if yesorno.lower()=='yes':
      injury=injury_list[max_index]
counter=0
able_to_run=input('Has it been at least %s since your\ninjury and have you had clearance by a healthcare\nprofessional to start returning to sports? ' %(injury_return_times[injury_list.index(injury)]))

yesorno=''
if able_to_run.lower()=='yes':
  while yesorno.lower()!='yes' and counter<len(return_to_run_parameters):
    if counter==0:
      print('Welcome to return to run!\nIf you are able to do all 9 steps pain free, you can begin your return to running.')
    print('\nStep %s: %s.' %(str(counter+1), return_to_run_parameters[counter]))
    yesorno=input('Was there any pain? ')
    if yesorno.lower()!='no' and yesorno.lower!='yes':
      while yesorno.lower() not in yesnolst:
        yesorno=input('Was there any pain? ')
    counter+=1
  if counter==len(return_to_run_parameters) and yesorno.lower()=='no':
    print('\nCongratulations! You are able to start the process of returning to running.')
    returntorun=True
  else:
    print('Unfortunately, you are currently unable to start the process of returning to running. Continue to rest and ice your injury until you are able to complete all 9 steps. Get better soon!')
else:
  print('\nUnfortunately, you are currently unable to start the process of returning to running. Continue to rest and ice your injury until you are able to complete all 9 steps. Get better soon!')

if returntorun:
  yesorno='yes'
  counter=0
  while yesorno.lower()=='yes' and counter<len(alterg):
    if counter==0:
      print('Great! You are ready to start the return to running.\nFor each week, you will be guided through Alter G training.')
    print('\nWeek %s: %s' %(str(counter+1),alterg[counter]))
    counter+=1
    yesorno=input('Would you like to view week %s? (yes or no) ' %(str(counter+1)))
    if yesorno.lower()!='no' and yesorno.lower!='yes':
      while yesorno.lower() not in yesnolst:
        yesorno=input('Would you like to view week %s? (yes or no) ' %(str(counter)))




  