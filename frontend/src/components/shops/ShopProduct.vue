<template>
<v-card class="product-card">
    <v-img
        contain
        class="white--text"
        :src="`${mediaUrl}${product.photo}`">

    </v-img>
    <v-card-title class="w-100">
        <div>
            <span class="title">{{product.name}}</span><br>
            <span class="title text-h4"> ${{ parseFloat(product.price).toFixed(2)}}</span>
        </div>
    </v-card-title>
    <v-card-actions class="justify-center">

        <v-btn variant="outlined"
                v-if="!isItemInCart" 
                size="large" 
                :color="product.in_stock ? 'primary' : 'grey'" 
                class="mx-auto mb-2" 
                :disabled="!product.in_stock"
                @click="addToCart">
            {{ product.in_stock ? 'ADD TO CART' : 'NOT IN STOCK' }}
        </v-btn>

        <div v-else class="d-flex mb-2">
            <v-text-field
                label="Outlined"
                placeholder="Placeholder"
                variant="underlined"
                type="number"
                single-line
                append-icon="mdi-plus"
                prepend-icon="mdi-minus"
                :rules="rules" 
                v-model="qty"
                @click:append="increaseQty"
                @click:prepend="decreaseQty"
                @change="updateQty">
            </v-text-field>
            <v-btn class="ms-2"
                color="primary"
                size="lg"
                variant="outlined"
                prepend-icon="mdi-cart"
                @click="() => {$router.push({name: 'cart'})}">
                
            </v-btn>
            <v-btn class="ms-2"
                color="red"
                size="lg"
                variant="outlined"
                prepend-icon="mdi-close"
                @click="removeItemFromCard">
                
            </v-btn>
        </div>

    </v-card-actions>
</v-card>
</template>

<script>
import { useStore } from 'vuex'
import { useToast } from "vue-toastification"
import { ref, watch } from 'vue'

export default {
    //TODO: replace textfield qty with ProductQtyComponent
    name: "ShopProductComponent",
    inject: ["mediaUrl", "anime"],
    setup() {
        const store = useStore()
        const toast = useToast()
        const qty = ref(1)
        const rules = [
            v => !!v || 'Required',
            v => v >= 1 || 'minimum 1 item',
            v => v <= 10 || 'maximum 10 items',
        ]
        watch(qty, (currentValue) => {
            if(currentValue < 1){
                qty.value = 1
            }
            if(currentValue > 10){
                qty.value = 10
            }
        })
        return { store, toast, qty, rules, }
    },

    props: {
        //TODO: remove object
        product: {
            type: Object,
            required: true,
        }
    },

    computed: {
        isItemInCart(){
            return this.store.getters['getCart'].items.some(x => x.id === this.product.id)
        },
    },

    mounted() {
        this.anime({
            targets: `.product-card`,
            duration: 1000,
            opacity: [0, 1],
            scale: [0.85, 0.99],
            elasticity: 500
        })
        if(this.isItemInCart){
            this.qty = this.store.getters['getCart'].items.find(x => x.id === this.product.id).qty
        }
    },

    methods: {
        addToCart(){
            this.store.dispatch('addCartItem', this.product)
            this.store.dispatch('updateCartAmount')
            this.toast.success(`${this.product.name} added to cart!`)
        },

        decreaseQty(){
            this.qty -= 1
            if(this.qty < 1){
                this.qty = 1
                return
            }
            this.store.dispatch('decreaseQtyCartItem', this.product.id)
            this.store.dispatch('updateCartAmount')
        },

        increaseQty(){
            this.qty += 1
            if(this.qty > 10){
                this.qty = 10
                return
            }
            this.store.dispatch('increaseQtyCartItem', this.product.id)
            this.store.dispatch('updateCartAmount')
        },

        removeItemFromCard(){
            this.qty = 1
            this.store.dispatch('deleteCartItem', this.product.id)
            this.store.dispatch('updateCartAmount')
        },

        updateQty(){
            this.store.dispatch('updateQtyCartItem', {id: this.product.id, qty: this.qty})
            this.store.dispatch('updateCartAmount')
        },
    },

}
</script>