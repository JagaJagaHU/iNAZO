<template>
    <v-app-bar
        app
        color="primary"
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
                        class="px-xs-0 px-xs-1"
                        to="/"
                        text
                    >
                        HUsearch
                    </v-btn>
                </v-col>

                <v-spacer />

                <!-- PC用 -->
                <v-col
                    cols="1"
                    class="d-none d-sm-flex"
                >
                    <v-toolbar-items>
                        <v-btn
                            to="/search"
                            text
                        >
                            <v-icon>mdi-magnify</v-icon>
                            <span class="mr-2">search</span>
                        </v-btn>
                    </v-toolbar-items>
                </v-col>

                <!-- スマホ用 -->
                <v-col
                    class="d-sm-none"
                    cols="3"
                >
                    <v-menu offset-y>
                        <template v-slot:activator="{ on }">
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
    data() {
        return {
            menuItems: [
                {title: 'Search', link: '/search', icon: 'mdi-magnify'},
            ]
        };
    }
};

</script>