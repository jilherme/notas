format short e

f = @(x) x^2*sin(x);
fl = @(x) 2*x*sin(x) + x^2*cos(x);

x=pi/3;
eax=0.1
erx = eax/abs(x)

eay = abs(fl(x))*eax
ery = eay/abs(f(x))


