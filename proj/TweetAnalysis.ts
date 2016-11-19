class Location{
	Latitude: number;
	Longitute: number;

}

function httpGet(url){
	var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); 
    xmlHttp.responseType = 'json';
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

var sentiments: Map<Location, number> = new Map<Location, number>();

var tweets = httpGet("https://api.twitter.com/1.1/search/tweets.json?q=%23freebandnames&since_id=24012619984051000&max_id=250126199840518145&result_type=mixed&count=4")

let tweet_list: Array<json>;

//convert json to list

for (let tweet in tweets_list{
	//analyze tweet
	//add to map
}

return sentiments;