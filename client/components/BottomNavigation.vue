<template>
    <v-bottom-navigation
        fixed
        app
        color="primary"
        active-class="no-active"
    >
        <v-btn
            to="/"
            nuxt
        >
            <span>Home</span>

            <v-icon>mdi-home</v-icon>
        </v-btn>

        <v-btn
            to="/search"
            nuxt
        >
            <span>Search</span>

            <v-icon>mdi-magnify</v-icon>
        </v-btn>

        <v-btn
            to="/bookmark"
            nuxt
        >
            <span>Bookmark</span>

            <v-icon>mdi-star-outline</v-icon>
        </v-btn>

        <v-btn
            href="https://hu-jagajaga.com/"
            target="_blank"
            rel="noopener noreferrer"
            active-class="v-btn-href no-active"
        >
            <span>JagaJaga</span>

            <v-avatar size="25">
                <img
                    src="@/assets/JagaJaga_logo.png"
                    alt=""
                >
            </v-avatar>
        </v-btn>
    </v-bottom-navigation>
</template>

<script>
export default {
};
</script>

<style>
.v-btn--active.no-active::before {
  opacity: 0 !important;
}

.v-btn-href {
    color: rgba(0, 0, 0, 0.6) !important;
}
</style>
