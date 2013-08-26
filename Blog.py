'''
    @author: DaeTa
    Created on 15/08/2013
    Contains the blog title, URL and other metadata.
    All other Blog classes aggregate from this object
    Multiplicity is 1
    revisions by Ze'ev:
    * merged into one file - added appropriate structure
    Blog class, represents the entire blog.
    Use addPost to append a Post object to the post list.
    Wasn't sure about finer implimentation details so Blog
    can be constructed with or without a list of Post objects
    eg. without a Post list (if you want to append later)
    b = Blog("http://www.blog.com", "Awesome blog", "John Snow")
    OR
    b = Blog("http://www.blog.com", "Awesome blog", "John Snow", list(1,2,3,4,5))
'''
 
class Blog():    
    #WHAT IS ALL THIS STUFF????
    self.url = url
    self.name = name
    self.owner = owner
    self.posts = posts
    
    #CONSTRUCTOR - ARE WE HAPPY WITH THE IMPORTS????
    def __init__(self, url, name, owner, posts=list()):
    '''
        CONFIRM OK????
        This constructor requires 3 parameters
        url: The url of the blog
        name: The name of the blog
        owner: The name of the owner of the blog
        There is also an optional 4th parameter
        posts: This is a list of post objects which the Blog
        will be constructed with.
        If this is not provided the blog will be constructed
        with an empty list of Posts
    '''
        
    def setUrl(self, inUrl):
        #do
    def setName(self, inName):    
        #do
    def setOwner(self, inOwn):
        #do
        
    def getUrl(self):
        #do
    def getName(self):    
        #do
    def getOwner(self):
        #do  
    
    #SHOULD THIS BE IN THIS CLASS????   
    def addPost(self, post):
        #self.posts.append(post)
    
    def editPost(self, singlePost,setDraftFlag):
        #something happens
        
    def publish(self, singlePost):
        #something happens
    
    def listPosts(self):
        #returns main post list excluding all drafts
        #return mainPostList



"------------END OF CLASS ONE -------------" 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
'''
    Created on 15/08/2013
    Contains date, author, text
    Aggregate from Post class
    Multiplicity 0:*
    @author: DaeTa
'''
class Post():
    def __init__(self, name, date, author, body):
        #do it
    
    def setName(self, inName):
        #do
    def setDate(self, inDate):
        #do
    def setAuthor(self, inAuth):
        #do
    def setBody(self, inBody):
        #do
    
    def getName(self):
        #do
    def getDate(self):
        #do
    def getAuthor(self):
        #do
    def getBody(self):
        #do


"------------END OF CLASS TWO -------------" 





































 
'''
    Created on 15/08/2013
    Contains name, date, author, body
    Aggregate from Blog class
    Multiplicity is 0:*
    @author: DaeTa
'''
class Comment():
        
    def __init__(self, date, author, text):
        #do
    
    def getDate(self):
        #do
    def getAuthor(self):
        #do
    def getText(self):
        #do
        
    def setDate(self, inDate):
        #do
    def setAuthor(self, inAuth):
        #do
    def setText(self, inText):
        #do
    
    #EH WHAT DOES THIS DO????
    #def Post():


"------------END OF CLASS THREE -------------" 