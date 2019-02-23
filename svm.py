import sklearn
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

def load_data():
    f = open('F:/importantfilecopy/tandomrepeat/2019.121test/results', 'r')
    # f = open('F:/importantfilecopy/tandomrepeat/3/1x/total.txt', 'r')
    data_set = []
    label_set = []
    for line in f:
        line = line.strip().split("\t")
        line_list = line[0].strip().split(" ")
        data_set.append(line_list)
        label_set.append(line[1])
    return data_set, label_set

if __name__ == "__main__":
    #     svm_baseline()
    data, label = load_data()
    X_train,X_test,y_train,y_test = train_test_split(data,label,test_size=0.3,random_state=0)

    for i in range(len(data)):
        label[0] = (int)(label[0])
        for j in range(len(data[i])):
            data[i][j] = (float)(data[i][j])
    model_svc = svm.SVC(C=8.0, kernel='rbf', gamma=1,cache_size=8000,probability=False)
    model_svc.fit(X_train, y_train)
    scoring = 'accuracy'
    scores = cross_val_score(model_svc,X_test, y_test, cv=7)

    print(scores.mean())






# import sys
# i = 0
# f2 = open('F:/importantfilecopy/tandomrepeat/newtry/v0.txt', 'r')
# for line1 in f2:
#     line1 = line1.strip().split("\t")
#     if int(line1[0]) == 19:
#         i += 1
# print i
# # start.append(line1[1])
#     pos = line1[7]
#     end.append(int(pos.split(";")[1].split("=")[1]))
#     if int(pos.split(";")[2].split("=")[1]) == 3:
#         type.append(int(pos.split(";")[2].split("=")[1])-1)
#     else:
#         type.append(1)