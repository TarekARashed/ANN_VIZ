from DeepLearningTools import FeedForward 

model=DeepLearning()
model.Add_Layer(100, "Relu")
model.Add_Layer(15, "Relu")
model.Add_Layer(15, "Relu")
model.Add_Layer(15, "Relu")
model.Add_Layer(15, "Relu")
model.Add_Layer(5, "Sigmoid", Threshold_Value=0.5)
Sample_Data=[2,1,1,8,7,9,9,9,9,9,9]
model.compile(Inputs=len(Sample_Data), Random_Values=[0,1])
model.ANNToolBox(Action="predict", Sample_Data=Sample_Data, Digram_Title="ANN Visulization and Prediction")
