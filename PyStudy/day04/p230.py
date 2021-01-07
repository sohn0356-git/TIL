

st = [{'id':'st1','ko':90,'en':100,'ma':99},
      {'id':'st2','ko':92,'en':80,'ma':100},
      {'id':'st3','ko':95,'en':70,'ma':86}
]

total_score = {}
for s in st:
    print(s['id']+"의 성적 평균은 : %.2f" %((s['ko']+s['en']+s['ma'])/3))
    for k,v in s.items():
        if k!='id':
            if k in total_score:
                total_score[k] += v
            else:
                total_score[k] = v

print("전체 학생의 과목 별 평균 : KO(%.2f) EN(%.2f) MA(%.2f)"
      %(total_score['ko']/len(st),total_score['en']/len(st),
        total_score['ma']/len(st)))