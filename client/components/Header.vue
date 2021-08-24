<template>
    <v-app-bar
        app
        color="#1E88E5"
        dark
        absolute
    >
        <v-container>
            <!-- header -->
            <v-row>
                <v-col
                    cols="5"
                    sm="2"
                >
                    <v-btn
                        class="px-0 px-sm-1"
                        to="/"
                        text
                        nuxt
                    >
                        <v-img
                            max-width="160"
                            :src="require('@/assets/iNAZO_logo.png')"
                        />
                    </v-btn>
                </v-col>

                <v-spacer />

                <!-- PC用 -->
                <v-col
                    cols="4"
                    class="d-none d-sm-flex justify-end"
                >
                    <v-toolbar-items>
                        <v-btn
                            to="/search"
                            nuxt
                            text
                        >
                            <span class="mr-2">
                                <v-icon class="mr-1">mdi-magnify</v-icon>search
                            </span>
                        </v-btn>
                        <v-btn
                            to="/bookmark"
                            text
                            nuxt
                        >
                            <span class="mr-2"><v-icon class="mr-1 mb-1">mdi-star-outline</v-icon>bookmark</span>
                        </v-btn>
                    </v-toolbar-items>
                </v-col>

                <!-- スマホ用 -->
                <v-col
                    class="d-sm-none"
                    cols="3"
                >
                    <v-menu offset-y>
                        <template #activator="{ on }">
                            <v-btn
                                class="mx-2"
                                dark
                                elevation="0"
                                color="primary"
                                v-on="on"
                            >
                                <v-icon dark>
                                    mdi-format-list-bulleted-square
                                </v-icon>
                            </v-btn>
                        </template>

                        <v-list>
                            <v-subheader>Get help</v-subheader>

                            <v-list-item
                                v-for="item in menuItems"
                                :key="item.title"
                                :to="item.link"
                                nuxt
                            >
                                <v-list-item-icon>
                                    <v-icon>{{ item.icon }}</v-icon>
                                </v-list-item-icon>
                                <v-list-item-content>
                                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                        </v-list>
                    </v-menu>
                </v-col>
            </v-row>
        </v-container>
    </v-app-bar>
</template>

<script>

export default {
    data () {
        return {
            menuItems: [
                { title: 'Search', link: '/search', icon: 'mdi-magnify' },
                { title: 'Bookmark', link: '/bookmark', icon: 'mdi-star-outline' }
            ]
        };
    }
};

</script>
