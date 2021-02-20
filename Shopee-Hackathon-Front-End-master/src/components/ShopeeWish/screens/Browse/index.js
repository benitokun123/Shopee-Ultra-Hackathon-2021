import React, { useState, useCallback } from 'react'
import ProductCard from '../../components/ProductCard'
import ProductList from './style/ProductList'
import SearchInput from './style/SearchInput'
import SearchButton from './style/SearchButton'


import { get } from 'libraries/utils/fetch'
import consts from 'consts'

function Browse() {
    const [keyword, setKeyword] = useState("")
    const [items, setItems] = useState([])

    const searchItems = useCallback(() => {
        (async () => {
          const response = await get(`${consts.API_URL}item/search`, {
            keyword: keyword,
            offset: 0,
            limit: 10,
          });
          if (response && response.data && response.data.items) {
            setItems(response.data.items);
          }
          console.log("success");
        })();
    }, [keyword]);

    const Products = items.map((item, index) => <ProductCard key={index} {...item}/>)

    return (
        <div>
            <SearchInput onChange={event => setKeyword(event.target.value)}/>
            <SearchButton onClick={searchItems}>Search</SearchButton>
            <ProductList>
                {Products}
            </ProductList>
        </div>
    )    
}

export default Browse