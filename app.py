import time
import requests

#http://localhost:3000
#https://api.stg.gistalk.gistory.me

lecture_name = []

lecture_code = []

prof_name = []

diff = []
lots = []

helpful = 

# print(len(diff))
# print(len(lots))
# print(len(helpful))
# print(len(interest))
# print(len(strength))
# print(len(satisfy))
# print(len(oneline))

# for i in range(0, 470):
#     print(str(i) + "번째 시도 시작##############################################################################")
#     payload_P = {"lecture_code" : lecture_code[i], "lecture_name" : lecture_name[i], "prof_name" : prof_name[i]}
#     r = requests.post('url/lectures/add', data=payload_P)
#     print(r.json())
#     print(str(i) + "번째 시도 완료###############################################################################")

r = requests.get('url/lectures/getting'+lecture_code[34])
source = r.json()
src = source["id"]
print(source)
print('\n')
print(src)

#강의 평가 추가 api
# payload_R = {
#     "difficulty" : "1",
#     "strength" : "1",
#     "helpful" : "1",
#     "interest" : "1",
#     "lots" : "1",
#     "satisfy" : "1",
#     "oneline" : "한줄평123",
#     "user" : "user122",
#     "lecture_id" : "13"
# }

# r2 = requests.post('http://localhost:3000/records/add', data=payload_R)

# print(r2.json())







