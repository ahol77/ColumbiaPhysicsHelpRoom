import os
import shutil

def write_link(f):
	f.write(b'<link rel="stylesheet" href="styles.css">\n\n')

def write_course_link(f):
	f.write(b'<link rel="stylesheet" href="../styles.css">\n\n')

def write_intro(f):
	f.write(b'''<h1>Welcome to the Columbia Physics Help Room!</h1>
<p>Please select your course number below. From there, you can check out the TA schedule and enter one of the rooms.</p>
<p>In order for the TA to help every student, please only enter the TA room when you or your group have a question. Then, please leave the TA room when your questions are answered.''' + b'\n\n')

def write_course_intro(f, course):
	f.write(b'<h1>Welcome to the Columbia Physics Help Room for Course ' + course + b'''!</h1>
<p>You can see the TA schedule below. Please select a room to enter below. You can change your room at any time.</p>
<p>In order for the TA to help every student, please only enter the TA room when you or your group have a question. Then, please leave the TA room when your questions are answered.''' + b'\n\n')

def write_footer(f):
	f.write(b'''<footer>
<p><small>This project is maintained by <a href="https://github.com/AddingAddict">AddingAddict</a>. Hosted on GitHub Pages &mdash; Theme by <a href="https://github.com/orderedlist">orderedlist</a></small></p>
</footer>''' + b'\n\n')

def write_courses(f, courses):
	f.write(b'<h1>Courses</h1>\n')
	for i in range(len(courses)):
		f.write(b'<p><a href="' + courses[i] + b'/index.html">' + courses[i] + b'</a></p>\n')
	f.write(b'\n')

def write_rooms(f, nstudrooms, nroom=-1):
	f.write(b'''<h1>Rooms</h1>
<p>''')
	for i in range(nstudrooms):
		if nroom==i:
			f.write(b'Room ' + str(i+1).encode() + b' &nbsp;')
		else:
			f.write(b'<a href="room' + str(i+1).encode() + b'.html">Room ' + str(i+1).encode() + b'</a> &nbsp;')
	f.write(b'</p>\n<p>')
	if nroom==nstudrooms:
		f.write(b'TA Room')
	else:
		f.write(b'<a href="room' + str(nstudrooms+1).encode() + b'.html">TA Room</a>')
	f.write(b'</p>\n\n')

def write_schedule(f, course):
	f.write(b'''<h1>TA Schedule</h1>
<img src="../''' + course + b'.png" alt="TA schedule" style="height:calc(100% - 400px); padding-bottom:20px">\n\n')

def write_iframe(f, course, nroom):
	f.write(b'<iframe src="https://meet.jit.si/CPHRCourse' + course + b'Room' + str(nroom+1).encode() + b'" allow="camera;microphone" style="width:100%; height:calc(100% - 160px)"></iframe>\n\n')

