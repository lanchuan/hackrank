class Solution(object):
	def findSubstring(self, s, words):

		lw=len(words[0])
		l=len(words)
		d={}
		res=[]

		def init():
			for i in words:
				d[i]=0
			for i in words:
				d[i]+=1
		def equal(a,b):
			if b-a==lw*l:
				if a not in res:
					res.append(a)
		def window(s,start,end):
			init()
			while end<len(s):
				s1=s[end:end+lw]
				print s1,'s1'
				if s1 not in words:
					return end
				else:
					d[s1]-=1
					end+=lw
				while d[s1]<0:
					s2=s[start:start+lw]
					print s2,'s2'
					d[s2]+=1
					start+=lw			
				equal(start,end)
			return end

		for k in range(lw):
			i=k
			j=len(s)-lw*l
			while i<=j:
				r=window(s,i,i)
				i=r+lw

		return sorted(res)

s=Solution()
a="aaa"
b=["a","b"]
print s.findSubstring(a,b)
c="barfoothefoobarman"
d=["foo", "bar"]
print s.findSubstring(c,d)
e="barfoofoobarthefoobarman"
f=["bar","foo","the"]
print s.findSubstring(e,f)
g="aaaaaaaaaa"
h=["aa","aa","aa"]
print s.findSubstring(g,h)
i="eplcxnqwwrxqcwhnsgjheooerswiabzeqmgqcxmyqjqshxhadqjjgypxsoitphxiveyxdmxvxnnelxgqnqcuqrtihbbzkzhgfhfktdfqquwdrdwftabjtutbwvagwhodqunjzsbrmxxgatlvtmgmianevpntybwoxjxwdaorylxagkwbycnhedlbuautcqhzbhwghmyfzxifieggivnnabovblofdvffcdlmrltqjbxthdbqapfbsvwvgkbmhirmneygstwdvtwcyxuyobbizxehjhtrrmfgrfmjyiovdkydjudyyfgxemeovyhmkmsdteorocntmnywjcwhjcenrjbmjibtwvxpcljsoymclmawqwezbknuvqgebjyzfxphkabaypdlcfhscnufyhztzhyaryayvrhfrigrylcaqluuzozzxysxiszzqbznsgvlodcmogoesjbtxasxbmujfvkxxjnrpiffljszqifkrgdrjvokhkvoffoeobyfjdkwmevencoglrxuongyxbofgclwdjboonkbshhhkwnxplrgazeaaufgxseceftssdvmndtzzhwqupwwocwoxdwwwaachtuzzqomvjlwsjmmyjlonhcknagjahljchkbzypuicqaldploazbjdowfwhhfuqicblbzbyjdomrtbejdgnolblrxuydppltqyurzudfjpyeseoxkblwcynbtlekcrduqzorurwfiwjabxzlakjelwgekmoogrjyqxpmqorykbanazbblkfwjnataqhgjsecpvofjgfwjfjjgkksxsogfrbhjkntdtvuplaythwcngmtsynpsevavyhejvzmqwgfiigbqcgfkuadsounssnpqutzrvnkrwpbexfwalbmfcpzsmokebzuyuwrrjbjftmmqtkqgofnsupkidumhvjfphyhqasytgmjawcgkhwcdloooiavdlcvsbeldwjwexhevlniujmyubmkloipakmunqfsoqoupybljotezfevgshsgpjicxfppkifdyzsyadkqyoreummmugujrfnomdfynkbnkummzwdymueijswfzsqqzehljmkwxlljhzvjxahlvntgfplgibzjfgvoufmtsacczalzaukxhedovqvfuupzckqwresjgwlgwwhzqryzveorujwofnqjxihoozavwldukkvcbuczasswdoniedrbnysbasywfbsplqspmwomogirwvbaauenswruqpsvtllebfvpbjbrrlkqhlqjfwzzsquihmgazrhcycrbosshgcxnpqyumxvhprpxgvxfogkojbpzwhgcleraupwgpunelfdrcdztjjhsmxtigam"
j=["dkqyoreummmugujrfnomdfynkbnk","nolblrxuydppltqyurzudfjpyese","fmtsacczalzaukxhedovqvfuupzc","kqwresjgwlgwwhzqryzveorujwof","achtuzzqomvjlwsjmmyjlonhckna","umhvjfphyhqasytgmjawcgkhwcdl","ofjgfwjfjjgkksxsogfrbhjkntdt","oxkblwcynbtlekcrduqzorurwfiw","myubmkloipakmunqfsoqoupybljo","girwvbaauenswruqpsvtllebfvpb","oooiavdlcvsbeldwjwexhevlniuj","oniedrbnysbasywfbsplqspmwomo","fkrgdrjvokhkvoffoeobyfjdkwme","nqjxihoozavwldukkvcbuczasswd","kbshhhkwnxplrgazeaaufgxsecef","ummzwdymueijswfzsqqzehljmkwx","gjahljchkbzypuicqaldploazbjd","jabxzlakjelwgekmoogrjyqxpmqo","owfwhhfuqicblbzbyjdomrtbejdg","vencoglrxuongyxbofgclwdjboon","zmqwgfiigbqcgfkuadsounssnpqu","tssdvmndtzzhwqupwwocwoxdwwwa","rykbanazbblkfwjnataqhgjsecpv","vuplaythwcngmtsynpsevavyhejv","lljhzvjxahlvntgfplgibzjfgvou","zuyuwrrjbjftmmqtkqgofnsupkid","tezfevgshsgpjicxfppkifdyzsya","tzrvnkrwpbexfwalbmfcpzsmokeb"]
k="mississippi"
l=["si","is"]
print s.findSubstring(i,j)
print s.findSubstring(k,l)
m="lingmindraboofooowingdingbarrwingmonkeypoundcake"
n=["fooo","barr","wing","ding","wing"]
print s.findSubstring(m,n)