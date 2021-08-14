<template>
    <v-container>
        <!-- 表示・検索機能 -->
        <v-row>
            <v-spacer />

            <v-col
                class="d-none d-sm-flex mx-5 mx-sm-0"
                cols="6"
                sm="2"
            >
                <v-select
                    v-model="chartGridCol"
                    prepend-icon="mdi-grid-large"
                    label="grid"
                    :items="gridItems"
                />
            </v-col>

            <v-col
                class="mx-5 mx-sm-0"
                cols="6"
                sm="2"
            >
                <v-select
                    v-model="query.ordering"
                    prepend-icon="mdi-sort-descending"
                    :items="sortItems"
                    label="Sort"
                    @change="sort"
                />
            </v-col>
        </v-row>

        <v-row>
            <v-col>
                <v-alert
                    color="blue"
                    type="info"
                >
                    あなたのブックマーク一覧
                </v-alert>
            </v-col>
        </v-row>

        <!-- main cards -->
        <v-row>
            <template v-if="!isVisible">
                <v-col
                    v-for="i in 10"
                    :key="i"
                    :cols="chartGridCol"
                >
                    <v-sheet class="pa-3">
                        <v-skeleton-loader
                            class="mx-auto"
                            type="card"
                        />
                    </v-sheet>
                </v-col>
            </template>

            <template v-else>
                <v-col
                    v-for="(item, index) in items"
                    :key="item.id"
                    :cols="chartGridCol"
                >
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
                                @click="postBookMark(index)"
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
                </v-col>
            </template>
        </v-row>
    </v-container>
</template>

<script>
import BarChart from '../components/BarChart.vue';
import Star from '../components/Star.vue';

const protocol = process.env.VUE_APP_PROTOCOL;
const origin = process.env.VUE_APP_ORIGIN;
const bookmarkURL = `${protocol}://${origin}/api/bookmark/`;

const HTTP_201_CREATED = 201;
const HTTP_204_NO_CONTENT = 204;

export default {
    components: {
        BarChart,
        Star,
    },
    data() {
        return {
            items: [{},{},{},{},{},{},],
            bookMarkIDs: [],
            chartGridCol: 12,
            chartHight: 300,
            isVisible: false,
            sortItems: [
                { text: '新着順', value: '' },
                { text: 'GPA (降順)', value: '-gpa' },
                { text: 'GPA (昇順)', value: 'gpa' },
                { text: '単位取得', value: 'failure' },
                { text: '落単', value: '-failure' },
                { text: 'A帯 (降順)', value: '-a_band'},
                { text: 'A帯 (昇順)', value: 'a_band'},
                { text: 'F (降順)', value: '-f' },
            ],
            gridItems: [
                {text: '１列', value: 12},
                {text: '２列', value: 6},
            ],
            query: {
                'ordering': '',
            },
        };
    },
    computed: {
        chartStyle() {
            return {
                height:`${this.chartHight}px`,
                position: 'relative',
            };
        }
    },
    created() {
        this.chartGridCol = window.innerWidth <= 600 ? 12 : 6;
    },
    async mounted() {
        if (this.$route.fullpath != '/service') {
            this.query.ordering = this.$route.query.ordering || '';
        }
        await this.fetchBookmarkAPIData();
    },
    beforeRouteUpdate(to, from, next) {
        // クエリなしに対応
        this.query.ordering = to.query.ordering || '';
        window.scrollTo(0, 0);
        this.fetchBookmarkAPIData();
        next();
    },
    methods: {
        sort() {
            const fullURL = this.joinQuery(this.$route.path);
            this.$router.push(fullURL).catch(err => { console.log(err); });
        },

        joinQuery(url) {
            let queryURL = '';
            Object.keys(this.query).forEach(key => queryURL += '&' + key + '=' + this.query[key]);
            if (url.indexOf('?') == -1) {
                queryURL = queryURL.replace('&', '?'); // 先頭の&を?に置換
            }
            return url + queryURL;
        },

        async postBookMark(index) {
            const item = this.items[index];
            const bookMarkID = item.id;

            if (item.isBookMark) {
                // ブックマーク解除
                const res = await this.axios.delete(`${bookmarkURL}${bookMarkID}/`, {
                    withCredentials: true
                });
                if (res.status == HTTP_204_NO_CONTENT) {
                    this.bookMarkIDs = this.bookMarkIDs.filter(id => id != bookMarkID);
                    item.isBookMark = !item.isBookMark;
                    this.$set(this.items, index, item);
                }
            } else {
                // 登録
                const res = await this.axios.post(bookmarkURL, {'bookMarkID': bookMarkID}, {
                    withCredentials: true
                });

                if (res.status == HTTP_201_CREATED) {
                    this.bookMarkIDs = res.data.bookMarkIDs;
                    item.isBookMark = !item.isBookMark;
                    this.$set(this.items, index, item);
                }
            }
        },

        async fetchBookmarkAPIData() {
            this.isVisible = false;

            const res = await this.axios.get(this.joinQuery(bookmarkURL), {
                withCredentials: true
            });

            this.items.splice(0, this.items.length);
            this.items.push(...res.data);

            // 取得したデータがブックマーク
            this.bookMarkIDs = res.data.map(item => item.id);
            this.items.map(item => {
                item.isBookMark = this.bookMarkIDs.includes(item.id);
            });
            
            this.isVisible = true;
        },

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
                        data: [item.ap, item.a, item.am, item.bp, item.b,
                            item.bm, item.cp, item.c, item.d, item.dm, item.f],
                    }
                ]
            };
        },
    }
};
</script>
