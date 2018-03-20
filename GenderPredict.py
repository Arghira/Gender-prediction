from sklearn import tree
#[height, weight, shoe size]
a = [0, 0, 0]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43], [180, 92, 41]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male', 'male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

a[0] = int(raw_input("Enter the Height: "))
a[1] = int(raw_input("Enter the weight: "))
a[2] = int(raw_input("Enter the shoe size: "))
prediction = clf.predict([a])

print("The prediction: ")
print (prediction)
