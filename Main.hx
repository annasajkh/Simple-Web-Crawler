import haxe.ds.List;
import sys.thread.Thread;

class Main 
{
    static public function main()
    {
        var links = new List<String>();
        var result = Crawler.crawl("http://www.google.com/");

        for(link in result)
        {
            links.add(link);
        }

        while(!links.isEmpty())
        {
            Thread.create(() -> {
                var link = links.pop();
    
                try
                {
                    result = Crawler.crawl(link);
                }
                catch(e)
                {
                    trace("Failed crawling url " + link);
                    trace(e);
                }
    
                for(link in result)
                {
                    links.add(link);
                }
            });
        }
    }
}