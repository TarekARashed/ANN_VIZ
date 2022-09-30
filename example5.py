from DeepLearningTools import DeepLearning 

model=DeepLearning()
model.Add_Layer(5, "relu")
model.Add_Layer(6, "relu")
model.Add_Layer(5, "softmax")
Sample_Data=[3,2, 5]
model.compile(Inputs=len(Sample_Data), Random_Values=[[-1,1],[-5, 5]])
model.ANNToolBox(Action="predict", Sample_Data=Sample_Data, Digram_Title="ANN Visulization")
