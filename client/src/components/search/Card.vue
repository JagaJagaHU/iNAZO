<template>
    <v-card
        class="my-5"
        flat
        outlined
    >
        <v-card-title v-if="item.subject == ' '">
            {{ item.lecture }}
        </v-card-title>
        <v-card-title v-else>
            {{ item.subject }} &emsp; {{ item.lecture }}
        </v-card-title>

        <v-card-text>
            <Star
                :active="item.isBookMark"
                @click="$emit('starClick', index)"
            />
            <p class="card-text">
                {{ item.year }}年度 {{ item.semester }}
            </p>
            <p class="card-text">
                開講学部：{{ item.faculty }}
            </p>
            <p class="card-text">
                クラス：{{ item.group }}
            </p>
            <p class="card-text">
                履修者数 : {{ item.numOfStudents }}人
            </p>
            <p>担当教員名：{{ item.teacher }}</p>
            <p>GPA : {{ item.gpa }}</p>
        </v-card-text>
        <v-card-text>
            <BarChart
                :chart-data="getChartData(item)"
                :styles="chartStyle"
            />
        </v-card-text>
    </v-card>
</template>

<script>
import BarChart from './BarChart.vue';
import Star from './Star.vue';

export default {
    components: {
        BarChart,
        Star,
    },
    props: {
        item: {
            type: Object,
            required: true,
        },
        index: {
            type: Number,
            required: true,
        },
    },
    data() {
        return {
            chartHight: 300,
        };
    },
    computed: {
        chartStyle() {
            return {
                height: `${this.chartHight}px`,
                position: 'relative',
            };
        },
    },

    methods: {

        getChartData(item) {
            return {
                labels: ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'D', 'D-', 'F'],
                datasets: [
                    {
                        label: '人数',
                        backgroundColor: [
                            'rgba(33, 150, 243, 1)',
                            'rgba(33, 150, 243, 1)',
                            'rgba(33, 150, 243, 1)',
                            'rgba(187, 222, 251, 1)',
                            'rgba(187, 222, 251, 1)',
                            'rgba(187, 222, 251, 1)',
                            'rgba(255, 152, 0, 1)',
                            'rgba(255, 152, 0, 1)',
                            'rgba(244, 67, 54, 1)',
                            'rgba(244, 67, 54, 1)',
                            'rgba(244, 67, 54, 1)',
                        ],
                        data: [
                            item.ap,
                            item.a,
                            item.am,
                            item.bp,
                            item.b,
                            item.bm,
                            item.cp,
                            item.c,
                            item.d,
                            item.dm,
                            item.f,
                        ],
                    },
                ],
            };
        },
    },
};
</script>