<template>

    <v-app>
        <v-app-bar
        app
        color="primary"
        dark
        absolute
        >
        <v-toolbar-title>
            <v-btn to="/" text><h1>HUsearch</h1></v-btn>
        </v-toolbar-title>
            
        <v-spacer></v-spacer>

        <v-toolbar-items>
            <v-btn
            to="/about"
            text
            >
            <span class="mr-2">about</span>
            <v-icon>mdi-information-outline</v-icon>
            </v-btn>
            <v-btn
            to="/service"
            text
            >
            <span class="mr-2">service</span>
            <v-icon>mdi-toolbox-outline</v-icon>
            </v-btn>
        </v-toolbar-items>
        </v-app-bar>

        <v-main app>
            <router-view/>
        </v-main>

        <v-footer color="primary" padless dark app absolute>
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

                <v-divider></v-divider>

                <v-card-text class="white--text">
                {{ new Date().getFullYear() }} — <strong>HUsearch</strong>
                </v-card-text>
            </v-card>
        </v-footer>

    </v-app>

</template>

<script>

export default {
    name: 'App',

    data: () => ({
        icons: [
            'mdi-email',
            'mdi-github',
            'mdi-facebook',
            'mdi-twitter',
        ],
    }),
};
</script>
