<template>
<v-app-bar color="primary" prominent>        
    <div class="me-3">
        <router-link to="/">
            <v-img src="@/assets/logo.png" width="48px" />
        </router-link>
    </div>

    <v-toolbar-title>Delivery App</v-toolbar-title>

    <v-spacer></v-spacer>

    <router-link to="/history">
        <v-btn class="me-4"
            variant="outlined"
            icon
            color="white">
            <v-icon icon="mdi-history"></v-icon>
        </v-btn>      
    </router-link>

    <router-link to="/cart">
        <v-btn
            variant="outlined"
            icon
            color="white">
            <v-icon v-if="cartItemsCount === 0">mdi-cart</v-icon>
            <v-badge v-else :content="cartItemsCount" color="white">
                <v-icon icon="mdi-cart"></v-icon>
            </v-badge>
            
        </v-btn>        
    </router-link>
</v-app-bar>    
</template>

<script>
import { useStore } from 'vuex'

export default {
    name: "HeaderComponent",
    setup() {
        const store = useStore()

        return { store }
    },

    computed: {
        cartItemsCount(){
            return this.store.getters['getCartItemsCount']
        }
    },
}
</script>