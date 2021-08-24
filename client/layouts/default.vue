<template>
    <v-app>
        <Header />

        <v-main
            class="my-10"
            app
        >
            <Nuxt />
        </v-main>

        <BottomNavigation class="d-sm-none" />
        <Footer />
        <GoTopBtn />
    </v-app>
</template>
