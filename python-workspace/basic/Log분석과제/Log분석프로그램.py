

location = "d:/Lecture/python-workspace/basic/Log분석과제/data/log.txt"



countI = 0
countW = 0
countE = 0

#1번
#file = open(location, 'r')


#2번
#with open(location, 'r',encoding='utf-8') as file:
#    data = file.read()
#    print(data)
    
#3번
# with open(location, 'r',encoding='utf-8') as file:
#     for _ in range(47):
#         data = file.readline().strip('\n')
#         if "INFO" in data:
#             countI += 1
            
#         elif "WARNING" in data:
#             countW += 1
            
#         elif "ERROR" in data:
#             countE += 1
    
#     print(f'INFO : {countI}')
#     print(f'WARING : {countW}')    
#     print(f'ERROR : {countE}')    

#4번
# counts = {f"2026-03-0{i}": 0 for i in range(1, 9)}

# with open(location, 'r', encoding='utf-8') as file:
#     for _ in range(47):
#         data = file.readline() 

#         
#         for date in counts:
#             if date in data:
#                 counts[date] += 1
#                 break 

# 
# for i in range(1, 9):
#     date_key = f"2026-03-0{i}"
#     print(f"{i}일 : {counts[date_key]}")


#5번
# with open(location, 'r', encoding='utf-8') as file:
#     for _ in range(47):
#         data = file.readline().strip('\n')
#         if "ERROR" in data:
#             print(data)   

#6번
# level = input()
# with open(location, 'r', encoding='utf-8') as file:
#     for _ in range(47):
#         data = file.readline().strip('\n')

#         if level in data:
#             print(data)

#7번
# date = input()
# with open(location, 'r', encoding='utf-8') as file:
#     for _ in range(47):
#         data = file.readline().strip('\n')
#         if date in data:
#             print(data)

#8번
# list = []
# with open(location, 'r', encoding='utf-8') as file:
#     for _ in range(47):
#         data = file.readline().strip('\n')
#         if "INFO" in data:
#             countI += 1
            
#         elif "WARNING" in data:
#             countW += 1
            
#         elif "ERROR" in data:
#             countE += 1

#     list.append(countI)
#     list.append(countW)
#     list.append(countE)
#     if max(list) == countI:
#         print(f"가장 많이 발생한 로그는 INFO : {countI}")
#     elif max(list) == countW:
#         print(f"가장 많이 발생한 로그는 WARNING : {countW}")
#     elif max(list) == countE:
#         print(f"가장 많이 발생한 로그는 ERROR : {countE}")
    
# 9번
# counts = {f"2026-03-0{i}": 0 for i in range(1, 9)}
# with open(location, 'r', encoding='utf-8') as file:
#     for _ in range(47):
#         data = file.readline().strip('\n')

#         for date in counts:
#             if date in data and "ERROR" in data:
#                 counts[date] += 1
#                 break
#     max_error_date = max(counts, key=counts.get)
# print(f"가장 에러가 많은 날짜: {max_error_date} (에러 횟수: {counts[max_error_date]}회)")      


#10번
# result_text = print(f"가장 에러가 많은 날짜: {max_error_date} (에러 횟수: {counts[max_error_date]}회)")    
# with open(location, 'w', encoding='utf-8') as file:
#     file.write(result_text)

#11번
# count1 =0
# count2 =0
# hour_list = []
# with open(location, 'r', encoding='utf-8') as file:
#     for _ in range(47):
#         data = file.readline().strip('\n')
#         if not data:
#             continue
#         time = data[11:19].split(":")
#         hour = int(time[0])
#         if hour < 12:
#             count1 += 1
#         elif hour >= 12:
#             count2 += 1
    
#     print(f"오전 로그는 : {count1}, 오후 로그는 : {count2}")

#12번
# with open(location, 'r', encoding='utf-8') as file:
#     for _ in range(47):
#         line1 = file.readline() 
#         line2 = file.readline() 
#         if "ERROR" in line1 and "ERROR" in line2:
#             print(line1,line2)
    

#13번 

# msg = input()
# umsg = msg.upper()
# print(msg)
# with open(location, 'r', encoding='utf-8') as file:
#     for _ in range(47):
#         data = file.readline().strip("\n")

#         if umsg in data :
#             print(data)


#14번
# log_set = set()
# with open(location, 'r', encoding='utf-8') as file:
#     for _ in range(47):
#         data = file.readline().strip("\n")
#         if not data:
#             continue
#         log = data.split(",")
#         log_set.add(log[1])
#     print(len(log_set))

#15번 
# file = open(location, 'r')
# file.close()


       



