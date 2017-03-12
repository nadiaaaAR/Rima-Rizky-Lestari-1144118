import time
start_time = time.time()
print("menghitung nilai rumus matematika menggunakan bahasa korea")
s = raw_input("Masukan Nilai 1: ")
e = raw_input("Masukan Nilai 2: ")
h = raw_input("Masukan Nilai 3: ")
u = raw_input("Masukan Nilai 4: ")
n = raw_input("Masukan Nilai 5: ")

if s == 'hana':
	s=1

if s == 'dul':
	s=2

if s == 'set':
	s=3

if s == 'net':
	s=4

if s == 'dhasot':
	s=5

if s == 'yosot':
	s=6

if s == 'ilghop':
	s=7

if s == 'yodhol':
	s=8

if s == 'ahop':
	s=9

if s == 'zero':
	s=0


if e == 'hana':
	e=1

if e == 'dul':
	e=2

if e == 'set':
	e=3

if e == 'net':
	e=4

if e == 'dhasot':
	e=5

if e == 'yosot':
	e=6

if e == 'ilghop':
	e=7

if e == 'yodhol':
	e=8

if e == 'ahop':
	e=9

if e == 'zero':
	e=0

if h == 'hana':
	h=1

if h == 'dul':
	h=2

if h == 'set':
	h=3

if h == 'net':
	h=4

if h == 'dhasot':
	h=5

if h == 'yosot':
	h=6

if h == 'ilghop':
	h=7

if h == 'yodhol':
	h=8

if h == 'ahop':
	h=9

if h == 'zero':
	h=0


if u == 'hana':
	u=1

if u == 'dul':
	u=2

if u == 'set':
	u=3

if u == 'net':
	u=4

if u == 'dhasot':
	u=5

if u == 'yosot':
	u=6

if u == 'ilghop':
	u=7

if u == 'yodhol':
	u=8

if u == 'ahop':
	u=9

if u == 'zero':
	u=0


if n == 'hana':
	n=1

if n == 'dul':
	n=2

if n == 'set':
	n=3

if n == 'net':
	n=4

if n == 'dhasot':
	n=5

if n == 'yosot':
	n=6

if n == 'ilghop':
	n=7

if n == 'yodhol':
	n=8

if n == 'ahop':
	n=9

if n == 'zero':
	n=0


jumlah =(s*e)+(h/u-n)
print ("hasil" , jumlah)
print("time : %s detik " % (time.time() - start_time))
