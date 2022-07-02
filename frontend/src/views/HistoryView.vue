<template>
<v-container>
  <v-row class="b-container history">

    <v-col cols=12>
        <form @submit.prevent="search" autocomplete="off">
            <v-text-field v-model="email" label="Type your email" :rules="[rules.required, rules.email]" required>
                <template v-slot:append>
                    <v-btn class="me-2" color="indigo" icon="mdi-magnify" type="submit"></v-btn>
                    <v-btn v-if="email" type="button" class="me-2" color="red" icon="mdi-close" @click="clearSearch"></v-btn>
                </template>
            </v-text-field>
        </form>
        <div class="text-caption">
            You can track your last order or see the history by typing your email.
        </div>
    </v-col>

    <v-col cols=12 v-for="i in items" :key="i.id" class="my-4">
        <HistoryOrderCard :item="i" />
    </v-col>

  </v-row>
</v-container>
</template>

<script>
import { ref } from 'vue'
import HistoryOrderCard from '@/components/HistoryOrderCard.vue'
import { useStore } from 'vuex'

export default {
    name: "HistoryView",
    inject: ["api",],
    setup() {
        const store = useStore()
        const email = ref("")
        const items = ref([])
        const rules = {
          required: value => !!value || 'Required.',
          email: value => {
            const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            return pattern.test(value) || 'Invalid e-mail.'
          },          
        }
        return { items, email, rules, store, }
    },

    components: {
        HistoryOrderCard,
    },

    methods: {
        async search(){
            try{
                if(this.email){
                    this.store.dispatch('setAlertState', false)
                    const response = (await this.api.orders.getOrders({search: this.email})).data
                    this.items = response
                }
            }
            catch(ex){
                this.store.dispatch('setAlertState', true)
                console.log(ex)
            }
        },

        clearSearch(){
            this.items = []
            this.email = ""
        },

    }
}
</script>