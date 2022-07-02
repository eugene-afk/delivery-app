<template>
<v-footer class="pa-0">
    <v-card
    elevation="0"
    rounded="0"
    width="100%"
    class="bg-primary text-center">

        <v-card-text class="text-white text-left">
        {{ new Date().getFullYear() }} — <strong>Test task for ElifTech</strong>
        </v-card-text>
    </v-card>
</v-footer>
</template>

<script>
export default {
    name: "FooterComponent",

}
</script>