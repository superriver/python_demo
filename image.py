import  urllib.request
import  os

def main(url,index):
	path = os.getcwd()+u"/思维之剑/"
	if not os.path.isdir(path):
		os.makedirs(path)
	urllib.request.urlretrieve(url,path+'%s.png'%index)
	print("url->"+url)

if __name__ == '__main__':
	global index
	for i in range(1,147):
		if len(str(i)) == 1:
			index ='00'+str(i);
		elif len(str(i)) == 2:
			index = '0'+str(i);
		else:
			index=str(i)
		url = 'http://readsvr.chaoxing.com/n/30e00e3abf99e6c2ac3108282a67a05eMC187465269553/img0/7C72AF8226CC9582C94236A48D487D230745D7D4F483F2E312FCC326DFAFA6E9289DBA73FC48E4A9197E2451956879918B277E6926AB3A987C7B293A9BFF6EC2E751C767BB6B5AA77F2A11CEFF9EE6A64943F0CF836C16073A1C72D77EE15D613B9FA2ACF3C828B8B3F27A0E8DDDD065CA93/bf1/readsvr/11781347/9D3B7625F8C24F3187F4AE84B2FB494B/000'+index+'?.&uf=ssr&zoom=0'
		main(url,index)
		
