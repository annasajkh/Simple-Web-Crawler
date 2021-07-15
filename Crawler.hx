import sys.Http;

class Crawler 
{
    public static function crawl(link : String) : List<String> 
    {
        trace("crawling " + link);
        
        var result : String = Http.requestUrl(link);
        var links = new List<String>();

        for(line in result.split(">"))
        {
            if(StringTools.contains(line, "href=\""))
            {
                var link : String = line.split("href=\"")[1].split("\"")[0];

                if(StringTools.contains(link, "http"))
                {
                    links.add(link);
                }
            }
        }

        return links;
    }

}