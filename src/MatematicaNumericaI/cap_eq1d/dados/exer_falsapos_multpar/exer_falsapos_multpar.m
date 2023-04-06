pkg load symbolic
syms x
f = @(x) (-x.^2+1.154*x-0.332929).*cos(x)+x.^2-1.154*x+0.332929;
fl = function_handle(diff(f(x)))

a=0.55;
b=0.65;
x0=0;
for k=1:30
  x = a - (b-a)/(fl(b)-fl(a))*fl(a);
  printf("%d %1.5E\n",k,x)
  if ((fl(x)==0) | (abs(x-x0)<1e-4))
    disp('aprox. encontrada')
    break;
  elseif (fl(a)*fl(x)>0)
    a=x;
  else
    b=x;
  end
  x0=x;
endfor
printf("%1.6E\n",x)