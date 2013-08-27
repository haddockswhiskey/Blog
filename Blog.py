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
    using set/geters to maintain OO concepts and best practices as decided by the group
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
        url = inUrl
    def setName(self, inName):    
        name = inName
    def setOwner(self, inOwn):
        owne = inOwn
        
    def getUrl(self):
        return self.url
    #duplicate method getName in TextMaster - same thing?
    def getName(self):    
        return self.name
    def getOwner(self):
        return self.owner
    
    def addPost(self, post):
        Post.__init__(name,date,author,body)
    def editPost(self, singlePost, setDraftFlag):
        #I assume this method is for editing ALL (un/published) posts?
    def publish(self, singlePost):
        #selected draft post is published to the site
    def listPosts(self):
        #returns main post list excluding all drafts
        return self.posts

"------------END OF CLASS ONE -------------" 
 
 
 
'''
    Created on 27/08/2013
    Contains date, author, text
    Aggregate from Blog class
    Multiplicity - NOT DISCUSSED
    @author: DaeTa
'''
def TextMaster
    def __init__():
        #do
        
    def setName(self, inName):
        name = inName
    def setDate(self, inDate):
        date = inDate
    def setAuthor(self, inAuth):
        author = inAuth
    def setText(self, inText):
        text = inText
    
    def getName(self):
        return self.name
    def getDate(self):
        return self.date
    def getAuthor(self):
        return self.author
    def getText(self):
        return self.text

"------------END OF CLASS TWO -------------" 


 
'''
    Created on 15/08/2013
    Contains date, author, text
    Inherits from TextMaster
    Multiplicity NOT DECIDED
    @author: DaeTa
'''
#note extra field "name" in this constructor
class Post(TextMaster):
    def __init__(self, name, date, author, text):
        TextMaster.__init__()
    
"------------END OF CLASS THREE -------------" 



'''
    Created on 15/08/2013
    Contains name, date, author, body
    Inherits from TextMaster
    Multiplicity is NOT DECIDED
    @author: DaeTa
'''
class Comment(TextMaster):
        
    def __init__(self, date, author, text):
        TextMaster.__init__()
   
"------------END OF CLASS FOUR -------------" 