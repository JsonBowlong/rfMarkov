import numpy as np
import matplotlib.pyplot as plt

maxn=0
######dodonew_crack_12306
plt.title("dodonew crack 12306")
rfpath="C:/Users/ZZJ/Desktop/rf_markov/result/dodonew_12306_rf10_smooth00001_nestim=50_feature=none.txt"
listpath="C:/Users/ZZJ/Desktop/实验室/result/Real Case/dodonew_12306/dodonew_crack_12306_noPI_list_result_10000.txt"
markovpath="C:/Users/ZZJ/Desktop/实验室/result/第三组中文/dodonew_crack_12306_male_markov_result_10e7.txt"
pcfgpath="E:/eclipse-cpp-neon/eclipse/workspace/Personal_PCFG+/dodonew_crack_12306_PCFG_10e7.txt"

personal_markovpath="C:/Users/ZZJ/Desktop/实验室/result/10e7/dodonew_crack_12306_personal_markov_result_10e7.txt"
personal_EPCFGpath="C:/Users/ZZJ/Desktop/实验室/result/10e7/dodonew_crack_12306_personal_PCFG+_result_10e7.txt"
tarlistpath="C:/Users/ZZJ/Desktop/实验室/result/10e7/dodonew_crack_12306_target_list_result_10e7.txt"
personal_rfpath="C:/Users/ZZJ/Desktop/rf_markov/result/dodonew_crack_12306_personal_rf10_result_nestim=50_feature=none_40w.txt"

#######dodonew_dayu8_crack_csdn
#plt.title("dodonew crack csdn")
#rfpath="C:/Users/ZZJ/Desktop/dodonew_dayu8_csdn_dayu8_rf10_smooth00001_nestim=50_feature=none.txt"
#listpath="C:/Users/ZZJ/Desktop/实验室/result/Real Case/dodonew_dayu8_csdn/dodonew_dayu8_crack_csdn_noPI_list_result_10000.txt"
#markovpath="C:/Users/ZZJ/Desktop/实验室/result/第三组中文/dodonew_crack_csdn_male_markov_result_10e7.txt"
#pcfgpath="E:/eclipse-cpp-neon/eclipse/workspace/Personal_PCFG+/dodonew_dayu8_csdn_pcfg_10e7.txt"

#personal_markovpath="C:/Users/ZZJ/Desktop/实验室/result/第三组中文/dodonew_crack_csdn_male_allPI_personal_markov_result_10e7.txt"
#personal_EPCFGpath="C:/Users/ZZJ/Desktop/实验室/result/第三组中文/dodonew_crack_csdn_male_personalPCFG+_result_10e7.txt"
#tarlistpath=""
#personal_rfpath="C:/Users/ZZJ/Desktop/dodonew_crack_csdn_personal_rf10_result_nestim=50_feature=none_40w.txt"

#######dodonew_crack_126
#plt.title("dodonew crack 126")
#rfpath="C:/Users/ZZJ/Desktop/rf_markov/result/dodonew_126_rf10_smooth00001_nestim=50_feature=none.txt"
#listpath="C:/Users/ZZJ/Desktop/实验室/result/Real Case/dodonew_126/dodonew_crack_126_noPI_list_result_10000.txt"
#markovpath="C:/Users/ZZJ/Desktop/实验室/result/第三组中文/dodonew_crack_126_male_markov_result_10e7.txt"
#pcfgpath="E:/eclipse-cpp-neon/eclipse/workspace/Personal_PCFG+/dodonew_crack_126_PCFG_10e7.txt"

#personal_markovpath="C:/Users/ZZJ/Desktop/实验室/result/第三组中文/dodonew_crack_126_male_allPI_personal_markov_result_10e7.txt"
#personal_EPCFGpath="C:/Users/ZZJ/Desktop/实验室/result/第三组中文/dodonew_crack_126_male_personalPCFG+_result_10e7.txt"
#tarlistpath=""
#personal_rfpath="C:/Users/ZZJ/Desktop/rf_markov/result/dodonew_crack_126_personal_rf10_result_nestim=50_feature=none_40w.txt"

#############12306_crack dodonew
#plt.title("12306 crack dodonew")
#rfpath="C:/Users/ZZJ/Desktop/rf_markov/result/12306_dodonew_rf10_smooth00001_nestim=50_feature=none.txt"
#listpath="C:/Users/ZZJ/Desktop/实验室/result/Real Case/12306_dodonew/12306_crack_dodonew_noPI_list_result_10000.txt"
#markovpath="C:/Users/ZZJ/Desktop/实验室/result/第三组中文/12306_crack_dodonew_male_markov_result_10e7.txt"
#pcfgpath="C:/Users/ZZJ/Desktop/实验室/result/Real Case/12306_dodonew/12306_crack_dodonew_PCFG_result_10000.txt"

