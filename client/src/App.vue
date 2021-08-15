<template>
    <v-app>
        <Header />

        <v-main
            class="my-10"
            app
        >
            <router-view />
        </v-main>
        
        <BottomNavigation class="d-sm-none" />
        <Footer />
    </v-app>
</template>

<script>
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
import BottomNavigation from './components/BottomNavigation';

export default {
    name: 'App',
    components: {
        Header,
        Footer,
        BottomNavigation,
    },
    data: () => ({
        titleInner: 'ホーム',
        discriptionContent: '',
    }),
    watch: {
        $route(to, from) { // eslint-disable-line no-unused-vars
            this.titleInner = this.$route.meta.title;
            this.$emit('updateHead');
        }
    },
    head: {
        title() {
            return {
                inner: this.titleInner,
                separator: '|',
                complement: '成績分布検索サービス iNAZO'
            };
        },
        meta() {
            return [
                { name: 'description', content: this.discriptionContent },
                { property: 'og:type', content: 'website' },
            ];
        },
    }
};
</script>
