<template>
    <v-row>
        <v-col>
            <div class="text-center my-10">
                <p v-if="count !== null">
                    {{ count }}件
                </p>
                <!-- PC -->
                <client-only>
                    <v-pagination
                        v-model="internalCurrentPage"
                        class="d-none d-sm-flex"
                        :length="size"
                        :total-visible="totalVisible"
                        @input="$emit('updatePage', $event)"
                    />
                </client-only>

                <!-- スマホ -->
                <div class="d-sm-none d-flex justify-center align-center">
                    <v-btn
                        class="mx-2 white--text"
                        color="light-blue"
                        :disabled="prevDisabled"
                        @click="updatePage(internalCurrentPage-1)"
                    >
                        &lt; &nbsp; 前へ
                    </v-btn>
                    <div
                        v-if="size !== 0"
                        class="text-h8 px-5"
                        style="color:#999"
                    >
                        {{ internalCurrentPage }} &nbsp; of &nbsp; {{ size }}
                    </div>
                    <v-btn
                        class="mx-2 white--text"
                        color="light-blue"
                        :disabled="nextDisabled"
                        @click="updatePage(internalCurrentPage+1)"
                    >
                        次へ &nbsp; &gt;
                    </v-btn>
                </div>
            </div>
        </v-col>
    </v-row>
</template>

<script>
export default {
    props: {
        size: {
            type: Number,
            required: true
        },
        totalVisible: {
            type: Number,
            required: true
        },
        currentPage: {
            type: Number,
            required: true
        },
        count: {
            type: Number,
            default: null,
            required: false
        }
    },
    computed: {
        internalCurrentPage: {
            get () {
                return this.currentPage;
            },
            set (newPage) {
                if (this.currentPage !== newPage) { this.$emit('input', newPage); }
            }
        },
        prevDisabled () {
            return this.internalCurrentPage <= 1;
        },
        nextDisabled () {
            return this.internalCurrentPage >= this.size;
        }
    },
    methods: {
        updatePage (page) {
            if (page <= 0 || this.size < page) { return; }
            this.$emit('updatePage', page);
        }
    }
};
</script>
