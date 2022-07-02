<template>
<div>
    <div v-if="products.length > 0">
        <v-row class="mx-auto w-100 products-card py-2">
            <v-col v-for="i in products" :key="i.id" cols=12 md=6 lg=4>
                <ShopProduct :product="i" />
            </v-col>
        </v-row>

    </div>

    <div v-else>
        <v-progress-circular
            :size="70"
            :width="7"
            color="primary"
            indeterminate
            class="text-center w-100">
        </v-progress-circular>
    </div>
    
</div>
</template>

<script>
import { useStore } from 'vuex'
import ShopProduct from '@/components/shops/ShopProduct.vue'

export default {
    name: "ShopProductsComponent",

    components: {
        ShopProduct,
    },

    setup() {
        const store = useStore()

        return { store, }
    },

    computed: {
        products(){
            return this.store.getters['getShopProducts']
        }
    },

}
</script>