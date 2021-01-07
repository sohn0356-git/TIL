print("start");
data=[98,87,90,34,56,43];
sum=0;
avg=0;
for d in data:
    sum+=d;
print(d)

avg = sum/len(data)
if avg>=90:
    print("A");
elif avg>=80:
    print("B");
elif avg>=70:
    print("C");
elif avg >= 60:
    print("D");
else:
    print("F");

print(sum);
