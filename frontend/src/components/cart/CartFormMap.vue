<template>
<div id="map" style="height: 220px;"></div>
</template>

<script>
import { useStore } from 'vuex'
import axios from 'axios'

export default {
    inject: ["L",],
    name: "CartFormMapComponent",
    setup() {
        const store = useStore()
        const map = null

        return { map, store, }
    },

    computed: {
        shopLocation(){
            return this.store.getters['getShopLocation']
        }
    },

    mounted() {
        this.map = this.L.map('map').setView([ this.shopLocation.lat, this.shopLocation.lng], 16)

        this.L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '© OpenStreetMap'
        }).addTo(this.map)

        var shopIcon = this.L.icon({
            iconUrl: require('@/assets/shop-marker.png'),

            iconSize:     [52, 52], 
            shadowSize:   [50, 64], 
            iconAnchor:   [22, 94], 
            shadowAnchor: [4, 62],  
            popupAnchor:  [-3, -76] 
        })

        var userIcon = this.L.icon({
            iconUrl: require('@/assets/user-marker.png'),

            iconSize:     [52, 52], 
            shadowSize:   [50, 64], 
            iconAnchor:   [22, 94], 
            shadowAnchor: [4, 62],  
            popupAnchor:  [-3, -76] 
        })

        var drawnItems = new this.L.FeatureGroup()
        this.map.addLayer(drawnItems)

        var drawControl = new this.L.Control.Draw({
            draw: {
                polyline: false,
                polygon: false,
                rectangle: false,
                circle: false,
                circlemarker: false,
                marker: {
                    icon: userIcon,
                },
            },            
            edit: {
                featureGroup: drawnItems
            },
        })

        this.map.addControl(drawControl)

        var marker = this.L.marker([this.shopLocation.lat, this.shopLocation.lng], {icon: shopIcon}).addTo(this.map)
        marker.bindPopup("<b>From here we will be delivering your order!</b>.").openPopup()

        var self = this
        this.map.on(this.L.Draw.Event.CREATED, async function (e) {
            let layer = e.layer;
            drawnItems.addLayer((layer))
            const address = (await axios.get('https://nominatim.openstreetmap.org/reverse', {params: {format: 'jsonv2',lat: layer._latlng.lat,lon: layer._latlng.lng}})).data
            self.$emit("typeAddressFromMap", address.display_name)
        })
    }
}
</script>