from sklearn import tree

X = [[181, 80, 44],
     [177, 70, 43],
     [160, 60, 38],
     [154, 54, 37],
     [166, 65, 40],
     [190, 90, 47],
     [175, 64, 39],
     [177, 70, 40],
     [159, 55, 37],
     [171, 75, 42],
     [181, 85, 43]]

y = ["Male",
     "Female",
     "Female",
     "Female",
     "Male",
     "Male",
     "Male",
     "Female",
     "Male",
     "Female",
     "Male"]

model = tree.DesicionTreeClassifier()
model = model.fit(X, y)

print(clf.predict([171, 75, 42]))