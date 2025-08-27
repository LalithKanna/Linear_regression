class LinearRegression:
    def __init__(self,X,y):
        self.X=X
        self.y=y
        self.n=len(X)
        self.Xy=self.calc_Xy()
        self.X_square=self.calc_X_square()
        self.sum_of_X=self.sum_of_X()
        self.sum_of_y=self.sum_of_y()
        self.sum_of_Xy=self.sum_of_Xy()
        self.sum_of_Xsquare=self.sum_of_Xsquare()
        self.slope,self.intercept=self.optimal_parameters()
        self.Y=self.training()
        self.ss_res=self.sum_of_square_of_residuals()
        self.mean_of_y=self.y_mean()
        self.ss_total=self.sum_of_squared_total()
        self.R_s=self.R_square()
        self.mae=self.Mean_absolute_error()
        self.mse=self.Mean_squared_error()
        self.rmse=self.Root_mean_squared_error()
    def calc_Xy(self):
        Xy=[]
        for i in range(self.n):
            Xy.append(self.X[i]*self.y[i])
        return Xy  
    def calc_X_square(self):
        X_square=[]
        for i in range(self.n):
            X_square.append(self.X[i]*self.X[i])
        return X_square
    def sum_of_X(self):
        sum_of_X=0
        for i in self.X:
            sum_of_X+=i
        return sum_of_X
    def sum_of_y(self):
        sum_of_y=0
        for i in self.y:
            sum_of_y+=i
        return sum_of_y
    def sum_of_Xy(self):
        soXy=0
        for i in self.Xy:
            soXy+=i
        return soXy
    def sum_of_Xsquare(self):
        sum_of_Xsquare=0
        for i in self.X_square:
            sum_of_Xsquare+=i
        return sum_of_Xsquare

    def optimal_parameters(self):
        numerator=self.n*self.sum_of_Xy-self.sum_of_X*self.sum_of_y
        denominator=self.n*self.sum_of_Xsquare-self.sum_of_X*self.sum_of_X
        slope=numerator/denominator
        intercept=self.sum_of_y - slope*self.sum_of_X
        intercept/=self.n
        return slope,intercept
    def training(self):
        y_predict=[]
        for i in self.X:
            y_predict.append(self.slope*i+self.intercept)
        return y_predict

    def sum_of_square_of_residuals(self):
        s=0
        for i in range(self.n):
            s+=(self.y[i] -self.Y[i])**2
        return s
    def y_mean(self):
        s=self.sum_of_y/self.n
        return s
        
    def sum_of_squared_total(self):
        s=0
        for i in range(self.n):
            s+=(self.y[i]-self.mean_of_y)**2
        return s
    def R_square(self):
        r=1-(self.ss_res/self.ss_total)
        return r
    def Mean_absolute_error(self):
        s=0
        for i in range(self.n):
            s+=abs(self.y[i]-self.Y[i])
        mae=(1/self.n)*s
        return mae
    def Mean_squared_error(self):
        s=0
        for i in range(self.n):
            s+=(self.y[i]-self.Y[i])**2
        mse=s/self.n
        return mse
    def Root_mean_squared_error(self):
        rmse=self.mse**0.5
        return rmse
    def PrintMainDetails(self):
        print("slope:",self.slope)
        print("intercept:",self.intercept)
        print("Y_predicted_values_trained:",self.Y)
        print("R_square_value:",self.R_s)
        print("Mean_absolute_error:",self.mae)
        print("Mean_squared_error:",self.mse)
        print("Root_mean_squared_error:",self.rmse)
class Predict:
    def __init__(self,model,new_X):
        self.slope=model.slope
        self.intercept=model.intercept
        self.new_X=new_X
        self.Y=self.simple_linear_regression()
    def simple_linear_regression(self):
        y_predict=[]
        for i in self.new_X:
            y_predict.append(self.slope*i+self.intercept)
        return y_predict
        
if __name__=="__main__":
    n=int(input("Enter total number of rows:"))
    X=[]
    for i in range(n):
        X.append(int(input(f"Enter the {i+1}th element in indepent row:")))
    print(X)
    y=[]
    for j in range(n):
        y.append(float(input(f"Enter the {j+1}th element in target row:")))
    print(y)
    new_X=[]
    for i in range(n):
        new_X.append(float(input(f"Enter the {i+1}th element of the new data:")))
    print(new_X)
    Regression=LinearRegression(X,y)
    Regression.PrintMainDetails()
    Predict_data=Predict(Regression,new_X)
    print("Y_predicted_values:",Predict_data.Y)
    
    