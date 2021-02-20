import React, {useState} from 'react'

import Container from './style/Container'
import ProductImg from './style/ProductImg'
import Description from './style/Description'
import Price from './style/Price'
import AddButton from './style/AddButton'

import CreateFeed from '../CreateFeed'

function ProductCard(props) {
    const [visible, setVisible] = useState(false);

    return (
        <Container>
            <ProductImg 
                src={props.cover}
            />

            <Description>
                {props.name}
            </Description>
            
            <Price>
                {props.price.toFixed(2)}
            </Price>
            
            <AddButton onClick={() => setVisible(!visible)}>
                Add
            </AddButton>

            {visible && <CreateFeed setVisible={() => setVisible(!visible)} {...props}/>}
        </Container>
    )
}

export default ProductCard