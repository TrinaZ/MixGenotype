from skrvm import RVC
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

def load_data():
    f = open('F:/importantfilecopy/tandomrepeat/2019.121test/5results', 'r')
    # f = open('F:/importantfilecopy/tandomrepeat/3/1x/total.txt', 'r')
    data_set = []
    label_set = []
    for line in f:
        line = line.strip().split("\t")
        line_list = line[0].strip().split(" ")
        data_set.append(line_list)
        label_set.append(line[1])
    return data_set, label_set

data, label = load_data()
X_train,X_test,y_train,y_test = train_test_split(data,label,test_size=0.3,random_state=0)
clf = RVC()
# clf.fit(rvm_data, rvm_target)
# print(clf.score(rvm_data, rvm_target))
clf.fit(X_train, y_train)
scoring = 'accuracy'
scores = cross_val_score(clf,X_test, y_test, cv=7)
print(scores.mean())