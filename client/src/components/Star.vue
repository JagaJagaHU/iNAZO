<template>
    <v-btn
        class="px-5 py-5 mx-sm-10 my-sm-10 star"
        icon
        :color="color"
        x-large
        absolute
        right
        @click="$emit('click')"
    >
        <v-icon>mdi-star</v-icon>
    </v-btn>
</template>

<script>
export default {
    props: {
        active: Boolean,
    },
    computed: {
        color() {
            return this.active ? 'yellow' : 'gray';
        }
    }
};
</script>

<style>
.star {
    border: 3px solid;
}
</style>