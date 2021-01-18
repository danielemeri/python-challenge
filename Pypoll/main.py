#PYPOLL



import csv
import os

#path to collect data
csvpath = os.path.join("", "Resources", "election_data.csv")
csvpath_output = ("", "analysis", "election_data.txt")

# function to get name of key
# def getName(vote,dic)
# # iterating for each items
# for n, v in dic.items
# #if matches then return the name
# if vote ==v:
#     return net_change

total_votes = 0
candidates = {}


    #read a file by lines
    with open(csvpath) as csvfile:
        #lines = file.readlines()
        csvreader = csv.reader(csvfile)

        # next pops off header and skips the line of data
        header = next(csvreader)

        # for writing purpose
        #fw= open("election_result.txt"'"w+")
        
        for row in csvreader:
            # starts counter for votes
            total_votes =  total_votes + 1
            candidate + row[2]
            if candidate in candidates.keys():
                candidates[candidate] += 1
            else:
                candidates[candidate] = 1
        print(candidates)


        #initially total votes =0
        total=0
        #empty dictionary
        dic= {}

        #iterating each line to read id, country and name
        for row in lines:
            total=total+1
            #split line by space
            id,country,name = row.split('')

            # check whether name is already found in dict or not
            # if found then increment it count
            if name in dic:
                dic[name]=dic[name]+1
                #if not found then add in dict

                else:
                    dic[name]=1
                    # retrieve the list of names and votes
                    names = list(dic.keys())
                    votes = list(dic.values())

                    #sort the votes
                    votes.sort(reverse=True)

                    # find the winners
                    for name, vote in dic.items():
                        if vote == votes[0]:
                            winner = name

                            # print format
                            print("Election Results")
                            print("-------------------------")
                            print("Total Votes: " + str(total))

                            print("-------------------------\n")

                            # print all candidates
                            for i in votes:
                                # find name
                                name = getName(i,dic)
                                #remove last new line from name
                                name=name[:-1]
                                #calculate % by votes*100/total
                                percent = i*100/total
                                #print name % and total vote the candidate got
                                print(str(name) + ":" + str(round(percent,3)) +"%" "("+str(i) + ")")
                                
                                # write to file
                                fw.write("\n" + str(name) + ":" + str(round(percent,3)) + "%" "(" + str(i) +")")
                                
                                # print winner
                                print("\n---------------------------")
                                print("Winner:" + str(winner))
                                fw.write("\nWinner :%s"% winner)
                                print("--------------------")

                                # close the file
                                fw.close()
                                file.close()



