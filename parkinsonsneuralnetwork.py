from numpy import save
from stratified import *
from parkinsons import *

raw_category_p, raw_data_p = dataforharry()
hidden1 = [4]
hidden2 = [4,4]
hidden3 = [8]
hidden4 = [8,8]
listoflayers = [hidden1,hidden2,hidden3,hidden4]
epochp_1 = 4000

def savef(rawdata,rawcategory,hiddenlayer,epoch,filename):
    loflofoutputs, acc, lofj = kfoldcrossvalidneuralnetwork(rawdata,rawcategory,hiddenlayer,k=10,minibatchk=5,lambda_reg=0.1, learning_rate=0.05, epsilon_0=0.00001, softstop=epoch, printq=False)
    accuracyp, precisionp, recallp, fscore_p= meanevaluation(loflofoutputs,1)
    plt.figure()
    print("Parkinson Data Neural Network with " + str(hiddenlayer) + " hidden layers and " + str(epoch) + " epochs")
    print("Accuracy:",  float("{0:.4f}". format(acc)))
    print("F-score:",  float("{0:.4f}". format(fscore_p)))
    plt.plot(range(epoch+1), lofj[1])
    plt.xlabel("epoch")
    plt.ylabel("J")
    plt.title("Parkinson Data Neural Network with " + str(hiddenlayer) + " hidden layers and " + str(epoch) + " epochs")
    plt.savefig("nnfig/parkinson_nn_{}.png".format(filename))


filenames = ['4','44','8','88']

n = 0
for layer in listoflayers:
    savef(raw_data_p,raw_category_p,layer,epochp_1+1000*n,filenames[n])
    n+=1

# Parkinson Data Neural Network with [4] hidden layers and 4000 epochs
# Accuracy: 0.857(251461988304)
# F-score: 0.909(2946287120369)

# Parkinson Data Neural Network with [4, 4] hidden layers and 5000 epochs
# Accuracy: 0.857(6959064327484)
# F-score: 0.9095533250546992

# Parkinson Data Neural Network with [8] hidden layers and 6000 epochs
# Accuracy: 0.8608771929824561
# F-score: 0.9121042018789517

# Parkinson Data Neural Network with [8, 8] hidden layers and 7000 epochs
# Accuracy: 0.8414327485380116
# F-score: 0.8983464632018581
