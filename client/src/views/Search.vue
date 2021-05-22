<template>
    <v-container>
        <!-- pagination -->
        <v-row>
            <v-col>
                <Pagination
                    :size="size"
                    :total-visible="totalVisible"
                    :current-page="currentPage"
                    @updatePage="setPageAndGetData"
                    @input="page => currentPage = page"
                />
            </v-col>
        </v-row>

        <!-- 表示・検索機能 PC -->
        <v-row class="d-none d-sm-flex">
            <v-col
                cols="4"
            >
                <v-text-field
                    v-model="search"
                    :counter="100"
                    label="Search"
                    required
                    @keydown.enter="filterSearch"
                />
            </v-col>

            <v-col
                cols="4"
            >
                <v-btn
                    color="green"
                    elevation="2"
                    dark
                    @click="filterSearch"
                >
                    Search
                </v-btn>
            </v-col>

            <v-spacer />

            <v-col
                cols="1"
            >
                <v-select
                    v-model="chartGridCol"
                    :items="gridItems"
                    label="grid"
                />
            </v-col>

            <v-col
                cols="2"
            >
                <v-select
                    v-model="query.ordering"
                    :items="sortItems"
                    label="Sort"
                    @change="sort"
                />
            </v-col>
        </v-row>

        <!-- 表示・検索機能 スマホ -->
        <v-row class="d-sm-none">
            <v-col
                cols="12"
            >
                <v-text-field
                    class="mx-5"
                    v-model="search"
                    :counter="100"
                    label="Search"
                    required
                    @keydown.enter="filterSearch"
                />
            </v-col>
        </v-row>

        <v-row class="d-sm-none">

            <v-col
                cols="6"
            >
                <v-select
                    class="mx-5"
                    v-model="query.ordering"
                    :items="sortItems"
                    label="Sort"
                    @change="sort"
                />
            </v-col>

            <v-col
                cols="6"
                class="d-flex align-center justify-center"
            >
                <v-btn
                    color="green"
                    elevation="2"
                    dark
                    @click="filterSearch"
                >
                    Search
                </v-btn>
            </v-col>
        </v-row>

        <v-row class="d-sm-none">

            <v-spacer />

            
        </v-row>

        <!-- Alert-->
        <v-row>
            <v-col>
                <v-alert
                    v-if="searchResultText"
                    type="success"
                >
                    検索結果：{{ searchResultText }}
                </v-alert>
            </v-col>
        </v-row>

        <!-- main cards -->
        <v-row>
            <v-col
                v-for="item, index in items"
                :key="item.id"
                :cols="chartGridCol"
            >
                <v-card
                    class="my-5"
                    flat
                    outlined
                >
                    <v-card-title v-if="item.subject == &quot; &quot;">
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
                        <BarChart :chart-data="getChartData(item)" />
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>

        <!-- pagination -->
        <v-row>
            <v-col>
                <Pagination
                    :size="size"
                    :total-visible="totalVisible"
                    :current-page="currentPage"
                    @updatePage="setPageAndGetData"
                    @input="page => currentPage = page"
                />
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import BarChart from '../components/BarChart.vue';
import Star from '../components/Star.vue';
import Pagination from '../components/search/Pagination.vue';

const protocol = process.env.VUE_APP_PROTOCOL;
const origin = process.env.VUE_APP_ORIGIN;
const gradeURL = `${protocol}://${origin}/api/gradeinfo/`;
const bookmarkURL = `${protocol}://${origin}/api/bookmark/`;

const HTTP_201_CREATED = 201;
const HTTP_204_NO_CONTENT = 204;

export default {
    components: {
        BarChart,
        Star,
        Pagination,
    },
    data() {
        return {
            items: [],
            bookMarkIDs: [],
            currentPage: 1,
            totalVisible: 0,
            size: 0,
            search: '',
            searchResultText: null,
            chartGridCol: 12,
            query: {
                'search': '',
                'ordering': '',
                'page': 1,
            },
            sortItems: [
                {text: '新着順', value: ''},
                {text: 'A+', value: '-ap'},
                {text: 'A', value: '-a'},
                {text: 'A-', value: '-am'},
                {text: 'B+', value: '-bp'},
                {text: 'B', value: '-b'},
                {text: 'B-', value: '-bm'},
                {text: 'C+', value: '-cp'},
                {text: 'C', value: '-c'},
                {text: 'D', value: '-d'},
                {text: 'D-', value: '-dm'},
                {text: 'F', value: '-f'},
                {text: 'GPA', value: '-gpa'},
            ],
            gridItems: [
                {text: '１列', value: 12},
                {text: '２列', value: 6},
            ],
        };
    },
    beforeRouteUpdate(to, from, next) {
        // クエリなしに対応
        this.query.page = to.query.page || 1;
        this.query.ordering = to.query.ordering || '';
        this.query.search = to.query.search || '';
        window.scrollTo(0, 0);
        this.fetchGradeAPIData();
        next();
    },
    created() {
        // 画面サイズがxsなら表示個数を減らす
        this.totalVisible = window.innerWidth <= 600 ? 5 : 10;
    },
    async mounted() {
        if (this.$route.fullpath != '/service') {
            this.query.page = this.$route.query.page || 1;
            this.query.ordering = this.$route.query.ordering || '';
            this.query.search = this.$route.query.search || '';
        }
        // 初期取得はbookmarkを始めにfetchする。
        await this.fetchBookmarkAPIdata();
        await this.fetchGradeAPIData();
    },
    methods: {
        filterSearch() {

            this.query['search'] = this.search;
            this.query.page = 1;

            const fullURL = this.joinQuery(this.$route.path);
            this.$router.push(fullURL).catch(err => { console.log(err); });
        },

        sort() {
            this.query.page = 1;

            const fullURL = this.joinQuery(this.$route.path);
            this.$router.push(fullURL).catch(err => { console.log(err); });
        },

        setPageAndGetData(page) {
            if (page <= 0 || page > this.size) return;
            if (page == this.query.page) return;
            this.query.page = page;
            window.scrollTo(0, 0);

            const fullURL = this.joinQuery(this.$route.path);
            this.$router.push(fullURL).catch(err => {}); // eslint-disable-line no-unused-vars
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

        async fetchGradeAPIData() {
            const res = await this.axios.get(this.joinQuery(gradeURL), {
                withCredentials: true
            });

            // chartを更新
            this.items.splice(0, this.items.length);
            this.items.push(...res.data.results);
            this.size = res.data.size;
            this.currentPage = Number(this.query.page);
            this.searchResultText = this.query.search;

            // 取得したデータがブックマークされているか確認
            this.items.map(item => {
                item.isBookMark = this.bookMarkIDs.includes(item.id);
            });
        },

        // ページに訪れた時のみに使用
        async fetchBookmarkAPIdata() {
            const res = await this.axios.get(bookmarkURL, {
                withCredentials: true
            });
            this.bookMarkIDs = res.data.map(item => item.id);
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
    },
};

</script>