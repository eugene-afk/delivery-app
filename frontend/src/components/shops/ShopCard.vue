<template>
    <div v-if="!isThisShopAvailable">
        <div @click="changeShop" :class="`${selectedShopId === id ? 'font-weight-bold' : ''}`" class="pa-4 shop-card">
            <v-card :id="`shop_card_${id}`" class="w-100 cursor-pointer"
                    @mouseover="() => animeCardImage(0.9, 800, 400, [0, 1])"
                    @mouseleave="() => animeCardImage(0.99, 600, 300, [0.35, 0])"
                    @mouseout="cancelAnime">

                <v-card-header>
                    <v-card-header-text>
                        <v-row>
                            <v-col cols=3>
                                <v-img :src="`${mediaUrl}${logo}`" width="68px" />
                            </v-col>
                            <v-col cols=7>
                                <v-card-title>
                                    {{ name }}
                                </v-card-title>
                                <v-card-subtitle>
                                    Lorem ipsum dolor
                                </v-card-subtitle>
                            </v-col>
                            <v-col cols=2 v-if="selectedShopId === id && !closed" class="align-self-center shop-cursor">
                                <v-img src="@/assets/cursor.png" />
                            </v-col>
                            <v-col cols=2 v-if="closed" class="align-self-center shop-cursor">
                                <v-img src="@/assets/closed.png" />
                            </v-col>
                        </v-row>

                    </v-card-header-text>
                </v-card-header>

            </v-card>
        </div>
    </div>
</template>

<script>
import { useStore } from 'vuex'
import { useToast } from "vue-toastification"

export default {
    inject: ["mediaUrl", "anime",], 
    name: "ShopCardComponent",
    setup() {
        const store = useStore()
        const toast = useToast()

        return { store, toast, }
    },

    computed: {
        selectedShopId(){
            return this.store.getters['getSelectedShopId']
        },
        isThisShopAvailable(){
            return this.store.getters['getCartItemsCount'] > 0 && this.store.getters['getSelectedShopId'] !== this.id
        },
    },

    props: {
        name: {
            default: "unknown",
            type: String,
        },
        id: {
            default: 0,
            type: Number,
        },
        logo: {
            default: "",
            type: String,
        },
        closed: {
            default: false,
            type: Boolean,
        },
        lat: {
            default: 0,
            type: Number
        },
        lng: {
            default: 0,
            type: Number
        },
    },

    mounted() {
        this.anime({
            targets: `.shop-card`,
            duration: 1500,
            opacity: [0, 1],
            scale: [0.7, 0.99],
            elasticity: 1000
        })
    },

    methods: {
        changeShop(){
            if(this.isThisShopAvailable){
                this.toast.warning("Clear your cart to choose another shop!")
                return
            }
            if(this.closed){
                this.toast.info("This shop is already closed!")
                return
            }
            this.store.dispatch('setSelectedShop',this.id)
            this.store.dispatch('setShopLocation', {lat: this.lat, lng: this.lng})

            this.$emit('changeShopProducts', this.id)
        },

        animeCardImage(scale, duration, elasticity){
            this.anime({
                targets: `#shop_card_${this.id}`,
                scale: scale,
                duration: duration,
                elasticity: elasticity
            })
        },
        
        cancelAnime(){
            this.anime.remove(`#shop_card_${this.id}`)
        },
    },
}
</script>