<template>
    <v-row>
        <v-col>
            <v-alert
                type="success"
            >
                検索結果：{{ searchResultText }}
            </v-alert>
        </v-col>
    </v-row>
</template>

<script>
export default {
    props: {
        searchResultText: {
            type: String,
            required: true
        }
    }
};
</script>
