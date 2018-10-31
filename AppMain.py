import os,time,sys

def append(str):
	print str
	f1.write(str);
	f1.write('\n');
pass
def append_http(str):
	f1.write('<br>');
	f1.write('<a href = "');
	f1.write(str + '"');
	f1.write('>');
	f1.write('File: ');
	f1.write(str);
	f1.write('</a>');
	f1.write('\n');
pass
def init_html():
	append('<html>');
	append('<title>Just Do It</title>');
	append('<body>');
pass
def done_html():
	append('</body>');
	append('</html>');
pass

path=os.getcwd()
list = os.listdir(path+'/releases')
filenum = 0
subfilenum = 0
f1= open('./releases/index.html','w')
init_html();

for line in list:
	filepath = os.path.join(path,line)
	if os.path.isdir(filepath):
		for li in os.listdir(filepath):
			print li
	    		subfilenum = subfilenum + 1
	elif os.path:
		append_http(line)
		filenum = filenum + 1
done_html();
f1.close();
print filenum,"File Found In Dir..."
print subfilenum,"File Found In Sub Dir..."
