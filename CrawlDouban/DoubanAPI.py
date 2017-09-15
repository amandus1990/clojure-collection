from urllib.request import urlopen
import json

# get user information

apikey="%s"
## 要么返回一个长度大于0的列表，要么返回0
def user_following(apikey,name,start=0):
    url="https://api.douban.com/shuo/v2/users/%s/following?apikey=%s&count=200&start=%s"%(str(name),apikey,str(start))
    try:
        htmlfile=urlopen(url).read().decode('utf-8')
        jsonfile=json.loads(htmlfile)
        if(len(jsonfile)>0):
            return(jsonfile)
        else:
            return(0)
    except:
        return(0)

def user_followers(apikey,name,start=0):
    url="https://api.douban.com/shuo/v2/users/%s/followers?apikey=%s&count=200&start=%s"%(str(name),apikey,str(start))
    try:
        htmlfile=urlopen(url).read().decode('utf-8')
        jsonfile=json.loads(htmlfile)
        if(len(jsonfile)>0):
            return(jsonfile)
        else:
            return(0)
    except:
        return(0)

def user_get(apikey,name):
    url="https://api.douban.com/v2/user/%s?apikey=%s"%(str(name),apikey)
    try:
        htmlfile=urlopen(url).read().decode('utf-8')
        jsonfile=json.loads(htmlfile)
        if(len(jsonfile)>0):
            return(jsonfile)
        else:
            return(0)
    except:
        return(0)

def user_search(apikey,query):
    url="https://api.douban.com/v2/user?apikey=%s&q=%s"%(apikey,query)
    try:
        htmlfile=urlopen(url).read().decode('utf-8')
        jsonfile=json.loads(htmlfile)
        if(len(jsonfile)>0):
            return(jsonfile)
        else:
            return(0)
    except:
        return(0)

# get book information

def book_get(apikey,bookid):
    url="https://api.douban.com/v2/book/%s?apikey=%s"%(str(bookid),apikey)
    htmlfile=urlopen(url).read().decode('utf-8')
    jsonfile=json.loads(htmlfile)
    return(jsonfile)

def book_search(apikey,query):
    url="https://api.douban.com/v2/book/search?apikey=%s&q=%s"%(apikey,query)
    htmlfile=urlopen(url).read().decode('utf-8')
    jsonfile=json.loads(htmlfile)
    return(jsonfile)

def book_tags(apikey,bookid):
    url="https://api.douban.com/v2/book/%s/tags?apikey=%s"%(str(bookid),apikey)
    htmlfile=urlopen(url).read().decode('utf-8')
    jsonfile=json.loads(htmlfile)
    return(jsonfile)

def user_booktags(apikey,name):
    url="https://api.douban.com/v2/book/user/%s/tags?apikey=%s"%(str(name),apikey)
    try:
        htmlfile=urlopen(url).read().decode('utf-8')
        jsonfile=json.loads(htmlfile)
        if(len(jsonfile)>0):
            return(jsonfile)
        else:
            return(0)
    except:
        return(0)

def user_bookcollections(apikey,name,start=0):
    status='read'
    url="https://api.douban.com/v2/book/user/%s/collections?apikey=%s&status=%s&count=100&start=%s"%(str(name),apikey,status,str(start))
    try:
        htmlfile=urlopen(url).read().decode('utf-8')
        jsonfile=json.loads(htmlfile)
        if(len(jsonfile)>0):
            return(jsonfile)
        else:
            return(0)
    except:
        return(0)

# get movie information

def movie_get(apikey,movieid):
    url="https://api.douban.com/v2/movie/subject/"+str(movieid)+"?apikey="+apikey
    try:
        htmlfile=urlopen(url).read().decode('utf-8')
        jsonfile=json.loads(htmlfile)
        if(len(jsonfile)>0):
            return(jsonfile)
        else:
            return(0)
    except:
        return(0)

def movie_search(apikey,query):
    url="https://api.douban.com/v2/movie/search?apikey="+apikey+"&q="+query
    try:
        htmlfile=urlopen(url).read().decode('utf-8')
        jsonfile=json.loads(htmlfile)
        if(len(jsonfile)>0):
            return(jsonfile)
        else:
            return(0)
    except:
        return(0)

def movie_in_theaters(apikey,city):
    url="https://api.douban.com/v2/movie/in_theaters?apikey="+apikey+"&city="+city
    try:
        htmlfile=urlopen(url).read().decode('utf-8')
        jsonfile=json.loads(htmlfile)
        if(len(jsonfile)>0):
            return(jsonfile)
        else:
            return(0)
    except:
        return(0)

