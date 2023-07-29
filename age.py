driving = input('Have you ever driven a car before? ')
if driving != 'yes' and driving != 'no': # !=表示不等於
	print('Sorry, please answer the question above in yes or no.')
	raise SystemExit #表示程式終止

age = input('How old are you? ')
if driving == 'yes':
	if int(age) >= 18:
		print('You pass the test.')
	else:
		print('You fail the test.')
elif driving == 'no':
	if int(age) >= 18:
		print('You can sign for your driver license test now.')
	else :
		print('you can have your driver license test few years later.')