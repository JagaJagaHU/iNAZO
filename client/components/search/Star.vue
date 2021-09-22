<template>
    <v-tooltip top>
        <template #activator="{ on, attrs }">
            <v-btn
                elevation="0"
                class="my-sm-6 star"
                fab
                :color="color"
                absolute
                right
                small
                outlined
                :attrs="attrs"
                v-on="on"
                @click="$emit('click')"
            >
                <v-icon>mdi-star-outline</v-icon>
            </v-btn>
        </template>
        <span>ブックマーク</span>
    </v-tooltip>
</template>

<script>
export default {
    props: {
        active: Boolean
    },
    computed: {
        color () {
            return this.active ? '#FBC02D' : 'gray';
        }
    }
};
</script>

<style>
.star {

}

.star:hover {
    opacity: 0.5;
}
</style>
