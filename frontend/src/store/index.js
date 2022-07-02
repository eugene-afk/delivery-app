import { createStore } from 'vuex'

//TODO: add modules
export default createStore({
  state: {
    alert: false,    
    cart: {
      amount: 0,
      items: []
    },
    shopProducts: [],
    selectedShop: 0,
    shopLocation: {
      lat: 0,
      lng: 0,
    }
  },
  getters: {
    getShopProducts(state){
      return state.shopProducts
    },

    getCart(state){
      return state.cart
    },

    getCartItemsCount(state){
      return state.cart.items.length
    },

    getSelectedShopId(state){
      return state.selectedShop
    },    

    getShopLocation(state){
      return state.shopLocation
    },
    getAlertState(state){
      return state.alert
    },  
  },
  mutations: {
    SET_SHOP_PRODUCTS(state, items){
      state.shopProducts = items
    },
    
    SET_SELECTED_SHOP(state, id){
      state.selectedShop = id
    },

    ADD_CART_ITEM(state, item){
      item.qty = 1
      item.price = parseFloat(item.price).toFixed(2)
      item.total = parseFloat(item.price).toFixed(2)
      state.cart.items.push(item) 
    },

    DELETE_CART_ITEM(state, id){
      state.cart.items = state.cart.items.filter(x => {
        if(x.id !== id){
          return x
        }
      })
    },

    EMPTY_CART(state){
      state.cart.items = []
      state.cart.amount = 0
    },

    UPDATE_QTY_CART_ITEM(state, {id, qty}){
      let item = state.cart.items.find(x => x.id === id)
      item.qty = qty
      item.total = parseFloat((item.qty * parseFloat(item.price).toFixed(2))).toFixed(2) 
    },

    INCREASE_QTY_CART_ITEM(state, id){      
      let item = state.cart.items.find(x => x.id === id)
      item.qty += 1
      item.total = parseFloat((item.qty * parseFloat(item.price).toFixed(2))).toFixed(2)
    },

    DECREASE_QTY_CART_ITEM(state, id){
      let item = state.cart.items.find(x => x.id === id)
      item.qty -= 1
      item.total = parseFloat((item.qty * parseFloat(item.price).toFixed(2))).toFixed(2) 
    },

    UPDATE_CART_AMOUNT(state){
      var amount = 0;
      for(var i = 0; i < state.cart.items.length; ++i){
        amount += (state.cart.items[i].qty * state.cart.items[i].price)
      }
      state.cart.amount = parseFloat(amount).toFixed(2)
    },

    SET_SHOP_LOCATION(state, {lat, lng}){
      state.shopLocation.lat = lat
      state.shopLocation.lng = lng
    },

    SET_ALERT_STATE(state, status){
      state.alert = status
    },

  },
  actions: {
    setSelectedShop({commit}, id){
      commit('SET_SELECTED_SHOP', id)
    },

    setShopProducts({commit}, items){
      commit('SET_SHOP_PRODUCTS', items)
    },

    addCartItem({commit}, item){
      commit('ADD_CART_ITEM', item)
    },

    deleteCartItem({commit}, id){
      commit('DELETE_CART_ITEM', id)
    },

    updateQtyCartItem({commit}, {id, qty}){
      commit('UPDATE_QTY_CART_ITEM', {id, qty})
    },

    increaseQtyCartItem({commit}, id){
      commit('INCREASE_QTY_CART_ITEM', id)
    },

    decreaseQtyCartItem({commit}, id){
      commit('DECREASE_QTY_CART_ITEM', id)
    },

    updateCartAmount({commit}){
      commit('UPDATE_CART_AMOUNT')
    },

    emptyCart({commit}){
      commit('EMPTY_CART')
    },

    setShopLocation({commit}, {lat, lng}){
      commit('SET_SHOP_LOCATION', {lat, lng})
    },

    setAlertState({commit}, status){
      commit('SET_ALERT_STATE', status)
    },
  },
  modules: {
  }
})
