<template>

    <v-app>
        
        <Header></Header>
        
        <v-main class="my-10" app>
            <router-view/>
        </v-main>

        <Footer></Footer>

    </v-app>

</template>

<script>
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';

export default {
    name: 'App',
    components: {
        Header,
        Footer,
    },
    data: () => ({
        titleInner: 'ホーム',
        discriptionContent: '',
    }),
    head: {
        title() {
            return {
                inner: this.titleInner,
                separator: '|',
                complement: 'HUsearch'
            }
        },
        meta() { 
            return [
                { name: 'description', content: this.discriptionContent },
                { property: 'og:type', content: 'website' },
            ]
        },
    },
    watch: {
        $route(to, from) { // eslint-disable-line no-unused-vars
            this.titleInner = this.$route.meta.title;
            this.$emit('updateHead');
        }
    }
}
</script>
