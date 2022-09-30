from tkinter import *
import json
from turtle import shape
import numpy as np
import random as rn
import sys

# This class offers the following services:
# 1- To create the ANN layers using the metod Add_Layer(No_Neurons, ActivationF, Threshold_Value="None")
# 2- To create the input layer and apply random weights using the method compile(self,File_Name=None, Inputs=None, Random_Values=None):
# 3- To create the input, hideen, and output layers from JSON file using the method compile(self,File_Name=None, Inputs=None, Random_Values=None):
# 4- To create JSON file ANN structure of the current ANN using the method Create_JSON_Structure(self)
# 5- To Visulize any Artificial Neural Network (ANN) structure using the metod ANNToolBox(Action="draw", Digram_Title="ANN Visulization")
# 6- To visulize and predict outputs at the output layer using the method ANNToolBox(Action="predict", Digram_Title="ANN Visulization")
                                        # Note: This class is not used to train ANN  
# see example1.py
# see example2.py
# see example3.py
# see example4.py
# see example5.py

class DeepLearning():
    
    def __init__(self):
        self.Layers={}
        self.ActivationF=""
        self.No_Neurons=0
        self.Layer_Number=0
        self.Neurons=[]
        self.Neurons_intercept=[0]
        self.List_Neurons_intercept=[]
        self.Threshold_Value="None"
        self.Neuron_Weights=[0]
        self.Neuron_Coordinates=[]
        self.Neuron_List_Of_Coordinates={}
        self.List_Of_ActivationF=['Sigmoid', "Tanh", "Softmax", "Softsign", "ReLU", "Leaky ReLU", "ELUs", "Linear", "Binary Step"]
        self.width=1500
        self.height=900
        self.Arrow_Lenth=25
        self.Neuron_Radious=70
        self.Input_Radious=30
        self.TBReserved_Space=300
        self.LRReserved_Space=200
        self.The_Last_Neuron=self.height-self.TBReserved_Space
        self.Many_Ouput_Neurons=False

    def Add_Layer(self, No_Neurons, ActivationF, Threshold_Value="None"):
        Flag=0
        for Act_F in self.List_Of_ActivationF:
            if Act_F.lower()==ActivationF.lower():
                self.ActivationF=Act_F
                Flag=1
                break
        if Flag==0:
            print (" Error in formatting the Activation Function argument")
            sys.exit()
        self.No_Neurons=int(No_Neurons)
        self.Threshold_Value=Threshold_Value
        self.Layer_Number+=1
        if isinstance(self.Threshold_Value, int) or isinstance(self.Threshold_Value, float):
            self.Threshold_Value=float(self.Threshold_Value)
        else:
            if self.Threshold_Value.lower() =="none":
                self.Threshold_Value="None"
            else:
                print (" Error in formatting the Threshold Value argument")
                sys.exit()

        for i in range(self.No_Neurons):
            self.Neurons.append(self.Neuron_Weights)
            self.List_Neurons_intercept.append(self.Neurons_intercept)
        self.Layers[self.Layer_Number]=self.ActivationF,  self.Threshold_Value, self.Neurons,  self.List_Neurons_intercept
        self.Neurons=[]
        self.List_Neurons_intercept=[]
    def ANNToolBox(self, Action="Draw", Sample_Data=[], Digram_Title="ANN Visualization"):
        if Action.lower() != "draw" and Action.lower() != "predict":
            print (f" Error")
            sys.exit()
        else:
            if Action.lower() == "draw":
                self.canvas, self.window=self.__Window_Para()
                self.__Draw(Digram_Title)
            else:
                if len(Sample_Data)<=0:
                    print (f" Error")
                    sys.exit()
                else:
                    self.canvas, self.window=self.__Window_Para()
                    self.__Draw(Digram_Title + " and Predication")
                    self.__predict(Sample_Data)
        self.window.mainloop() 

    def __Draw_NN_Digram(self, x1,y1,x2,y2, Radious, Space_Padding, border, color, i):
        
        for j in range(0, len(self.Layers[i][2])):
            self.canvas.create_oval(x1, y1, x2, y2,outline = border, fill = color,width = 2)
            self.__Add_XY_Coordinates(x1,y1)
            y1=y1+Radious+Space_Padding
            y2=y2+Radious+Space_Padding
        
        self.Neuron_List_Of_Coordinates[i]=self.Neuron_Coordinates
        self.Neuron_Coordinates=[]

    def __Add_XY_Coordinates(self,x1,y1):
            xy=[]
            xy.append(x1)
            xy.append(y1)
            self.Neuron_Coordinates.append(xy)

    def __Add_XY_Dashed_Line_Coordinates(self,x1,y1, y2):
        for i in range (2):
            xy=[]
            xy.append(x1)
            xy.append(y1)
            self.Neuron_Coordinates.append(xy)
            y1=y2

    def __Draw_Dashed_Lines(self, x1, y1, x2, y2, Radious, Space_Padding, i,  border, color, d, s):  
        self.__Draw_Box(x1-10,y1-10,x1+Radious+10,self.The_Last_Neuron+Radious+10, "#fb0","#fb0")
        self.canvas.create_oval(x1, y1, x2, y2,outline =border, fill = color,width = 2)
        coordinates = x1+Radious/2, y1+Radious+Space_Padding, x1+Radious/2,self.The_Last_Neuron-Space_Padding
        self.canvas.create_line(coordinates, dash=(d,s))
        y0=y1
        y1=self.The_Last_Neuron
        y2=y1+Radious
        self.canvas.create_oval(x1, y1, x2, y2,outline = border, fill = color,width = 2)
        self.__Add_XY_Dashed_Line_Coordinates(x1,y0,y1)
        self.Neuron_List_Of_Coordinates[i]=self.Neuron_Coordinates
        self.Neuron_Coordinates=[]
    
    def __Draw_Box(self, x1, y1, x2, y2, border, color):
        self.canvas.create_rectangle(x1, y1, x2, y2,outline=border, fill=color)


    def __Window_Para(self):
        window = Tk()
        Screen_width=window.winfo_screenwidth()
        Screen_height=window.winfo_screenheight()
        x=(Screen_width/2)-(self.width/2)
        y=(Screen_height/2)-(self.height/2)
        window.geometry(f'{self.width}x{self.height}+{int(x)}+{int(y)}')
        window.configure(background = "grey")
        window.resizable(False, False)
        canvas = Canvas(window, width=self.width , height=self.height , bg = "white")
        canvas.pack(pady = 5)
        self.Many_Ouput_Neurons=False
        return canvas,window

    def  __Set_Para(self, Layer_No,Number_Of_Layers, Input_Radious, Neuron_Radious):
        if Layer_No==0:
            Radious=Input_Radious
            Space_Padding=10
            border="black"
            color="blue"
        else:
            Radious=Neuron_Radious
            Space_Padding=20
            if (Layer_No==Number_Of_Layers-1):
                border="black"
                color="red"
            else:
                border="black"
                color="green"
        return Radious, Space_Padding, border, color
    
    def __Draw_ANN_Mesh(self, n):
        for Layer_N_Mins1 in range(0,n-1):
            Layer_N_Plus1=Layer_N_Mins1+1
            for i in range(0, len(self.Neuron_List_Of_Coordinates[Layer_N_Mins1])):
                Radious, Space_Padding, border, color=self.__Set_Para(Layer_N_Mins1,n, self.Input_Radious, self.Neuron_Radious)
                x1=self.Neuron_List_Of_Coordinates[Layer_N_Mins1][i][0]+Radious
                y1=self.Neuron_List_Of_Coordinates[Layer_N_Mins1][i][1]+(Radious/2)
                Radious, Space_Padding, border, color=self.__Set_Para(Layer_N_Plus1,n, self.Input_Radious, self.Neuron_Radious)
                for j in range(0, len(self.Neuron_List_Of_Coordinates[Layer_N_Plus1])):
                    x2=self.Neuron_List_Of_Coordinates[Layer_N_Plus1][j][0]
                    y2=self.Neuron_List_Of_Coordinates[Layer_N_Plus1][j][1]+(Radious/2)
                    coordinates = x1,y1,x2,y2
                    self.canvas.create_line(coordinates, dash=(8,2))
    
    def __Draw_Arrows_And_Data_Input_Output_Layer(self, Input, Output, n, case):
        last_key = list(self.Neuron_List_Of_Coordinates)[-1]
        Input = np.reshape(Input, (1, len(Input)))
        for Layer in (0, last_key):
            Radious, Space_Padding, border, color=self.__Set_Para(Layer,n, self.Input_Radious, self.Neuron_Radious)
            Number_Of_Neurons_In_List=len(self.Neuron_List_Of_Coordinates[Layer])
            if Layer==0:
                Neurons_In_ANN_Layer=len(self.Layers[Layer][2])
                X1_Location=-Radious
                Data=Input
            else:
                if Layer==last_key:
                    Neurons_In_ANN_Layer=len(self.Layers[len(self.Layers)-1][2])
                    X1_Location=+Radious
                    Data=Output
                else:
                    print(f'Error')
                    sys.exit()
            if Number_Of_Neurons_In_List == Neurons_In_ANN_Layer :
                for Neurons_In_Input_Output_Layer in range (0, Number_Of_Neurons_In_List):
                    x1=self.Neuron_List_Of_Coordinates[Layer][Neurons_In_Input_Output_Layer][0]+X1_Location
                    y1=self.Neuron_List_Of_Coordinates[Layer][Neurons_In_Input_Output_Layer][1]+(Radious/2)
                    coordinates=x1,y1,x1+self.Arrow_Lenth,y1
                    self.canvas.create_line(coordinates, fill="blue", arrow="last", width=10, dash=(4,2))
                    if case ==1:
                        self.canvas.create_text(x1+X1_Location, y1, text=str(Data[0][Neurons_In_Input_Output_Layer]), fill="black", font=('Helvetica 15 bold'))
                          
            else:
                if  Number_Of_Neurons_In_List <= Neurons_In_ANN_Layer :
                    for Neurons_In_Input_Output_Layer in (0, 1):
                        x1=self.Neuron_List_Of_Coordinates[Layer][Neurons_In_Input_Output_Layer][0]+X1_Location
                        y1=self.Neuron_List_Of_Coordinates[Layer][Neurons_In_Input_Output_Layer][1]+(Radious/2)
                        coordinates=x1,y1,x1+self.Arrow_Lenth,y1
                        self.canvas.create_line(coordinates, fill="blue", arrow="last", width=10, dash=(4,2))
                        if case ==1:
                            if Neurons_In_Input_Output_Layer == 0:
                                Colum=0
                            else:
                                Colum=Data.shape[1]-1
                            self.canvas.create_text(x1+X1_Location, y1, text=str(Data[0][Colum]), fill="black", font=('Helvetica 15 bold'))
                else:
                    print(f'Error')
                    sys.exit()


    def __Draw(self, Digram_Title): 
        self.window.title(Digram_Title)
        Space_Padding=None
        W_Padding=140
        i=0
        flag=1
        n=len(self.Layers)
        W_Jump=200
        HLayer_Space_Needed=(self.Neuron_Radious*2+W_Padding)*len(self.Layers)
        Fit=True # to add mesh to ANN
        if HLayer_Space_Needed < self.width:
            x1=(self.width-HLayer_Space_Needed)/2+self.LRReserved_Space
            for i in range (n):
                Radious, Space_Padding, border, color= self.__Set_Para(i,n, self.Input_Radious, self.Neuron_Radious)
                VLayer_Space_Needed=(Radious+Space_Padding)*len(self.Layers[i][2])
                x2=x1+Radious
                if VLayer_Space_Needed < (self.height-self.TBReserved_Space):
                    Fit=Fit and True
                    Satrt_Drawing = int((self.height-VLayer_Space_Needed)/2)
                    y1=0
                    y1=y1+Satrt_Drawing
                    y2=y1+Radious   
                    self.__Draw_Box(x1-10,y1-10,x2+10,y1+VLayer_Space_Needed-10, "#fb0","#fb0")
                    self.__Draw_NN_Digram(x1,y1,x2,y2, Radious, Space_Padding,border, color, i)
                else:
                    Fit=Fit and False
                    if i==0:
                        y1=self.TBReserved_Space/2+Space_Padding
                    else:
                        y1=self.TBReserved_Space/2
                    y2=y1+Radious
                    self.__Draw_Dashed_Lines(x1, y1, x2, y2, Radious, Space_Padding,i, border, color, 5, 1)
                x1=x1+Radious+W_Padding
                x2=x1+Radious 
            if Fit == True:
                self.__Draw_ANN_Mesh(n)
        else:
            Fit=Fit and False
            x1=self.LRReserved_Space
            m=[0,1,2,n-2,n-1]
            for i in m:
                Radious, Space_Padding, border, color= self.__Set_Para( i,n, self.Input_Radious, self.Neuron_Radious)
                VLayer_Space_Needed=(Radious*len(self.Layers[i][2]) + (len(self.Layers[i][2])-1)*Space_Padding)
                x2=x1+Radious
                if i>=n-2:
                    if flag==1:
                        coordinates = self.width/2-Radious, self.height/2, self.width/2+Radious*2,self.height/2
                        self.canvas.create_line(coordinates, fill="blue", arrow="last", width=10, dash=(5,1))
                        x1=self.width/2+W_Jump
                        x2=x1+Radious
                        flag=0
                if VLayer_Space_Needed < self.height: #note
                    Satrt_Drawing = int((self.height-VLayer_Space_Needed)/2)
                    y1=0
                    y1=y1+Satrt_Drawing
                    y2=y1+Radious   
                    self.__Draw_Box(x1-10,y1-10,x2+10,y1+VLayer_Space_Needed, "#fb0","#fb0") #Note
                    self.__Draw_NN_Digram(x1,y1,x2,y2, Radious, Space_Padding, border, color, i)
                else:
                    if i==0:
                        y1=self.TBReserved_Space
                    else:
                        y1=self.TBReserved_Space/2
                    y2=y1+Radious
                    self.__Draw_Dashed_Lines(x1, y1, x2, y2, Radious, Space_Padding,i, border, color, 2, 1)
                
                x1=x1+Radious+W_Padding
                x2=x1+Radious
        self.__Draw_Arrows_And_Data_Input_Output_Layer([], [], n, 0)
    def Create_JSON_Structure(self, File_Name):
        JSON_String=json.dumps(self.Layers, indent=4)
        jsonFile = open(File_Name, "w")
        jsonFile.write(JSON_String)
        jsonFile.close()

    def compile(self,File_Name=None, Inputs=None, Random_Values=None):
        if (File_Name) and not (Inputs or Random_Values):
            fileObject = open(File_Name, "r")
            jsonContent = fileObject.read()
            self.Layers = json.loads(jsonContent)
            self.Layers = {int(key):value for key, value in self.Layers.items()}
        else:
            if not (File_Name) and  (Inputs and Random_Values):
                if (len(Random_Values) == 2):
                    if len(Random_Values[0]) !=0 and len(Random_Values[1]) !=0 : 
                        self.Inputs=Inputs
                        for i in range(self.Inputs):
                            self.Neurons.append(self.Neuron_Weights)
                        self.Layers[0]="None", "None", self.Neurons
                        self.Neurons=[]
                        Min_W=Random_Values[0][0]
                        Max_W=Random_Values[0][1]
                        Min_intercept_W=Random_Values[1][0]
                        Max_intercept_W=Random_Values[1][1]
                        self.__Weights_Settings(Min_W, Max_W)
                        self.__intercept_Settings(Min_intercept_W, Max_intercept_W)
                    else:
                        print (f" Error in the argument Random Values ")
                        sys.exit()
                else:
                    print (f" Error in the argument Random Values ")
                    sys.exit()
            else:
                print (f" Error")

    def __intercept_Settings(self, Min_intercept_W, Max_intercept_W ):
        for Current_Layer in range(1, len(self.Layers)):
            for N1 in range (len(self.Layers[Current_Layer][2])):
                self.Layers[Current_Layer][3][N1]=rn.uniform(Min_intercept_W, Max_intercept_W)

    def __Weights_Settings(self, Min_W, Max_W):
        for Current_Layer in range(0, len(self.Layers)-1):
            Weights = []
            Neurons_Of_The_Current_Layer=len(self.Layers[Current_Layer][2])
            Next_Layer=Current_Layer+1
            Neurons_Of_The_Next_Layer=len(self.Layers[Next_Layer][2])
            for N1 in range (Neurons_Of_The_Current_Layer):
                for  N2 in range (Neurons_Of_The_Next_Layer):    
                    Weights.append(rn.uniform(Min_W, Max_W))
                self.Layers[Current_Layer][2][N1]=Weights
                Weights = []
        
    def __predict(self, Sample_Data):
        Inputs=np.array(Sample_Data, dtype=np.float64)
        Inputs = np.reshape(Inputs, (1, len(Sample_Data)))
        np.array((), dtype=np.float64)
        for Layer in range(1, len(self.Layers)):
            w=[]
            b=[]
            Pre_Layer=Layer-1
            
            for N1 in range (len(self.Layers[Pre_Layer][2])): 
                w.append(self.Layers[Pre_Layer][2][N1])
            for N1 in range (len(self.Layers[Layer][3])):  
                b.append(self.Layers[Layer][3][N1])

            w=np.array(w, dtype=np.float64)
            b=np.array(b, dtype=np.float64)
            b = np.reshape(b, (1, len(b)))
            Sum_of_Product=np.dot(Inputs, w)+b
            Sum_of_Product.astype(np.int64)
            Inputs=self.__Activation_Function(Sum_of_Product, self.Layers[Layer][0], self.Layers[Layer][1])
        self.__Draw_Arrows_And_Data_Input_Output_Layer(Sample_Data, Inputs, len(self.Layers), 1)

    
    def __Activation_Function(self, Neuron_Output, Activation_Fun, Threshold_Value):
        m,n = Neuron_Output.shape
        for j in range(n):
            if Activation_Fun=="Sigmoid":
                Neuron_Output[0][j]=1/(1+np.exp(-Neuron_Output[0][j]))
            elif Activation_Fun=="Tanh":
                Neuron_Output[0][j]=(np.exp(-Neuron_Output[0][j]) - np.exp(-Neuron_Output[0][j]))/(np.exp(-Neuron_Output[0][j]) + np.exp(-Neuron_Output[0][j]))
            elif Activation_Fun=="Softmax":
                Neuron_Output=self.__SoftMax_Act(Neuron_Output)
                break
            elif Activation_Fun=="Softsign":
                pass
            elif Activation_Fun=="ReLU":
                Neuron_Output[0][j] = max(0.0, Neuron_Output[0][j])
            elif Activation_Fun=="Leaky ReLU":
                Neuron_Output[0][j] = max(0.1*Neuron_Output[0][j], Neuron_Output[0][j])
            elif Activation_Fun=="ELUs":
                pass
            elif Activation_Fun=="Linear":
                pass
            elif Activation_Fun=="Binary Step":
                if Neuron_Output[0][j]<0:
                    Neuron_Output[0][j]=0
                else:
                    Neuron_Output[0][j]=1
            else:
                print (f" Error in formatting Activation Fun")
                sys.exit()
            if Threshold_Value !="None":
                if Neuron_Output[0][j]>=Threshold_Value:
                    Neuron_Output[0][j]=1
                else:
                    Neuron_Output[0][j]=0
        return (Neuron_Output)
    
    def __SoftMax_Act(self, Z):
        Exp_z = np.exp(Z)
        Sum = Exp_z.sum()
        Softmax_z = np.round(Exp_z/Sum,3)
        return Softmax_z
