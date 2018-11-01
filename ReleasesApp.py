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
	append('<title>Software Releases Site</title>');
	append('<body>');
	append('Last update time is: ' + time.strftime('%Y-%m-%d %H:%M:%S') + '<br>');
pass
def done_html():
	append('</body>');
	append('</html>');
pass
def file_extension(path):
	return os.path.splitext(path)[1]
pass
def compare(x, y):
	stat_x = os.stat(path + "/" + x)
	stat_y = os.stat(path + "/" + y)
	if stat_x.st_ctime > stat_y.st_ctime:
		return -1
	elif stat_x.st_ctime < stat_y.st_ctime:
		return 1
	else:
		return 0
pass

path=os.getcwd()+'/releases'

list = os.listdir(path)
list.sort(compare)

filenum = 0
subfilenum = 0
f1= open(path + '/index.html','w')
init_html();

for line in list:
	filepath = os.path.join(path,line)
	print filepath
	if os.path.isdir(filepath):
		for li in os.listdir(filepath):
			print li
	    		subfilenum = subfilenum + 1
	elif os.path.isfile(filepath):
		exec_name = file_extension(filepath);
		if('.html' == exec_name):
			continue;
		if('.htm' == exec_name):
			continue;
		append_http(line)
		filenum = filenum + 1
done_html();
f1.close();
print filenum,"File Found In Dir..."
print subfilenum,"File Found In Sub Dir..."
