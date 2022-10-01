<template>
    <v-card
        class="px-10 py-10"
        height="300"
        color="#1976D2"
        dark
    >
        <v-card-title class="justify-center text-h4 pt-5 pb-10 px-0">
            {{ title }}
        </v-card-title>
        <v-card-subtitle class="text-h5 text-sm-h6 pb-5">
            {{ contents }}<br>
        </v-card-subtitle>
    </v-card>
</template>

<script>
export default {
    props: {
        title: {
            type: String,
            required: true
        },
        contents: {
            type: String,
            required: true
        }
    }
};
</script>
