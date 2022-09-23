from DeepLearningTools import FeedForward 

model=DeepLearning()

Sample_Data=[200,100,121,88,77,99]
model.compile("ANN.json")
model.ANNToolBox(Action="predict", Sample_Data=Sample_Data, Digram_Title="ANN Visulization and Prediction")
