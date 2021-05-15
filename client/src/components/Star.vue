<template>
    <v-btn
        class="px-5 py-10"
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