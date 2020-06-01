using Printf

features = Dict(
		"Height"=> ["Tall","Tall","Short","Medium","Short","Medium","Tall","Tall","Medium","Medium"],
		"Weight"=> ["Skinny","Medium","Fat","Medium","Skinny","Fat","Fat","Fat","Skinny","Skinny"],
		"Eyes"=> ["Blue","Brown","Brown","Green","Blue","Blue","Green","Blue","Green","Brown"]
	)

label = Dict(
        "Result" => ["Pass","Pass","Fail","Fail","Pass","Fail","Fail","Pass","Pass","Fail"]
        )
		

function count_label(labels)
    
    freqs = Dict{String,Int64}()
	
    for elem in labels
		freqs[elem] = get(freqs,elem,0)+1
	end
    
    return freqs
end

function count_features(features, labels, label_cnt)

    total_freqs = Dict{String,Dict}()
    for (key,args) in features
        
        total_freqs[key] = Dict{String,Dict}()
        for label in Set(labels)
            total_freqs[key][label] = Dict{String,Float32}()
		end
		
		#print(total_freqs)
    
        for i in 1:length(args)
		
			elem = args[i]
            total_freqs[key][labels[i]][elem] = get(total_freqs[key][labels[i]],elem,0) + 1
		end
    end
	
	for (fkey,val) in total_freqs
		for (skey,sval) in val
			for (tkey,tval) in sval
				total_freqs[fkey][skey][tkey] /= label_cnt[skey]
				#print(fkey," ",skey," ",tkey," ",total_freqs[fkey][skey][tkey],"\n")
			end
		end
	end
	
    return total_freqs
end

cnt_label = count_label(label["Result"])
cnt_feat = count_features(features,label["Result"],cnt_label)


function predict(cnt_feat, cnt_label, predict_entry)
    predict_probs = Dict()
    total_sum = 0.0
    for predict_label in Set(label["Result"])
        prob = cnt_label[predict_label] / length(label["Result"])

		for (key, val) in predict_entry
			prob *= cnt_feat[key][predict_label][val]
		end
	
		predict_probs[predict_label] = prob
		total_sum += prob
	end
    #normalize values
    for (k,v) in predict_probs
        predict_probs[k] = v / total_sum
	end
    
    return predict_probs
end

features_predict = Dict(
        "Height"=> "Short",
        "Weight"=> "Medium",
        "Eyes"=> "Green"
        )

result = predict(cnt_feat, cnt_label, features_predict)
for (k,v) in result
	@printf("%s -> %.2f\n",k,v)
end
