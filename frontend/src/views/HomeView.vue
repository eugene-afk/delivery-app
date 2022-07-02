<template>
<v-container>
  <v-row class="b-container">

      <v-col cols=12 lg=3>
        <v-card class="h-100">
          <v-card-header>
            <v-card-header-text>
              <v-card-title class="my-2">
                <v-icon icon="mdi-store"></v-icon>
                <span>
                  Choose shop
                </span> 
              </v-card-title>
            </v-card-header-text>
          </v-card-header>
          <Shops :shops="shops" />
        </v-card>
      </v-col>

      <v-col cols=12 lg=9>
        <v-card class="h-100" >
          <v-card-header>
            <v-card-header-text>
              <v-card-title class="my-2">
                <v-icon icon="mdi-food-fork-drink"></v-icon>
                <span>
                  Food
                </span>
              </v-card-title>
            </v-card-header-text>
          </v-card-header>
          <ShopProducts />
        </v-card>
      </v-col>

  </v-row>
</v-container>
  
</template>

<script>
import Shops from '@/components/shops/Shops.vue'
import ShopProducts from '@/components/shops/ShopProducts.vue'
import { ref, defineComponent } from 'vue'
import { useStore } from 'vuex'

export default defineComponent({
  inject: ["api"],
  name: 'HomeView',

  setup() {
    const shops = ref([])
    const store = useStore()

    return { shops, store, }
  },

  components: {
    Shops,
    ShopProducts,
  },

  async mounted() {
    //TODO: refactor shops to use with the store
    await this.fetchShops()
  },

  methods: {
      async fetchShops() {
        try{
          this.store.dispatch('setAlertState', false)
          const response = (await this.api.shops.getShops()).data
          this.shops = response
          if(this.store.getters['getSelectedShopId'] !== 0){
            return
          }
          this.store.dispatch('setSelectedShop', this.shops[0].id)
          this.store.dispatch('setShopProducts', this.shops[0].products)
          this.store.dispatch('setShopLocation', {lat: this.shops[0].lat, lng: this.shops[0].lng})
        }
        catch(ex){
          this.store.dispatch('setAlertState', true)
          console.log(ex)
        }
      },
  }
})
</script>
