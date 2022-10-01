<template>
    <v-row>
        <v-col cols="12">
            <v-parallax
                class="mb-5 mb-sm-10 px-10 py-10"
                :src="require('@/assets/background-title.png')"
                :height="height"
            >
                <v-row align="center" justify="center">
                    <v-col cols="12" sm="6">
                        <v-img
                            max-height="200"
                            max-width="500"
                            :src="require('@/assets/logo_top.png')"
                        />
                    </v-col>
                </v-row>
                <v-row align="center" justify="center">
                    <v-col cols="12" sm="9" md="6">
                        <v-text-field
                            v-model="search"
                            clearable
                            solo
                            label="講義・教授・学部で検索する"
                            prepend-inner-icon="mdi-magnify"
                            clear-icon="mdi-close-circle"
                            autocomplete="off"
                            @keydown.enter="filterSearch"
                        />
                    </v-col>
                </v-row>
            </v-parallax>
        </v-col>
    </v-row>
</template>

<script>
export default {
    data () {
        return {
            search: ''
        };
    },
    computed: {
        height () {
            switch (this.$vuetify.breakpoint.name) {
            case 'xs': return 300;
            case 'sm': return 400;
            case 'md': return 400;
            case 'lg': return 500;
            case 'xl': return 500;
            }
            return 0;
        }
    },
    methods: {
        filterSearch () {
            // vuetifyのclearはnullが挿入される
            const query = `?search=${this.search || ''}`;
            const fullURL = `/search${query}`;
            this.$router.push(fullURL);
        }
    }
};
</script>
