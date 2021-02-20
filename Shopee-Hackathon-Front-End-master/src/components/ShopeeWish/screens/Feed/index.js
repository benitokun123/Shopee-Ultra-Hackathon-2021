import React, {useState, useEffect} from 'react'
import FeedCard from '../../components/FeedCard'

const url = 'https://flaskshopeebackend.herokuapp.com/friends/2';
function Feed() {
    const [feeds, setFeeds] = useState([])

    useEffect(() => {
        console.log("hello")

        let reqHeader = new Headers();
        reqHeader.append('Content-Type', 'text/json');
    
        let initObject = {
            method: 'GET', headers: reqHeader
        };
    
        fetch(url, initObject)
        .then(function (response) {
            console.log(response);
            return response.json();
        })
        .then(function (data) {
            console.log(data);
            setFeeds(data);
        })
        .catch(function (err) {
            console.log("Something went wrong!", err);
        });

    }, [])

    const FeedCards = feeds.map((f, index) => <FeedCard key={index} {...f}/>)

    return (
        <div>
            {FeedCards}
        </div>
    )
}

export default Feed