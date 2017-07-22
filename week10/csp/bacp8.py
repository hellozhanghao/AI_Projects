# data file for 8 period probelm

p=8 
a=10 # minimum academic load allowed per period 
b=24 # maximum academic load allowed per period 
c=2  # minimum amount of courses allowed per period, 4 to make problem  tighter
d=10 # maximum amount of courses allowed per period 8 to make problem tighter

courses8 = [
'dew100','fis100','hcw310','iwg101','mat190','mat192', 'dew101',
'fis101', 'iwi131', 'mat191' , 'mat193' , 'fis102' , 'hxwxx1', 
'iei134' , 'iei141' ,  'mat194', 
'dewxx0', 'hcw311' ,'iei132' ,'iei133', 'iei142', 'iei162', 
'iwn170', 'mat195',  'hxwxx2',  'iei231', 'iei241', 'iei271', 'iei281', 'iwn261', 
'hfw120',  'iei233', 'iei238', 'iei261', 'iei272',  'iei273', 'iei161',  'iei232', 
'iei262', 'iei274',  'iwi365',   'iwn270' , 'hrw130' , 'iei218' , 'iei219' ,'iei248' ]

credit8 = [
1,  3,  1,  2,  4, 
 4,  1,  5,  3,  4, 
 4,  5, 1,  3, 3, 
 4,  1,  1,  3,  3, 
 3,  3,  3,  3,  1, 
 4,  4,  3,  3, 3, 
 2,  4,  3,  3,  3, 
 3,  3,  3,  3,  3, 
 3,  3,  2,  3, 3, 
 3
]

prereq8= [
('dew101','dew100'),
('fis101', 'fis100'),
('fis101', 'mat192'),
('mat191', 'mat190'),
('mat193','mat190'),
('mat193','mat192'),
('fis102','fis101'),
('fis102', 'mat193'),
('iei134' ,  'iwi131'),
('iei141' ,  'iwi131'),
('mat194' , 'mat191'),
('mat194' , 'mat193'),
('dewxx0' ,  'dew101'),
('hcw311' ,  'hcw310'),
('iei132' ,  'iei134'),
('iei133' ,  'iei134'),
('iei142' ,  'iei141'),
('mat195' ,  'mat194'),
('iei231' ,  'iei134'),
('iei241' ,  'iei142'),
('iei271' ,  'iei162'),
('iei281' ,  'mat195'),
('iei233' ,  'iei231'),
('iei238' ,  'iei231'),
('iei261' ,  'iwn261'),
('iei272' , 'iei271'),
('iei273' , 'iei271'),
('iei273' , 'iei271'),
('iei161' , 'iwn261'),
('iei161' , 'iwn261'),
('iei232' , 'iei273'),
('iei232' , 'iei273'),
('iei262' , 'iwn261'),
('iei274' , 'iei273'),
('iei274' , 'iei273'),
('iei219' , 'iei232'),
('iei248' ,  'iei233'),
('iei248' , 'iei233')
]