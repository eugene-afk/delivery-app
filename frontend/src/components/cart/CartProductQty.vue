<template>
    <v-text-field
        style="min-width: 6rem;"
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
</template>

<script>
import { ref, watch } from 'vue'
import { useStore } from 'vuex'

export default {
    name: "CartProductQtyComponent",
    inject: ["mediaUrl"],
    setup(props) {
        const store = useStore()
        const qty = ref(props.product.qty)
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
        return { qty, rules, store, }
    },

    props: {
        //TODO: remove object
        product: {
            type: Object,
            required: true,
        }
    },

    methods: {
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

        updateQty(){
            this.store.dispatch('updateQtyCartItem', {id: this.product.id, qty: this.qty})
            this.store.dispatch('updateCartAmount')
        },
    }
}
</script>