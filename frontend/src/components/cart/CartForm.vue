<template>
<div>
    <CartFormMap @typeAddressFromMap="typeAddressFromMap" />
    <div class="text-caption pa-4">
        You can place a marker on the map instead of typing your address manually.
    </div>
    <v-form @submit.prevent="makeOrder" autocomplete="off" class="pa-4">
        <div class="text-left text-lg-h4 font-weight-bold">
            Personal information
        </div>

        <div class="text-left pb-6 text-caption font-weight-medium">
            Lorem ipsum dolor.
        </div>
        <v-row>
            <v-col>
                <v-text-field v-model="form.name" 
                            type="text" 
                            label="Name" 
                            :disabled="disabled"                             
                            :rules="[rules.required]"
                            required>

                </v-text-field>
                <v-text-field v-model="form.phone" 
                            type="text" 
                            :rules="[rules.required, rules.phone]"
                            label="Phone" 
                            hint="example: 0974445566"
                            :disabled="disabled" 
                            required>

                </v-text-field>
                <v-text-field v-model="form.email" 
                            type="text" 
                            :rules="[rules.required, rules.email]"
                            label="Email" 
                            :disabled="disabled" 
                            required>

                </v-text-field>
                <v-text-field v-model="form.address" 
                            type="text" 
                            :rules="[rules.required]"
                            label="Address" 
                            :disabled="disabled" 
                            required>

                </v-text-field>
            </v-col>
        </v-row>
        <div class="text-center">
            <v-btn variant="outlined"    
                    type="submit"   
                    :disabled="disabled"
                    size="large" 
                    color="primary" 
                    class="mx-auto mb-2" >
                {{ btnText }}
            </v-btn>
        </div>
    </v-form>
</div>
</template>

<script>
import { reactive, ref } from 'vue'
import CartFormMap from '@/components/cart/CartFormMap.vue'
import { useStore } from 'vuex'

export default {
    name: "CartFormComponent",
    inject: ["api",],
    setup() {
        const store = useStore()
        const disabled = ref(false)
        const form = reactive({
            name: "",
            phone: "",
            email: "",
            address: "",
        })

        const rules = {
          required: value => !!value || 'Required.',
          email: value => {
            const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            return pattern.test(value) || 'Invalid e-mail.'
          },
          phone: value => {
            const pattern = /^(?:\+38)?(0[5-9][0-9]\d{7})$/
            return pattern.test(value) || 'Invalid phone number.'
          },
        }

        return { form, rules, disabled, store, }
    },

    components: {
        CartFormMap,
    },

    computed: {
        btnText(){
            return this.disabled ? 'Pending...' : 'Submit order'
        }
    },

    methods: {
        async makeOrder(){
            //TODO: for some reason required fields rules are not block submit 
            if(!this.disabled && this.form.name !== "" && this.form.email !== ""
                && this.form.phone !== "" && this.address !== ""){
                try{
                    this.store.dispatch('setAlertState', false)
                    this.disabled = true
                    this.form.shop_id = this.store.getters['getSelectedShopId']
                    this.form.amount = this.store.getters['getCart'].amount.toString()
                    this.form.order_products = []

                    for(var i = 0; i < this.store.getters['getCart'].items.length; i++){
                        this.form.order_products.push({
                            product_id: this.store.getters['getCart'].items[i].id,
                            qty: this.store.getters['getCart'].items[i].qty,
                        })
                    }

                    const response = (await this.api.orders.sendOrder(this.form)).data
                    this.store.dispatch('emptyCart')
                    this.$emit('changeViewToSuccessOrder', response.id)
                }
                catch(ex){
                    this.store.dispatch('setAlertState', true)
                    console.log(ex)
                }
                this.disabled = false
            }
        },
        
        typeAddressFromMap(address){
            this.form.address = address
        },

        allAreEqual(obj) {
            return new Set(Object.values(obj)).length > 1;
        },

    }
}
</script>