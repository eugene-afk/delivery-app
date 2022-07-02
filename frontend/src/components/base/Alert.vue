<template>
<v-alert v-if="alertState" border="start" class="ma-4" color="red">
    Something went wrong.
</v-alert>
</template>

<script>
import { useStore } from 'vuex'

export default {
    //TODO: make alert closable
    name: "AlertComponent",
    setup() {
        const store = useStore()

        return { store }
    },

    computed: {
        alertState(){
            return this.store.getters['getAlertState']
        }
    },
}
</script>