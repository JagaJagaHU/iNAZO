<template>
    <v-app>
        <Header />

        <v-main class="my-10" app>
            <v-alert v-show="isMaintenanceMode" type="error">
                現在システムメンテナンス中です。
                サイト内のページが一時的に正しく表示されない場合がございますので、ご了承ください。
            </v-alert>

            <Nuxt />
        </v-main>

        <BottomNavigation class="d-sm-none" />
        <Footer />
        <GoTopBtn />
    </v-app>
</template>

<script>
export default {
    data () {
        return {
            isMaintenanceMode: 0
        };
    },

    mounted () {
        this.isMaintenanceMode = this.$config.isMaintenanceMode;
    }
};
</script>
