<template>
    <v-footer
        color="primary"
        padless
        dark
        app
        absolute
    >
        <v-card
            flat
            tile
            width="100%"
            color="primary"
            class="lighten-1 text-center"
        >
            <v-card-text>
                <v-btn
                    v-for="icon in icons"
                    :key="icon"
                    class="mx-4"
                    icon
                >
                    <v-icon size="24px">
                        {{ icon }}
                    </v-icon>
                </v-btn>
            </v-card-text>

            <v-divider />

            <v-card-text class="white--text">
                {{ new Date().getFullYear() }} — <strong>iNAZO</strong>
            </v-card-text>
        </v-card>
    </v-footer>
</template>

<script>
export default {
    data() {
        return {
            icons: [
                'mdi-email',
                'mdi-github',
                'mdi-facebook',
                'mdi-twitter',
            ],
        };
    }
};

</script>