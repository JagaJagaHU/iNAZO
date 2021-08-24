<template>
    <v-container>
        <v-row>
            <v-col>
                <h1 v-if="error.statusCode === 404">
                    Page not found
                </h1>
                <h1 v-else>
                    An error occurred
                </h1>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    props: {
        error: {
            type: Object,
            required: true
        }
    }
};
</script>
