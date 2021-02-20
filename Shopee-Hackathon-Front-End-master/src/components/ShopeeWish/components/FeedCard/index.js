import React, {useState, useEffect} from 'react'
import Container from './style/Container'
import ProductPic from './style/ProductPic'
import Profile from './style/Profile'
import ProfilePic from './style/ProfilePic'
import BuyButton from './style/BuyButton'

import { get } from 'libraries/utils/fetch'
import consts from 'consts'

import users from 'data/users.js'

import {LinkToProduct} from 'libraries/components/Link'

function FeedCard(props) {
    const [item, setItem] = useState({})
    
    useEffect(() => {
        let isMounted = true;
        
        (async () => {
            const response = await get(`${consts.API_URL}item/get_info`, {
                item_id: props.item_id || 1642351377,
                shop_id: props.shop_id || 102338025,
            });
            if (isMounted && response) {
                setItem(response.data);
            }
        })();

        return () => {
            isMounted = false;
        };
    }, []);

    const user_id = parseInt(props.user_id)
    const user = users[user_id - 1]
    
    return (
        <Container>
            <ProductPic 
              src={item.cover}
            />
            
            <div style={{margin: "1vw", position: "relative", width: "48vw"}}>
                <Profile>
                    <ProfilePic
                        // src="data:image/jpeg;base64,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"
                        src = {user.pic}
                    />
                    <h4>
                        {user.name}<br/>
                        50 mins ago
                    </h4>
                </Profile>
                
                <p>
                    {props.post}
                </p>
                
                <LinkToProduct shopid={item.shop_id} itemid={item.item_id}>
                    <BuyButton>
                            Buy Now
                    </BuyButton>
                </LinkToProduct>
            </div>
        
        </Container>
    )
}

export default FeedCard