def movie_coming_soon(apikey):
    url="https://api.douban.com/v2/movie/coming_soon?apikey="+apikey+"&count=100"
    try:
        htmlfile=urlopen(url).read().decode('utf-8')
        jsonfile=json.loads(htmlfile)
        if(len(jsonfile)>0):
            return(jsonfile)
        else:
            return(0)
    except:
        return(0)

# get music information

def music_get(apikey,musicid):
    url="https://api.douban.com/v2/music/"+musicid+"?apikey="+apikey
    htmlfile=urlopen(url).read().decode('utf-8')
    jsonfile=json.loads(htmlfile)
    return(jsonfile)

def music_tags(apikey,musicid):
    url="https://api.douban.com/v2/music/"+musicid+"/tags?apikey="+apikey
    htmlfile=urlopen(url).read().decode('utf-8')
    jsonfile=json.loads(htmlfile)
    return(jsonfile)

def music_search(apikey,query):
    url="https://api.douban.com/v2/music/search?apikey="+apikey+"&q="+query
    htmlfile=urlopen(url).read().decode('utf-8')
    jsonfile=json.loads(htmlfile)
    return(jsonfile)

# insert or update data

def userlist_insert(userjson,cur,conn):
    if(type(userjson)==int):
        return(0)
    res="SELECT * from userlist where id=%s;"%(str(userjson['id']))
    isinlist=cur.execute(res)
    if(isinlist>0):
        try:
            cur.execute('UPDATE userlist SET uid=%s,name=%s,avatar=%s,created=%s,`desc`=%s,signature=%s,updated=NOW() where id=%s;',(str(userjson['uid']),str(userjson['name']),str(userjson['avatar']),str(userjson['created']),str(userjson['desc']),str(userjson['signature']),str(userjson['id'])))
            conn.commit()
            return(1)
        except:
            print("userlist_insert,wrong:"+str(userjson['id'])+",with isinlist="+str(isinlist))
            return(0)
    else:
        try:
            cur.execute('INSERT INTO userlist (id,uid,name,avatar, created,`desc`,signature,updated) VALUES (%s,%s,%s,%s,%s,%s,%s,NOW());',(str(userjson['id']),str(userjson['uid']),str(userjson['name']),str(userjson['avatar']),str(userjson['created']),str(userjson['desc']),str(userjson['signature'])))
            conn.commit()
            return(1)
        except:
            print("userlist_insert,wrong:"+str(userjson['id'])+",with isinlist="+str(isinlist))
            return(0)

def usercount_insert(userjson,cur,conn):
    if(type(userjson)==int):
        return(0)
    for i in range(0,len(userjson)):
        res="SELECT * from usercount where id=%s;"%(str(userjson[i]['id']))
        isinlist=cur.execute(res)
        if(isinlist>0):
            res="UPDATE usercount SET statusescount=\'"+str(userjson[i]['statuses_count'])+"\',followingcount=\'"+str(userjson[i]['following_count'])+"\',followerscount=\'"+str(userjson[i]['followers_count'])+"\',updated=NOW() where id="+str(userjson[i]['id'])+";"
        else:
            res="INSERT INTO usercount (id,statusescount,followingcount,followerscount,updated) VALUES (\'"+str(userjson[i]['id'])+"\',\'"+str(userjson[i]['statuses_count'])+"\',\'"+str(userjson[i]['following_count'])+"\',\'"+str(userjson[i]['followers_count'])+"\',NOW());"
        try:
            cur.execute(res)
            conn.commit()
        except:
            print("usercount_insert,wrong:"+str(userjson[i]['id'])+",with isinlist="+str(isinlist))
            continue
    return(1)

def userbookcount_insert(userid,count,status,cur,conn):
    res="SELECT * from userbookcount where id=%s;"%(userid)
    isinlist=cur.execute(res)
    if(isinlist>0):
        if(status=="wish"):
            res="UPDATE userbookcount SET wish="+str(count)+",updated=NOW() where id="+str(userid)+";"
        if(status=="reading"):
            res="UPDATE userbookcount SET reading="+str(count)+",updated=NOW() where id="+str(userid)+";"
        if(status=="read"):
            res="UPDATE userbookcount SET `read`="+str(count)+",updated=NOW() where id="+str(userid)+";"
    else:
        if(status=="wish"):
            res="INSERT INTO userbookcount (id,wish,updated) VALUES (%s,%s,NOW());"%(str(userid),str(count))
        if(status=="reading"):
            res="INSERT INTO userbookcount (id,reading,updated) VALUES (%s,%s,NOW());"%(str(userid),str(count))
        if(status=="read"):
            res="INSERT INTO userbookcount (id,`read`,updated) VALUES (%s,%s,NOW());"%(str(userid),str(count))
    try:
        cur.execute(res)
        conn.commit()
        return(1)
    except:
        print("userbookcount_insert,wrong:"+str(userid)+",with isinlist="+str(isinlist))
        return(0)

