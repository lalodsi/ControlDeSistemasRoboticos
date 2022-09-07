A=[0 1;-1 -4]; B=[0;1]; C=[1 0]; D=0;
W=[-5 1;1 0];
[num,den]=ss2tf(A,B,C,D);
tfsis=tf(num,den)
Co=ctrb(A,B); Ob=obsv(A,C);
n=length(A);

disp('los eigenvalores de A son: ')
eigenvalores=eig(A)
if real(eigenvalores)<=0
    disp('Es estable')
else
    disp('No es estable')
end


if rank(Co)==n
    disp('Es completamente controlable')
    % Obtenci?n de la FCC
    disp('Sistema en FCC')
    T=Co*W;iT=inv(T);
    Ac=iT*A*T 
    Bc=iT*B 
    Cc=C*T
else 
    disp('No es completamente controlable')
end
if rank(Ob)==n
    disp('Es completamente observable')
    Q=inv(W*Ob); iQ=W*Ob;
    Ao=iQ*A*Q 
    Bo=iQ*B 
    Co=C*Q
else 
    disp('No es completamente observable')
end


