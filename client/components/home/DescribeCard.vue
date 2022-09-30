<template>
    <v-card
        class="px-10 py-10"
        height="300"
        color="#1976D2"
        dark
    >
        <p class="text-center text-h4 py-5">
            {{ title }}
        </p>
        <v-card-subtitle class="text-h6 pb-5">
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