def userbookcollections_insert(collectionjson,cur,conn):
    if(type(collectionjson)==int):
        return(0)
    res="SELECT * from userbookcollections where id=%s;"%(str(collectionjson['id']))
    isinlist=cur.execute(res)
    if(isinlist>0):
        try:
            cur.execute('UPDATE userbookcollections SET userid=%s,bookid=%s,status=%s,rating=%s,tags=%s,comment=%s,updated=%s where id=%s;',(str(collectionjson['user_id']),str(collectionjson['book_id']),str(collectionjson['status']),str(collectionjson.get('rating',None)),str(collectionjson.get('tags',None)),str(collectionjson.get('comment','Null')),str(collectionjson['updated']),str(collectionjson['id'])))
            conn.commit()
            return(1)
        except:
            print("userbookcollections_insert,wrong:"+str(collectionjson['id'])+",with isinlist="+str(isinlist))
            return(0)
    else:
        try:
            cur.execute('INSERT INTO userbookcollections (id, userid, bookid, status, rating, tags, comment, updated) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);',(str(collectionjson['id']),str(collectionjson['user_id']),str(collectionjson['book_id']),str(collectionjson['status']),str(collectionjson.get('rating',None)),str(collectionjson.get('tags',None)),str(collectionjson.get('comment','Null')),str(collectionjson['updated'])))
            conn.commit()
            return(1)
        except:
            print("userbookcollections_insert,wrong:"+str(collectionjson['id'])+",with isinlist="+str(isinlist))
            return(0)

def booklist_insert(bookjson,cur,conn):
    if(type(bookjson)==int):
        return(0)
    res="SELECT * from booklist where id=%s;"%(str(bookjson['id']))
    isinlist=cur.execute(res)
    if(isinlist>0):
        try:
            cur.execute('UPDATE booklist SET isbn10=%s,isbn13=%s,title=%s,origintitle=%s,alttitle=%s,subtitle=%s,image=%s,author=%s,translator=%s,publisher=%s,pubdate=%s,rating=%s,tags=%s,binding=%s,price=%s,series=%s,pages=%s,authorintro=%s,summary=%s,catalog=%s,updated=NOW() where id=%s;',(str(bookjson['isbn10']),str(bookjson.get('isbn13',None)),str(bookjson['title']),str(bookjson.get('origin_title',None)),str(bookjson.get('alt_title',None)),str(bookjson.get('subtitle',None)),str(bookjson.get('image',None)),str(bookjson.get('author',None)),str(bookjson.get('translator',None)),str(bookjson.get('publisher',None)),str(bookjson.get('pubdate','1001-01-01')),str(bookjson.get('rating',None)),str(bookjson.get('tags',None)),str(bookjson.get('binding',None)),str(bookjson.get('price',None)),str(bookjson.get('series',None)),str(bookjson.get('pages',0)),str(bookjson.get('author_intro',None)),str(bookjson.get('summary',None)),str(bookjson.get('catalog',None)),str(bookjson['id'])))
            conn.commit()
            return(1)
        except:
            print("booklist_insert,wrong:"+str(bookjson['id'])+",with isinlist="+str(isinlist))
            return(0)
    else:
        try:
            cur.execute('INSERT INTO booklist (id, isbn10, isbn13, title, origintitle, alttitle, subtitle, image, author, translator, publisher, pubdate, rating, tags, binding, price, series, pages, authorintro, summary, catalog, updated) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW());',(str(bookjson['id']),str(bookjson['isbn10']),str(bookjson.get('isbn13',None)),str(bookjson['title']),str(bookjson.get('origin_title',None)),str(bookjson.get('alt_title',None)),str(bookjson.get('subtitle',None)),str(bookjson.get('image',None)),str(bookjson.get('author',None)),str(bookjson.get('translator',None)),str(bookjson.get('publisher',None)),str(bookjson.get('pubdate','1001-01-01')),str(bookjson.get('rating',None)),str(bookjson.get('tags',None)),str(bookjson.get('binding',None)),str(bookjson.get('price',None)),str(bookjson.get('series',None)),str(bookjson.get('pages',0)),str(bookjson.get('author_intro',None)),str(bookjson.get('summary',None)),str(bookjson.get('catalog',None))))
            conn.commit()
            return(1)
        except:
            print("booklist_insert,wrong:"+str(bookjson['id'])+",with isinlist="+str(isinlist))
            return(0)
