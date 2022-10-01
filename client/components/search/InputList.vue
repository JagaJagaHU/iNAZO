<template>
    <div>
        <client-only>
            <!-- 表示・検索機能 PC -->
            <div class="d-none d-sm-flex">
                <v-row>
                    <v-col cols="5">
                        <v-text-field
                            :value="search"
                            clearable
                            outlined
                            label="講義を検索する"
                            prepend-inner-icon="mdi-magnify"
                            clear-icon="mdi-close-circle"
                            hint="講義名・教員名・年度・学部・クラスなどで検索ができます。"
                            autocomplete="off"
                            @input="updateSearch"
                            @keydown.enter="$emit('filterSearch')"
                        />
                    </v-col>

                    <v-spacer />

                    <v-col cols="2">
                        <v-select
                            :value="chartGridCol"
                            prepend-icon="mdi-grid-large"
                            :items="gridItems"
                            label="grid"
                            @input="updateChartGridCol"
                        />
                    </v-col>

                    <v-col cols="2">
                        <v-select
                            :value="ordering"
                            prepend-icon="mdi-sort-descending"
                            :items="sortItems"
                            label="Sort"
                            @input="updateOrdering"
                            @change="$emit('sortChange')"
                        />
                    </v-col>
                </v-row>
            </div>

            <!-- 表示・検索機能 スマホ -->
            <div class="d-sm-none">
                <v-row>
                    <v-col cols="12">
                        <v-text-field
                            :value="search"
                            class="mx-5"
                            label="講義を検索する"
                            clearable
                            outlined
                            prepend-inner-icon="mdi-magnify"
                            clear-icon="mdi-close-circle"
                            hint="講義名・教員名・年度・学部・クラスなどで検索ができます。"
                            @input="updateSearch"
                            @keydown.enter="$emit('filterSearch')"
                        />
                    </v-col>
                </v-row>

                <v-row>
                    <v-spacer />

                    <v-col
                        cols="6"
                        class="mx-5"
                    >
                        <v-select
                            :value="ordering"
                            prepend-icon="mdi-sort-descending"
                            label="Sort"
                            :items="sortItems"
                            @input="updateOrdering"
                            @change="$emit('sortChange')"
                        />
                    </v-col>
                </v-row>

                <v-row>
                    <v-spacer />
                </v-row>
            </div>
        </client-only>
    </div>
</template>

<script>
export default {
    props: {
        search: {
            type: String,
            required: true
        },
        ordering: {
            type: String,
            required: true
        },
        chartGridCol: {
            type: Number,
            required: true
        }
    },
    data () {
        return {
            sortItems: [
                { text: '新着順', value: '' },
                { text: 'GPA (降順)', value: '-gpa' },
                { text: 'GPA (昇順)', value: 'gpa' },
                { text: '単位取得者数', value: 'failure' },
                { text: '落単者数', value: '-failure' },
                { text: 'A帯 (降順)', value: '-a_band' },
                { text: 'A帯 (昇順)', value: 'a_band' },
                { text: 'F (降順)', value: '-f' }
            ],
            gridItems: [
                { text: '１列', value: 12 },
                { text: '２列', value: 6 }
            ]
        };
    },
    methods: {
        updateSearch (e) {
            this.$emit('update:search', e);
        },
        updateOrdering (e) {
            this.$emit('update:ordering', e);
        },
        updateChartGridCol (e) {
            this.$emit('update:chart-grid-col', e);
        }
    }
};
</script>
