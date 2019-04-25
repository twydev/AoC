## Javascript

1. Create a sleep function using promise  
```
    function sleep(sleepTime){  
       return new promise(resolve=>setTimeout(resolve,sleepTime));  
    }  
    sleep(500).then(()=>{//do stuff});  
```    
2. Create a retry function for a promise. retry should be executed after certain sleep. (Key points about this question: high order functions, promises, closure)  
```
function retry(promiseFun, sleepTime, retries){  
      let left_retries=retries;  
      return function operation(..arg){  
          return promiseFun(...arg).then((res)=>{return res;})  
                                   .catch((error)=>{  
                                      if(left_retries>0){  
                                          left_retries--;
                                          return sleep(sleepTime).then(()=>operation(...arg));  
                                      }  
                                      else{  
                                          throw error;  
                                      }  
                                   });  
      };  
  }  
  retry(promiseFun,500,3)(...arg).then((res)=>{//do stuff})  
                         .catch((error)=>console.log(error));  
  ``` 
 ## Web General  
   
 1. Describe the process of a page being displayed in browser/How does browser build a page  
    There are basically three steps that the browser takes to build a page.  
  - Build the DOM - a map of where things are displayed on a page according to the HTML.   
  - Build the CSSOM - a map of what styles should be applied to different parts of the page according to the CSS  
  - Build the Render Tree - The render tree essentially takes the DOM and the CSSOM and combines them to create a full map of how the page will actually be laid out and painted.  
    Then 2 main things,
- Layout/Reflow - computes the layout of the page. browser determines how big a screen is and how that will affect the way the page is displayed  
- Paint - convert each node in the render tree to actual pixels on the screen.  
  
 2. What triggers a reflow, repaint  
    There's always at least one initial page layout together with a paint (unless, of course you prefer your pages blank :)). After that, changing the input information which was used to construct the render tree may result in one or both of these.  
- Reflow - parts of the render tree (or the whole tree) will need to be revalidated and the node dimensions recalculated. 
  - insert, remove or update an element in the DOM
  - modify content on the page, e.g. the text in an input box
  - move a DOM element
  - animate a DOM element
  - take measurements of an element such as offsetHeight or getComputedStyle
  - change a CSS style
  - change the className of an element
  - add or remove a stylesheet
  - resize the window
  - scroll
  - A more detailed list https://gist.github.com/paulirish/5d52fb081b3570c81e3a
- Repaint - parts of the screen will need to be updated, either because of changes in geometric properties of a node or because of stylistic change, such as changing the background color. 
  - change visiblity
  - change background, color
  
3. Cookie: is cookie safe, how to secure cookie, how to delete cookie at server side
- Cookie can be vulnerable to XSS
- Use HttpOnly to protect cookie (HttpOnly prevents cookies to be read or set by client side JavaScript). Encrypt cookie at server.
- Just set the cookie on exactly the same name, path and domain, but with an Expires value in the past. Optionally, set the value to null/empty-string, even if it's just to save the bandwidth, it's otherwise ignored anyway by the average client.

4. Differences between Http1.0 and Http1.1
- Proxy support and the Host field:
  - HTTP 1.1 has a required Host header by spec.
  - HTTP 1.0 does not officially require a Host header, but it doesn't hurt to add one, and many applications (proxies) expect to see the Host header regardless of the protocol version.
- Persistent connections (!important)
  - HTTP 1.1 also allows you to have persistent connections which means that you can have more than one request/response on the same HTTP connection.
  - In HTTP 1.0 you had to open a new connection for each request/response pair. And after each response the connection would be closed. This lead to some big efficiency problems because of TCP Slow Start, i.e. 3 way handshake.
- OPTIONS method: HTTP/1.1 introduces the OPTIONS method. An HTTP client can use this method to determine the abilities of the HTTP server. It's mostly used for Cross Origin Resource Sharing in web applications.
- Caching
  - HTTP 1.0 had support for caching via the header: If-Modified-Since.
  - HTTP 1.1 expands on the caching support a lot by using something called 'entity tag'. If 2 resources are the same, then they will have the same entity tags. HTTP 1.1 also adds the If-Unmodified-Since, If-Match, If-None-Match conditional headers. There are also further additions relating to caching like the Cache-Control header.
- Extended: http1.1 vs http 2.2 https://medium.com/@factoryhr/http-2-the-difference-between-http-1-1-benefits-and-how-to-use-it-38094fa0e95b
  
5. Differences between localStorage and sessionStorage
The data stored in localStorage persists until explicitly deleted. Changes made are saved and available for all current and future visits to the site.
For sessionStorage, changes are only available per tab. Changes made are saved and available for the current page in the that tab until it is closed. Once it is closed, the stored data is deleted.

6. Use cases of cookie, localStorage and sessionStorage
- Cookie: session management like login
- localStorage: preferences, shopping carts
- sessionStorage: game score
