from DeepLearningTools import FeedForward 

model=DeepLearning()
model.Add_Layer(6, "Relu")
model.Add_Layer(2, "Relu")
model.Add_Layer(2, "Sigmoid", Threshold_Value=0.5)
Sample_Data=[200,100,121,88,77,99]
model.compile(Inputs=len(Sample_Data), Random_Values=[0,1])
model.Create_JSON_Structure("ANN.json")
