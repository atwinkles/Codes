function y = bisec(f,a,b,T,S)
% y = bisect(f,a,b,D,E)
%This is a bisection algorithm by Alexander Winkles used to find roots of 
% polynomials over a domain.
%
% f : the function being evaluated
% a : the lower domain value
% b : the upper domain value
% T : the tolerance of the final result
% S : the number of iterations


if sign(feval(f,a))==sign(feval(f,b))
    disp('Error: f(a) and f(b) have the same signs.');
else
    i = 0;
    while i <= S
        e = b - a;
        e = e/2;
        c = a + e;
        if feval(f,c) == 0 || abs(feval(f,c)) < T
            y = c;
            fprintf('\nThe solution is %d.\n The computation was a success after %d iterations!',y,i)
            break;
        end;
        i = i+1;
        if sign(feval(f,a))==sign(feval(f,c))
            a = c;
        else
            b = c;
        end;
    end;
    if i == S+1
        fprintf('Method failed after %d iterations.',S)
    end;
end;
    