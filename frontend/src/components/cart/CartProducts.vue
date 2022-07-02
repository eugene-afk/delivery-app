<template>

<v-table fixed-header>
    <thead>
        <tr>
            <th class="text-left">
            
            </th>
            <th class="text-left">
                Name
            </th>
            <th class="text-center">
                Qty
            </th>
            <th class="text-center">
                Price
            </th>
            <th class="text-right">
                Total
            </th>
            <th class="text-right">
                
            </th>
        </tr>
    </thead>
    <tbody v-if="cartProducts.length > 0">
        <tr v-for="i in cartProducts" :key="i.id">
            <td>
                <img :src="`${mediaUrl}${i.photo}`" width="54" heigth="auto" />
            </td>
            <td>
                {{ i.name }}
            </td>
            <td style="max-width: 8rem;" class="text-left">
                <CartProductQty :product="i" />
            </td>
            <td class="text-center">${{ i.price }}</td>
            <td class="text-right font-weight-bold">${{ i.total }}</td>
            <td class="text-center">
                <v-icon size="30" color="red cursor-pointer" icon="mdi-delete" @click="() => removeCartItem(i.id)"></v-icon>
            </td>
        </tr>
    </tbody>
</v-table>

</template>

<script>
import { useStore } from 'vuex'
import CartProductQty from '@/components/cart/CartProductQty.vue'

export default {    
    name: "CartProductsComponent",
    inject: ["mediaUrl"],
    setup() {
        const store = useStore()

        return { store }
    },

    components: {
        CartProductQty,
    },

    computed: {
        cartProducts(){
            return this.store.getters['getCart'].items
        },
    },

    methods: {
        removeCartItem(id){
            this.store.dispatch('deleteCartItem', id)
            this.store.dispatch('updateCartAmount')
        }
    }
}
</script>