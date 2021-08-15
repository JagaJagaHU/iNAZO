<template>
    <v-tooltip left>
        <template v-slot:activator="{ on, attrs }">
            <v-btn
                class="px-5 py-5 mx-sm-10 my-sm-10 star"
                icon
                :color="color"
                x-large
                absolute
                right
                :attrs="attrs"
                v-on="on"
                @click="$emit('click')"
            >
                <v-icon>mdi-star</v-icon>
            </v-btn>
        </template>
        <span>ブックマーク</span>
    </v-tooltip>
</template>

<script>
export default {
    props: {
        active: Boolean,
    },
    computed: {
        color() {
            return this.active ? '#FBC02D' : 'gray';
        }
    }
};
</script>

<style>
.star {
    border: 3px solid;
}

.star:hover {
    opacity: 0.5;
}
</style>