#personal_markovpath="C:/Users/ZZJ/Desktop/实验室/result/第三组中文/12306_crack_dodonew_male_allPI_personal_markov_result_10e7.txt"
#personal_EPCFGpath="C:/Users/ZZJ/Desktop/实验室/result/第三组中文/12306_crack_dodonew_male_personalPCFG+_result_10e7.txt"
#tarlistpath=""
#personal_rfpath="C:/Users/ZZJ/Desktop/rf_markov/result/12306_crack_dodonew_personal_rf10_result_nestim=50_feature=none_80000.txt"

############12306 half1 crack half2
#plt.title("12306 half1 crack half2")
#rfpath="C:/Users/ZZJ/Desktop/12306_half1_crack_half2_male_rf10_predict_smooth00001_nestim=50_feature=none_70w.txt"
#listpath="C:/Users/ZZJ/Desktop/实验室/result/Ideal Case/12306/12306_half1_crack_half2_noPI_list_result_10000.txt"
#markovpath="C:/Users/ZZJ/Desktop/实验室/result/Ideal Case/12306/12306_half1_crack_half2_markov_result_10000.txt"
#pcfgpath="C:/Users/ZZJ/Desktop/实验室/result/Ideal Case/12306/12306_half1_crack_half2_PCFG_result_10000.txt"

#personal_markovpath="C:/Users/ZZJ/Desktop/实验室/result/第一组中文/12306_half1_crack_half2_male_allPI_personal_markov_result_10e7.txt"
#personal_EPCFGpath="C:/Users/ZZJ/Desktop/实验室/result/第一组中文/12306_half1_crack_half2_male_personalPCFG+_result_10e7.txt"
#tarlistpath="C:/Users/ZZJ/Desktop/实验室/result/Ideal Case/12306/12306_half1_crack_half2_allPI_targeted_list_result_10000.txt"
#personal_rfpath="C:/Users/ZZJ/Desktop/12306_half1_crack_half2_personal_rf10_result_nestim=50_feature=none_50w.txt"

############dodonew half1 crack half2
#plt.title("dodonew half1 crack half2")
#rfpath="C:/Users/ZZJ/Desktop/dodoenw_half1_crack_half2_male_rf10_predict_smooth00001_nestim=50_feature=none_65w.txt"
#listpath="C:/Users/ZZJ/Desktop/实验室/result/Ideal Case/dodonew/dodonew_half1_crack_half2_noPI_list_result_10000.txt"
#markovpath="C:/Users/ZZJ/Desktop/实验室/result/Ideal Case/dodonew/dodonew_half1_crack_half2_markov_result_10000.txt"
#pcfgpath="C:/Users/ZZJ/Desktop/实验室/result/Ideal Case/dodonew/dodonew_half1_crack_half2_PCFG_result_10000.txt"

#personal_markovpath="C:/Users/ZZJ/Desktop/实验室/result/第一组中文/dodonew_half1_crack_half2_male_allPI_personal_markov_result_10e7.txt"
#personal_EPCFGpath="C:/Users/ZZJ/Desktop/实验室/result/第一组中文/dodonew_half1_crack_half2_male_personalPCFG+_result_10e7.txt"
#tarlistpath="C:/Users/ZZJ/Desktop/实验室/result/Ideal Case/dodonew/dodonew_half1_crack_half2_allPI_targeted_list_result_10000.txt"
#personal_rfpath="C:/Users/ZZJ/Desktop/rf_markov/result/dodonew_half1_crack_half2_male_personal_rf10_result_nestim=50_feature=none_60000.txt"





def drawline(path,style,lab):
    global maxn
    if path=="":
        return
    yn=[]
    fin=open(path,'r')
    tot=0
    n=0
    for line in fin:
        n+=1
        beg=line.find(',')
        if beg==-1:
            yn.append(float(line[:-1]))
        else :
            tot=int(line[beg+1:-1])
    n-=1
    if n>maxn:
        maxn=n
    y=[i/tot for i in yn]
    x=np.linspace(1,n,n)
    return plt.semilogx(x,y,style,label=lab)


drawline(rfpath,'r','rf')
drawline(markovpath,'c','markov')
drawline(pcfgpath,'m','PCFG')
drawline(listpath,'g','list')

drawline(personal_rfpath,'r--','personal_rf')
drawline(personal_markovpath,'c--','personal_markov')
drawline(personal_EPCFGpath,'m--','personal PCFG+')
drawline(tarlistpath,'g--','tarlist')






plt.legend(loc='best')# make legend

#plt.plot(x,y)
plt.xlabel('log(guess)')
plt.ylabel('cracked fraction')
plt.ylim(0.0,1.0)
plt.xlim(1,maxn)
plt.show()
