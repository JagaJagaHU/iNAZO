<template>
    <v-footer
        color="#1E88E5"
        padless
        dark
        app
        absolute
    >
        <v-card
            flat
            tile
            width="100%"
            color="#1E88E5"
            class="lighten-1 text-center"
        >
            <v-card-text>
                <v-btn
                    v-for="item in items"
                    :key="item.icon"
                    :href="item.link"
                    class="mx-4"
                    icon
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    <v-icon size="24px">
                        {{ item.icon }}
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
            items: [
                {
                    icon: 'mdi-form-select',
                    link: 'https://forms.gle/tLRiKrShckWsiuXs9',
                },
                {
                    icon: 'mdi-github',
                    link: 'https://github.com/karintou8710/iNAZO',
                },
                {
                    icon: 'mdi-twitter',
                    link: 'https://twitter.com/iNAZO_HU',
                }
            ]
        };
    }
};

</script>