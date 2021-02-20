import React from 'react'
import NavBar from './components/Navbar'
import {Route, Switch} from 'react-router-dom'
import Browse from './screens/Browse'
import Feed from './screens/Feed'
import WishList from './screens/WishList'


function ShopeeWish() {
    return (
        <div>
            <NavBar/>
            <Switch>
                <Route exact path='/ShopeeWish' component={Browse}/>
                <Route exact path='/ShopeeWish/Feed' component={Feed}/>
                <Route exact path='/ShopeeWish/WishList' component={WishList}/>
            </Switch>
        </div>
    )
}

export default ShopeeWish