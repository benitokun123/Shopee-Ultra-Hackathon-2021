import React, {useState} from 'react'
import Container from './style/Container'
import Text from './style/Text'
import TextArea from './style/TextArea'
import Button from '../Button'

import axios from 'axios'

const url = 'https://flaskshopeebackend.herokuapp.com/wishlist/2';

const sendToDb = (info) => {
    console.log("hello")
      axios.put(url, info).then(res => alert("Wished Weeshed"))
        .catch(err => console.log(err.response));

    // let reqHeader = new Headers();
    // reqHeader.append('Content-Type', 'text/json');
    
    // let initObject = {
    //     method: 'PUT', headers: reqHeader, body: JSON.stringify(info)
    // };

    // fetch(url, initObject)
    //     .then(function (response) {
    //         return response.json();
    //     })
    //     .then(function (data) {
    //         console.log(data);
    //     })
    //     .catch(function (err) {
    //         console.log("Something went wrong!", err);
    //     });
}

function CreateFeed(props) {
    const [comment, setComment] = useState('');
    
    return (
        <Container>
            <Text>Share what you think</Text>
            
            <TextArea onChange={e => setComment(e.target.value)}/>
            
            <Button onClick={props.setVisible}>Cancel</Button>
            
            &nbsp; &nbsp;
            <Button onClick={() => {
                sendToDb({item_id: props.item_id, post: comment, shop_id: props.shop_id})
                props.setVisible()
                }
            }>
                Share
            </Button>

        </Container>
    )
}

export default CreateFeed