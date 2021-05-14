<template>
<v-btn
    class="px-5 py-10"
    icon
    :color="color"
    @click="$emit('click')"
    x-large
    absolute
    right
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
}
</script>