def write_css(f):
	f.write(b'''@font-face{font-family:'Noto Sans';font-weight:400;font-style:normal;src:url("../fonts/Noto-Sans-regular/Noto-Sans-regular.eot");src:url("../fonts/Noto-Sans-regular/Noto-Sans-regular.eot?#iefix") format("embedded-opentype"),local("Noto Sans"),local("Noto-Sans-regular"),url("../fonts/Noto-Sans-regular/Noto-Sans-regular.woff2") format("woff2"),url("../fonts/Noto-Sans-regular/Noto-Sans-regular.woff") format("woff"),url("../fonts/Noto-Sans-regular/Noto-Sans-regular.ttf") format("truetype"),url("../fonts/Noto-Sans-regular/Noto-Sans-regular.svg#NotoSans") format("svg")}
@font-face{font-family:'Noto Sans';font-weight:700;font-style:normal;src:url("../fonts/Noto-Sans-700/Noto-Sans-700.eot");src:url("../fonts/Noto-Sans-700/Noto-Sans-700.eot?#iefix") format("embedded-opentype"),local("Noto Sans Bold"),local("Noto-Sans-700"),url("../fonts/Noto-Sans-700/Noto-Sans-700.woff2") format("woff2"),url("../fonts/Noto-Sans-700/Noto-Sans-700.woff") format("woff"),url("../fonts/Noto-Sans-700/Noto-Sans-700.ttf") format("truetype"),url("../fonts/Noto-Sans-700/Noto-Sans-700.svg#NotoSans") format("svg")}
@font-face{font-family:'Noto Sans';font-weight:400;font-style:italic;src:url("../fonts/Noto-Sans-italic/Noto-Sans-italic.eot");src:url("../fonts/Noto-Sans-italic/Noto-Sans-italic.eot?#iefix") format("embedded-opentype"),local("Noto Sans Italic"),local("Noto-Sans-italic"),url("../fonts/Noto-Sans-italic/Noto-Sans-italic.woff2") format("woff2"),url("../fonts/Noto-Sans-italic/Noto-Sans-italic.woff") format("woff"),url("../fonts/Noto-Sans-italic/Noto-Sans-italic.ttf") format("truetype"),url("../fonts/Noto-Sans-italic/Noto-Sans-italic.svg#NotoSans") format("svg")}
@font-face{font-family:'Noto Sans';font-weight:700;font-style:italic;src:url("../fonts/Noto-Sans-700italic/Noto-Sans-700italic.eot");src:url("../fonts/Noto-Sans-700italic/Noto-Sans-700italic.eot?#iefix") format("embedded-opentype"),local("Noto Sans Bold Italic"),local("Noto-Sans-700italic"),url("../fonts/Noto-Sans-700italic/Noto-Sans-700italic.woff2") format("woff2"),url("../fonts/Noto-Sans-700italic/Noto-Sans-700italic.woff") format("woff"),url("../fonts/Noto-Sans-700italic/Noto-Sans-700italic.ttf") format("truetype"),url("../fonts/Noto-Sans-700italic/Noto-Sans-700italic.svg#NotoSans") format("svg")}.highlight table td{padding:5px}.highlight table pre{margin:0}.highlight .cm{color:#999988;font-style:italic}.highlight .cp{color:#999999;font-weight:bold}.highlight .c1{color:#999988;font-style:italic}.highlight .cs{color:#999999;font-weight:bold;font-style:italic}.highlight .c,.highlight .cd{color:#999988;font-style:italic}.highlight .err{color:#a61717;background-color:#e3d2d2}.highlight .gd{color:#000000;background-color:#ffdddd}.highlight .ge{color:#000000;font-style:italic}.highlight .gr{color:#aa0000}.highlight .gh{color:#999999}.highlight .gi{color:#000000;background-color:#ddffdd}.highlight .go{color:#888888}.highlight .gp{color:#555555}.highlight .gs{font-weight:bold}.highlight .gu{color:#aaaaaa}.highlight .gt{color:#aa0000}.highlight .kc{color:#000000;font-weight:bold}.highlight .kd{color:#000000;font-weight:bold}.highlight .kn{color:#000000;font-weight:bold}.highlight .kp{color:#000000;font-weight:bold}.highlight .kr{color:#000000;font-weight:bold}.highlight .kt{color:#445588;font-weight:bold}.highlight .k,.highlight .kv{color:#000000;font-weight:bold}.highlight .mf{color:#009999}.highlight .mh{color:#009999}.highlight .il{color:#009999}.highlight .mi{color:#009999}.highlight .mo{color:#009999}.highlight .m,.highlight .mb,.highlight .mx{color:#009999}.highlight .sb{color:#d14}.highlight .sc{color:#d14}.highlight .sd{color:#d14}.highlight .s2{color:#d14}.highlight .se{color:#d14}.highlight .sh{color:#d14}.highlight .si{color:#d14}.highlight .sx{color:#d14}.highlight .sr{color:#009926}.highlight .s1{color:#d14}.highlight .ss{color:#990073}.highlight .s{color:#d14}.highlight .na{color:#008080}.highlight .bp{color:#999999}.highlight .nb{color:#0086B3}.highlight .nc{color:#445588;font-weight:bold}.highlight .no{color:#008080}.highlight .nd{color:#3c5d5d;font-weight:bold}.highlight .ni{color:#800080}.highlight .ne{color:#990000;font-weight:bold}.highlight .nf{color:#990000;font-weight:bold}.highlight .nl{color:#990000;font-weight:bold}.highlight .nn{color:#555555}.highlight .nt{color:#000080}.highlight .vc{color:#008080}.highlight .vg{color:#008080}.highlight .vi{color:#008080}.highlight .nv{color:#008080}.highlight .ow{color:#000000;font-weight:bold}.highlight .o{color:#000000;font-weight:bold}.highlight .w{color:#bbbbbb}.highlight{background-color:#f8f8f8}
body{background-color:#fff;padding:10px;font:14px/1.5 "Noto Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;color:#727272;font-weight:400}
h1,h2,h3,h4,h5,h6{color:#222;margin:0 0 20px}
p,ul,ol,table,pre,dl{margin:0 0 20px}
h1,h2,h3{line-height:1.1}
h1{font-size:28px}
h2{color:#393939}
h3,h4,h5,h6{color:#494949}
a{color:#267CB9;text-decoration:none}
a:hover,a:focus{color:#069;font-weight:bold}
a small{font-size:11px;color:#777;margin-top:-0.3em;display:block}
a:hover small{color:#777}.wrapper{width:860px;margin:0 auto}
blockquote{border-left:1px solid #e5e5e5;margin:0;padding:0 0 0 20px;font-style:italic}
code,pre{font-family:Monaco, Bitstream Vera Sans Mono, Lucida Console, Terminal, Consolas, Liberation Mono, DejaVu Sans Mono, Courier New, monospace;color:#333}
pre{padding:8px 15px;background:#f8f8f8;border-radius:5px;border:1px solid #e5e5e5;overflow-x:auto}
table{width:100%;border-collapse:collapse}
th,td{text-align:left;padding:5px 10px;border-bottom:1px solid #e5e5e5}
dt{color:#444;font-weight:700}
th{color:#444}
img{max-width:100%}
header{width:270px;float:left;position:fixed;-webkit-font-smoothing:subpixel-antialiased}
header ul{list-style:none;height:40px;padding:0;background:#f4f4f4;border-radius:5px;border:1px solid #e0e0e0;width:270px}
header li{width:89px;float:left;border-right:1px solid #e0e0e0;height:40px}
header li:first-child a{border-radius:5px 0 0 5px}
header li:last-child a{border-radius:0 5px 5px 0}
header ul a{line-height:1;font-size:11px;color:#676767;display:block;text-align:center;padding-top:6px;height:34px}
header ul a:hover,header ul a:focus{color:#675C5C;font-weight:bold}
header ul a:active{background-color:#f0f0f0}
strong{color:#222;font-weight:700}
header ul li+li+li{border-right:none;width:89px}
header ul a strong{font-size:14px;display:block;color:#222}
section{width:500px;float:right;padding-bottom:50px}
small{font-size:11px}
hr{border:0;background:#e5e5e5;height:1px;margin:0 0 20px}
footer{width:100%;float:left;position:fixed;bottom:0px;-webkit-font-smoothing:subpixel-antialiased}
@media print, screen and (max-width: 960px){div.wrapper{width:auto;margin:0}
header,section,footer{float:none;position:static;width:auto}
header{padding-right:320px}
section{border:1px solid #e5e5e5;border-width:1px 0;padding:20px 0;margin:0 0 20px}
header a small{display:inline}
header ul{position:absolute;right:50px;top:52px}}
@media print, screen and (max-width: 720px){body{word-wrap:break-word}
header{padding:0}
header ul,header p.view{position:static}
pre,code{word-wrap:normal}}
@media print, screen and (max-width: 480px){body{padding:15px}
header ul{width:99%}
header li,header ul li+li+li{width:33%}}
@media print{body{padding:0.4in;font-size:12pt;color:#444}}''')

