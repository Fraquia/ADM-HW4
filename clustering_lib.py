def eu_dist(v1,v2):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(v1, v2)])) #calculating for each component
    return distance

def totalcosts(res):
    Tot_sum = 0
    for i in range(len(res[0])):
        for el in range(len(res[0][i])):
            Tot_sum += eu_dist(res[0][i][el],res[1][i]) #in res[1][i] we find final centres
    return Tot_sum #sum of the distances of all points and their centres

def squareddist(res):
    Tot_sum = 0
    for i in range(len(res[0])):
        for el in range(len(res[0][i])):
            Tot_sum += (eu_dist(res[0][i][el],res[1][i]))**2 
    return Tot_sum

def clustering(k,clusters,vectors_list):
    count = 0                 #var to count in how many steps the algorithm reach the solution

    Final_clusters = []       #it will be a nested list, each sublist is a cluste
    final_mean = []           #here we store last values of centres

    l = []                       # ex : l=[mean1,mean2], used in while cycle to assign points to clusters 
    for i in range(k):
        l.append(clusters[i])

    mean_list = [l]

    var = True
    while var :

        c_dict = {}        #this dict is use to store temporary clusters of the i-th iteration
        for n in range(k):
            c_dict[n]=[]   #each key is a cluster, then we'll fill each one with its closest points

        for i in vectors_list:
            l_temp = []
            for j in range(len(l)):
                l_temp.append(eu_dist(i,l[j])) #store the distance between the sublists and all centres 

            minimum = min(l_temp)       #find the closest array for this sublist list
            ind = l_temp.index(minimum) #find in which cluster it shoul be

            c_dict[ind].append(i)  #each key of the dict is a number from 0 to k-1, so we store each sublist in the right cluster

        l_temp = []
        for n in range(k):
            arr = np.array(c_dict[n]) #c1_ = np.array(c[0])
            mean = list(np.mean(arr, axis = 0, dtype=np.float64)) #mean vector for each
            l_temp.append(mean)

        mean_list.append(l_temp)

        l = l_temp

        #print(mean_list[-2])
        #print(mean_list[-1])
        if mean_list[-2] == mean_list[-1]: #if the last mean is equeal to the previus last one, the mean is not chenging anymore,
                                           # so clusters are not changing continuing to iterate. We stop the algorithm
            for i in range(k):
                Final_clusters.append(c_dict[i]) #we take last clusters we build
            final_mean = mean_list[-1]           #we have memory of the last centres
            var = False
        count += 1
    print('Done In ',count,' steps')
    return [Final_clusters, final_mean]
