# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 14:37:39 2018

@author: Md. Kamrul Hasan
"""
print(__doc__)
import time
startTime = time.time()
import cv2
import glob
import numpy as np
from skimage.morphology import disk
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import jaccard_similarity_score
import matplotlib.pyplot as plt



imageName_Pre=sorted(glob.glob("predictions_1 - Copy\\*.png"))

Pr=[]
kernel=disk(5)
for image in imageName_Pre:
    im=cv2.imread(image,0)
#    im=cv2.erode(im,kernel,iterations = 1)
#    im=cv2.dilate(im,kernel,iterations = 1)
#    print(im.min())
#    print(im.max())

    ret,im = cv2.threshold(im,135,255,cv2.THRESH_BINARY)
    im=im/im.max()
#    print(im.min())
    Predicted=np.array(im).ravel()
    Pr.append(Predicted)


imageName_GT=sorted(glob.glob("TestGT\\*.png"))
Tr=[]
for image in imageName_GT:
    ime=cv2.resize(cv2.imread(image,0),(224,224))
    ret,ime = cv2.threshold(ime,254,255,cv2.THRESH_BINARY)
    ime=ime/ime.max()
    Predicted=np.array(ime).ravel()
    Tr.append(Predicted)
#
def compute_iou(y_pred, y_true):
     # ytrue, ypred is a flatten vector
     y_pred = y_pred.flatten()
     y_true = y_true.flatten()
     current = confusion_matrix(y_true, y_pred, labels=[0, 1])
     # compute mean iou
     intersection = np.diag(current)
     ground_truth_set = current.sum(axis=1)
     predicted_set = current.sum(axis=0)
     union = ground_truth_set + predicted_set - intersection
     IoU = intersection / union.astype(np.float32)
     return np.mean(IoU), current
##
def tanimoto(T,P):
    tA=0
    tB=0
    tAB=0
    for i in range(len(T)):
        if T[i]==P[i]:
            tAB=tAB+1
        elif T[i]>P[i]:
            tA=tA+1
        else:
              tB=tB+1
    Tanimoto=(tAB)/(tA+tB+tAB)
    return Tanimoto
IU=[]
Sensi=[]
Speci=[]
Accu=[]
B_Accu=[]
ROC=[]
sco=[]
T=[]
ltp=[]
ltn=[]
lfp=[]
lfn=[]
#Sensi=np.zeros(10)
for i in range(len(Tr)):
    IoU, ConfusionMatrix=compute_iou(Pr[i],Tr[i])
    IU.append(IoU)
    TP = ConfusionMatrix[0][0]
    FP = ConfusionMatrix[0][1]
    FN = ConfusionMatrix[1][0]
    TN = ConfusionMatrix[1][1]
    ltp.append(TP)
    ltn.append(TN)
    lfp.append(FP)
    lfn.append(FN)
    Sensitivity=(TP/(TP+FN))
    Sensi.append(Sensitivity)
    Specificity=(TN/(FP+TN))
    Speci.append(Specificity)
    Accuracy=((TP+TN)/(TP+TN+FP+FN))
    Accu.append(Accuracy)
    B_Accur=(Sensitivity+Specificity)/2
    B_Accu.append(B_Accur)
    fpr, tpr, thresholds =roc_curve(Tr[i], Pr[i])
    roc_auc = auc(fpr, tpr)
    ROC.append(roc_auc)
    F1=(2*TP)/(2*TP+FP+FN)
    sco.append(F1)
    tani=tanimoto(Tr[i], Pr[i])
    T.append(tani)

#ii=0
#for i in range(len(IU)):
#    if IU[i]<0.9:
#        print(i)
#        ii=ii+1
#print(ii)
#IoU, ConfusionMatrix=compute_iou(Pr[1],Tr[1])
#print("Intersection over Union = %0.8f (+/-%0.08f) and Range= [%0.4f (min) ~ %0.4f (max)]" % (np.mean(IU)*100, np.std(IU),(np.mean(IU)-np.std(IU)),(np.mean(IU)+np.std(IU))))
#print("Sensitivity = %0.4f (+/-%0.04f) and Range= [%0.4f (min) ~ %0.4f (max)]" % (np.mean(Sensi)*100, np.std(Sensi),(np.mean(Sensi)-np.std(Sensi)),(np.mean(Sensi)+np.std(Sensi))))
#print("Specificity = %0.4f (+/-%0.04f) and Range= [%0.4f (min) ~ %0.4f (max)]" % (np.mean(Speci)*100, np.std(Speci),(np.mean(Speci)-np.std(Speci)),(np.mean(Speci)+np.std(Speci))))
#print("Accuracy = %0.8f (+/-%0.08f) and Range= [%0.8f (min) ~ %0.4f (max)]" % (np.mean(Accu)*100, np.std(Accu),(np.mean(Accu)-np.std(Accu)),(np.mean(Accu)+np.std(Accu))))
#print("Balanced Accuracy = %0.4f (+/-%0.04f) and Range= [%0.4f (min) ~ %0.4f (max)]" % (np.mean(B_Accu)*100, np.std(B_Accu),(np.mean(B_Accu)-np.std(B_Accu)),(np.mean(B_Accu)+np.std(B_Accu))))
#print("AUC = %0.4f (+/-%0.04f) and Range= [%0.4f (min) ~ %0.4f (max)]" % (np.mean(ROC)*100, np.std(ROC),(np.mean(ROC)-np.std(ROC)),(np.mean(ROC)+np.std(ROC))))
#
#

print("Intersection over Union = %0.4f (+/-%0.04f)" % (np.mean(IU)*100, np.std(IU)*100))
print("Sensitivity = %0.4f (+/-%0.04f)" % (np.mean(Sensi)*100, np.std(Sensi)*100))
print("Specificity = %0.4f (+/-%0.04f)" % (np.mean(Speci)*100, np.std(Speci)*100))
print("Accuracy = %0.8f (+/-%0.04f)" % (np.mean(Accu)*100, np.std(Accu)*100))
print("Balanced Accuracy = %0.4f (+/-%0.04f)" % (np.mean(B_Accu)*100, np.std(B_Accu)*100))
print("AUC = %0.4f (+/-%0.04f)" % (np.mean(ROC)*100, np.std(ROC)*100))
print("DSC = %0.4f (+/-%0.04f)" % (np.mean(sco)*100, np.std(sco)*100))
print("Tanimoto = %0.4f (+/-%0.04f)" % (np.mean(T)*100, np.std(T)*100))
print('TP= %d (+/-%0.04f)'%(np.mean(ltp),np.std(ltp)))
print('TN= %d (+/-%0.04f)'%(np.mean(ltn),np.std(ltn)))
print('FP= %d (+/-%0.04f)'%(np.mean(lfp),np.std(lfp)))
print('FN= %d (+/-%0.04f)'%(np.mean(lfn),np.std(lfn)))
#
endTime = time.time()
print('It took {0:0.1f} seconds'.format(endTime - startTime))