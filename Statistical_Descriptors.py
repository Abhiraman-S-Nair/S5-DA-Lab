n = int(input("Enter the no of inputs: "))
inpt = input("Enter your elements seperated by spaces: ")
dat = [int(j) for j in inpt.split()]
dat.sort()

mean = sum(dat) / len(dat)
median = dat[(len(dat) // 2)]

mean_dat = "The mean of the given data is : " + str(mean)
median_dat = "The median of the given data is : " + str(median)

cpy = list(set(dat))
max = 0
cnt = {}
mode = []
for i in cpy:
  cnt[i] = dat.count(i)
for i in cpy:
  if dat.count(i) > max:
    max = dat.count(i)
for i in cpy:
  if dat.count(i) == max:
    mode.append(i)
if len(mode) == 1:
  mode_dat = "Data is Unimodal and mode is : " + str(mode)
elif len(mode) == 2:
  mode_dat = "Data is Bimodal and modes are : " + str(mode)
elif len(mode) == 3:
  mode_dat = "Data is Trimodal and modes are : " + str(mode)
else:
  mode_dat = "Data is Multimodal and modes are : " + str(mode)

left = dat[ : len(dat)//2]
right = dat[len(dat)//2+1 : ]
q1 = left[len(left)//2]
q3 = right[len(right)//2]
iqr = q3 - q1
quartile_dat = "The quartiles are : Q1 = " + str(q1) + " Q2 = " + str(median) + " Q3 = " + str(q3) + " and the IQR is : " + str(iqr) 
outliers = []
for i in dat:
  if i < q1 - 1.5 * iqr or i > q3 + 1.5 * iqr:
    outliers.append(i)
if len(outliers) == 0:
  outlier_dat = "There are no outliers"
else:
  outlier_dat = "The outliers are : " + str(outliers)

print("The Statistical Descriptors are as follows :-")
print("\n" + mean_dat + "\n" + median_dat + "\n" + mode_dat +"\n" + quartile_dat + "\n" + outlier_dat)
  

  

