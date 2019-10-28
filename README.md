# User-Query-Search-using-Python(CLI)
Stack Overflow is a question and answer site for professional and enthusiast programmers. It's built and run by the community of developer, as part of the Stack Exchange network of Q&amp;A sites. A lot of content is present in form of stack overflow questions and answers, various studies point that developers face problems while development life cycles and they ask questions on stack overflow which gets answered by fellow developers across the globe.

# What can this program do?
To identify most relevant questions to a query
Identify the matching tags and pick top relevant questions from stack overflow.

# Requirements
Python 3.7
Python Libraries: BeautifulSoup, Requests

# Steps to setup the requirements
  1.	Install python 3.7
  2.	Open Command Prompt/Terminal and write the following instructions
  
            pip install bs4 
            
            pip install beautifulsoup4
            
            pip install requests
          
# How does it work? 

The user has the ability to chose to search either by entering tags or by entering a string, representing their query.

# Output
1. Output varies based on the user input
2. You might see an output as "website pass", which means data is being processed from online.
3. Results will involve a series of link which may represent the user query.


# Programs Features
1.	If the user enters a series of tags, then our programs will, filter the set of tags to find those tags which gives the results, making sure that the maximum number of valid tags are involved in the search.
2.	Remove words which might give “No results” from the queries.
3.	See all possible combinations and return those results with highest upvotes.
4.	For more detailed information see “Information.txt” 


# NOTE
"Searching by queries" usually takes a lot of time. This is because the algorithm implemented here makes sure that it removes all the unnecessary words that exists in the query. For example, "How to install python". The algorithm will remove words like "How" and "to" because searching on Stackoverflow with the unmodified query yields no results. Instead searching for "install" and "python" has a better chance to provide results.

The procedure takes time due to the fact that we need to check every single word present in the query. Words are selected from the query if they are available at-

" https://www.oxfordreference.com/view/10.1093/acref/9780199688975.001.0001/acref-9780199688975?btog=chap&hide=true&pageSize=20&skipEditions=true&sort=titlesort&source=%2F10.1093%2Facref%2F9780199688975.001.0001%2Facref-9780199688975 "

The loading time/responsiveness for the above website is very slow. This is one of the main reasons of the slowness of the program.
Any other method to implement the same is appreciated.







