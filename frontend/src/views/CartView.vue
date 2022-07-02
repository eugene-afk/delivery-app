<template>
<v-container class="cart" v-if="cartItemsCount > 0 && !orderSended">
  <v-row class="b-container">

    <v-col cols=12 lg=4>
        <v-card class="h-100">
            <CartForm @changeViewToSuccessOrder="changeViewToSuccessOrder" />
        </v-card>
    </v-col>

    <v-col cols=12 lg=8>
        <v-card class="h-100">
            <CartProducts />
            <div class="pa-4 text-h4 text-right w-100 mt-4">
                <span>
                    Amount:
                </span>  
                <span class="font-weight-bold">
                    ${{ cartAmount }}
                </span>
            </div>
        </v-card>
    </v-col>

  </v-row>
</v-container>    
<v-container v-else>
    <v-row v-if="orderSended" class="b-container justify-center pt-8">
        Your order was successfully sended! Number of your order is 
        <span class="font-weight-bold">{{ ` ${orderId}` }}</span>.
    </v-row>
    <v-row v-else class="b-container justify-center pt-8">
        Your cart is empty.
    </v-row>
</v-container>
</template>

<script>
import CartForm from '@/components/cart/CartForm.vue'
import CartProducts from '@/components/cart/CartProducts.vue'
import { useStore } from 'vuex'
import { ref } from 'vue'

export default {
    name: "CartView",
    setup() {
        const store = useStore()
        const orderSended = ref(false)
        const orderId = ref(0)

        return { store, orderSended, orderId, }
    },

    components: {
        CartForm,
        CartProducts,
    },

    computed: {
        cartItemsCount(){
            return this.store.getters['getCartItemsCount']
        },
        cartAmount(){
            return this.store.getters['getCart'].amount
        },
    },

    methods: {
        changeViewToSuccessOrder(id){
            this.orderId = id
            this.orderSended = true
        },
    },
}
</script>