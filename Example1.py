from DeepLearningTools import DeepLearning

model=DeepLearning()
model.Add_Layer(5, "Relu")
model.Add_Layer(3, "Relu")
model.Add_Layer(1, "Sigmoid", Threshold_Value=0.5)
Sample_Data=[200,100,121,88,77,99]
model.compile(Inputs=len(Sample_Data), Random_Values=[[-1,1],[-5, 5]])
model.ANNToolBox(Action="draw", Digram_Title="ANN Visulization")
