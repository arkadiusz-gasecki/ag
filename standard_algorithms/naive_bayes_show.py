#this is simple code to demonstrate way, in which Naive Bayes algorithm behaves

from collections import defaultdict

#let us define some entries
features = {
        
        'Height': ['Tall','Tall','Short','Medium','Short','Medium','Tall','Tall','Medium','Medium'],
        'Weight': ['Skinny','Medium','Fat','Medium','Skinny','Fat','Fat','Fat','Skinny','Skinny'],
        'Eyes': ['Blue','Brown','Brown','Green','Blue','Blue','Green','Blue','Green','Brown']       
        }

#and results, entries correspond to themselves based on position in table
label = {
        
        'Result': ['Pass','Pass','Fail','Fail','Pass','Fail','Fail','Pass','Pass','Fail']
        }

#at first we are building function that will calculate counts for each label/result
#this will be then used in next function
def count_label(labels):
    
    freqs = defaultdict(int)
    for elem in labels:
        freqs[elem] += 1
    
    return freqs

# then we are building function that will calculate probability for features
# we provide features as they are, list with labels, and count for each of label
# as a result we return table of shape output[feature_name][label_name][feature_value] = probability
def count_features(features, labels, label_cnt):

    total_freqs = dict()    
    for key,args in features.items():
        
        total_freqs[key] = dict()
        for label in set(labels):
            total_freqs[key][label] = defaultdict(int)
    
        for (i,elem) in enumerate(args):
            total_freqs[key][labels[i]][elem] += 1
        
        for label,val in total_freqs[key].items():
            for elem in val:
                total_freqs[key][label][elem] /= label_cnt[label]
            
    return total_freqs



#apply functions and collect results
cnt_label = count_label(label['Result'])
cnt_feat = count_features(features,label['Result'],cnt_label)


#now we provide function for predcit, where apart from frequencies tables, we will provide dictionary with single entry
#for which we want to make prediction
def predict(cnt_feat, cnt_label, predict_entry):
    predict_probs = dict()
    total_sum = 0
    for predict_label in set(label['Result']):
        prob = cnt_label[predict_label] / len(label['Result'])
        
        for key, val in predict_entry.items():
            prob *= cnt_feat[key][predict_label][val]
        predict_probs[predict_label] =  prob
        total_sum += prob
    #normalize values
    for k,v in predict_probs.items():
        predict_probs[k] = v / total_sum
    
    return predict_probs
    
#run prediction for new single case
features_predict = {
        
        'Height': 'Short',
        'Weight': 'Medium',
        'Eyes': 'Green'       
        }

result = predict(cnt_feat, cnt_label, features_predict)
for k,v in result.items():
    print("%s -> %.2f" % (k,v))
