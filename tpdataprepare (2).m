load F:/importantfilecopy/tandomrepeat/newtry/results1
A = results1(:,1:9)
X = results1(:,1:8)
B = zeros(264,4)
t = results(:,9)
for i = 1:length(t)
    if t(i) == 1
        B(i,1)=1;
    end
    if t(i) == 2
        B(i,2)=1;
    end 
    if t(i) == 3
        B(i,3)=1;
    end 
    if t(i) ==4
        B(i,4)=1;
    end
end
t = B'
N = 264
C = 4
D = 8
save tpcompare1

        
% % A = result
% % normalized_data = mapminmax(results(:,1:8),0,1)
% % A = A./repmat(sqrt(sum(A.^2,1)),size(A,1),1);
% 
% y = mapminmax(A',0,1)
% 
% % [dim,num] = size(A)
% % tic
% % for i = 1:num
% %     A(:,i) = A(:,i)/norm(A(:,1));
% % end 
% % t1 = toc
% % for i = 1 : num
% % 
% %    X(:,i) = X(:,i) / norm(X(:,i)) ;
% % A(A==0)=0.025
% y(isnan(y)) = 0 
% y(y==0)=0.0125
% % t = results(:,9)
% % t(t~=3)=0
% % t(t==3)=1
% % normalized_data(normalized_data==0)=0.275
% m = [y',round(t)]
% % m(m==0)= 0.125
% m

