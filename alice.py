import json
#read file
fr = open("alice.txt", "r")
# to store chracters frequencies
WordCount = {}

for line in fr:
	# to remove blank rows beside every row
	line=line.strip()
	# do not loop with blank rows 
	if len(line) == 0:
		continue
	
	for word in line.split():
		if word in [' ', '\t', '\n', '。', '，', '(', ')', '（', '）', '：', '□', '？', '！', '《', '》', '、', '；', '“', '”', '……']:
			continue
		
		if word not in WordCount:
			WordCount[word]=1
		else:
			WordCount[word]+=1

fw = open('alice.json','w')
fw.write(json.dumps(WordCount))
fw.close()

WordCount = sorted(WordCount.items(), key = lambda w:w[1], reverse = True)
fw = open('alice.csv','w')
for item in WordCount:
	fw.write(item[0] +','+ str(item[1]) + '\n')
fw.close()

fr.close()