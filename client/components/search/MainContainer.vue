<template>
    <v-row>
        <template v-if="!isVisible">
            <v-col
                v-for="i in 10"
                :key="i"
                :cols="chartGridCol"
            >
                <search-skeleton-card />
            </v-col>
        </template>
        <template v-else>
            <v-col
                v-for="(item, index) in items"
                :key="item.id"
                :cols="chartGridCol"
            >
                <search-card
                    :item="item"
                    :index="index"
                    @starClick="$emit('starClick', index)"
                />
            </v-col>
        </template>
    </v-row>
</template>

<script>
export default {
    props: {
        isVisible: {
            type: Boolean,
            required: true
        },
        chartGridCol: {
            type: Number,
            required: true
        },
        items: {
            type: Array,
            required: true
        }
    }
};
</script>
