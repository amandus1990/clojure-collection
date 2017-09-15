import DoubanAPI
import pymysql
import sys,time

conn=pymysql.connect(host='localhost', user='XXXXXX', passwd='XXXXXX', db='douban', charset='utf8')
cur=conn.cursor()

userjson=DoubanAPI.user_get(1647881)
DoubanAPI.userlist_insert(userjson,cur,conn)

requestphrase="insert into userlist xxx"
cur.excute(requestphrase)
for r in cur:
        print r

conn.commit()
cur.close()
conn.close()

for i in range(1009758,1018001):
    userjson=DoubanAPI.user_get(str(i))
    sys.stdout.write(str(i)+"\r")
    sys.stdout.flush()
    time.sleep(8)
    if(userjson==0):
        continue
    sqlphrase=DoubanAPI.userlist_insert(userjson)
    try:
        cur.execute(sqlphrase)
        conn.commit()
    except:
        continue

for i in range(1000001,1001001):
    userjson=DoubanAPI.user_followers(str(i))
    sys.stdout.write(str(i)+"\r")
    sys.stdout.flush()
    time.sleep(8)
    if(userjson==0):
        continue
    length=len(userjson)
    sqlphrase=DoubanAPI.userfollowers_insert(userjson)
    try:
        cur.execute(sqlphrase)
        conn.commit()
    except:
        continue

while(True):
    cur.execute("select * from usercount where followerscount>100 order by rand() limit 1;")
    for r in cur:
        username=str(r[0])
    userjson=DoubanAPI.user_followers(username)
    DoubanAPI.usercount_insert(userjson,cur,conn)
    print(username)
    time.sleep(8)