courses = [b'UN1201-Shaevitz', b'UN1201-Dodd', b'UN1401', b'UN1403', b'UN1601']
pwd = os.getcwd()
# courses = list(sorted(map(lambda file: file[0:-4].encode(), filter(lambda file: '.png' in file, os.listdir(pwd)))))
nstudrooms = 3

# sched_id = b'1H6gcrSlbn07FCXwlsoLYI-wH9QeDpY-917sJPh6tl_M'
# sched_gid = {
# 	b'UN1201-Shaevitz':	b'1317068772',
# 	b'UN1201-Dodd': 	b'1761739564',
# 	b'UN1401':			b'76900165',
# 	b'UN1403':			b'699048309',
# 	b'UN1601':			b'358473072'
# }

# write styles.css
with open('styles.css', 'w') as f:
	write_css(f)

# make directories for each course
for course in courses:
	try:
		os.mkdir(pwd + '/' + course)
	except:
		pass
	# shutil.copy('styles.css', course + '/' + 'styles.css')

# write index.html
with open('index.html', 'w') as f:
	write_link(f)
	write_intro(f)
	write_courses(f, courses)
	write_footer(f)

# write /course/room#.html
for course in courses:
	with open(course + '/index.html', 'w') as f:
		write_course_link(f)
		write_course_intro(f, course)
		write_rooms(f, nstudrooms)
		write_schedule(f, course)
		write_footer(f)
	for n in range(nstudrooms + 1):
		with open(course + '/room' + str(n+1) + '.html', 'w') as f:
			write_course_link(f)
			write_rooms(f, nstudrooms, n)
			write_iframe(f, course, n)
			write_footer(f)
