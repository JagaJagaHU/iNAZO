<template>
    <v-fab-transition>
        <v-btn
            color="primary"
            dark
            bottom
            right
            fab
            fixed
            large
            class="mb-sm-5 mb-15 mr-sm-5"
            @click="goTop"
        >
            <v-icon>mdi-chevron-up</v-icon>
        </v-btn>
    </v-fab-transition>
</template>

<script>
export default {
    methods: {
        goTop() {
            window.scrollTo(0, 0);
        }
    }
};
</script>