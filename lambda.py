lambda_list = [lambda х: х + 1,
	lambda х: х * 2,
	lambda х: х ** 3]
for i in lambda_list:
	print(i(2)) #выполняются все lamda-функции

print(lambda_list[0](4)) #выполняется конкретная lamda-функция