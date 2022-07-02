<template>
    <div>

        <div v-if="shops.length > 0">
            <div v-for="i in shops" :key="i.id">
                <ShopCard :name="i.name" 
                        :logo="i.logo" 
                        :id="i.id" 
                        :closed="i.is_closed" 
                        :lat="i.lat"
                        :lng="i.lng"
                        @changeShopProducts="changeShopProducts" />
            </div>
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
import ShopCard from '@/components/shops/ShopCard.vue'
import { useStore } from 'vuex'

export default {
    name: "ShopsComponent",
    setup() {
        const store = useStore()
        
        return { store, }
    },

    components: {
        ShopCard,
    },

    props: {
        shops: {
            type: Array,
            required: true,
        }
    },

    methods: {
        changeShopProducts(id){
            const shop = this.shops.find(x => x.id === id)
            this.store.dispatch('setShopProducts', shop.products)
        },
    },

}
</script>