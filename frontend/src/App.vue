<template>
  <v-app>
    <Header />
    <v-main>
      <Alert />
      <router-view/>
    </v-main>
    <Footer />
  </v-app>
</template>

<script>
import Header from '@/components/base/Header.vue'
import Footer from '@/components/base/Footer.vue'
import Alert from '@/components/base/Alert.vue'

export default {
  name: 'App',
  components: {
    Header,
    Footer,
    Alert,
  }
}
</script>
